#!/usr/bin/env python3
"""运镜小测试（合并稿编号 003，2026-10-11 13:50；hh 指出：全片几乎没有镜头语言，全是死板的固定镜头，是“怪异”的一大因素）。

事实（都核对过）：
  ① 002 稿 42 个任务全写了 "The camera holds still."；真实片段里镜头并不是真的不动（第 15 集 10 个里 3 个自己慢慢推近、1 个横移，4 个不动），
     只是没有目的地漂。
  ② 我当初改成“镜头固定”，是因为最早一次写 "pushes in with small amplitude at slow speed"（6 秒任务）放大了 3–4 倍、脸糊成特写（手册 O29，3/3）。
     当时手册写着“要运镜时单独做一个任务验证”——之后所有集都没做。这里补上。
  ③ 第三方资料（转述 MiniMax 官方提示词指南，未核实原文）：H3 的运镜用自然英语写，格式“镜头动作＋幅度＋速度”，一个镜头一个运镜；
     幅度小/大、速度慢/快的修饰词写了未必听。所以这里一律不写修饰词，只写“动作＋终点”（推近到刀刃占满画面、拉远到整间屋子入画），
     看默认幅度够不够用。
  ④ 05（拔匕首，没有毒液）→ 06（匕首特写，刃口有毒液，人不见了）是同一件事被拆成两个镜头：人没了、毒液凭空出现。
     T1 把它们并成一个镜头：先拍人举匕首，再推近到刃口，毒液在推近过程中渗出来。

五个任务（同一间客厅、同一批人物，素材全部沿用 002，没有新增）：
  T1  匕首一镜到底：中近景→推近到刃口特写，毒液渗出（5 秒，无台词）。验证“一件事一个镜头”＋推近的幅度能不能停在刀刃上。
  T2  同 T1，只把运镜写成方括号 [Push in]（同种子）。验证方括号写法在 H3 里有没有用、会不会被念出来。
  T3  玛丽看手机说一句话，运镜写“推近”。种子、开场图文字、台词都和 002 第 15 集 07 号相同，只差运镜一句（07 号就是对照）。验证说台词时推近：脸会不会糊、声音会不会变。
  T4  拉远揭示：保罗攥戒指的中近景→拉远到整间破败的客厅（5 秒，无台词）。验证拉远能不能把场景交代出来、有没有冒出多余的人。
  T5  跟拍：玛丽和猎手边走边被横向跟拍（5 秒，无台词）。002 里 02 号“走进来”两人其实没动；这里开场图就画成迈步中，运镜写跟拍。
种子：7001（T1、T2 同种子，故意）、6507（T3，与 002-07 同种子，故意）、7004、7005。
"""
import copy, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _h3draft import Batch, FOLDER, breathy

BASE = '合并稿/002_第15-18集_重写故事_制作稿_追加.json'
OUT = '合并稿/003_运镜测试_制作稿_追加'
SRC = json.load(open(os.path.join(FOLDER, BASE), encoding='utf-8'))
a = Batch(BASE, SRC['title'], 7000)

PV = '[[asset:paul_villa]]'; PL = '[[asset:paul]]'; MB = '[[asset:mary_black]]'; RG = '[[asset:rogue]]'
LAY_PV = (" Fixed stage layout: the tall bay window with torn curtains and cold pale dawn light is at frame-left; the overturned leather sofa and the shards of the smashed coffee table are in the middle; "
          "the wide double doorway to a dim hallway is at frame-right; the smashed wooden cabinet stands against the back wall under bare walls with pale rectangles where paintings once hung.")
END_PV = " Cold pale dawn light, dust hanging in the air, the wrecked room softly blurred behind."


def T(title, dur, chars, assets, img, vis_zh, cam_zh, shot_en, shot_zh, sound, dlg=None, seed=None):
    s = a.task(title, dur, chars, assets, ['paul_villa'], img, END_PV + LAY_PV, vis_zh, cam_zh, dlg, shot_en, shot_zh, sound)
    s['depends_on_previous'] = False
    if seed:
        s['seed'] = seed
    return s


