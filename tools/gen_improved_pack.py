"""生成改进稿（12 个任务）。读取旧稿 JSON 当底板，写出改进稿 JSON 和全选复制粘贴 txt。
用法: python3 tools/gen_improved_pack.py
"""
import json,copy,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PACK_OLD=os.path.join(ROOT,'packs','旧稿_3集x15任务','旧稿_制作稿.json')
PACK_NEW=os.path.join(ROOT,'packs','改进稿_12任务')
base=json.load(open(PACK_OLD,encoding='utf-8'))
SEED=1001
d=copy.deepcopy(base)
d['title']='H3试验片｜第3轮'
d['style']=("Photorealistic live-action romantic thriller with a glossy, high-end drama look. Warm tungsten key light with a soft cool fill, "
 "shallow depth of field, rich natural skin texture with visible pores, luxurious cream-and-gold interiors, restrained cinematic color grading, "
 "and an ultra-wide 8:3 cinemascope frame in which the people are placed deliberately and the room is visible around them.")
LEAD=("Live-action, cinematic, photorealistic with natural skin texture, shallow depth of field and warm luxurious lighting, ultra-wide 8:3 cinemascope frame. ")
IMG=("One coherent first frame from a photorealistic live-action romantic thriller, ultra-wide 8:3 cinemascope composition. "
     "Natural skin with visible pores, realistic fabric and materials. The fixed scene reference defines the room, and the character portraits define only the named people. ")
IMGEND=" Warm luxurious light, the fitting room softly blurred behind."
SOUND_EN="Quiet room tone and a faint brush of fabric. Voices stay close and clear."
SOUND_ZH="安静的房间底噪和轻微的衣料摩擦声。人声近而清楚。"
SILENT_EN=("Only the faint rustle of silk and quiet room tone. The recording is completely free of voices: no speech, no humming, no sighs, no vocal sounds of any kind.")
SILENT_ZH="只有丝绸的轻微摩擦声和安静的房间底噪。录音里完全没有人声：没有说话、哼声、叹息或任何发声。"
def seg(title,dur,chars,img,vis_zh,cam_zh,dlg,shots,sound=('en','zh')):
    s={'title':title,'duration_seconds':dur,'generation_seconds':dur,'continuity':'cut','depends_on_previous':False,
       'use_previous_episode_state':False,'characters':chars,'asset_keys':['room','lily','killian'],'image_reference_keys':['room'],
       'image_prompt':IMG+img+IMGEND,'visual_zh':vis_zh,'camera_zh':cam_zh,
       'dialogue':[{'speaker':sp,'text':tx,'start_seconds':a,'end_seconds':b,'language':'zh'} for sp,tx,a,b in dlg],
       'shots':[],'sound_en':sound[0] if sound!=('en','zh') else SOUND_EN,'sound_zh':sound[1] if sound!=('en','zh') else SOUND_ZH,
       'seed':SEED,'dialogue_language':'zh'}
    for a,b,en,zh,idx in shots:
        s['shots'].append({'start_seconds':a,'end_seconds':b,'visual_en':en,'visual_zh':zh,'dialogue_indices':idx})
    return s
K='[[asset:killian]]';L='[[asset:lily]]';R='[[asset:room]]'
LINE='你养父母欠了我三千万美金。'
solo_img=("Medium shot of Killian alone in the center of the frame, in his black suit, his body angled slightly to the left, his eyes fixed on the closed dark door at the left side of the room. Nobody else is in the frame. His hands hang at his sides.")
def solo_vis(extra=''):
    return (LEAD+f"A steady medium shot opens from the adopted first frame in {R}: {K} alone in the center of the frame, eyes fixed on the door at the left side of the room. No one else is visible. "
            f"His jaw is tight and his mouth set in a flat line; he speaks in a quiet, low, menacing voice without moving his gaze from the door. The camera holds still."+extra)
tasks=[]
tasks.append(seg('E1 互相对视',6,['Lily','Killian'],
 "Wide two-shot at eye level: Lily in her ivory silk gown on the left and Killian in his black suit on the right stand about one stride apart, turned toward each other in near-profile, each looking at the other's face. Both fully visible from head to knees, centered in the frame as a pair. Their hands hang at their sides.",
 "两人面对面站着互相看对方，基利安说一句短台词。","0—6秒宽双人镜头，镜头固定。",
 [('Killian','走吧，车在楼下。',0.5,3.2)],
 [(0,6,LEAD+f"A steady wide two-shot opens from the adopted first frame in {R}: {K} and {L} face each other about one stride apart, each looking at the other's face. {K} speaks calmly in a low voice. {L} listens with her lips pressed together and a slight tension in her jaw. Both keep their positions. The camera holds still.","宽双人镜头，面对面互相看，基利安说话，莉莉听。",[0])]))
tasks.append(seg('E2 单人看门',6,['Killian'],solo_img,"基利安单人居中，视线落在左边的门上，说一句短台词。","0—6秒中景单人居中，镜头固定。",
 [('Killian','你逃不掉的。',0.5,2.8)],[(0,6,solo_vis(),"基利安居中，视线落在门上，说话。",[0])]))
tasks.append(seg('P3 手腕握住',6,['Lily','Killian'],
 "Side-on wide two-shot at eye level, the pair centered in the frame: Killian in a black suit and Lily in her ivory gown stand facing each other. His right hand, with his whole arm and shoulder fully visible, holds her left wrist at chest height. Both faces are visible in profile, her eyes fixed on his face.",
 "手腕握住：握人的人的肩、臂、手都在画面里。","0—6秒侧面宽双人镜头，镜头固定。",
 [('Lily','你放开我！',0.5,2.5)],
 [(0,6,LEAD+f"A steady side-on wide two-shot opens from the adopted first frame in {R}: {K} stands facing {L}; his right hand, with his whole arm and shoulder visible in the frame, holds her left wrist at chest height and keeps the same grip. Her eyes stay on his face. She speaks in a tight, trembling, low voice. {K} looks down at her with his jaw tight. The camera holds still.","侧面宽双人，基利安右手握住莉莉左手腕，莉莉看着他说话。",[0])]))
