from __future__ import annotations
import asyncio
import copy
import hashlib
import json
import os
import secrets
import time
import uuid
from pathlib import Path
import aiohttp
from .domain import DEFAULTS, PREFIX, build_graph, dependent_indices, media_state, validate_plan, validate_rewrite, validate_settings, video_timing
from .providers import AIClient, APIError
from .comfy_client import ComfyClient, SubmissionUnknown, SubmissionRejected, ExecutionFailed, TaskMissing
from .media_tools import command, merge, probe, resolve_tools, keep_duration, keep_full
from . import workflows
from . import timing_policy
from . import image_workflows
from .image_generator import ImageGenerator
from .files import generated_image_name
from .asset_plans import normalize_asset_plan
from .review import Reviewer, ReviewPaused, validate_review, enabled as review_enabled
from .telemetry import scope, measure
from . import dialogue_plan, dialogue_check, dialogue_timing, prompt_compiler
from .dialogue_check import DialogueCheckMixin
from .production import PRODUCTION_RULES, NO_SUBTITLES, enforce_subtitles, bind_plan, binding_ids, fingerprint, preparation_dependency

class Paused(RuntimeError):pass

# --- keep the generated tail -------------------------------------------------------------
# For a continued clip H3 generates 12 alignment frames (0.5s) after the planned end, the Trim node
# dropped them, and keep_duration then cut another 0-14 frames with ffmpeg -t. The model was often
# still speaking there, so the last 1-5 characters of the line vanished no matter how long the
# clip was made. True = keep everything the model generated and never cut the tail.
# Set False to restore the old behaviour exactly.
KEEP_ALIGNMENT_TAIL=True
TRIM_NODE_CLASSES={'H3ContinueTrim','H3ADv1Trim'}
TRIM_KEEP_ALL=1000   # > any frame count (15s ~ 360 frames); node does min(images, start+count)

def keep_alignment_tail(graph):
    """Make every Trim node keep frames/audio through the end of the generated timeline."""
    changed=0
    for node in graph.values():
        if isinstance(node,dict) and node.get('class_type') in TRIM_NODE_CLASSES and 'trim_output_frames' in node.get('inputs',{}):
            node['inputs']['trim_output_frames']=TRIM_KEEP_ALL;changed+=1
    return changed

PLAN_INSTRUCTIONS='''你是短剧分镜导演。把用户剧本拆成可自动执行的H3视频片段，保留情节顺序，所有台词必须逐字取自剧本，不能省略、改写或新增台词。短剧默认无背景音乐，H3本身生成中文说话声音，有声音参考时跟随人物声音参考。
每段2至15秒；台词按正常说话速度安排，不要把太长台词挤进短视频。一个片段可含少量紧密相关小镜头。明确同一时间地点且需接上一段动作时continuity=continue，切换场景/时间/视角时cut，首段cut。不能把整集一律续接。
优先使用已有角色、场景、道具、声音参考。角色和场景缺少图片时才放入assets_to_create，生成一次，多段复用。不生成声音。图片prompt用英文，画面说明用中文。不使用真实人名冒充未知人物。
返回JSON对象：{"style":"全片视觉风格","assets_to_create":[{"id":"new_character_1","role":"character|scene|prop|style","label":"名称","description":"中文外观或场景说明","image_prompt":"英文生图提示词","reference_asset_ids":[]}],"segments":[{"title":"片段名","duration_seconds":8,"continuity":"cut|continue","visual_zh":"具体画面动作","camera_zh":"构图镜头运动","image_prompt":"该段开场构图英文提示词，保持角色场景一致，不含文字字幕","asset_ids":["素材编号，包含所有需给H3的图音视频"],"image_reference_ids":["生成该段参考图要参考的图片素材编号"],"dialogue":[{"speaker":"角色名","text":"原文中文台词"}],"sound_zh":"环境音和物理声"}]}。
新增素材编号只能使用字母数字下划线，且不得和已有编号重复；引用只能用给出的编号和新增编号。每段最多8张已有图片（另预留1张生成的开场图）、3段音频、3段视频，总参考素材含开场图不能超过12。不要将所有人物不加区分全部放入每段。角色声音素材只给该段说话人物。
assets_to_create不超过100，所有新增人物和场景在image_prompt中共享全片风格，身份服装颜色保持一致。禁止任何人工审核等待步骤。JSON。'''

from .pipeline import ProductionPipelineMixin