# ---------------------------------------------------------------- T1 / T2 匕首一镜到底（推近）
ROGUE_IMG = ("Medium close-up of Rogue alone, from the head to the chest, in profile facing frame-left, in the middle third of the frame, in the patched black leather jacket, "
             "the long scar down his left cheek and across his eye, his right hand holding the silver dagger up in front of his chest, the polished blade pointing up and catching the pale light, "
             "his heavy brows lowered, his lips curling into a cruel grin over yellowed teeth, his narrowed eyes on the blade. The frame holds exactly one person, Rogue.")
ROGUE_ACT = (f"A steady medium close-up opens from the adopted first frame in {PV}: {RG} tilts the silver dagger a little toward the light, his lips curling into a cruel grin over his yellowed teeth, "
             "his heavy brows low and his narrowed eyes on the blade. ")
VENOM = ("a bead of pale green venom swells at the edge near the tip, slides down the polished steel and drips, a faint wisp of smoke rising where it falls.")
ROGUE_SND = breathy("A faint hiss like acid dripping and the creak of leather.", "一声像酸液滴落的细微嘶声和皮革的吱嘎声。")

T('01｜运镜·匕首一镜到底（自然语言推近）', 5, ['Rogue'], ('paul_villa', 'rogue'), ROGUE_IMG,
  "流浪狼人举着银匕首向光里偏了偏；镜头从中近景推近到刀刃占满画面，一滴淡绿色毒液在刃口鼓起、滑落。",
  "0—5秒，镜头从中近景推近，直到刀刃占满画面。",
  ROGUE_ACT + "The camera pushes in toward the blade until the blade fills the frame; " + VENOM,
  "一个稳定的中近景，从已采用的开场图继续，场景是破败的客厅：流浪狼人把银匕首向光里偏了偏，咧开的残忍笑容露出发黄的牙，眉头压得很低，眯着的眼睛盯着刀刃。镜头向刀刃推近，直到刀刃占满画面；"
  "一滴淡绿色的毒液在刃口靠近尖端的地方鼓起，顺着打磨光亮的钢刃滑下、滴落，落下的地方升起一缕细细的烟。",
  ROGUE_SND, seed=7001)

T('02｜运镜·匕首一镜到底（方括号写法）', 5, ['Rogue'], ('paul_villa', 'rogue'), ROGUE_IMG,
  "同上，只把运镜写成方括号 [Push in]（同种子）。",
  "0—5秒，镜头从中近景推近，直到刀刃占满画面。",
  ROGUE_ACT + "[Push in] toward the blade until the blade fills the frame; " + VENOM,
  "一个稳定的中近景，从已采用的开场图继续，场景是破败的客厅：流浪狼人把银匕首向光里偏了偏，咧开的残忍笑容露出发黄的牙，眉头压得很低，眯着的眼睛盯着刀刃。[推近]向刀刃推近，直到刀刃占满画面；"
  "一滴淡绿色的毒液在刃口靠近尖端的地方鼓起，顺着打磨光亮的钢刃滑下、滴落，落下的地方升起一缕细细的烟。",
  ROGUE_SND, seed=7001)

# ---------------------------------------------------------------- T3 说台词时推近（002 第 15 集 07 号 + 只换运镜一句）
t07 = copy.deepcopy(SRC['episodes'][0]['segments'][6])
assert t07['title'].startswith('07｜') and t07['seed'] == 6507
t07['title'] = '03｜运镜·说台词时推近（对照：第15集07号）'
t07['camera_zh'] = '0—6秒，镜头向前推近。'
t07['visual_zh'] = '玛丽看着手机说台词；同第15集07号，只是运镜由“固定”改成“推近”。'
sh = t07['shots'][0]
assert sh['visual_en'].endswith('The camera holds still.') and sh['visual_zh'].endswith('镜头固定不动。')
sh['visual_en'] = sh['visual_en'][:-len('The camera holds still.')] + 'The camera pushes in.'
sh['visual_zh'] = sh['visual_zh'][:-len('镜头固定不动。')] + '镜头向前推近。'
a.tasks.append(t07)

