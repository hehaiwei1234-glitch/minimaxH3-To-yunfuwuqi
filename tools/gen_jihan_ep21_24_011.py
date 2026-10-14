#!/usr/bin/env python3
"""《极寒末日：我的隐秘安全屋》剧本第 21–24 集，追加稿 011（2026-10-14）。以 010 的 JSON 为底（style／素材／角色逐字复制），必须等 010 在插件里全部跑完再追加。
hh 2026-10-14 11:11：“17-20、21-24 四集四集更新，先更新这 8 集。”

写法＝010 同一套（每个任务先定景别＋机位＋运镜；每句台词带语气；两人以上写 exactly N people；dep 一律不用；对话任务 ≤12 秒；机械／物理变化只拍结果）。
偏离大纲（交稿时已告诉 hh）：
  · 第 21 集：两台游戏主机、雪茄不拍（电子娱乐删除）；“一整墙名酒、雪茄”只在背景里；盲盒里只拍护肤品、香水、酒红色真丝睡袍（长袖、高领、系腰带）；
    “灯光黯淡一半”拍成结果（开场图里天花板一半的灯已灭）；
  · 第 22 集：身体贴合改成并排挤在窄井里、双手撑着井壁、不碰对方；“苏医生，你最好快点……不然我可能先做点别的事”改成“苏医生，你最好快一点”；
    水管崩开只拍一个 6 秒任务（开场图是刚裂开一条缝），林峰用身体护住她，不写“曲线毕露”；
  · 第 23 集：吻保留（穿着衣服、不露骨）；“抱着她吻着退回生活区”拆成“并肩走回生活区（腿软／我扶着你）”；林峰不脱衬衫，只擦头发；
    《同居守则》第三条 → “守则第三条，禁止越界接触。”；收音机里的陌生人声音，用一台摆在画面里的军用收音机“出声”（旁白式），不画人；
  · 第 24 集：大纲里嘲笑林峰的“王局长”→ 林峰的前合伙人周宁（我们的故事里气象局局长没出现过，周宁在第 1 集出现过）；
    “几千难民涌来”只用台词，不拍人群。
H3 方面的风险（交稿时单列，不算我的错）：
  · 21-01 冰雕被新雪盖住（静止画面）；21-03 美工刀划胶带＋掀盖子；21-07 天花板一半灯灭（开场图要画对）；
  · 22-03 两人并排挤在窄井里（空间、手脚）；22-04 阀门轮转了四分之一（机械）；22-05 水管崩开、喷水、林峰护住她（快大动作，单独 6 秒）；
  · 23-01 亲吻（两张脸可能融合、可能自己切镜）；23-04 蒸汽里的浴室门；23-05 倒酒、擦头发（手部动作）、独白时嘴型；
  · 23-06、24-01、24-03、24-04 收音机“旁白”：画面里只有收音机和人，收音机里的声音可能被画成多出来一个人，或者让画面里的人张嘴念；
  · 开场图约一成不按文字画；“同一处”场景（供给大厅、窄井）用参照图（没测过）。
"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _jihan_base5 import *

OUT = '合并稿/011_第21-24集_盲盒窄井越界幽灵电台_制作稿_追加'
S = Session('合并稿/010_第17-20集_猎犬热成像诱饵井蒸汽闪冻冰雕广场_制作稿_追加.json', OUT, 41000)

# ---------------------------------------------------------------------------------------------- 新外貌
look('su_silk', 'SuSilk', "in a long wine-red satin robe-style nightgown with long sleeves and a high neckline belted at the waist, a white towel around her neck, her damp long black hair loose over her shoulders", 'soft dark-brown', 'her', eth=CN_F28)
# 收音机里的声音：只出声，不进画面（人物素材用收音机本身）
look('radio_op', 'RadioOp', "a military long-wave radio", 'none', 'its')
look('radio_ning', 'RadioNing', "a military long-wave radio", 'none', 'its')

# ---------------------------------------------------------------------------------------------- 场景
DEPOT = Scene('supply_hall', " Rows of ceiling sensor lamps glow warm white over the huge underground supply hall.",
              " Fixed stage layout: tall steel shelves packed with sacks of rice and flour and cases of canned food fill the left half of the frame; a wall of wine and liquor bottles with stacked cigar crates fills the back wall; a wide concrete aisle runs through the middle of the frame; a pallet with three large black sealed plastic boxes stands in the corner at frame-right.")
DEPOT_DIM = Scene('supply_hall', " Half of the ceiling lamps have gone dark, so the left side of the huge hall lies in deep shadow while the right side glows dimly.",
                  DEPOT.layout + " A square metal ventilation grille is set in the ceiling above the aisle in the middle of the frame.")
DEPOT_BOX = Scene('supply_hall', DEPOT.end,
                  " Fixed stage layout: a large black plastic box stands open in the middle of the frame on the concrete floor, its lid tipped back, its contents neatly packed; tall steel shelves of rice sacks and canned food rise behind it.")
SHAFT = Scene('service_shaft', " Dim yellow work-lamp light and drifting damp warmth fill the cramped maintenance shaft.",
              " Fixed stage layout: a narrow concrete shaft runs horizontally across the frame from right to left, barely wider than a person's shoulders; a thick insulated pipe runs along its upper wall with a flanged joint in the middle; a rusted red valve wheel sits at the far left end; damp concrete walls close in on both sides.")
SHAFT_LEAK = Scene('service_shaft', SHAFT.end, SHAFT.layout + " A hair-thin crack has just opened at the flanged joint and a thin jet of warm water hisses from it.")
SHAFT_WET = Scene('service_shaft', " Dim yellow work-lamp light and drifting white steam fill the cramped maintenance shaft; warm water streams down the walls.",
                  SHAFT.layout + " The flanged joint above has been sealed by its own pressure and only drips; thin steam hangs in the air.")
PUMP_GAUGE = Scene('pump_room', PUMP.end, PUMP.layout + " A big round pressure gauge with a red danger zone is mounted above the control panel in the middle of the frame, its needle quivering deep in the red; thin jets of steam hiss from the pipe seams.")
CORRIDOR = Scene('bunker_hall', " Warm lamps glow along the bare concrete service corridor.",
                 " Fixed stage layout: a bare concrete service corridor recedes down the middle of the frame with thick pipes running along the ceiling and warm lamps at regular intervals; a heavy steel door stands at the far end.")
SOFA2 = Scene('bunker_sofa', SOFA.end, SOFA.layout + " A folded wine-red silk nightgown lies on the arm of the sofa.")
LIVING_GLASS = Scene('bunker_living', LIVING.end,
                     " Fixed stage layout: the open kitchen with a black-and-gold stove and a marble counter is at frame-left, a crystal glass and a bottle of amber whiskey standing on the counter; a thick cream wool rug and the small round wooden dining table fill the middle of the frame; a wall of small security monitors is at frame-center-right; the heavy round steel hatch door is in the right wall at far frame-right.")
BATH2 = Scene('bathroom', BATH.end, BATH.layout + " A folded wine-red silk nightgown lies on the wooden bench beside the towels.")
CONTROL_R = Scene('bunker_control', CONTROL.end, CONTROL.layout + " A steel side table at frame-right holds an olive-green military long-wave radio with a large round dial glowing amber, a pole antenna and a cloth speaker grille.")

# ---------------------------------------------------------------------------------------------- 声音
RADIOOP_EN = "A thin, exhausted adult woman's voice heard through crackling radio static, hoarse and halting, speaking clear Mandarin Chinese." + VT_EN
RADIOOP_ZH = '隔着收音机沙沙杂音传来的、疲惫沙哑、断断续续的成年女声，普通话清楚。' + VT_ZH
RADIONING_EN = 'A hoarse adult male voice heard through crackling radio static, frantic and pleading, breaking into a shout, speaking clear Mandarin Chinese.' + VT_EN
RADIONING_ZH = '隔着收音机沙沙杂音传来的、嘶哑的成年男声，慌乱又哀求，说到后面喊了起来，普通话清楚。' + VT_ZH
SOUND_DEPOT = voiced('The faint hum of the air system, the soft click of ceiling sensor lamps and quiet footsteps on concrete.', '空气系统轻微的嗡鸣、天花板感应灯轻轻的咔哒声和水泥地上安静的脚步声。')
SOUND_DEPOT_B = breathy('The faint hum of the air system and the soft rustle of tissue paper and glass jars.', '空气系统轻微的嗡鸣、薄纸和玻璃瓶罐轻轻的窸窣声。')
SOUND_DEPOT_DIM = voiced('A heavy dull hum that fades away overhead and the faint tick of cooling lamps.', '头顶渐渐消失的沉闷嗡鸣和灯管冷却时细细的嘀嗒声。')
SOUND_GAUGE = breathy('The hiss of steam from the pipe seams and a rising low groan of straining metal.', '管缝里蒸汽的嘶嘶声和金属绷紧时越来越响的低沉呻吟。')
SOUND_PUMP = voiced('The hiss of steam from the pipe seams and the low groan of straining metal.', '管缝里蒸汽的嘶嘶声和金属绷紧时低沉的呻吟。')
SOUND_SHAFT = voiced('The close drip of water, the faint groan of old pipes and slow breathing in a tight space.', '近处的滴水声、老旧管道细细的吱呀声和狭窄空间里缓慢的呼吸声。')
SOUND_SHAFT_B = breathy('Heavy breathing in a tight space, the squeal of a rusted wheel turning and a deep clunk.', '狭窄空间里粗重的呼吸声、生锈轮子转动的尖响和一声沉闷的咔哒。')
SOUND_BURST = breathy('A sudden roar of hissing water, a startled gasp and steam filling a tight space.', '突然爆出的水声嘶吼、一声受惊的抽气和狭窄空间里涌起的蒸汽。')
SOUND_SHAFT_W = breathy('Dripping water, soft steam and two people breathing hard.', '滴水声、轻轻的蒸汽声和两个人粗重的呼吸。')
SOUND_CORR = voiced('The soft squelch of wet shoes on concrete, the hum of the pipes and a low shaky laugh.', '湿鞋子踩在水泥地上轻轻的啪嗒声、管道的嗡鸣和一声低低发颤的笑。')
SOUND_WARM = voiced('The faint hum of the air system and the soft rustle of a towel.', '空气系统轻微的嗡鸣和毛巾轻轻的摩擦声。')
SOUND_SHOWER = breathy('The soft steady patter of a shower behind a door and a hush of steam.', '门后淋浴轻轻稳定的哗哗声和蒸汽的轻响。')
SOUND_GLASS = voiced('The clink of a bottle against crystal, the gentle pour of whiskey and the faint hum of the air system.', '酒瓶碰到水晶杯的轻响、威士忌缓缓倒进杯子的声音和空气系统轻微的嗡鸣。')
SOUND_RADIO = voiced('Crackling radio static with a thin tuning whistle and the faint hum of the control room.', '收音机沙沙的杂音、细细的调频啸叫和控制室轻微的嗡鸣。')
SOUND_RADIO_B = breathy('Crackling radio static, a thin tuning whistle and a trembling speaker cone.', '收音机沙沙的杂音、细细的调频啸叫和扬声器纸盆的震颤声。')


def insert_task(tid, title, dur, scene, framing, act_en, zh, snd, holds, cam, bg='', extra_assets=(), groups=()):
    return S.T(tid, title, dur, scene, [], framing, act_en, zh, snd, cam=cam, holds=holds, room={g[0] for g in groups}, groups=list(groups), new=True, bg=bg, extra_assets=extra_assets)


# ================================================================================================ 第 21 集
b21 = S.episode('剧本第21集｜末日里的顶级盲盒', '大雪封山第十五天，外面坑边的冰雕被新雪盖住；地下三层物资大厅里，感应灯一排排亮起，苏清月被满墙的粮油酒震住；林峰指着角落的黑色密封箱：给你准备的；箱子里是护肤品、香水和酒红色真丝睡袍；她问你怎么知道我的尺码，他说从你签合同那天起，活下去靠卡路里，活得像人靠这些没用的东西；头顶的通风格栅嗡嗡一响，大厅的灯暗了一半：地源热泵的阀门卡住了。', 21)
new_person(b21, 'su_silk', '苏清月（酒红色长袖真丝睡袍，高领系腰带，毛巾搭在脖子上，湿发披肩）', 'woman',
           'Su, the same elegant Chinese woman in her late twenties as in the reference, wearing a long wine-red satin robe-style nightgown with long sleeves and a high neckline belted at the waist, a white towel around her neck, her damp long black hair loose over her shoulders.',
           '苏清月，和参考图是同一位二十八岁左右、优雅美丽的中国女性，穿着长袖高领、腰间系带的酒红色真丝睡袍，脖子上搭着一条白毛巾，湿的长黑发披在肩上。',
           'wearing a long wine-red satin robe-style nightgown with long sleeves and a high neckline belted at the waist, a white towel around her neck, her damp long black hair loose over her shoulders',
           'a soft, relaxed expression', ref='su_cozy')
b21.prop('radio_set', '军用长波收音机（橄榄绿钢壳，大圆形调谐盘亮着琥珀色，一根杆状天线，布面扬声器）',
         'An olive-green steel military long-wave radio with a large round tuning dial glowing amber, two big knobs, a pole antenna on top and a cloth-covered speaker grille. The reference fixes its shape.',
         '一台橄榄绿钢壳的军用长波收音机：大圆形调谐盘亮着琥珀色的光，两个大旋钮，顶上一根杆状天线，布面的扬声器。参考图固定它的外形。',
         'A photorealistic product shot of an olive-green steel military long-wave radio with a large round tuning dial glowing amber, two big knobs, a pole antenna on top and a cloth-covered speaker grille, standing on a steel side table against a plain neutral gray background.')
new_scene(b21, 'supply_hall', '地下三层物资大厅（钢货架堆满米面罐头，后墙是一整面酒和雪茄箱）',
          'A vast underground supply hall: tall steel shelves packed with sacks of rice and flour and cases of canned food fill the left half, a wall of wine and liquor bottles with stacked cigar crates fills the back wall, a wide concrete aisle runs through the middle, and a pallet with three large black sealed plastic boxes stands in the corner at the right.',
          '宽阔的地下物资大厅：左半边是堆满米面袋和罐头箱的高大钢货架，后墙是一整面酒瓶和叠着的雪茄箱，中间是一条宽阔的水泥过道，右边墙角的托盘上放着三个大黑色密封塑料箱。',
          'the tall steel shelves, the wall of bottles and cigar crates and the pallet of black boxes in the corner')
new_scene(b21, 'service_shaft', '狭窄的混凝土检修井（只比肩膀宽一点，有一条粗保温管，尽头是一个生锈的红色阀门轮）',
          'A very narrow horizontal concrete maintenance shaft, barely wider than a person\'s shoulders, with dim yellow work-lamp light, a thick insulated pipe with a flanged joint along its upper wall, a rusted red valve wheel at the far left end and damp concrete walls on both sides.',
          '一条非常狭窄的水平混凝土检修井，只比人的肩膀宽一点，昏黄的工作灯光，上方井壁上有一条带法兰接头的粗保温管，左边尽头是一个生锈的红色阀门轮，两侧是潮湿的混凝土墙。',
          'the narrow shaft, the insulated pipe with its flanged joint and the rusted red valve wheel at the end')
new_scene(b21, 'bunker_hall', '地下的裸混凝土服务走廊（暖黄灯、天花板管线）',
          'A bare concrete service corridor with warm lamps at regular intervals, thick pipes along the ceiling and a heavy steel door at the far end.',
          '裸混凝土的服务走廊，等距的暖黄灯，天花板上是粗管线，远端是一扇厚重的钢门。',
          'the long corridor receding with its pipes and warm lamps')
b21.character('SuSilk', 'su_silk', SU_EN, SU_ZH)
b21.character('RadioOp', 'radio_set', RADIOOP_EN, RADIOOP_ZH)
b21.character('RadioNing', 'radio_set', RADIONING_EN, RADIONING_ZH)

insert_task('21-01', '01｜插镜：坑边那一圈冰雕被新雪盖住了半截，风吹着粉雪', 5, PIT_ICE,
            'Wide high shot over the pit, the pit and the ring of ice figures in the middle third of the frame.',
            "A thin wind drives fresh powder snow in drifts against the legs of the ring of ice-encased men around the pit, burying them halfway, their frozen faces fixed in screams under a veil of snow, the grille capped with clear ice in the pit below them. Nothing else moves.",
            "一阵细风把新落的粉雪一阵阵吹到坑边那一圈冰雕的腿上，埋住了他们半截，他们冻住的脸还定在尖叫的样子，上面蒙着一层雪，坑底的格栅盖着透明的冰。别的什么都不动。",
            SOUND_ICE, 'The frame holds the pit with its capped grille and the ring of snow-dusted ice figures around it, and nobody else in the scene.',
            rise('the whole snowfield with the pit and its ring of ice figures small', '整片雪原和坑边那一圈很小的冰雕'),
            groups=[('the ice figures', 'center', 'obj:the pit')])

S.T('21-02', '02｜物资大厅：感应灯一排排亮起，苏清月仰头看着满墙的粮油说这是一座粮仓，林峰让她去角落看看', 10, DEPOT,
    [P('lin_home', 'left', "walking down the concrete aisle in profile facing frame-right, one hand trailing along a steel shelf, glancing back at her", 'Su', "his jaw relaxed, one corner of his mouth lifting in a dry amused curve, his brows soft"),
     P('su_cozy', 'right', "walking beside him in profile facing frame-left, her head tipped back to look up at the towering shelves", 'obj:the towering shelves of rice sacks and canned food', "her eyes wide, her lips parted, her brows lifted")],
    'Medium wide shot, both from the head to the knees, in the middle third of the frame, walking down the aisle.',
    "<su_cozy> turns slowly with her head tipped back and speaks the first line to <lin_home> in a stunned, breathless voice, her eyes wide, her lips parted and her brows lifted. <lin_home> glances at her and speaks the second line to <su_cozy> in a low amused voice, one corner of his mouth lifting in a dry amused curve and his brows soft, and nods toward the corner at frame-right.",
    "苏清月仰着头慢慢转着圈看货架，用惊呆又屏着气的声音对林峰说出第一句，眼睛睁大、嘴唇微张、眉毛上扬。林峰侧头看她，用低沉带笑的声音对苏清月说出第二句，嘴角带着一丝干干的觉得好笑的弧度、眉毛舒展，朝画面右边的墙角点了点头。",
    SOUND_DEPOT, lines=[('su_cozy', "这是……一座粮仓？", 1.0, 'Lin'), ('lin_home', "还有更好的，去角落看看。", 4.2, 'Su')],
    cam=track('the two of them walking', '两人'), room={'Lin', 'Su'}, new=True,
    bg='Around them the rows of ceiling lamps glow warm white above the steel shelves of rice sacks and canned food, and the wall of wine bottles and cigar crates fills the back.',
    holds='The frame holds exactly two people: Lin and Su, walking down the aisle.',
    st={'Lin': ('灰色棉质家居服，走在过道里', '灰色棉质家居服，走在过道里'), 'Su': ('奶白色毛衣，走在过道里', '奶白色毛衣，走在过道里')})

S.T('21-03', '03｜墙角：苏清月蹲在黑色密封箱前，用美工刀划开胶带，林峰靠着货架说这几箱是给你的', 9, DEPOT,
    [P('su_cozy', 'center', "kneeling on the concrete in front of the largest black sealed box in profile facing frame-right, a utility knife in her right hand slicing along the taped seam of the lid", 'obj:the taped seam of the black box lid', "her lips parted, her brows lifted in curiosity"),
     P('lin_home', 'left', "leaning against a steel shelf behind her in profile facing frame-right, his arms loosely folded", 'Su', "his jaw relaxed, one corner of his mouth lifting in a dry curve, his brows soft")],
    'Medium two-shot, both from the head to the knees, in the middle third of the frame, in the corner of the hall.',
    "<lin_home> watches her and speaks the first line to <su_cozy> in a low even voice, one corner of his mouth lifting in a dry curve and his brows soft. <su_cozy> looks up and speaks the second line to <lin_home> in a small startled voice, her lips parted and her brows lifted, then <lin_home> speaks the third line to <su_cozy>. <su_cozy> finishes slicing the tape and lifts the lid.",
    "林峰看着她，用低沉平稳的声音对苏清月说出第一句，嘴角带着一丝干干的弧度、眉毛舒展。苏清月抬头，用小小吃惊的声音对林峰说出第二句，嘴唇微张、眉毛上扬，然后林峰对苏清月说出第三句。苏清月划完胶带，把盖子掀了起来。",
    SOUND_DEPOT, lines=[('lin_home', "这几箱，是给你的。", 0.8, 'Su'), ('su_cozy', "给我的？", 3.4, 'Lin'), ('lin_home', "拆开看看。", 5.2, 'Su')],
    cam=slide('right', '右', 'the two of them stand in the middle third of the frame with the black boxes between them', '两人占画面中间三分之一、中间是黑色箱子'),
    room={'Lin', 'Su'}, new=True,
    bg='Behind them the pallet of black boxes stands in the corner and the tall steel shelves of rice sacks rise at frame-left.',
    holds='The frame holds exactly two people: Su kneeling at the black box and Lin leaning on the shelf.',
    st={'Lin': ('灰色棉质家居服，靠着货架', '灰色棉质家居服，靠着货架'), 'Su': ('奶白色毛衣，蹲在黑箱前', '奶白色毛衣，蹲在黑箱前')})

insert_task('21-04', '04｜插镜：敞开的黑色箱子里整整齐齐码着护肤品瓶罐、金盖子的香水和一叠酒红色的真丝', 4, DEPOT_BOX,
            'Close shot looking down into the open black box in the middle third of the frame, nobody in the scene.',
            "Inside the open black box rows of blue skincare jars and tubes are packed neatly beside perfume bottles with gold caps and a folded stack of wine-red silk, all wrapped in thin tissue paper. Nothing else moves.",
            "敞开的黑色箱子里，一排排蓝色的护肤品瓶罐整整齐齐地码着，旁边是金色瓶盖的香水瓶和一叠折好的酒红色真丝，全都包着薄薄的棉纸。别的什么都不动。",
            SOUND_DEPOT_B, 'The frame holds the open black box with its jars, perfume bottles and folded wine-red silk, and nobody in the scene.',
            push1('the folded wine-red silk and the perfume bottles', '折好的酒红色真丝和香水瓶'))

S.T('21-05', '05｜墙角：苏清月抱着折好的酒红色真丝睡袍，眼眶红了，问你什么时候准备的，你怎么知道我的尺码', 11, DEPOT,
    [P('su_cozy', 'left', "standing in profile facing frame-right, hugging a folded wine-red silk nightgown against her chest with both arms", 'Lin', "her eyes glistening, her lips trembling in a half-laugh, her brows pulled together"),
     P('lin_home', 'right', "leaning against a steel shelf in profile facing frame-left, his arms loosely folded", 'Su', "his jaw relaxed, his eyes warm and lazy, his brows soft")],
    'Medium two-shot, both from the head to the knees, in the middle third of the frame, in the corner of the hall.',
    "<su_cozy> speaks the first line to <lin_home> in a trembling voice, then the second line, her eyes glistening, her lips trembling in a half-laugh and her brows pulled together. <lin_home> answers with the third line to <su_cozy> in a deep unhurried voice, his jaw relaxed, his eyes warm and lazy and his brows soft.",
    "苏清月用发颤的声音对林峰说出第一句，接着说出第二句，眼睛含着泪光、嘴唇颤抖带着半个笑、眉头拧在一起。林峰用低沉不紧不慢的声音对苏清月答出第三句，下颌放松、眼神温暖慵懒、眉毛舒展。",
    SOUND_DEPOT, lines=[('su_cozy', "你什么时候准备的？", 0.8, 'Lin'), ('su_cozy', "你怎么知道我的尺码？", 3.4, 'Lin'), ('lin_home', "从你签合同那天起。", 6.8, 'Su')],
    cam=slide('left', '左', 'the two of them stand in the middle third of the frame', '两人占画面中间三分之一'), room={'Su', 'Lin'}, new=True,
    bg='Behind them the pallet of black boxes stands in the corner and the tall steel shelves rise at frame-left.',
    holds='The frame holds exactly two people: Su and Lin, in the corner of the hall.',
    st={'Su': ('奶白色毛衣，抱着一件酒红色真丝睡袍', '奶白色毛衣，抱着一件酒红色真丝睡袍'), 'Lin': ('灰色棉质家居服，靠着货架', '灰色棉质家居服，靠着货架')})

S.T('21-06', '06｜墙角：林峰说活下去靠卡路里，活得像人靠这些没用的东西', 8, DEPOT,
    [P('lin_home', 'right', "standing against a steel shelf in profile facing frame-left, his arms loosely folded, his gaze steady", 'Su', "his jaw relaxed, his eyes dark and deep, his brows soft"),
     P('su_cozy', 'left', "standing in profile facing frame-right, the folded wine-red silk nightgown held against her chest", 'Lin', "her eyes glistening, her lips parted, her brows lifted")],
    'Medium two-shot, both from the head to the waist, in the middle third of the frame, in the corner of the hall.',
    "<lin_home> speaks the first line to <su_cozy> in a low even voice, then the second line in a deeper, softer voice, his jaw relaxed, his eyes dark and deep and his brows soft. <su_cozy> listens, her eyes glistening, her lips parted and her brows lifted.",
    "林峰用低沉平稳的声音对苏清月说出第一句，接着用更深更轻的声音说出第二句，下颌放松、眼神又黑又深、眉毛舒展。苏清月听着，眼睛含着泪光、嘴唇微张、眉毛上扬。",
    SOUND_DEPOT, lines=[('lin_home', "活下去，靠卡路里。", 0.8, 'Su'), ('lin_home', "活得像人，靠这些没用的东西。", 3.6, 'Su')],
    cam=push1('Lin', '林峰'), room={'Lin', 'Su'}, new=True,
    bg='Behind them the tall steel shelves of rice sacks and canned food rise in the warm white light.',
    holds='The frame holds exactly two people: Lin and Su, in the corner of the hall.',
    st={'Lin': ('灰色棉质家居服，靠着货架', '灰色棉质家居服，靠着货架'), 'Su': ('奶白色毛衣，抱着酒红色真丝睡袍', '奶白色毛衣，抱着酒红色真丝睡袍')})

S.T('21-07', '07｜物资大厅：天花板一半的灯暗了，两人抬头看通风格栅，林峰说地源热泵的阀门卡住了', 8, DEPOT_DIM,
    [P('lin_home', 'right', "standing in the aisle in profile facing frame-left, his head tilted up toward the ceiling grille", 'obj:the square ceiling ventilation grille', "his jaw tight, his lips set flat, his brows low"),
     P('su_cozy', 'left', "standing beside him in profile facing frame-right, the folded wine-red silk nightgown held against her chest, her face turned up to the ceiling", 'Lin', "her eyes wide, her lips parted, her brows pulled together")],
    'Medium two-shot, both from the head to the knees, in the middle third of the frame, in the aisle half in shadow.',
    "<lin_home> keeps his eyes on the ceiling grille and speaks the first line to <su_cozy> in a low flat voice, his jaw tight, his lips set flat and his brows low. <su_cozy> looks at him and speaks the second line to <lin_home> in a small tense voice, her eyes wide, her lips parted and her brows pulled together.",
    "林峰眼睛盯着天花板的格栅，用低沉平淡的声音对苏清月说出第一句，下颌绷紧、嘴唇抿平、眉头压低。苏清月看着他，用小而紧张的声音对林峰说出第二句，眼睛睁大、嘴唇微张、眉头拧在一起。",
    SOUND_DEPOT_DIM, lines=[('lin_home', "地源热泵的阀门，卡住了。", 1.0, 'Su'), ('su_cozy', "那怎么办？", 4.8, 'Lin')],
    cam=push('both of them', '两人'), room={'Lin', 'Su'}, new=True,
    bg='Above them half of the ceiling lamps are dark, the left side of the hall lies in deep shadow and the square ventilation grille is set in the ceiling above the aisle.',
    holds='The frame holds exactly two people: Lin and Su, in the aisle half in shadow.',
    st={'Lin': ('灰色棉质家居服，站在过道里', '灰色棉质家居服，站在过道里'), 'Su': ('奶白色毛衣，抱着酒红色真丝睡袍', '奶白色毛衣，抱着酒红色真丝睡袍')})

# ================================================================================================ 第 22 集
b22 = S.episode('剧本第22集｜狭窄井里的呼吸', '设备间里，压力表的指针一路冲进红区，管缝里喷着蒸汽，再不泄压地暖管就要爆；阀门在不到半米宽的检修井里，林峰挤不进去，苏清月说我来，我的手比你稳；两人并排挤在井里，林峰低声催她快一点，她回嘴你再说话我就不修了；她咬牙拧动阀门轮；水管接头崩开，温水喷出来，林峰用身体护住她；水声渐渐停下，两人湿透，贴得很近，彼此的呼吸都很重。', 22)

insert_task('22-01', '01｜插镜：设备间的大压力表，指针发着抖顶进红区，管缝里喷着白色蒸汽', 4, PUMP_GAUGE,
            'Close shot of the big pressure gauge above the control panel, the gauge in the middle third of the frame, nobody in the scene.',
            "The needle of the big round pressure gauge quivers deep in the red danger zone while thin jets of white steam hiss from the seams of the pipes around it and the metal groans. Nothing else moves.",
            "大圆压力表的指针发着抖，顶在红色危险区的深处，周围管子的接缝里嘶嘶喷着细细的白色蒸汽，金属发出呻吟。别的什么都不动。",
            SOUND_GAUGE, 'The frame holds the pressure gauge with its needle in the red and the steaming pipe seams, and nobody in the scene.',
            push1('the quivering pressure gauge', '发抖的压力表'))

S.T('22-02', '02｜设备间：林峰说再不泄压管子就爆，阀门在井里他进不去，苏清月说我来，我的手比你稳', 10, PUMP_GAUGE,
    [P('lin_work', 'right', "standing at the control panel in profile facing frame-left, one hand flat on the panel", 'Su', "his jaw tight, his lips set flat, his brows low"),
     P('su_surgeon', 'left', "standing beside him in profile facing frame-right, her hands already tugging on a pair of thin white surgical gloves", 'Lin', "her chin lifted, her lips pressed in a firm line, her brows level")],
    'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the control panel.',
    "<lin_work> speaks the first line to <su_surgeon> in a low urgent voice, then the second line, his jaw tight, his lips set flat and his brows low. <su_surgeon> pulls on her gloves and speaks the third line to <lin_work> in a calm, firm voice, her chin lifted, her lips pressed in a firm line and her brows level.",
    "林峰用低沉急迫的声音对苏清月说出第一句，接着说出第二句，下颌绷紧、嘴唇抿平、眉头压低。苏清月戴着手套，用平静坚定的声音对林峰说出第三句，下巴微抬、嘴唇紧抿成一条线、眉毛平直。",
    SOUND_PUMP, lines=[('lin_work', "再不泄压，管子就爆。", 0.8, 'Su'), ('lin_work', "阀门在井里，我进不去。", 3.2, 'Su'), ('su_surgeon', "我来，我的手比你稳。", 6.0, 'Lin')],
    cam=slide('left', '左', 'the two of them stand in the middle third of the frame', '两人占画面中间三分之一'), room={'Lin', 'Su'}, new=True,
    bg='Behind them the big pressure gauge with its needle in the red hangs above the control panel and thin jets of steam hiss from the pipe seams.',
    holds='The frame holds exactly two people: Lin and Su, at the control panel.',
    st={'Lin': ('深灰亨利衫和工装背心，站在控制面板前', '深灰亨利衫和工装背心，站在控制面板前'), 'Su': ('黑色长袖打底衫，戴上手套', '黑色长袖打底衫，戴上手套')})

S.T('22-03', '03｜检修井里：两人并排挤着，林峰低声催她快一点，苏清月回嘴你再说话我就不修了', 10, SHAFT,
    [P('su_surgeon', 'left', "lying on her stomach in the narrow shaft in profile facing frame-left, both gloved hands reaching toward the rusted valve wheel at the far end", 'obj:the rusted red valve wheel', "her lips pressed tight, her brows drawn together in concentration"),
     P('lin_work', 'right', "lying on his stomach in the narrow shaft behind her in profile facing frame-left, his elbows braced against the concrete walls, his head just behind her shoulder", 'Su', "his jaw tight, his lips set flat, his brows low")],
    'Medium side shot along the shaft, both from the head to the hips, in the middle third of the frame, in the cramped maintenance shaft.',
    "<lin_work> speaks the first line to <su_surgeon> in a rough low voice, his jaw tight, his lips set flat and his brows low. <su_surgeon> keeps her eyes on the valve wheel and speaks the second line to <lin_work> in a sharp breathless voice, her lips pressed tight and her brows drawn together. <lin_work> answers with the third line to <su_surgeon> in a low, wry voice.",
    "林峰用粗哑的低声对苏清月说出第一句，下颌绷紧、嘴唇抿平、眉头压低。苏清月眼睛盯着阀门轮，用尖锐带喘的声音对林峰说出第二句，嘴唇紧抿、眉头因专注拧在一起。林峰用低低带点无奈的声音对苏清月答出第三句。",
    SOUND_SHAFT, lines=[('lin_work', "苏医生，你最好快一点。", 1.0, 'Su'), ('su_surgeon', "你再说话，我就不修了。", 4.0, 'Lin'), ('lin_work', "……我闭嘴。", 7.0, 'Su')],
    cam=track('the two of them lying in the shaft', '趴在井里的两人'), room={'Lin', 'Su'}, new=True,
    bg='Around them the damp concrete walls close in, a thick insulated pipe with a flanged joint runs along the upper wall and the rusted red valve wheel sits at the far left end.',
    holds='The frame holds exactly two people: Su and Lin, lying one behind the other in the narrow shaft, nobody else.',
    st={'Su': ('黑色长袖打底衫，戴着手套，趴在井里伸手够阀门', '黑色长袖打底衫，戴着手套，趴在井里伸手够阀门'), 'Lin': ('深灰亨利衫，趴在井里', '深灰亨利衫，趴在井里')})

S.T('22-04', '04｜检修井里：苏清月双手抱住阀门轮，咬牙拧动，轮子转了四分之一圈', 6, SHAFT,
    [P('su_surgeon', 'left', "lying on her stomach in the narrow shaft in profile facing frame-left, both gloved hands clamped on the rusted valve wheel, her shoulders bunched to heave it round", 'obj:the rusted red valve wheel', "her teeth clenched, her brows pulled together"),
     P('lin_work', 'right', "lying on his stomach behind her in profile facing frame-left, both hands braced flat against the concrete walls on either side of her", 'Su', "his jaw tight, his lips set flat, his brows low")],
    'Medium side shot along the shaft, both from the head to the hips, in the middle third of the frame, in the cramped maintenance shaft.',
    "<su_surgeon> heaves with her whole body and turns the rusted wheel a quarter turn with a deep clunk, her teeth clenched and her brows pulled together. <lin_work> holds himself braced against the walls and watches her, his jaw tight, his lips set flat and his brows low.",
    "苏清月用全身的力气拧动生锈的轮子，轮子沉闷地咔哒一声转了四分之一圈，她咬紧牙关、眉头拧在一起。林峰撑着井壁稳住自己，看着她，下颌绷紧、嘴唇抿平、眉头压低。",
    SOUND_SHAFT_B, cam=push1('Su\'s gloved hands on the valve wheel', '苏清月戴着手套握在阀门轮上的双手'), room={'Lin', 'Su'}, new=True,
    bg='Around them the damp concrete walls close in and the thick insulated pipe with its flanged joint runs along the upper wall.',
    holds='The frame holds exactly two people: Su and Lin, lying one behind the other in the narrow shaft, nobody else.',
    st={'Su': ('黑色长袖打底衫，戴着手套，趴在井里伸手够阀门', '黑色长袖打底衫，戴着手套，趴在井里')})

S.T('22-05', '05｜检修井里：头顶的水管接头崩开，温水喷出来，林峰一下罩住苏清月', 6, SHAFT_LEAK,
    [P('su_surgeon', 'left', "lying on her stomach in the narrow shaft in profile facing frame-left, her gloved hands just loosening from the valve wheel, her face turning up toward the joint above", 'obj:the leaking pipe joint above her', "her eyes widening, her lips parted"),
     P('lin_work', 'right', "lying on his stomach behind her in profile facing frame-left, his head raised toward the joint, one arm already coming forward over her", 'obj:the leaking pipe joint above them', "his jaw clenched, his brows low")],
    'Medium side shot along the shaft, both from the head to the hips, in the middle third of the frame, in the cramped maintenance shaft.',
    "The flanged pipe joint above them splits and a jet of warm water roars across the shaft; <lin_work> throws his arm and his body over <su_surgeon> and takes the water on his back as she ducks her head under him, <lin_work> with his jaw clenched and his brows low, <su_surgeon> with her eyes squeezed shut and her lips pressed together. Steam fills the shaft.",
    "头顶的法兰接头一下裂开，一股温水轰地横扫过井里；林峰伸出手臂、整个人罩在苏清月身上，用后背挡住水，苏清月把头埋到他身下，林峰咬紧下颌、眉头压低，苏清月紧闭着眼、嘴唇紧抿。蒸汽涌满了井里。",
    SOUND_BURST, cam=push('both of them', '两人'), room={'Lin', 'Su'}, new=True,
    bg='Around them the damp concrete walls close in and the thick insulated pipe runs along the upper wall.',
    holds='The frame holds exactly two people: Su and Lin, lying one behind the other in the narrow shaft, nobody else.',
    st={'Su': ('黑色长袖打底衫，戴着手套，趴在井里', '黑色打底衫被水浇透，湿发贴在脸颊上，趴在井里')})

S.T('22-06', '06｜检修井里：水渐渐停了，两人湿透，贴得很近，林峰低声问没事吧，苏清月轻轻说没事', 9, SHAFT_WET,
    [P('lin_work', 'right', "lying on his side in the narrow shaft in profile facing frame-left, soaked through, one arm still curved over her shoulders, water dripping from his hair", 'Su', "his jaw loosening, his eyes dark and intent, his brows drawn together", outfit="in a soaked charcoal henley clinging to his shoulders"),
     P('su_surgeon', 'left', "lying on her side in the narrow shaft in profile facing frame-right, her wet hair stuck to her cheek, one gloved hand resting on his chest", 'Lin', "her cheeks flushed, her lips parted as she catches her breath, her brows lifted", outfit="in a soaked black thermal top")],
    'Close medium side shot, both from the head to the chest, in the middle third of the frame, in the steaming shaft.',
    "<lin_work> speaks the first line to <su_surgeon> in a low rough voice, his jaw loosening, his eyes dark and intent and his brows drawn together. <su_surgeon> looks up at him and answers with the second line to <lin_work> in a soft breathless voice, her cheeks flushed, her lips parted as she catches her breath and her brows lifted.",
    "林峰用低沉粗哑的声音对苏清月说出第一句，下颌放松、眼神又黑又专注、眉头拧在一起。苏清月抬头看他，用轻轻带喘的声音对林峰答出第二句，脸颊泛红、嘴唇微张喘着气、眉毛上扬。",
    SOUND_SHAFT_W, lines=[('lin_work', "没事吧？", 1.4, 'Su'), ('su_surgeon', "……没事。", 4.2, 'Lin')],
    cam=push('both of them', '两人'), room={'Lin', 'Su'}, new=True,
    bg='Around them thin white steam drifts through the damp shaft, water drips from the pipe above and the rusted valve wheel stands at the far end.',
    holds='The frame holds exactly two people: Lin and Su, lying close together in the steaming shaft, nobody else.',
    st={'Su': ('黑色打底衫被水浇透，湿发贴在脸颊上，趴在井里', '黑色打底衫被水浇透，湿发贴在脸颊上'), 'Lin': ('深灰亨利衫，趴在井里', '深灰亨利衫被水浇透')})

# ================================================================================================ 第 23 集
b23 = S.episode('剧本第23集｜25℃的越界', '水声停了，井里只剩滴水和两个人的心跳，苏清月抬头，林峰低头吻住了她；两人湿漉漉地并肩走回生活区，她说腿有点软，他说我扶着你；沙发上放着那件酒红色睡袍，她说守则第三条禁止越界接触，他说协议是我定的，我撕了，去洗澡别感冒；浴室里水声响起，林峰擦着头发倒了一杯威士忌，低声说外面零下八十度，里面是春天；控制室里的军用收音机忽然沙沙响起，传出一个微弱的人声：这里是体育馆避难所，呼叫任何幸存者。', 23)

S.T('23-01', '01｜检修井里：只剩滴水声，林峰低头吻住苏清月，苏清月抓住他湿透的衣领', 7, SHAFT_WET,
    [P('lin_work', 'right', "lying on his side in the narrow shaft in profile facing frame-left, one hand cupping her jaw, his head bent toward her", 'Su', "his jaw loosening, his eyes dark, his brows drawn together", outfit="in a soaked charcoal henley"),
     P('su_surgeon', 'left', "lying on her side in the narrow shaft in profile facing frame-right, her wet hair stuck to her cheek, one gloved hand gripping his soaked collar", 'Lin', "her lips parted, her cheeks flushed, her brows lifted", outfit="in a soaked black thermal top")],
    'Close medium side shot, both from the head to the chest, in the middle third of the frame, in the steaming shaft.',
    "<lin_work> lowers his head and kisses <su_surgeon> firmly while his hand cups her jaw, his jaw loosening, his eyes dark and his brows drawn together; <su_surgeon> grips his soaked collar and kisses him back, her cheeks flushed and her brows lifted, then closes her eyes. Water drips from the pipe above them.",
    "林峰低下头，手托着她的下颌，用力吻住苏清月，下颌放松、眼神深黑、眉头拧在一起；苏清月抓住他湿透的衣领回吻，脸颊泛红、眉毛上扬，然后闭上了眼睛。头顶的管子滴着水。",
    SOUND_SHAFT_W, cam=push('both of them', '两人'), room={'Lin', 'Su'}, new=True,
    bg='Around them thin white steam drifts through the damp shaft and water drips from the pipe above.',
    holds='The frame holds exactly two people: Lin and Su, lying close together in the steaming shaft, nobody else.',
    st={'Su': ('黑色打底衫被水浇透', '黑色打底衫被水浇透'), 'Lin': ('深灰亨利衫被水浇透', '深灰亨利衫被水浇透')})

S.T('23-02', '02｜走廊里：两人湿漉漉地并肩走回生活区，苏清月说腿有点软，林峰说我扶着你', 8, CORRIDOR,
    [P('su_surgeon', 'left', "walking down the corridor in profile facing frame-right, her gloves off, her wet hair stuck to her neck, one hand on his arm", 'Lin', "her cheeks flushed, her lips curved in a shy sweet smile, her brows lifted", outfit="in a damp black thermal top"),
     P('lin_work', 'right', "walking beside her in profile facing frame-left, one arm around her shoulders, his damp henley clinging to him", 'Su', "his jaw relaxed, a warm curve at one corner of his mouth, his brows soft", outfit="in a damp charcoal henley")],
    'Medium two-shot, both from the head to the knees, in the middle third of the frame, walking in the corridor.',
    "<su_surgeon> leans a little on his arm and speaks the first line to <lin_work> in a soft shaky laughing voice, her cheeks flushed, her lips curved in a shy sweet smile and her brows lifted. <lin_work> tightens his arm around her shoulders and speaks the second line to <su_surgeon> in a low warm voice, his jaw relaxed, a warm curve at one corner of his mouth and his brows soft.",
    "苏清月微微靠在他的手臂上，用轻轻发颤带着笑的声音对林峰说出第一句，脸颊泛红、嘴角带着害羞的甜笑、眉毛上扬。林峰把揽着她肩膀的手臂收紧，用低沉温暖的声音对苏清月说出第二句，下颌放松、嘴角带着温暖的弧度、眉毛舒展。",
    SOUND_CORR, lines=[('su_surgeon', "腿有点软。", 1.0, 'Lin'), ('lin_work', "我扶着你。", 3.8, 'Su')],
    cam=follow('the two of them', '两人', 'they reach the end of the corridor at the heavy steel door', '两人走到走廊尽头的钢门前'), room={'Lin', 'Su'}, new=True,
    bg='Around them the bare concrete corridor recedes with its ceiling pipes and warm lamps and a heavy steel door stands at the far end.',
    holds='The frame holds exactly two people: Su and Lin, walking in the corridor, nobody else.',
    st={'Su': ('黑色打底衫被水浸湿', '黑色打底衫被水浸湿'), 'Lin': ('深灰亨利衫被水浸湿', '深灰亨利衫被水浸湿')})

S.T('23-03', '03｜生活区沙发前：苏清月说守则第三条禁止越界接触，林峰说协议是我定的，我撕了，去洗澡别感冒', 10, SOFA2,
    [P('su_cozy', 'left', "standing in front of the sofa in profile facing frame-right, a big white towel around her shoulders, her damp hair dripping", 'Lin', "her cheeks flushed, her eyes sparkling, her lips curved in a coy smile, her brows lifted", outfit="in a damp cream knit sweater"),
     P('lin_home', 'right', "standing in front of the sofa in profile facing frame-left, rubbing his wet hair with a small towel in one hand", 'Su', "his jaw relaxed, his eyes dark and warm, one corner of his mouth lifting, his brows soft", outfit="in a dry soft grey henley")],
    'Medium two-shot, both from the head to the knees, in the middle third of the frame, in front of the sofa.',
    "<su_cozy> speaks the first line to <lin_home> in a breathless teasing voice, her cheeks flushed, her eyes sparkling, her lips curved in a coy smile and her brows lifted. <lin_home> lowers the towel and speaks the second line to <su_cozy> in a low firm voice, then the third line in a softer voice, his jaw relaxed, his eyes dark and warm, one corner of his mouth lifting and his brows soft.",
    "苏清月用带喘的、逗弄的声音对林峰说出第一句，脸颊泛红、眼睛发亮、嘴角带着逗弄的笑、眉毛上扬。林峰放下毛巾，用低沉坚定的声音对苏清月说出第二句，接着用更轻的声音说出第三句，下颌放松、眼神又黑又暖、嘴角微微上扬、眉毛舒展。",
    SOUND_WARM, lines=[('su_cozy', "守则第三条，禁止越界接触。", 0.8, 'Lin'), ('lin_home', "协议是我定的，我撕了。", 4.4, 'Su'), ('lin_home', "去洗澡，别感冒。", 7.0, 'Su')],
    cam=slide('right', '右', 'the two of them stand in the middle third of the frame with the sofa behind them', '两人占画面中间三分之一、身后是沙发'), room={'Su', 'Lin'}, new=True,
    bg='Behind them the deep brown leather sofa stands against the room with a folded wine-red silk nightgown lying on its arm, and the open kitchen glows warm at frame-left.',
    holds='The frame holds exactly two people: Su and Lin, standing in front of the sofa.',
    st={'Su': ('奶白色毛衣被水浸湿，肩上披着白毛巾', '奶白色毛衣被水浸湿，肩上披着白毛巾'), 'Lin': ('浅灰色干亨利衫，擦着头发', '浅灰色干亨利衫，擦着头发')})

insert_task('23-04', '04｜插镜：浴室里热气蒸腾，磨砂玻璃门后水声哗哗，长凳上叠着那件酒红色的睡袍', 4, BATH2,
            'Close shot of the bathroom, the frosted-glass shower door in the middle third of the frame, nobody in the scene.',
            "Warm white steam rolls off the frosted-glass shower door as the shower patters steadily behind it, and on the wooden bench beside the towels a folded wine-red silk nightgown waits. Nothing else moves.",
            "暖白色的蒸汽从磨砂玻璃淋浴门上滚出来，门后淋浴哗哗地响着，毛巾旁边的木头长凳上叠着一件酒红色的睡袍。别的什么都不动。",
            SOUND_SHOWER, 'The frame holds the frosted-glass shower door with its steam, the bench with the towels and the folded wine-red nightgown, and nobody in the scene.',
            push1('the frosted-glass door and the folded silk on the bench', '磨砂玻璃门和长凳上叠着的真丝'))

S.T('23-05', '05｜生活区：林峰一个人擦着头发，倒了半杯威士忌，低声说外面零下八十度，里面是春天', 9, LIVING_GLASS,
    [P('lin_home', 'center', "standing at the marble counter in profile facing frame-right, a small towel over one shoulder, pouring amber whiskey from the bottle into the crystal glass with his right hand", 'obj:the crystal glass filling with amber whiskey', "his jaw relaxed, one corner of his mouth lifting in a quiet curve, his brows soft", outfit="in a dry soft grey henley")],
    'Medium shot, the figure from the head to the knees, in the middle third of the frame, at the kitchen counter.',
    "<lin_home> pours the whiskey slowly, his eyes on the glass, then murmurs one line to himself in a low quiet voice, talking to nobody, his lips moving softly, then lifts the glass, one corner of his mouth lifting in a quiet curve, his jaw relaxed and his brows soft. Nobody else is in the room.",
    "林峰慢慢倒着酒，眼睛看着杯子，然后低声对自己说出一句，不是对任何人说的，嘴唇轻轻动着，接着举起杯子，嘴角带着一丝安静的弧度、下颌放松、眉毛舒展。屋里没有别人。",
    SOUND_GLASS, vo=[('lin_home', "外面零下八十度，里面，是春天。", 1.6, 'Lin')],
    cam=slide('left', '左', 'Lin stands in the middle third of the frame with the glass raised', '林峰占画面中间三分之一、举着酒杯'), room={'Lin'}, new=True,
    bg='Behind him the round wooden dining table and the thick cream rug lie in the warm amber light, and the wall of small security monitors shows white blizzards.',
    holds='The frame holds exactly one person: Lin, standing at the kitchen counter, nobody else.',
    st={'Lin': ('浅灰色干亨利衫，站在厨房台边', '浅灰色干亨利衫，站在厨房台边')})

S.T('23-06', '06｜控制室：林峰端着杯子站在收音机前，收音机忽然沙沙响起，传出微弱的人声', 10, CONTROL_R,
    [P('lin_home', 'left', "standing at the control console in profile facing frame-right, a glass of whiskey in his right hand, his body gone still, his eyes on the military radio", 'obj:the olive-green military radio on the side table', "his jaw tight, his lips set flat, his brows low", outfit="in a dry soft grey henley")],
    'Medium shot, the figure from the head to the knees, in the left-center of the frame, in the middle third of the frame at the control console with the radio beside him.',
    "A thin crackling woman's voice from the radio speaks the first line as a voice-over, then the second line, the sound weak and broken by static. <lin_home> stands frozen with his eyes on the radio, his grip tightening on the glass until his knuckles whiten, his jaw tight, his lips set flat and his brows low. Nobody else is in the room.",
    "收音机里传出一个细细、沙沙作响的女声，以旁白的方式说出第一句，接着说出第二句，声音微弱，被杂音切得断断续续。林峰僵在原地，眼睛盯着收音机，握着杯子的手越收越紧，指节发白，下颌绷紧、嘴唇抿平、眉头压低。屋里没有别人。",
    SOUND_RADIO, vo=[('radio_op', "这里是体育馆避难所。", 1.0, 'Lin'), ('radio_op', "呼叫……任何幸存者。", 4.2, 'Lin')],
    cam=push1('Lin and the radio', '林峰和身边的收音机'), extra_assets=('radio_set',), room={'Lin'}, new=True,
    bg='Beside him on the steel side table the olive-green military radio glows with its amber dial, and the wall of six small monitors glows at frame-left.',
    holds='The frame holds exactly one person: Lin, with the radio on the side table, nobody else.',
    st={'Lin': ('浅灰色干亨利衫，端着酒杯站在控制台前', '浅灰色干亨利衫，手紧握着酒杯')})

# ================================================================================================ 第 24 集
b24 = S.episode('剧本第24集｜幽灵电台', '苏清月穿着酒红色睡袍擦着头发走进控制室，林峰站在收音机前，里面断断续续地说柴油快烧完了，几千个老人孩子在冻死；她靠在他身边，说体育馆扛不住零下八十度；他说道德绑架而已，同情心是最致命的毒药；收音机里忽然换成一个林峰熟悉的声音：林峰，是我，周宁，你有地下设施，你不能见死不救，把物资交出来；苏清月脸色骤变：他们怎么知道这里；林峰看着收音机：门，不会为任何人开。', 24)

S.T('24-01', '01｜控制室：苏清月擦着头发走到林峰身边，收音机里说柴油快烧完了，几千个老人孩子在冻死', 10, CONTROL_R,
    [P('lin_home', 'right', "standing at the console in profile facing frame-left, a glass of whiskey in his right hand, his eyes on the radio", 'obj:the olive-green military radio on the side table', "his jaw tight, his lips set flat, his brows low", outfit="in a dry soft grey henley"),
     P('su_silk', 'left', "walking up beside him in profile facing frame-right, rubbing her damp hair with a white towel, her eyes on the radio", 'obj:the olive-green military radio on the side table', "her lips parting, her brows pulled together")],
    'Medium two-shot, both from the head to the knees, in the middle third of the frame, at the control console with the radio beside them.',
    "A thin crackling woman's voice from the radio speaks the first line as a voice-over, then the second line, weak and broken by static. <lin_home> stands without moving, his jaw tight, his lips set flat and his brows low. <su_silk> stops rubbing her hair, the towel stilling in her hands, her lips parting and her brows pulled together.",
    "收音机里传出一个细细、沙沙作响的女声，以旁白的方式说出第一句，接着说出第二句，声音微弱，被杂音切得断断续续。林峰站着一动不动，下颌绷紧、嘴唇抿平、眉头压低。苏清月停下擦头发的手，毛巾在手里静住，嘴唇微张、眉头拧在一起。",
    SOUND_RADIO, vo=[('radio_op', "柴油快烧完了……", 1.0, 'Lin'), ('radio_op', "几千个老人孩子，正在冻死。", 3.4, 'Lin')],
    cam=follow('Su', '苏清月', 'she stops beside Lin at the console', '她停在控制台边林峰的身旁'), extra_assets=('radio_set',), room={'Lin', 'Su'}, new=True,
    bg='Beside them on the steel side table the olive-green military radio glows with its amber dial, and the wall of six small monitors glows at frame-left.',
    holds='The frame holds exactly two people: Lin and Su, at the control console with the radio beside them, nobody else.',
    st={'Lin': ('浅灰色干亨利衫，端着酒杯站在控制台前', '浅灰色干亨利衫，端着酒杯站在控制台前'), 'Su': ('酒红色真丝睡袍，肩上搭着白毛巾', '酒红色真丝睡袍，肩上搭着白毛巾')})

S.T('24-02', '02｜控制室：苏清月说体育馆扛不住零下八十度，林峰喝了一口酒说道德绑架而已，同情心是最致命的毒药', 10, CONTROL_R,
    [P('su_silk', 'left', "standing beside him in profile facing frame-right, her arm resting along his shoulder, the white towel around her neck", 'Lin', "her brows pulled together in worry, her lips pressed tight"),
     P('lin_home', 'right', "standing at the console in profile facing frame-left, taking a slow sip from the whiskey glass in his right hand", 'Su', "his jaw tight, his eyes cold and flat, his brows low", outfit="in a dry soft grey henley")],
    'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the control console.',
    "<su_silk> speaks the first line to <lin_home> in a worried low voice, her brows pulled together in worry and her lips pressed tight. <lin_home> takes a slow sip, lowers the glass and speaks the second line to <su_silk> in a cold flat voice, then the third line in an even colder voice, his jaw tight, his eyes cold and flat and his brows low.",
    "苏清月用担忧的低声对林峰说出第一句，眉头担忧地拧着、嘴唇紧抿。林峰慢慢喝了一口，放下杯子，用冰冷平淡的声音对苏清月说出第二句，接着用更冷的声音说出第三句，下颌绷紧、眼神冰冷淡漠、眉头压低。",
    SOUND_RADIO, lines=[('su_silk', "体育馆，扛不住零下八十度。", 0.8, 'Lin'), ('lin_home', "道德绑架而已。", 4.2, 'Su'), ('lin_home', "同情心，是最致命的毒药。", 6.0, 'Su')],
    cam=slide('left', '左', 'the two of them stand in the middle third of the frame', '两人占画面中间三分之一'), extra_assets=('radio_set',), room={'Su', 'Lin'}, new=True,
    bg='Beside them on the steel side table the olive-green military radio glows with its amber dial and hisses softly, and the wall of six small monitors glows at frame-left.',
    holds='The frame holds exactly two people: Su and Lin, at the control console with the radio beside them, nobody else.',
    st={'Su': ('酒红色真丝睡袍，肩上搭着白毛巾', '酒红色真丝睡袍，肩上搭着白毛巾'), 'Lin': ('浅灰色干亨利衫，端着酒杯站在控制台前', '浅灰色干亨利衫，端着酒杯站在控制台前')})

S.T('24-03', '03｜控制室：林峰正要关掉收音机，里面忽然变成周宁嘶哑的声音，喊他的名字', 10, CONTROL_R,
    [P('lin_home', 'right', "standing at the console in profile facing frame-left, his hand lifted toward the radio's off-switch and frozen an inch from it", 'obj:the olive-green military radio on the side table', "his jaw clenched, his lips set flat, his brows low", outfit="in a dry soft grey henley"),
     P('su_silk', 'left', "standing beside him in profile facing frame-right, one hand pressed to her chest", 'Lin', "her eyes wide, her lips parted, her brows pulled high")],
    'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the control console.',
    "A hoarse man's voice from the radio breaks through the static and speaks the first line as a voice-over, then the second line, then the third, frantic and rising to a shout. <lin_home> freezes with his hand an inch from the switch, his jaw clenched, his lips set flat and his brows low. <su_silk> stares at him, her eyes wide, her lips parted and her brows pulled high.",
    "收音机里一个嘶哑的男人声音冲破杂音，以旁白的方式说出第一句，接着说出第二句和第三句，慌乱，越说越高，最后变成了喊。林峰的手停在开关前一寸，僵住了，下颌咬紧、嘴唇抿平、眉头压低。苏清月盯着他，眼睛睁大、嘴唇微张、眉毛高高挑起。",
    SOUND_RADIO, vo=[('radio_ning', "林峰！是我，周宁！", 0.8, 'Lin'), ('radio_ning', "我知道你在听！", 3.4, 'Lin'), ('radio_ning', "你有地下设施，不能见死不救！", 5.4, 'Lin')],
    cam=push('both of them', '两人'), extra_assets=('radio_set',), room={'Su', 'Lin'}, new=True,
    bg='Beside them on the steel side table the olive-green military radio glows with its amber dial and its speaker cone trembles.',
    holds='The frame holds exactly two people: Lin and Su, at the control console with the radio beside them, nobody else.',
    st={'Lin': ('浅灰色干亨利衫，手伸向收音机开关', '浅灰色干亨利衫，手停在收音机开关前'), 'Su': ('酒红色真丝睡袍，肩上搭着白毛巾', '酒红色真丝睡袍，肩上搭着白毛巾')})

S.T('24-04', '04｜控制室：收音机里喊把物资交出来，这是全人类的财产，苏清月脸色发白', 6, CONTROL_R,
    [P('su_silk', 'left', "standing beside him in profile facing frame-right, her fingers gripping his sleeve", 'Lin', "her face drained pale, her lips trembling, her brows pulled together"),
     P('lin_home', 'right', "standing at the console in profile facing frame-left, his eyes fixed on the radio", 'obj:the olive-green military radio on the side table', "his jaw clenched, his lips set flat, his brows low", outfit="in a dry soft grey henley")],
    'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the control console.',
    "The hoarse man's voice from the radio rises to a screaming shout and speaks one line as a voice-over, the speaker cone buzzing with the echo. <su_silk> grips his sleeve, her face drained pale, her lips trembling and her brows pulled together. <lin_home> does not move, his jaw clenched, his lips set flat and his brows low.",
    "收音机里那个嘶哑的男人声音拔高成尖叫，以旁白的方式喊出一句，扬声器纸盆随着回音嗡嗡震着。苏清月抓紧他的袖子，脸色发白、嘴唇发颤、眉头拧在一起。林峰一动不动，下颌咬紧、嘴唇抿平、眉头压低。",
    SOUND_RADIO, vo=[('radio_ning', "把物资交出来！这是全人类的财产！", 0.8, 'Lin')],
    cam=push('both of them', '两人'), extra_assets=('radio_set',), room={'Su', 'Lin'}, new=True,
    bg='Beside them on the steel side table the olive-green military radio glows with its amber dial and its speaker cone trembles.',
    holds='The frame holds exactly two people: Su and Lin, at the control console with the radio beside them, nobody else.',
    st={'Su': ('酒红色真丝睡袍，肩上搭着白毛巾', '酒红色真丝睡袍，肩上搭着白毛巾'), 'Lin': ('浅灰色干亨利衫，站在控制台前', '浅灰色干亨利衫，站在控制台前')})

S.T('24-05', '05｜控制室：苏清月问他们怎么知道这里，几千人涌过来怎么办，林峰看着收音机说门不会为任何人开', 10, CONTROL_R,
    [P('su_silk', 'left', "standing beside him in profile facing frame-right, both arms wrapped around herself", 'Lin', "her face pale, her lips trembling, her brows pulled together"),
     P('lin_home', 'right', "standing at the console in profile facing frame-left, motionless, his eyes on the dead radio", 'obj:the olive-green military radio on the side table', "his jaw set, his eyes colder than the ice outside, his brows low", outfit="in a dry soft grey henley")],
    'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the control console.',
    "<su_silk> speaks the first line to <lin_home> in a tight whisper, then the second line, her face pale, her lips trembling and her brows pulled together. <lin_home> keeps his eyes on the radio and speaks the third line to <su_silk> in a flat low voice, his jaw set, his eyes colder than the ice outside and his brows low.",
    "苏清月用紧绷的耳语对林峰说出第一句，接着说出第二句，脸色发白、嘴唇发颤、眉头拧在一起。林峰眼睛一直盯着收音机，用平淡低沉的声音对苏清月说出第三句，下颌绷紧、眼神比外面的冰雪还冷、眉头压低。",
    SOUND_RADIO, lines=[('su_silk', "他们怎么知道这里？", 0.8, 'Lin'), ('su_silk', "几千人涌过来，怎么办？", 3.3, 'Lin'), ('lin_home', "门，不会为任何人开。", 6.2, 'Su')],
    cam=push1('Lin', '林峰'), extra_assets=('radio_set',), room={'Su', 'Lin'}, new=True,
    bg='Beside them on the steel side table the olive-green military radio sits dark and silent, and the wall of six small monitors glows at frame-left.',
    holds='The frame holds exactly two people: Su and Lin, at the control console with the dark radio beside them, nobody else.',
    st={'Su': ('酒红色真丝睡袍，肩上搭着白毛巾', '酒红色真丝睡袍，肩上搭着白毛巾'), 'Lin': ('浅灰色干亨利衫，站在控制台前', '浅灰色干亨利衫，站在控制台前')})

doc = S.finish()