class Engine(ProductionPipelineMixin,DialogueCheckMixin):
    def __init__(self,store,files,root,local_url):
        self.store=store;self.files=files;self.root=Path(root);self.local_url=local_url
        self.tasks={};self.render_lock=asyncio.Lock();self.episode_lock=asyncio.Lock()
        self.ready_events={};self.preparation_events={};self.preparing_projects=set()
        self.prepare_slots=asyncio.Semaphore(2)
        self.template=json.loads((self.root/'templates/h3_api.json').read_text(encoding='utf-8'))
        self.guide=(self.root/'guides/h3_reference.txt').read_text(encoding='utf-8')+'\n'+(self.root/'guides/h3_base.txt').read_text(encoding='utf-8')
        for p in store.list('project'):
            if p['status'] in {'running','queued','pausing'}:
                store.update('project',p['id'],lambda x:x.update(status='paused',phase='服务已重启；点击继续核对原任务并接着跑',pause_requested=False))
    def config(self,p):
        config=validate_settings({**self.store.settings(),**p['settings']})
        snapshot=p.get('workflow_snapshot')
        if snapshot:
            meta=workflows.resolved(snapshot)['metadata']
            config['duration_seconds']=meta['duration_seconds']
            for key in ('width','height'):
                if key in meta:config[key]=meta[key]
            config['seed_mode']='random' if meta['seed_mode']=='random' else 'fixed'
            if meta['seed'] is not None:config['seed']=meta['seed']
            if 'overlap' in meta:config['overlap_seconds']=meta['overlap']
            if 'continue_audio' in meta:config['continue_audio']=meta['continue_audio']
            if meta['media_mode']=='single_image' and any(b.get('voice_id') for b in p.get('character_bindings',{}).values()):
                raise ValueError('固定音色需要能接收音频的批量素材视频工作流；单张图工作流不支持。')
            if meta['media_mode']=='single_image' and not config['generate_shot_images']:
                raise ValueError('单张开场图工作流需要启用每个片段自动生成开场参考图。')
        if not config['comfy_url']:config['comfy_url']=self.local_url
        return resolve_tools(config,self.root)
    def set(self,id,**values):return self.store.update('project',id,lambda p:p.update(**values))
    def clip_set(self,id,index,**values):return self.store.update('project',id,lambda p:p['clips'][index].update(**values))
    def prepare_dialogue_timing(self,id,index,cfg):
        def apply(p):
            clip=p['clips'][index]
            if dialogue_timing.prepare(p,clip,cfg):
                p['planned_duration_seconds']=sum(c['duration_seconds'] for c in p['clips'])
                if p.get('plan') and index<len(p['plan'].get('segments',[])):
                    segment=p['plan']['segments'][index]
                    for key in ('duration_seconds','generation_seconds','generation_exact','dialogue_timing','shots','dialogue'):
                        if key in clip:segment[key]=copy.deepcopy(clip[key])
        self.store.update('project',id,apply)
        return self.store.get('project',id)
    def paused(self,id):
        p=self.store.get('project',id)
        if p.get('pause_requested'):raise Paused('已暂停，继续可从保存的进度接着跑。')
        if p.get('series_id') and self.store.get('series',p['series_id']).get('pause_requested'):raise Paused('整剧已暂停。')
    def assign_workflow(self,id,workflow_id):
        p=self.store.get('project',id)
        if id in self.tasks and not self.tasks[id].done():raise ValueError('请先暂停项目，再关联工作流。')
        if p.get('plan') or p.get('clips'):raise ValueError('项目已准备过镜头，不能更换执行工作流；请新建项目。')
        snapshot=workflows.resolved(self.store.get('workflow',workflow_id))
        if snapshot.get('archived'):raise ValueError('请选择未归档的工作流。')
        self.set(id,workflow_snapshot=snapshot,error='',phase='工作流已关联，点击继续可加入整集队列')
    def script_editable(self,p):
        task=self.tasks.get(p['id'])
        return not (p['id'] in self.preparing_projects or p.get('archived') or p.get('plan') or p.get('clips') or p.get('generated_assets') or p.get('final') or
                    p['status'] in {'running','queued','pausing','complete'} or task and not task.done())
    def check_script_edit(self,p,body):
        if not self.script_editable(p):raise ValueError('本集已开始准备或生成，请用镜头重做；修改剧本仅用于尚未开始的集。')
        if body.get('expected_revision')!=p.get('script_revision',1):raise ValueError('剧本已被修改，请重新打开编辑窗口。')
        script=str(body.get('script','')).strip()
        if not script or len(script)>500000:raise ValueError('请填写本集剧本，最多50万字。')
    def edit_script(self,id,body):
        with self.store.lock:
            p=self.store.get('project',id)
            if p.get('series_id'):raise ValueError('请通过所属整剧修改本集剧本。')
            self.check_script_edit(p,body)
            self.set(id,script=str(body['script']).strip(),script_revision=p.get('script_revision',1)+1,error='',phase='剧本已修改，点击开始制作')
            return self.store.public_project(id)
    def start(self,id,require_workflow=False):
        p=self.store.get('project',id)
        if id in self.preparing_projects:raise ValueError('整剧正在提前准备本集，准备完成后会自动继续；请勿重复启动。')
        if p.get('archived'):raise ValueError('请先恢复已归档的项目。')
        if p.get('series_id') and self.store.get('series',p['series_id']).get('archived'):raise ValueError('请先恢复所属整剧。')
        if require_workflow and not p.get('workflow_snapshot') and not any(c.get('job_id') for c in p.get('clips',[])):
            raise ValueError('请先选择并关联你在ComfyUI跑通的工作流；软件不再默认使用内置int8模板。')
        if id in self.tasks and not self.tasks[id].done():return
        if p['status']=='complete':raise ValueError('项目已经完成。要修改镜头请使用重做。')
        if not p.get('plan') and not p.get('clips') and not p.get('timing_policy'):
            p.update(timing_policy=timing_policy.normalize(),episode_target_seconds=0)
        if p.get('workflow_snapshot'):
            p['workflow_snapshot']=workflows.resolved(p['workflow_snapshot'])
        for c in p['clips']:
            if c.get('known_failed'):
                for key in ('job_id','prompt_id','api_graph','output_prefix','submission_unknown','known_failed'):c.pop(key,None)
                c.update(status='ready' if c.get('prompt_en') else 'pending',retry_count=0)
        self.store.put('project',id,p)
        self.set(id,status='queued',phase='已加入整集队列；轮到后自动制作',error='',pause_requested=False)
        self.ready_events[id]=asyncio.Event();self.preparation_events[id]=asyncio.Event()
        task=asyncio.create_task(self.run_queued(id),name=PREFIX+'_'+id);self.tasks[id]=task
    async def run_queued(self,id):
        try:
            # A whole episode owns this lock, including AI, images and final merge.
            # asyncio.Lock admits waiting tasks in the order they started waiting.
            async with self.episode_lock:
                self.set(id,status='running',phase='准备自动流程')
                try:
                    await self.run(id)
                finally:
                    if self.store.get('project',id)['status']!='complete':
                        # A failure/pause must not spend AI credits on later episodes.
                        for other,task in list(self.tasks.items()):
                            if other!=id and not task.done() and self.store.get('project',other)['status']=='queued':
                                self.set(other,status='paused',phase='前一集未完成，整集队列已暂停；处理后按顺序点击继续',pause_requested=False)
                                task.cancel()
        except asyncio.CancelledError:
            if self.store.get('project',id)['status'] in {'queued','pausing'}:
                self.set(id,status='paused',phase='排队已暂停，点击继续可重新加入队列',pause_requested=False)
            raise
    def pause(self,id):
        p=self.store.get('project',id)
        if p['status'] not in {'running','queued','pausing'}:return
        if p['status']=='queued':
            self.set(id,pause_requested=False,status='paused',phase='排队已暂停，点击继续可重新加入队列')
            task=self.tasks.get(id)
            if task and not task.done():task.cancel()
            return
        self.set(id,pause_requested=True,status='pausing',phase='当前ComfyUI任务完成后暂停；不终止渲染')
        if p.get('series_id'):
            self.store.update('series',p['series_id'],lambda s:s.update(pause_requested=True,status='pausing',phase='当前任务完成后暂停整剧'))
    def redo(self,id,indices,feedback='',new_seed=True,regenerate_image=False):
        p=self.store.get('project',id)
        if new_seed and p.get('workflow_snapshot') and not p['workflow_snapshot']['bindings'].get('seed'):
            raise ValueError('本工作流未关联Seed，不能由软件更换Seed；请取消使用新的随机Seed。')
        if id in self.tasks and not self.tasks[id].done():raise ValueError('项目正在执行，请等完成或暂停后再重做。')
        selected=sorted(set(int(i) for i in indices))
        if not selected or any(i<0 or i>=len(p['clips']) for i in selected):raise ValueError('请选择有效镜头。')
        affected=dependent_indices(p['clips'],selected)
        for i in affected:
            c=p['clips'][i]
            if c.get('output'):
                c.setdefault('versions',[]).append({k:copy.deepcopy(c[k]) for k in ('output','raw_output','seed','prompt_en','prompt_zh','frame_asset_id','generation','meta') if k in c})
            for key in ('output','raw_output','meta','prompt_id','job_id','api_graph','output_prefix','submission_unknown','finished_at','known_failed','retry_count','quality_accepted','adopted_ng','quality_verdict','quality_attempt','dialogue_check','dialogue_adoption','video_reviewed'):c.pop(key,None)
            c['generation']=int(c.get('generation',0))+1
            if new_seed:c['seed']=secrets.randbits(63)
            if i not in selected:
                for key in ('frame_asset_id','image_asset_id','state_reference_id','state_reference_source','prompt_en','prompt_zh'):c.pop(key,None)
            if i in selected:
                c['redo_feedback']=str(feedback)
                if feedback:
                    c.pop('prompt_en',None);c.pop('prompt_zh',None)
                if regenerate_image:
                    c.pop('image_asset_id',None);c.pop('state_reference_source',None);
                    c.pop('frame_asset_id',None);c.pop('prompt_en',None);c.pop('prompt_zh',None)
            c['status']='ready' if c.get('prompt_en') else 'pending'
        if p.get('final'):p.setdefault('final_versions',[]).append(p['final'])
        p.update(final=None,status='paused',phase='准备重做',error='',pause_requested=False)
        self.store.put('project',id,p);self.store.event(id,'重做片段：'+', '.join(str(i+1) for i in affected)+'。续接片段会跟随前段重做。')
        self.start(id);return affected
    def asset_summary(self,assets):
        return [{k:a.get(k,'') for k in ('id','name','kind','role','label','description','speaker')} for a in assets]
    def images(self,assets,limit=8):
        return [{**a,'path':self.files.asset_path(a)} for a in assets if a['kind']=='image'][:limit]
    async def checked_text(self,ai,instructions,request,validator,images=(),metric='planning_api'):
        last=''
        for attempt in range(ai.config['retry_limit']+1):
            with measure(metric):
                result=await ai.text(instructions,request+('\n修正上一次JSON的校验问题：'+last if last else ''),images)
            try:return validator(result)
            except (ValueError,KeyError,TypeError) as e:
                last=str(e)
                if hasattr(ai,'validation_failed'):ai.validation_failed(last,result)
        raise ValueError('AI格式校验仍未通过：'+last)
    async def plan(self,id,ai,cfg):
        p=self.store.get('project',id)
        if p.get('plan'):return
        self.paused(id);self.set(id,phase='AI拆解剧本、安排分镜和角色素材')
        assets=[self.store.get('asset',aid) for aid in p['asset_ids']]
        def check(result):
            result=bind_plan(result,p.get('character_bindings',{}),assets)
            for segment in result.get('segments',[]):segment.setdefault('depends_on_previous',True)
            if p.get('series_id'):
                parent=self.store.get('series',p['series_id'])
                result=normalize_asset_plan(result,assets,'assets_to_create',aliases=parent.get('generated_assets'))
            result=validate_plan(result,assets,cfg['max_segments'],min_duration=.25 if p.get('timing_policy') else 2)
            result['dialogue_coverage']=dialogue_plan.check_coverage(result,p['script'])
            if p.get('timing_policy'):
                result=dialogue_plan.prepare(result,p['timing_policy'],p.get('episode_target_seconds',0))
                result=timing_policy.prepare_segments(result,p['timing_policy'],p.get('episode_target_seconds',0))
            if p.get('series_id'):
                known={(a.get('role'),a.get('label','').strip()) for a in assets}
                for item in result.get('assets_to_create',[]):
                    if (item['role'],item['label'].strip()) in known:raise ValueError('全剧已有'+item['label']+'素材，必须复用已有编号，不能重复生成。')
            for s in result['segments']:
                if p.get('workflow_snapshot'):
                    meta=p['workflow_snapshot']['metadata']
                    if not p.get('timing_policy') and abs(s['duration_seconds']-meta['duration_seconds'])>.001:raise ValueError('本工作流每段固定'+str(meta['duration_seconds'])+'秒，不能改变工作流时长。')
                    if s['continuity']=='continue' and not meta['continuation']:raise ValueError('本工作流只支持独立切镜，请将continuity设为cut。')
                for line in s.get('dialogue',[]):
                    if line['text'] not in p['script']:raise ValueError('台词不是剧本原文：'+line['text'])
            return result
        policy=p.get('timing_policy')
        target=p.get('episode_target_seconds',0) or timing_policy.seconds(policy,'episode') or timing_policy.seconds(policy,'total')
        request=json.dumps({'script':p['script'],'instructions':p['instructions'],'target_segment_seconds':timing_policy.seconds(policy,'task') if policy else cfg['duration_seconds'],
                            'timing_policy':policy,
                            'target_episode_seconds':target,'episode_duration_mode':'auto' if target==0 else 'target',
                            'assets':self.asset_summary(assets),'character_bindings':p.get('character_bindings',{}),
                            'previous_episode_script':p.get('previous_episode_script','')},ensure_ascii=False)
        instructions=PLAN_INSTRUCTIONS+dialogue_plan.PLANNING_RULES+'\n'+PRODUCTION_RULES+'\n固定角色character_bindings必须使用对应图片与音频。每段返回characters出镜角色姓名列表。每段返回depends_on_previous布尔值：续接、同场景人物位置或道具状态承接均为true，即使cut也一样；只有可独立确定、无需前段实际画面状态的插镜才可false。首段另返回use_previous_episode_state，承接上一集相同场景/人物状态时为true，明显换地点时间为false。已有参考图每段最多7张，为状态参考与开场图留位置。'
        if policy:instructions=instructions.replace('每段2至15秒','每次H3生成2至15秒；分镜实际保留时长可短至0.25秒')+timing_policy.instructions(policy,target)
        instructions+='\n每集目标时长为0时，按原文对白、动作和自然节奏决定镜头数量，禁止把0当作零秒或套用120秒。目标时长大于0时按此目标规划镜头数量，但不得省略原文对白来凑时长。'
        if p.get('workflow_snapshot'):
            meta=p['workflow_snapshot']['metadata']
            if not policy:instructions+='\n用户导入工作流的每段时长固定为'+str(meta['duration_seconds'])+'秒，所有segments.duration_seconds必须使用此数值；较长对白拆为多个固定时长片段。'
            if not meta['continuation']:instructions+='\n本工作流未关联续接，所有segments.continuity必须为cut。'
        plan=await self.checked_text(ai,instructions,request,check,self.images(assets))
        for segment in plan['segments']:
            dialogue_timing.prepare(p,segment,cfg)
        clips=[]
        for segment in plan['segments']:
            seed=secrets.randbits(63) if cfg['seed_mode']=='random' else cfg['seed']
            if p.get('workflow_snapshot') and p['workflow_snapshot']['metadata']['seed'] is None:seed=None
            clips.append({**segment,'status':'pending','seed':seed,'generation':1,'versions':[]})
        planned=sum(s['duration_seconds'] for s in clips)
        self.set(id,plan=plan,clips=clips,planned_duration_seconds=planned)
        self.store.event(id,f'剧本已拆成{len(clips)}个片段，预计共{planned:.2f}秒；最终以成片实际时长为准。')
    def resolve_id(self,p,id):return p.get('generated_assets',{}).get(id,id)
    async def generate_image(self,id,ai,cfg,aid,prompt,references):
        p=self.store.get('project',id)
        snapshot=p.get('image_workflow_snapshots')
        if cfg['image_provider']=='local' and not snapshot:
            snapshot=image_workflows.snapshots(self.store,cfg)
            self.set(id,image_workflow_snapshots=snapshot)
        generator=ImageGenerator(self.store,self.files,cfg,ai.session,self.render_lock,snapshot)
        return await generator.image(ai,aid,id,prompt,references)
    async def create_missing_assets(self,id,ai,cfg):
        p=self.store.get('project',id)
        for item in p['plan'].get('assets_to_create',[]):
            self.paused(id);p=self.store.get('project',id)
            if item['id'] in p['generated_assets']:continue
            self.set(id,phase='自动建立素材：'+item['label'])
            references=[]
            for aid in item.get('reference_asset_ids',[]):
                real=self.resolve_id(p,aid)
                try:asset=self.store.get('asset',real)
                except KeyError:continue
                if asset['kind']=='image':references.append(self.files.asset_path(asset))
            prompt=item['image_prompt']+'\nConsistent production style: '+p['plan'].get('style','')+'\nNo captions, no watermarks, no text overlays.'
            aid=hashlib.sha256((id+':'+item['id']).encode()).hexdigest()[:40]
            try:asset=self.store.get('asset',aid)
            except KeyError:
                blob=await self.generate_image(id,ai,cfg,aid,prompt,references)
                asset=self.files.write_asset(self.store,generated_image_name(item['label']),blob,{**item,'generated':True},id=aid)
            self.store.update('project',id,lambda x:x['generated_assets'].update({item['id']:asset['id']}))
            self.store.event(id,'已保存素材：'+asset['name'])
    def clip_assets(self,p,clip):
        ids=list(dict.fromkeys(clip.get('asset_ids',[])+clip.get('image_reference_ids',[])))
        return [self.store.get('asset',self.resolve_id(p,aid)) for aid in ids]
    def clip_media(self,p,clip):
        assets=prompt_compiler.authoritative_audio(self.clip_assets(p,clip),clip.get('dialogue',[]),p.get('character_bindings',{}),self.store)
        if clip.get('frame_asset_id'):assets=[self.store.get('asset',clip['frame_asset_id'])]+assets
        unique={};ordered=[]
        for a in assets:
            if a['id'] not in unique:unique[a['id']]=True;ordered.append(a)
        if p.get('workflow_snapshot',{} ) and p['workflow_snapshot']['media_mode']=='single_image':
            if not clip.get('frame_asset_id'):raise ValueError('此工作流需要已生成的开场图。')
            ordered=[self.store.get('asset',clip['frame_asset_id'])]
        return media_state([a['relative_path'] for a in ordered if a['kind']=='image'],[a['relative_path'] for a in ordered if a['kind']=='video'],[a['relative_path'] for a in ordered if a['kind']=='audio']),ordered
    async def prepare_clip(self,id,index,ai,cfg):
        self.paused(id);p=self.store.get('project',id);clip=p['clips'][index]
        if cfg['generate_shot_images'] and not clip.get('frame_asset_id'):
            # Repair a lost database link from the durable, deterministic asset
            # before the submitted-job fast path. Never generate a replacement.
            aid=clip.get('image_asset_id') or hashlib.sha256(f'{id}:clip:{index}:v{clip["generation"]}'.encode()).hexdigest()[:40]
            try:asset=self.store.get('asset',aid)
            except KeyError:asset=None
            if asset and asset['kind']=='image' and self.files.asset_path(asset).is_file():
                self.clip_set(id,index,frame_asset_id=aid,image_asset_id=aid)
                p=self.store.get('project',id);clip=p['clips'][index]
        if any(clip.get(key) for key in dialogue_timing.COMMITTED):return
        p=self.prepare_dialogue_timing(id,index,cfg);clip=p['clips'][index]
        if clip.get('prompt_en') and clip.get('prompt_compiler_version')==prompt_compiler.VERSION:
            if clip.get('state_reference_source'):await self.state_reference(id,index,cfg)
            media,current_assets=self.clip_media(p,clip)
            from .prompt_content import can_reuse
            if can_reuse(self,clip,current_assets):
                try:
                    validate_rewrite({'prompt_en':clip['prompt_en'],'prompt_zh':clip.get('prompt_zh','')},media,clip.get('dialogue',[]))
                except ValueError as error:
                    # Invalid compiled text is a recoverable cache, not a new
                    # asset or a submitted job. Rebuild from saved structured
                    # content while retaining the existing opening frame.
                    def clear_prompt(record):
                        item=record['clips'][index]
                        for key in ('prompt_en','prompt_zh','prompt_compiler_version','compiled_asset_versions'):
                            item.pop(key,None)
                    self.store.update('project',id,clear_prompt)
                    self.store.event(id,f'第{index+1}段已保存提示词需要重组，保留素材和进度：'+str(error))
                    p=self.store.get('project',id);clip=p['clips'][index]
                else:return
        self.clip_set(id,index,status='preparing')
        assets=self.clip_assets(p,clip)
        if cfg['generate_shot_images'] and not clip.get('frame_asset_id'):
            self.set(id,phase=f'准备第{index+1}段开场图')
            refs=[self.store.get('asset',self.resolve_id(p,a)) for a in clip.get('image_reference_ids',[])]
            if not refs:refs=[a for a in assets if a['kind']=='image']
            ref_paths=[self.files.asset_path(a) for a in refs if a['kind']=='image']
            state=await self.state_reference(id,index,cfg)
            if state:
                pinned=set(binding_ids(p.get('character_bindings',{})))
                fixed=[self.files.asset_path(a) for a in refs if a['id'] in pinned and a['kind']=='image']
                others=[r for r in ref_paths if r not in fixed]
                cap=8
                wf=(p.get('image_workflow_snapshots') or {}).get('reference')
                if wf:cap=min(cap,wf.get('metadata',{}).get('reference_capacity',8))
                if len(fixed)+1>cap:raise ValueError('带参考图工作流容量不足以同时容纳固定角色与前段状态。')
                ref_paths=(fixed+[state]+others)[:cap]
            prompt=clip['image_prompt']+'\nProduction style: '+p['plan'].get('style','')+'\n'+p['instructions']+'\n'+clip.get('redo_feedback','')
            if state:prompt+='\nThe previous adopted frame is a state reference for positions and props only. Follow the new storyboard composition. Preserve identity from the fixed character image. Do not reproduce extra limbs, malformed anatomy or text from the state reference.'
            prompt+='\n'+NO_SUBTITLES
            prompt+='\nUse the reference images for the exact character identity, clothing, props and environment. Single opening-frame composition, no montage, no captions, no watermark.'
            aid=clip.get('image_asset_id') or hashlib.sha256(f'{id}:clip:{index}:v{clip["generation"]}'.encode()).hexdigest()[:40]
            self.clip_set(id,index,image_asset_id=aid)
            try:
                asset=self.store.get('asset',aid)
            except KeyError:
                blob=await self.generate_image(id,ai,cfg,aid,prompt,ref_paths)
                asset=self.files.write_asset(self.store,f'片段_{index+1:03d}_开场图_v{clip["generation"]}.png',blob,{'label':clip['title'],'role':'scene','generated':True},id=aid)
            image_seed=None
            try:
                quality=self.store.get('quality_asset',aid);image_seed=quality.get('seed')
            except KeyError:
                try:image_seed=self.store.get('image_job',aid).get('seed')
                except KeyError:pass
            self.clip_set(id,index,frame_asset_id=asset['id'],image_seed=str(image_seed) if image_seed is not None else None)
        self.paused(id);p=self.store.get('project',id);clip=p['clips'][index]
        media,assets=self.clip_media(p,clip)
        if not media['images']:raise ValueError(f'第{index+1}段没有图片参考。请开启自动生成开场图或提供图片素材。')
        axis=workflows.timing(p['workflow_snapshot'],clip,p['clips'][index-1] if index else None) if p.get('workflow_snapshot') else video_timing(clip,cfg,p['clips'][index-1] if index else None)
        request=json.dumps({'compiler_contract':prompt_compiler.VERSION,
            'segment':{k:clip.get(k) for k in ('title','duration_seconds','continuity','visual_zh','camera_zh','dialogue','sound_zh','redo_feedback','dialogue_budget','dialogue_timing')},
            'style':p['plan'].get('style',''),'user_instructions':p['instructions'],
            'references':prompt_compiler.request_references(assets),
            'previous_segment':{k:p['clips'][index-1].get(k) for k in ('visual_zh','dialogue','sound_zh')} if index and clip['continuity']=='continue' else None,
            'time_axis':axis},ensure_ascii=False)
        from .prompt_content import compile_saved
        result=await compile_saved(self,id,index,ai,prompt_compiler.INSTRUCTIONS,request,assets,media,axis)
        self.clip_set(id,index,**result,status='ready')
        self.store.event(id,f'第{index+1}段的图像和H3提示词已就绪；素材与对白由程序绑定。')
    async def producer(self,id,ai,cfg,queue):
        try:
            for i in range(len(self.store.get('project',id)['clips'])):
                if self.store.get('project',id)['clips'][i].get('output'):continue
                await self.prepare_clip(id,i,ai,cfg)
                await queue.put((i,None))
            await queue.put((None,None))
        except asyncio.CancelledError:raise
        except Exception as e:await queue.put((None,e))
    async def render_clip(self,id,index,comfy,cfg):
        self.paused(id);p=self.store.get('project',id);clip=p['clips'][index]
        if clip.get('output'):return
        if clip.get('raw_output'):
            await self.accept_output(id,index,clip['raw_output'],cfg);return
        previous=None
        if clip['continuity']=='continue':
            before=p['clips'][index-1].get('output')
            if not before:raise ValueError('续接镜头的上一段还未生成。')
            previous=(Path(before.get('subfolder',''))/before['filename']).as_posix()+' [output]'
        if not clip.get('api_graph'):
            guarded=enforce_subtitles({'prompt_en':clip['prompt_en'],'prompt_zh':clip.get('prompt_zh','')})
            if guarded['prompt_en']!=clip['prompt_en']:
                self.clip_set(id,index,**guarded);clip={**clip,**guarded}
        media,_=self.clip_media(p,clip)
        suffix=f'_r{clip["retry_count"]}' if clip.get('retry_count') else ''
        prefix=clip.get('output_prefix') or f'{PREFIX}/projects/{id}/片段_{index+1:03d}_v{clip["generation"]}{suffix}'
        snapshot=p.get('workflow_snapshot')
        fresh=not clip.get('api_graph')
        graph=clip.get('api_graph') or (workflows.instantiate(snapshot,clip,media,previous,prefix) if snapshot else build_graph(self.template,clip,cfg,media,previous,prefix))
        if fresh and KEEP_ALIGNMENT_TAIL and keep_alignment_tail(graph):self.store.event(id,f'第{index+1}段：已取消ComfyUI裁尾，保留模型生成的完整尾部。')
        output_node_id=clip.get('output_node_id') or (snapshot['output_node_id'] if snapshot else '20')
        job=clip.get('job_id') or uuid.uuid4().hex
        # A durable intent is committed before POST, so a crash cannot cause an
        # automatic second submission even if prompt_id was not received.
        if not clip.get('job_id'):
            await comfy.preflight(graph,output_node_id)
            self.clip_set(id,index,job_id=job,api_graph=graph,output_prefix=prefix,output_node_id=output_node_id,status='submitting',submission_unknown=True)
            snapshot=self.files.project_dir(id)/f'片段_{index+1:03d}_v{clip["generation"]}_API.json'
            snapshot.write_text(json.dumps(graph,ensure_ascii=False,indent=2),encoding='utf-8')
            try:prompt_id=await comfy.submit(graph,job,id)
            except SubmissionRejected:
                self.clip_set(id,index,known_failed=True,submission_unknown=False,status='error');raise
            self.clip_set(id,index,prompt_id=prompt_id,status='submitted',submission_unknown=False)
        else:
            prompt_id=clip.get('prompt_id')
            if not prompt_id:
                prompt_id=await comfy.find(job)
                if not prompt_id:
                    recovered=self.files.recover_output(prefix)
                    if recovered:
                        await self.accept_output(id,index,recovered,cfg);return
                    raise SubmissionUnknown('未查到原任务或输出，不能确定是否提交成功。为避免重复生成，已暂停。请核对ComfyUI后使用“原任务不存在，允许重新提交”。')
                self.clip_set(id,index,prompt_id=prompt_id,status='submitted',submission_unknown=False)
        self.set(id,phase=f'ComfyUI生成第{index+1}段')
        self.store.event(id,f'第{index+1}段ComfyUI任务编号：{prompt_id}')
        try:output=await comfy.wait(prompt_id,output_node_id)
        except TaskMissing as error:
            output=self.files.recover_output(prefix)
            if not output:
                self.clip_set(id,index,prompt_id=None,missing_prompt_id=prompt_id,
                              submission_unknown=True,status='error',quality_error=str(error))
                raise
        await self.accept_output(id,index,output,cfg)
    async def accept_output(self,id,index,output,cfg):
        clip=self.store.get('project',id)['clips'][index]
        path=self.files.output_path(output)
        if not path.exists():raise ValueError('ComfyUI返回的视频不在本机output目录。此版本请与生成视频的ComfyUI安装在同一台服务器、同一实例。')
        self.clip_set(id,index,raw_output=output,submission_unknown=False)
        meta=await probe(path,cfg)
        if clip.get('dialogue') and not meta['audio']:raise RuntimeError('此片段有台词，但ComfyUI输出没有音轨。请检查H3声音输出后重做此片段。')
        if clip.get('timing_version'):
            target=path.with_name(path.stem+'_保留.mp4')
            if KEEP_ALIGNMENT_TAIL:path,meta=await keep_full(path,clip['duration_seconds'],cfg)
            else:path,meta=await keep_duration(path,target,clip['duration_seconds'],cfg)
            output=self.files.descriptor(path)
        self.clip_set(id,index,output=output,meta=meta,status='complete',finished_at=time.time())
        self.store.event(id,f'第{index+1}段已完成，时长{meta["duration"]:.2f}秒。')
    async def render_with_retries(self,id,index,comfy,cfg):
        while True:
            try:return await self.render_clip(id,index,comfy,cfg)
            except ExecutionFailed as e:
                c=self.store.get('project',id)['clips'][index]
                attempts=c.get('failed_attempts',[])+[{'prompt_id':c.get('prompt_id'),'job_id':c.get('job_id'),'error':str(e),'time':time.time()}]
                self.clip_set(id,index,failed_attempts=attempts,known_failed=True,status='error')
                count=int(c.get('retry_count',0))
                if count>=cfg['retry_limit']:raise
                self.paused(id)
                def clear(p):
                    item=p['clips'][index]
                    for key in ('prompt_id','job_id','api_graph','output_prefix','submission_unknown','known_failed'):item.pop(key,None)
                    item.update(retry_count=count+1,status='ready')
                self.store.update('project',id,clear)
                self.store.event(id,f'第{index+1}段执行失败，技术重试{count+1}/{cfg["retry_limit"]}。')
                await asyncio.sleep(2)
    async def reviewed_clip(self,id,index,ai,comfy,cfg):
        reviewer=Reviewer(self.store,self.files,cfg,ai.session)
        while True:
            self.paused(id)
            c=self.store.get('project',id)['clips'][index]
            # Persisted verdicts are resolved before generating another candidate.
            verdict=c.get('quality_verdict')
            audio_ok=dialogue_check.approved(self.files,c,cfg)
            audio_resolved=dialogue_check.resolved(self.files,c,cfg)
            if verdict and verdict.get('dialogue_failed') and audio_ok:
                # The user may have confirmed the recording, or explicitly
                # disabled this independent gate while the project was paused.
                verdict=None
            elif verdict and not verdict.get('dialogue_failed') and not audio_resolved:
                # Old visual verdicts are not evidence that speech was heard.
                # Fall through to check the saved video without rerendering it.
                verdict=None
            if verdict and review_enabled(cfg,'video') and verdict.get('video_reviewed') is False:
                verdict=None
            if c.get('quality_accepted') and audio_resolved and (not review_enabled(cfg,'video') or c.get('video_reviewed')):return
            if verdict is not None:
                attempt=int(c.get('quality_attempt',1))
                if verdict['passed'] or attempt>=cfg['review_video_attempts']:
                    if not verdict['passed'] and cfg['review_video_exhausted']=='pause':
                        self.clip_set(id,index,status='blocked',quality_accepted=False,dialogue_adoption=None)
                        raise ReviewPaused('视频/对白共用次数已用完；按你选择的暂停策略等待处理。可改为采用最后结果后继续。')
                    report=dialogue_check.current_report(self.files,c)
                    decision=({'status':'adopted_ng','signature':report['signature'],
                               'attempt':attempt,'limit':cfg['review_video_attempts'],'created_at':time.time(),
                               'reason':'共用生成次数耗尽，按设置采用最后结果继续；对白核对仍未通过。'}
                              if dialogue_check.enabled(cfg) and report and not report.get('passed') else None)
                    self.clip_set(id,index,quality_accepted=True,video_reviewed=bool(verdict.get('video_reviewed',review_enabled(cfg,'video'))),
                                  adopted_ng=not verdict['passed'],dialogue_adoption=decision,quality_error='',status='complete')
                    self.store.event(id,f'第{index+1}段：'+('审核通过' if verdict['passed'] else
                        '共用次数耗尽，已采用最后一次NG视频继续'+('（对白未通过）' if decision else '')))
                    return
                def retry(p):
                    item=p['clips'][index]
                    report=copy.deepcopy(item.get('dialogue_check') or {})
                    item.setdefault('quality_history',[]).append({k:copy.deepcopy(item.get(k)) for k in ('output','raw_output','seed','prompt_en','prompt_zh','frame_asset_id','generation','dialogue_check','duration_seconds','generation_seconds','dialogue_timing')}|{'verdict':verdict,'attempt':attempt})
                    for key in ('output','raw_output','meta','prompt_id','job_id','api_graph','output_prefix','submission_unknown','finished_at','known_failed','retry_count','quality_verdict','quality_accepted','adopted_ng','video_reviewed','dialogue_adoption','prompt_en','prompt_zh','dialogue_check','prompt_compiler_version','compiler_warnings'):
                        item.pop(key,None)
                    dialogue_timing.prepare(p,item,cfg)
                    dialogue_timing.retry(p,item,cfg,report)
                    item.update(generation=int(item.get('generation',1))+1,quality_attempt=attempt+1,status='ready',
                                redo_feedback='修正视频/对白核对发现的问题：'+json.dumps(verdict.get('reasons',[]),ensure_ascii=False))
                    if not p.get('workflow_snapshot') or p['workflow_snapshot']['bindings'].get('seed'):
                        item['seed']=secrets.randbits(63)
                    p['planned_duration_seconds']=sum(c['duration_seconds'] for c in p['clips'])
                self.store.update('project',id,retry)
                updated=self.store.get('project',id)['clips'][index]
                if updated['duration_seconds']>c['duration_seconds']:
                    self.store.event(id,f'第{index+1}段缺尾重试：保留时长由{c["duration_seconds"]:g}增至{updated["duration_seconds"]:g}秒；仍只使用一次共用重做机会。')
                continue
            await self.prepare_clip(id,index,ai,cfg)
            await self.render_measured(id,index,comfy,{**cfg,'retry_limit':0})
            self.paused(id)
            p=self.store.get('project',id);c=p['clips'][index]
            speech=await self.check_dialogue(id,index,cfg,ai.session)
            if review_enabled(cfg,'video'):
                self.set(id,phase=f'自检第{index+1}段视频（第{c.get("quality_attempt",1)}次）')
                p=self.store.get('project',id);c=p['clips'][index]
                _,review_assets=self.clip_media(p,c)
                refs=[self.files.asset_path(a) for a in review_assets if a['kind']=='image']
                with measure('video_review',str(index+1)):
                    verdict=await reviewer.video(id,index,c,refs)
            else:
                verdict={'passed':True,'reasons':[],'summary':'对白核对完成；未开启视频视觉审核'}
            verdict=copy.deepcopy(verdict)
            verdict['video_reviewed']=bool(review_enabled(cfg,'video'))
            if not speech['passed']:
                verdict.update(passed=False,reasons=[speech['reason']]+verdict.get('reasons',[]),
                               summary='对白核对未通过'+('；'+verdict.get('summary','') if review_enabled(cfg,'video') else ''),
                               dialogue_failed=True,dialogue_uncertain=speech['status']=='needs_review')
            if not verdict['passed']:
                source=self.files.output_path(c['output'])
                target=reviewer.archive(id,'video_'+str(index+1),c.get('quality_attempt',1),source,verdict)
                # Commit the usable NG descriptor before removing the old output.
                self.clip_set(id,index,output=self.files.descriptor(target),quality_verdict=verdict,quality_attempt=c.get('quality_attempt',1))
                # Keep the original ComfyUI output as recovery evidence. It may
                # also be raw_output, and must survive an interrupted review.
            else:self.clip_set(id,index,quality_verdict=verdict,quality_attempt=c.get('quality_attempt',1))

    async def run(self,id):
        with scope(self.store,'project',id),measure('episode_active'):
            await self._run(id)

    async def _run(self,id):
        producer=None
        try:
            p=self.store.get('project',id)
            if p.get('workflow_snapshot'):
                self.set(id,workflow_snapshot=workflows.resolved(p['workflow_snapshot']))
            cfg=self.config(self.store.get('project',id))
            validate_review(cfg)
            async with aiohttp.ClientSession() as session:
                ai=AIClient(cfg,session);comfy=ComfyClient(cfg,session)
                self.set(id,phase='检查ComfyUI节点、模型和合并程序')
                snapshot=self.store.get('project',id).get('workflow_snapshot')
                if snapshot:
                    await comfy.preflight(snapshot['graph'],snapshot['output_node_id'])
                    self.store.event(id,'使用导入工作流：'+snapshot['name']+' v'+str(snapshot['version'])+'；视频参数保留导入值。')
                else:
                    check_graph=build_graph(self.template,{'prompt_en':'preflight','duration_seconds':cfg['duration_seconds'],'seed':cfg['seed'],'continuity':'cut'},cfg,media_state([],[],[]),None,f'{PREFIX}/check')
                    await comfy.preflight(check_graph)
                p=self.store.get('project',id)
                if cfg['image_provider']=='local':
                    image_snapshot=p.get('image_workflow_snapshots') or image_workflows.snapshots(self.store,cfg)
                    self.set(id,image_workflow_snapshots=image_snapshot)
                    await ImageGenerator(self.store,self.files,cfg,session,self.render_lock,image_snapshot).preflight()
                await command([cfg['ffmpeg'],'-version']);await command([cfg['ffprobe'],'-version'])
                await self.plan(id,ai,cfg);await self.create_missing_assets(id,ai,cfg)
                self.preparation_events.setdefault(id,asyncio.Event()).set()
                parallel=cfg.get('pipeline_enabled',True) and not cfg.get('gpu_handoff') and cfg.get('provider')!='local' and not ((review_enabled(cfg,'image') or review_enabled(cfg,'video')) and cfg.get('review_provider')=='local')
                self.set(id,execution_policy={'image_review':review_enabled(cfg,'image'),'video_review':review_enabled(cfg,'video'),'pipeline':parallel,
                    'dialogue_check':dialogue_check.enabled(cfg),'image_attempts':cfg['review_image_attempts'],'video_attempts':cfg['review_video_attempts']})
                if parallel:
                    await self.pipeline(id,ai,comfy,cfg)
                elif (review_enabled(cfg,'video') or dialogue_check.enabled(cfg)):
                    blocked=[]
                    for index in range(len(self.store.get('project',id)['clips'])):
                        self.paused(id)
                        clips=self.store.get('project',id)['clips']
                        if preparation_dependency(clips[index],index) is not None and not clips[index-1].get('quality_accepted'):
                            self.clip_set(id,index,status='blocked');blocked.append(f'第{index+1}段等待前段');continue
                        try:await self.reviewed_clip(id,index,ai,comfy,cfg)
                        except Paused:raise
                        except (SubmissionUnknown,APIError):raise
                        except Exception as error:
                            self.paused(id)
                            self.clip_set(id,index,status='blocked',quality_error=str(error))
                            blocked.append(f'第{index+1}段：{error}')
                            self.store.event(id,blocked[-1])
                    if blocked:raise ReviewPaused('部分任务等待处理；独立镜头已继续执行。'+'；'.join(blocked))
                else:
                    for index in range(len(self.store.get('project',id)['clips'])):
                        await self.prepare_clip(id,index,ai,cfg)
                        await self.render_measured(id,index,comfy,cfg)
                        self.clip_set(id,index,quality_accepted=True,video_reviewed=False)
                p=self.store.get('project',id);self.paused(id)
                if not all(c.get('output') and dialogue_check.resolved(self.files,c,cfg) for c in p['clips']):raise RuntimeError('仍有镜头未完成，不能合成成片。')
                self.ready_events.setdefault(id,asyncio.Event()).set()
                self.set(id,phase='合并成片，保留镜头原声')
                version=len(p.get('final_versions',[]))+1
                target=self.files.project_dir(id)/f'整集成片_v{version}.mp4'
                with measure('merge'):
                    result=await merge([self.files.output_path(c['output']) for c in p['clips']],target,cfg)
                self.set(id,status='complete',phase='成片已完成；可选择镜头重做',final={**result,**self.files.descriptor(target)},error='',pause_requested=False)
                self.store.event(id,'成片已完成。'+('视频和音频直接拼接，未重新编码。' if result['merge_mode']=='copy' else '镜头格式不同，已统一格式后合并。'))
        except (Paused,ReviewPaused) as e:self.set(id,status='paused',phase=str(e),pause_requested=False)
        except asyncio.CancelledError:
            self.set(id,status='paused',phase='服务停止，进度已保存；ComfyUI任务可继续',pause_requested=False);raise
        except Exception as e:
            self.set(id,status='error',phase='已保存进度，处理原因后点击继续',error=str(e),pause_requested=False)
            self.store.event(id,'暂停原因：'+str(e))
        finally:
            if producer and not producer.done():producer.cancel()
            if producer:
                try:await producer
                except (asyncio.CancelledError,Exception):pass
    def allow_resubmit(self,id,index):
        if id in self.tasks and not self.tasks[id].done():raise ValueError('请先暂停项目。')
        p=self.store.get('project',id);clip=p['clips'][index]
        if not clip.get('submission_unknown') or clip.get('prompt_id'):raise ValueError('此镜头不属于提交结果未知状态。')
        for key in ('job_id','api_graph','output_prefix','submission_unknown'):clip.pop(key,None)
        clip['status']='ready';self.store.put('project',id,p);self.store.event(id,f'用户确认第{index+1}段原任务不存在，允许重新提交。')