def turn_seg(title,name):
    return seg(title,6,['Lily','Killian'],
 "Wide two-shot at eye level: Lily in her ivory silk gown on the left, her body angled toward Killian and her face turned toward him; Killian in his black suit on the right, looking at her. They stand about one stride apart, centered in the frame as a pair.",
 f"姿势已经在开场图里：莉莉面向基利安，只说话。台词里的名字：{name}。","0—6秒宽双人镜头，镜头固定。",
 [('Lily',f'{name}，你疯了吗？',0.5,3.0)],
 [(0,6,LEAD+f"A steady wide two-shot opens from the adopted first frame in {R}: {L} stands angled toward {K}, her face turned to him, her eyes wide; {K} looks back at her. They keep their positions and posture. She speaks in a tight, trembling, low voice. The camera holds still.","莉莉面向基利安，保持姿势，说话。",[0])])
tasks.append(turn_seg('T3 姿势在开场图·名字基利安','基利安'))
tasks.append(turn_seg('N2 同T3·名字换成凯文','凯文'))
tasks.append(seg('M3 俯身耳语',6,['Lily','Killian'],
 "Wide two-shot in three-quarter view from the side, the pair centered in the frame: Lily on the left looks down at the carpet with tense shoulders; Killian stands close behind her and slightly to the right, his head bent toward her ear.",
 "不用镜子：基利安俯身耳语，莉莉视线落在地毯上。","0—6秒宽双人镜头，镜头固定。",
 [('Killian','别动，看着我。',0.5,2.8)],
 [(0,6,LEAD+f"A steady wide two-shot opens from the adopted first frame in {R}: {L} stands in front with her eyes on the carpet, her shoulders tense and her breathing short; {K} stands close behind her and slightly to her right. He lowers his head toward her ear and speaks in a low voice. She keeps her eyes on the carpet. The camera holds still.","基利安俯身对着莉莉耳边说话，莉莉看着地毯。",[0])]))
for ttl,dur in (('D1 同一句话·6秒',6),('D3 同一句话·5秒',5),('D4 同一句话·8秒',8)):
    tasks.append(seg(ttl,dur,['Killian'],solo_img,f"同一句台词放进{dur}秒的任务，量开口时间和结束时间。",f"0—{dur}秒中景单人居中，镜头固定。",
     [('Killian',LINE,0.5,3.8)],[(0,dur,solo_vis(),"基利安居中，视线落在门上，说话。",[0])]))
tasks.append(seg('D2 同一句话·6秒·第4.2秒切镜',6,['Lily','Killian'],solo_img,"同一句台词，第一镜 0—4.2 秒基利安说话，第二镜 4.2—6 秒切到莉莉的反应，不说话。","0—4.2秒基利安中景；4.2—6秒莉莉近景。",
 [('Killian',LINE,0.5,3.8)],
 [(0,4.2,solo_vis(),"基利安居中，视线落在门上，说话。",[0]),
  (4.2,6,f"The camera cuts to a medium close-up of {L} in the center of the frame, her eyes wide and her lips parted. She does not speak. She keeps her eyes on the door at the left side of the room. The camera holds still.","切到莉莉近景，眼睛睁大，不说话，视线落在门上。",[])]))
def silent(title,sound,desc):
    return seg(title,6,['Lily'],
 "Medium shot of Lily alone in her ivory silk gown, standing near the center of the frame with her back half turned, her head turned over her shoulder toward the door at the left side of the room, her hands reaching behind her back toward the zipper. Nobody else is in the frame.",
 desc,"0—6秒中景单人，镜头固定。",[],
 [(0,6,LEAD+f"A steady medium shot opens from the adopted first frame in {R}: {L} alone, no one else visible. She reaches behind her back and pulls the zipper of her gown up to the nape. Nothing else moves. Nobody speaks. The camera holds still.","莉莉独自拉上婚纱拉链，没有人说话。",[])],sound=sound)
tasks.append(silent('S1 无台词·明确无人声',(SILENT_EN,SILENT_ZH),"无台词片：声音描述里明确写了没有任何人声。"))
tasks.append(silent('S2 无台词·旧写法',(SOUND_EN,SOUND_ZH),"无台词片：沿用旧的声音描述（对照用）。"))
lines=[]
for t in tasks:
    lines.append((t['title'].split(' ')[0]+' '+t['visual_zh']).replace('：','，'))
    for x in t['dialogue']: lines.append(f"{x['speaker']}：“{x['text']}”")
d['episodes']=[{'title':'试验片第3轮｜种子1001','summary':f'第3轮试验片，共{len(tasks)}个任务，全部使用种子1001，按手册6.7的新规则重写，并测台词开口时间随任务时长的变化。',
 'script':'\n'.join(lines),'segments':tasks,'dialogue_language':'zh'}]
json.dump(d,open(os.path.join(PACK_NEW,'改进稿_制作稿.json'),'w',encoding='utf-8'),ensure_ascii=False,indent=1)
open(os.path.join(PACK_NEW,'改进稿_全选复制粘贴.txt'),'w',encoding='utf-8').write(json.dumps(d,ensure_ascii=False,indent=1))
print(len(tasks),'tasks written')