# ---------------------------------------------------------------- T4 拉远揭示
T('04｜运镜·拉远揭示整间屋子', 5, ['PaulOnScreen'], ('paul_villa', 'paul'),
  "Medium close-up of Paul alone, from the head to the chest, in profile facing frame-right, in the middle third of the frame, sitting on the dusty floor with his back against the overturned leather sofa, "
  "in the creased navy blazer over a white open-collared shirt, a dark purple bruise ringing his throat above the open collar, his right fist clenched around a small diamond ring held at chest height, "
  "his jaw trembling, his lips pulled tight, his brows drawn together, his red-rimmed wet eyes on the ring. The frame holds exactly one person, Paul.",
  "保罗攥着戒指，眼里有泪；镜头从中近景拉远，直到整间破败的客厅入画，保罗坐在翻倒的沙发边显得很小。",
  "0—5秒，镜头从中近景拉远，直到整间客厅入画。",
  f"A steady medium close-up opens from the adopted first frame in {PV}: {PL} squeezes the diamond ring in his fist, his jaw trembling, his lips pulled tight, his brows drawn together and a tear sliding from his red-rimmed eyes. "
  "The camera pulls out until the whole wrecked living room is in the frame and Paul sits small against the overturned sofa.",
  "一个稳定的中近景，从已采用的开场图继续，场景是破败的客厅：保罗把钻戒攥在拳头里，下颌发抖，嘴唇紧抿，眉头拧在一起，一滴泪从发红的眼睛里滑下来。镜头向后拉远，直到整间破败的客厅入画，保罗坐在翻倒的沙发边显得很小。",
  breathy("A rattling breath and the faint creak of the old floor.", "一声发颤的喘息和旧地板细微的吱嘎声。"), seed=7004)

# ---------------------------------------------------------------- T5 跟拍
T('05｜运镜·跟拍两人走进来', 5, ['MaryBlack', 'Rogue'], ('paul_villa', 'mary_black', 'rogue'),
  "Side-on medium two-shot, both people from the head to the knees, in the middle third of the frame, in the wrecked living room, both in profile facing frame-left and both caught mid-stride, walking. "
  "Mary in front at frame-left in a fitted black wool coat over a black dress and black high heels, her honey-blonde hair in a tight low bun, her chin lifted, her lips set in a cold smug smile, her sharp green eyes ahead of her, one heel just lifting off the floor. "
  "Rogue one step behind her at frame-right, a lean wiry man in a patched black leather jacket, a thick jagged scar down his left cheek and across his eye, his heavy brows lowered, his lips pulled into a cruel half-grin over yellowed teeth, his right hand resting on a sheathed silver dagger at his belt, his narrowed eyes on the back of Mary's head. "
  "The frame holds exactly two people: Mary and Rogue.",
  "玛丽和猎手一前一后穿过破败的客厅，镜头横向跟着他们走。",
  "0—5秒，镜头横向跟拍，两人始终在画面中间。",
  f"A steady side-on medium two-shot opens from the adopted first frame in {PV}: {MB} walks briskly across the wreckage, her heels crunching on broken glass, her chin lifted and her cold smug smile widening. "
  f"{RG} follows one step behind, his right hand tapping the hilt of the sheathed dagger, his lips curling into a cruel half-grin over his yellowed teeth and his heavy brows low. "
  "The camera tracks sideways with them, keeping both in the middle of the frame as they cross the room.",
  "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是破败的客厅：玛丽快步走过一地狼藉，高跟鞋踩在碎玻璃上咯吱作响，下巴抬起，冷冷的得意笑容更深。流浪狼人跟在她身后一步，右手轻轻敲着鞘里匕首的柄，咧开的残忍笑容露出发黄的牙，眉头压得很低。"
  "镜头横向跟着他们，两人始终在画面中间，一起穿过房间。",
  breathy("High heels crunching over broken glass and slow, heavy boot steps.", "高跟鞋踩过碎玻璃的咯吱声和缓慢沉重的靴子声。"), seed=7005)

a.finish('运镜测试（剧本第15集场景）', '同一间客厅里的 5 个运镜镜头：推近到刀刃、方括号写法、说台词时推近、拉远揭示、跟拍。', OUT)
