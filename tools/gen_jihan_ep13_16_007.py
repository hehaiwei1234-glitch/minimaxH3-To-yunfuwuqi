#!/usr/bin/env python3
"""《极寒末日：我的隐秘安全屋》剧本第 13–16 集，追加稿 007（2026-10-13 夜）。必须接在 006（剧本第 9–12 集）之后追加（以 006 的 JSON 为底，
style／素材／角色逐字复制）；hh 挂机跑的是最后合并出来的那一份（008），不单独贴它。

写法＝004／005／006 同一套（一个任务一件慢的事；每人看着谁写进开场图；每句台词对谁说且对象在画面里；独白＝一个人在画面里、手上有事、眼睛看着一个具体物件；
3–5 秒无人插镜；承接前段只在同场景同一批人的相邻任务打开；运镜写“动作＋终点”；机械变化只拍结果；快动作单独占 5–6 秒任务）。
本稿里直接测的写法：
  · 13-01…13-07、14-07 火锅一场：两人面对面坐着、手上都有事（涮肉、倒啤酒、夹肉），台词 2–3 句；
  · 13-07、14-01、14-05 关灯后的暗场：开场图直接画成“只有火锅下面一点蓝火”的暗房（灯怎么灭的不拍）；
  · 14-02 地面上两个流浪者的对话＋14-03 倒下（快动作单独成 5 秒任务）——“头顶的人”改成地面上真的拍出来的两个人，
    不用只有声音的人（观众会读成“画面缺人”）；
  · 16-01 苏清月一个人给番茄花刷粉（手上有事＋画外自言自语，眼睛看着花）；
  · 15 集两人白衣清雪、15-05 按倒（快动作单独成任务）、15-07 趴雪里一边说话一边慢慢后退。
养成链：水（第 11 集）→光（第 12 集）→苗（第 12 集）→花（16-01 刷子授粉）→第一串红番茄（16-02、16-03）→入口（16-04）；鸡（第 12 集孵化箱）。
偏离大纲（交稿时已告诉 hh）：
  · 第 13 集：和牛、毛肚、基围虾只拍“一桌子的菜”和涮毛肚；“超声波监听仪”改成餐桌旁矮架上的一个小灰盒（一盏灯、一根短天线）；
    灯怎么熄灭不拍，直接用暗房开场图；“按遥控器关灯”不拍；
  · 第 14 集：原来是头顶流浪者的“声音”，改成地面上拍出来的两个人（不用只有声音的人）；死亡只拍“靠着排气管慢慢睡过去／倒进雪里不动”，不拍冻僵特写；
    “监听仪红灯熄灭”拍成插镜（灯已灭），“灯重新亮起”不拍，直接用亮房开场图；
  · 第 15 集：不拍“钻出地表时睫毛结霜”的过程，只在开场图里画有霜的睫毛；远处四五个暴徒只拍“很小的深色人影站在远处山坡上”（插镜），不写具体动作；
    “用匕首”不拍；匍匐后退用“一边说话一边慢慢往后挪”；暗门锁死只用声音，拍结果（两人靠在舱门上）；
  · 第 16 集：原大纲只有“摘番茄”，补了“刷粉”（养成链要有具体过程）和“灯闪一下＋黄灯”两个无人插镜（不拍人上楼梯的瞬间）。
H3 方面的风险（交稿时单列，不算我的错）：暗房里两张脸能不能看清；火锅里的汤翻滚、涮肉的手；啤酒罐；小灰盒的灯（机械灯光）；
  地面上两个流浪者靠着冰封排气管（人物倒下的动作可能慢、可能自切镜）；14-03 倒下 5 秒任务；白衣两人一起（衣服一样、脸小）；
  15-05 按倒；15-06 远处小人影可能被画大；15-07 趴着说话；舱门“咔哒”；16-01 刷子刷花的手部动作；番茄串在手里；16-06 灯熄灭一盏；
  “同一处”场景用参照图（没测过）；开场图约一成不按文字画。
"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _jihan_base3 import *

OUT = '合并稿/007_第13-16集_火锅听脚印头顶死神白雪幽灵第一口鲜甜_制作稿_追加'
S = Session('合并稿/006_第9-12集_投名状手术契约白噪音伊甸园_制作稿_追加.json', OUT, 36000)

# ---------------------------------------------------------------------------------------------- 新外貌
look('su_arctic', 'SuArctic', "in a bulky pure-white polar expedition suit with the hood up, white goggles pushed up on her forehead and a white neck gaiter pulled down under her chin, a few strands of black hair at her temples, frost on her lashes", 'sharp dark-brown', 'her', eth=CN_F28)

# ---------------------------------------------------------------------------------------------- 新场景（同一素材键的变体只改开场图后缀和布局）
POT_LAYOUT = (" Fixed stage layout: the round wooden dining table stands in the middle of the frame with a copper yin-yang hotpot set in its center, one half bubbling with red chili oil and the other half pale mushroom broth, "
              "ringed with plates of paper-thin beef rolls, tripe and shrimp; two wooden chairs face each other across the table; the open kitchen with the black-and-gold stove is at frame-left; "
              "a wall of small security monitors is at frame-center-right; a small grey box with a short antenna and one small lamp %s sits on a low shelf at frame-right beside the heavy round steel hatch door. ")
KITCHEN = Scene('bunker_living', LIVING.end, " Fixed stage layout: the open kitchen with a black-and-gold stove and a marble counter is at frame-left, a wooden cutting board with a slab of red beef and a long knife lying on the counter; a thick cream wool rug and the small round wooden dining table fill the middle of the frame; a wall of small security monitors is at frame-center-right; the heavy round steel hatch door is in the right wall at far frame-right.")
HOT = Scene('bunker_living', LIVING.end, POT_LAYOUT % 'that is dark')
HOT_ALERT = Scene('bunker_living', LIVING.end, POT_LAYOUT % 'glowing yellow')
DARK = Scene('bunker_living', " The room is almost completely dark; only the small blue flame under the hotpot and the faint glow of the monitor wall dimly light the faces from below.",
             POT_LAYOUT.replace('a small grey box', 'the ceiling lamps are off; a small grey box') % 'glowing red')
AIRLOCK2 = Scene('airlock', AIRLOCK.end, " Fixed stage layout: a long steel bench with two pairs of white insulated boots and a shelf of white goggles runs along the left wall; the bare white-tiled floor lies in the middle of the frame; a heavy round steel hatch door stands in the right wall at frame-right.")
SOLAR = Scene('snow_solar', " A silent frozen pine clearing under a black sky with a faint green aurora; the white light of the snow glows.",
              " Fixed stage layout: three rows of black solar panels on steel frames, half buried in snow, stand in the middle of the frame; a long low snow bank runs along the foreground; a wide snow slope rises far behind the panels at frame-right; snow-laden pines stand on both sides.")
EDEN2 = Scene('eden', EDEN.end,
              " Fixed stage layout: long tiers of white hydroponic channels fill the middle of the frame, now with tall green tomato vines climbing strings up toward the rows of hanging pink-violet grow lamps, yellow flowers and clusters of red cherry tomatoes hanging among the leaves, lettuce and cucumber vines in the lower channels; a warm incubator box with a glass window and a red heat lamp stands at frame-right; a steel staircase rises at frame-left; the concrete walls fill the background.")

# ---------------------------------------------------------------------------------------------- 第 13 集
b13 = S.episode('剧本第13集｜隐秘的火锅', '苏清月举着两盒底料说全要，林峰在厨房切牛肉；鸳鸯锅咕嘟咕嘟，红油翻滚；她涮了第一口肉，说等了半个月；他递给她一罐啤酒；吃得额头冒汗，她说外面零下八十度我们在涮肉；桌边小灰盒的黄灯亮了，脚踩雪的咯吱声从扬声器里传出来，正在咀嚼的苏清月睁大眼睛；暗房里只剩火锅下一点蓝火，林峰握住她的手，口型说：别动。', 13)

new_person(b13, 'su_arctic', '苏清月（纯白极地防寒服，兜帽、白色护目镜推在额头上，睫毛上有霜）', 'woman',
           'Su, the same elegant Chinese woman in her late twenties as in the reference, wearing a bulky pure-white polar expedition suit with the hood up, white goggles pushed up on her forehead and a white neck gaiter pulled down under her chin, frost on her lashes.',
           '苏清月，和参考图是同一位二十八岁左右、优雅美丽的中国女性，穿着臃肿的纯白色极地防寒服、兜帽戴着、白色护目镜推在额头上、白色颈套拉到下巴下面，睫毛上有霜。',
           'wearing a bulky pure-white polar expedition suit with the hood up, white goggles pushed up on her forehead and a white neck gaiter pulled down under her chin, frost on her lashes',
           'a sharp, focused expression', ref='su_suit')
new_scene(b13, 'snow_solar', '雪林里的光伏板阵列（三排黑色太阳能板半埋在雪里）',
          'A silent frozen pine clearing under a black sky with a faint green aurora: three rows of black solar panels on steel frames, half buried in snow, stand in the middle of the frame; a long low snow bank runs along the foreground; a wide snow slope rises far behind the panels at the right; snow-laden pines stand on both sides.',
          '寂静冰封的松林空地，黑色天空里有淡淡的绿色极光：画面中间是三排立在钢架上、半埋在雪里的黑色太阳能板；前景有一道长长的低矮雪堤；板阵后面右侧是一面宽阔的远处雪坡；两侧是挂满雪的松树。',
          'the three rows of snow-covered solar panels, the low snow bank in front and the far snow slope')
for _a in b13.d['assets']:
    if _a['key'] == 'snow_solar': _a['generate']['reference_keys'] = ['snow_hatch']
b13.character('SuArctic', 'su_arctic', SU_EN, SU_ZH)

SOUND_POT = voiced('The soft bubbling of the hotpot, the clink of chopsticks on the bowls and the faint hum of the air system.', '火锅轻轻的咕嘟声、筷子碰碗的轻响和空气系统轻微的嗡鸣。')
SOUND_BOX = breathy('The soft bubbling of the hotpot and a thin electronic beep from the grey box, then the slow crunch of footsteps in snow coming through its little speaker.', '火锅轻轻的咕嘟声和小灰盒细细的电子滴声，然后是小喇叭里传出来的缓慢的踩雪咯吱声。')
SOUND_DARK = voiced('The low bubbling of the hotpot, slow crunching footsteps in snow overhead through the little speaker and a held breath.', '火锅低低的咕嘟声、小喇叭里头顶传来的缓慢踩雪咯吱声和屏住的呼吸。')


def insert_task(tid, title, dur, scene, framing, act_en, zh, snd, holds, cam, bg=''):
    return S.T(tid, title, dur, scene, [], framing, act_en, zh, snd, cam=cam, holds=holds, room=set(), new=True, bg=bg)


S.T('13-01', '01｜厨房台边：苏清月举着两盒底料说全要，林峰一边切牛肉一边回她', 10, KITCHEN,
    [P('lin_home', 'left', "standing at the marble counter in profile facing frame-right, slicing a slab of red beef on the wooden board with a long knife in his right hand, his left hand wrapped in white gauze holding the meat down", 'Su', "his jaw relaxed, a faint amused curve at one corner of his mouth, his brows soft"),
     P('su_cozy', 'right', "standing beside him in profile facing frame-left, holding up a red box and a yellow box of hotpot base in her two hands", 'Lin', "her lips curved in a sweet smile, her brows lifted")],
    'Medium two-shot, both from the head to the knees, in the middle third of the frame, at the kitchen counter.',
    "<su_cozy> holds up the two boxes and speaks the first line to <lin_home> in a bright cheeky voice, her lips curved in a sweet smile and her brows lifted. <lin_home> keeps slicing the beef in slow even strokes and speaks the second line to <su_cozy> in a dry low voice, a faint amused curve at one corner of his mouth and his brows soft.",
    "苏清月把两盒底料举起来，用明快俏皮的声音对林峰说出第一句，嘴角带着俏皮的笑、眉毛上扬。林峰一刀一刀慢而均匀地继续切着牛肉，用干干的低声对苏清月说出第二句，嘴角带着一丝觉得好笑的弧度、眉毛舒展。",
    SOUND_POT,
    lines=[('su_cozy', "辣锅、菌汤，我全要。", 0.8, 'Lin'), ('lin_home', "贪心的人，活得久。", 4.6, 'Su')],
    bg='Behind them the wall of small security monitors shows a white blizzard, and the round dining table stands in the middle of the room.',
    holds='The frame holds Lin and Su, the marble counter with the cutting board, and the stove.', room={'Lin', 'Su'}, new=True,
    st={'Lin': ('灰色棉质家居服，左手缠着白纱布，站在厨房台边', '灰色棉质家居服，左手缠着白纱布，站在厨房台边'), 'Su': ('奶白色毛衣，站在厨房台边拿着两盒底料', '奶白色毛衣，站在厨房台边拿着两盒底料')})

insert_task('13-02', '02｜插镜：圆桌中间的铜鸳鸯锅，一边红油翻滚，一边菌汤冒泡，旁边摆满了菜', 4, HOT,
    'Close shot of the round dining table, the copper yin-yang hotpot in the middle third of the frame, nobody in the scene.',
    "The copper hotpot simmers in the middle of the table, the red-oil half rolling with bubbles and chili flecks, the pale mushroom half gently bubbling, white steam curling upward, and the plates of paper-thin beef rolls, tripe and shrimp arranged around it. Nothing else moves.",
    "圆桌中间的铜鸳鸯锅咕嘟咕嘟地煮着，红油那半边翻着泡、漂着辣椒，白色菌汤那半边轻轻冒泡，白色蒸汽往上卷，四周摆着薄薄的牛肉卷、毛肚和虾。别的什么都不动。",
    breathy('A rolling bubbling of the hotpot and a soft warm hush.', '火锅翻滚的咕嘟声和温暖的寂静。'),
    'The frame holds the copper yin-yang hotpot and the plates around it on the round table, and nobody in the scene.',
    push('the bubbling hotpot', '翻滚的火锅'))

S.T('13-03', '03｜圆桌边：苏清月涮了第一口牛肉，说等了半个月，林峰递给她一罐啤酒', 11, HOT,
    [P('su_cozy', 'left', "sitting at the round table in profile facing frame-right, dipping a paper-thin slice of beef into the red-oil half of the hotpot with wooden chopsticks in her right hand", 'obj:the slice of beef swirling in the red broth', "her lips parted in delight, her brows lifted"),
     P('lin_home', 'right', "sitting across the table in profile facing frame-left, sliding a cold beer can toward her with his right hand, his left hand wrapped in white gauze on the table", 'Su', "his jaw relaxed, a faint amused curve at one corner of his mouth, his brows soft")],
    'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the round table.',
    "<su_cozy> swishes the slice of beef in the red broth, lifts it and eats it, then speaks the first line to <lin_home> with her eyes closing in bliss, her lips parted in delight and her brows lifted. <lin_home> slides the cold beer can across the table and speaks the second line to <su_cozy> in a dry low voice, a faint amused curve at one corner of his mouth and his brows soft. <su_cozy> opens her eyes, takes the can and speaks the third line to <lin_home> in a happy warm voice.",
    "苏清月把牛肉片在红汤里涮了涮，夹起来吃进嘴里，闭上眼睛享受着对林峰说出第一句，嘴唇因欢喜微张、眉毛上扬。林峰把冰啤酒罐滑过桌面，用干干的低声对苏清月说出第二句，嘴角带着一丝觉得好笑的弧度、眉毛舒展。苏清月睁开眼睛，接过罐子，用开心温暖的声音对林峰说出第三句。",
    SOUND_POT,
    lines=[('su_cozy', "等这一口，等了半个月。", 0.8, 'Lin'), ('lin_home', "慢点，没人跟你抢。", 4.0, 'Su'), ('su_cozy', "这才叫活着！", 6.8, 'Lin')],
    bg='Between them the copper hotpot steams in the middle of the table, and the open kitchen glows warm at frame-left.',
    holds='The frame holds Su and Lin, the copper hotpot and the plates on the table.', room={'Su', 'Lin'}, new=True,
    st={'Su': ('奶白色毛衣，坐在圆桌边', '奶白色毛衣，坐在圆桌边'), 'Lin': ('灰色棉质家居服，左手缠着白纱布，坐在圆桌边', '灰色棉质家居服，左手缠着白纱布，坐在圆桌边')})

S.T('13-04', '04｜圆桌边：两人吃得额头冒汗，苏清月说外面零下八十度我们在涮肉', 11, HOT,
    [P('su_cozy', 'left', "sitting at the round table in profile facing frame-right, a beer can in her left hand and wooden chopsticks lifting a slice of beef from the broth in her right, a fine sweat on her forehead", 'Lin', "her cheeks flushed, her lips curved in a sweet smile, her brows lifted"),
     P('lin_home', 'right', "sitting across the table in profile facing frame-left, a beer can raised in his right hand, a fine sweat on his forehead, his left hand wrapped in white gauze on the table", 'Su', "his jaw relaxed, a faint warm curve at one corner of his mouth, his brows soft")],
    'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the round table.',
    "<su_cozy> eats the beef and speaks the first line to <lin_home> in a warm happy voice, her cheeks flushed, her lips curved in a sweet smile and her brows lifted. <lin_home> takes a slow drink from his can and speaks the second line to <su_cozy> in a low calm voice, a faint warm curve at one corner of his mouth and his brows soft. <su_cozy> laughs and speaks the third line to <lin_home>, reaching her chopsticks toward the tripe plate.",
    "苏清月吃着牛肉，用温暖开心的声音对林峰说出第一句，脸颊泛红、嘴角带着温暖的笑、眉毛上扬。林峰慢慢喝了一口啤酒，用低沉平静的声音对苏清月说出第二句，嘴角带着一丝温暖的弧度、眉毛舒展。苏清月笑出声，把筷子伸向毛肚盘，对林峰说出第三句。",
    SOUND_POT,
    lines=[('su_cozy', "外面零下八十，我们涮肉。", 0.8, 'Lin'), ('lin_home', "所以才香。", 4.4, 'Su'), ('su_cozy', "再来一盘毛肚！", 6.6, 'Lin')], dep=True,
    bg='Between them the copper hotpot steams in the middle of the table, and the open kitchen glows warm at frame-left.',
    holds='The frame holds Su and Lin, the copper hotpot and the plates on the table.',
    st={'Su': ('奶白色毛衣，坐在圆桌边', '奶白色毛衣，坐在圆桌边'), 'Lin': ('灰色棉质家居服，左手缠着白纱布，坐在圆桌边', '灰色棉质家居服，左手缠着白纱布，坐在圆桌边')})

insert_task('13-05', '05｜插镜：桌边矮架上的小灰盒，一盏黄色的小灯亮着', 3, HOT_ALERT,
    'Close shot of the low shelf at the right of the dining room, the small grey box in the middle third of the frame, nobody in the scene.',
    "On the low shelf the small grey box with its short antenna has its one small lamp glowing steady yellow, and soft white steam from the hotpot drifts across the front of the frame. Nothing else moves.",
    "矮架上，带着一根短天线的小灰盒，那一盏小灯亮着稳定的黄光，火锅的白色蒸汽轻轻飘过画面前面。别的什么都不动。",
    SOUND_BOX,
    'The frame holds the small grey box with its yellow lamp and a drift of steam, and nobody in the scene.',
    push('the yellow lamp on the grey box', '小灰盒上的黄灯'))

S.T('13-06', '06｜圆桌边：苏清月嘴里塞着毛肚睁大眼睛，林峰盯着小灰盒再转向她说有人', 9, HOT_ALERT,
    [P('su_cozy', 'left', "sitting at the round table in profile facing frame-right, a slice of tripe just lifted to her mouth between the wooden chopsticks in her right hand", 'Lin', "her eyes widening, her lips parted around the chopsticks, her brows rising"),
     P('lin_home', 'right', "sitting across the table in profile facing frame-left, his beer can set down on the table, his right hand flat on the table beside it, his left hand wrapped in white gauze", 'Su', "his jaw tight, his lips set flat, his brows low")],
    'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the round table.',
    "<lin_home> lowers his eyes toward the small grey box, then slowly turns his head to <su_cozy> and speaks one line to <su_cozy> in a barely audible voice, his jaw tight, his lips set flat and his brows low. <su_cozy> freezes with the tripe at her lips, her eyes widening, her lips parted around the chopsticks and her brows rising.",
    "林峰低头看了一眼小灰盒，然后慢慢把头转向苏清月，用几乎听不见的声音对苏清月说出一句，下颌绷紧、嘴唇抿平、眉头压低。苏清月僵住，毛肚停在嘴边，眼睛慢慢睁大、嘴唇微张含着筷子、眉毛上扬。",
    SOUND_BOX, lines=[('lin_home', "有人。", 3.6, 'Su')], new=True, room={'Su', 'Lin'},
    bg='Between them the copper hotpot steams in the middle of the table, and the small grey box with its yellow lamp stands on the low shelf at frame-right.',
    holds='The frame holds Su and Lin, the copper hotpot and the plates on the table.',
    st={'Su': ('奶白色毛衣，坐在圆桌边', '奶白色毛衣，坐在圆桌边'), 'Lin': ('灰色棉质家居服，左手缠着白纱布，坐在圆桌边', '灰色棉质家居服，左手缠着白纱布，坐在圆桌边')})

S.T('13-07', '07｜暗房里：只剩火锅下一点蓝火，林峰越过桌子握住苏清月的手，口型说别动', 8, DARK,
    [P('su_cozy', 'left', "sitting at the round table in profile facing frame-right, both hands frozen in front of her, her right hand held across the table in his hand", 'Lin', "her eyes wide and wet, her lips pressed together, her brows pulled high"),
     P('lin_home', 'right', "sitting across the table in profile facing frame-left, leaning forward with his right hand closed firmly over her right hand on the table, his left hand wrapped in white gauze", 'Su', "his jaw tight, his lips set flat, his brows low")],
    'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the dark round table.',
    "<lin_home> holds her hand and shakes his head very slightly, then speaks one line to <su_cozy> in a barely breathed whisper, his jaw tight, his lips set flat and his brows low. <su_cozy> does not speak; her breath shakes and her eyes stay locked on <lin_home>, her eyes wide and wet, her lips pressed together and her brows pulled high.",
    "林峰握着她的手，极轻地摇了一下头，然后用几乎只是气息的耳语对苏清月说出一句，下颌绷紧、嘴唇抿平、眉头压低。苏清月一句话也不说，呼吸发着抖，眼睛一直盯着林峰，眼睛睁大含着泪、嘴唇紧抿、眉毛高高皱起。",
    SOUND_DARK, lines=[('lin_home', "别动。", 1.6, 'Su')], cam=push('both of them', '两人'),
    bg='Between them the little blue flame under the hotpot flickers, and the small grey box glows red on the low shelf at frame-right.',
    holds='The frame holds Su and Lin lit faintly from below by the blue flame, the hotpot and the dark room.', room={'Su', 'Lin'}, new=True,
    st={'Su': ('奶白色毛衣，坐在圆桌边，手被林峰握着', '奶白色毛衣，坐在圆桌边，手被林峰握着'), 'Lin': ('灰色棉质家居服，左手缠着白纱布，坐在圆桌边握着她的手', '灰色棉质家居服，左手缠着白纱布，坐在圆桌边握着她的手')})

# ---------------------------------------------------------------------------------------------- 第 14 集
b14 = S.episode('剧本第14集｜头顶的死神', '暗房里，林峰一直握着苏清月的手；头顶雪地上，两个流浪者倚着冰封的排气管，一个说走不动了，另一个喊别睡，他自己也栽进雪里，再也没动；苏清月说他们还有救，林峰摇头：开门，我们也死。小灰盒的灯灭了，灯重新亮起，林峰把牛肉夹进她碗里：吃吧，肉煮老了不好吃。她问：你一点都不怕吗？他说：有门，就不怕。', 14)

S.T('14-01', '01｜暗房里：苏清月发抖着低声说他们就在上面，林峰握紧她的手说别出声', 10, DARK,
    [P('su_cozy', 'left', "sitting at the round table in profile facing frame-right, her shoulders shaking, her right hand held across the table in his hand, her left hand pressed to her chest", 'Lin', "her eyes wide and wet, her lips trembling, her brows pulled high"),
     P('lin_home', 'right', "sitting across the table in profile facing frame-left, his right hand closed firmly over her right hand on the table, his left hand wrapped in white gauze", 'Su', "his jaw tight, his lips set flat, his brows low")],
    'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the dark round table.',
    "<su_cozy> speaks the first line to <lin_home> in a trembling whisper, her shoulders shaking, her eyes wide and wet, her lips trembling and her brows pulled high. <lin_home> tightens his hold on her hand and speaks the second line to <su_cozy> in a barely breathed whisper, his jaw tight, his lips set flat and his brows low.",
    "苏清月用发抖的耳语对林峰说出第一句，肩膀发着抖，眼睛睁大含着泪、嘴唇发颤、眉毛高高皱起。林峰把她的手握得更紧，用几乎只是气息的耳语对苏清月说出第二句，下颌绷紧、嘴唇抿平、眉头压低。",
    SOUND_DARK, lines=[('su_cozy', "他们，就在上面。", 1.2, 'Lin'), ('lin_home', "别出声。", 4.8, 'Su')],
    bg='Between them the little blue flame under the hotpot flickers, and the small grey box glows red on the low shelf at frame-right.',
    holds='The frame holds Su and Lin lit faintly from below by the blue flame, the hotpot and the dark room.',
    st={'Su': ('奶白色毛衣，坐在圆桌边，手被林峰握着', '奶白色毛衣，坐在圆桌边，手被林峰握着'), 'Lin': ('灰色棉质家居服，左手缠着白纱布，坐在圆桌边握着她的手', '灰色棉质家居服，左手缠着白纱布，坐在圆桌边握着她的手')})

S.T('14-02', '02｜雪地里：两个流浪者靠着冰封的排气管，一个说走不动了，另一个拉着他喊别睡', 10, VENT,
    [P('bearded_drifter', 'left', "kneeling in the deep snow in profile facing frame-right, both gloved hands gripping the sleeve of the slumped man and pulling", 'Gaunt', "his lips cracked and trembling, his brows pulled together in desperation"),
     P('gaunt_drifter', 'right', "sitting slumped in the deep snow against the base of the thick steel exhaust pipe in profile facing frame-left, one arm hanging limp, his head tilting", 'Bearded', "his eyelids heavy, his lips pale and barely moving, his brows slack")],
    'Medium two-shot, both from the head to the knees, in the middle third of the frame, in the deep snow beside the pipe.',
    "<gaunt_drifter> speaks the first line to <bearded_drifter> in a cracked fading voice, his eyelids heavy, his lips pale and barely moving and his brows slack. <bearded_drifter> pulls at his sleeve and speaks the second line to <gaunt_drifter> in a hoarse desperate voice, his lips cracked and trembling and his brows pulled together. <gaunt_drifter>'s head slowly sinks onto his chest and his eyes close.",
    "流浪者甲用干裂渐弱的声音对流浪者乙说出第一句，眼皮沉重、嘴唇发白、几乎不动、眉毛松垮。流浪者乙拉着他的袖子，用嘶哑绝望的声音对流浪者甲说出第二句，嘴唇干裂发抖、眉头拧在一起。流浪者甲的头慢慢垂到胸口，眼睛合上了。",
    voiced('A thin howl of wind across the snow, labored breathing and the squeak of frozen cloth.', '风掠过雪地细细的呼啸、吃力的呼吸声和冻硬的衣料吱吱的摩擦声。'),
    lines=[('gaunt_drifter', "我走不动了……", 1.0, 'Bearded'), ('bearded_drifter', "别睡！站起来！", 3.8, 'Gaunt')],
    bg='Behind them snow-laden pines stand in the dark and the thick steel exhaust pipe with its iced-over mouth rises beside the sitting man.',
    holds='The frame holds Bearded kneeling and Gaunt slumped against the exhaust pipe, and snow-laden pines.', room={'Bearded', 'Gaunt'}, new=True,
    st={'Bearded': ('破旧的棉袄和针织帽，跪在雪里拉着同伴', '破旧的棉袄和针织帽，跪在雪里拉着同伴'), 'Gaunt': ('破旧的多层冬衣，靠着排气管坐在雪里', '破旧的多层冬衣，靠着排气管坐在雪里，头垂在胸口')})

S.T('14-03', '03｜雪地里：喊别睡的人自己也撑不住，慢慢栽进雪里，一动不动', 5, VENT,
    [P('bearded_drifter', 'left', "kneeling in the deep snow in profile facing frame-right, swaying, one gloved hand still on the sleeve of the slumped man beside him", 'Gaunt', "his lips cracked and slack, his brows drooping"),
     P('gaunt_drifter', 'right', "sitting slumped in the deep snow against the base of the thick steel exhaust pipe in profile facing frame-left, his head sunk on his chest, his eyes shut", 'closed', "his lips pale and still, his brows slack")],
    'Medium two-shot, both from the head to the knees, in the middle third of the frame, in the deep snow beside the pipe.',
    "<bearded_drifter> sways, his hand slides off the sleeve of <gaunt_drifter>, and he pitches slowly forward and falls face-down in the snow beside him and lies still, his lips cracked and slack and his brows drooping. <gaunt_drifter> does not move, his eyes shut, his lips pale and still and his brows slack.",
    "流浪者乙晃了晃，手从流浪者甲的袖子上滑下来，慢慢向前栽倒，脸朝下倒在他身边的雪里，一动不动，嘴唇干裂松垮、眉毛耷拉。流浪者甲一动不动，眼睛合着，嘴唇发白不动、眉毛松垮。",
    breathy('A thin howl of wind across the snow and the soft muffled thump of a body settling into powder.', '风掠过雪地细细的呼啸和一个人倒进粉雪里轻轻闷闷的一声。'),
    dep=True,
    bg='Behind them snow-laden pines stand in the dark and the thick steel exhaust pipe with its iced-over mouth rises beside the sitting man.',
    holds='The frame holds Bearded and Gaunt beside the exhaust pipe, and snow-laden pines.',
    st={'Bearded': ('破旧的棉袄和针织帽，跪在雪里拉着同伴', '破旧的棉袄和针织帽，脸朝下倒在雪里'), 'Gaunt': ('破旧的多层冬衣，靠着排气管坐在雪里，头垂在胸口', '破旧的多层冬衣，靠着排气管坐在雪里，头垂在胸口')})

insert_task('14-04', '04｜插镜：雪地里，排气管脚下堆着两个圆圆的雪堆，风吹着粉雪', 4, VENT,
    'Wide shot of the snowy forest, the thick steel exhaust pipe and two low rounded drifts of snow at its foot in the middle third of the frame, nobody in the scene.',
    "At the foot of the thick steel exhaust pipe two low rounded drifts of snow lie side by side, and a thin wind lifts a veil of powder snow across them while the snow-laden pines stand in the dark. Nothing else moves.",
    "排气管脚下，两个低低圆圆的雪堆并排躺着，一阵细风把一层粉雪吹过它们，挂满雪的松树在黑暗里立着。别的什么都不动。",
    breathy('A long thin howl of wind across the snow and a deep hush.', '风掠过雪地长长的呼啸和深深的寂静。'),
    'The frame holds the thick steel exhaust pipe, the two low drifts at its foot and the snow-laden pines, and nobody in the scene.',
    push('the two drifts at the foot of the pipe', '排气管脚下的两个雪堆'))

S.T('14-05', '05｜暗房里：苏清月看了一眼天花板说他们还有救，林峰按紧她的手说开门我们也死', 10, DARK,
    [P('su_cozy', 'left', "sitting at the round table in profile facing frame-right, her face turned up toward the ceiling then back to him, her right hand held in his hand across the table", 'Lin', "her eyes glistening, her lips trembling, her brows pulled together"),
     P('lin_home', 'right', "sitting across the table in profile facing frame-left, his right hand closed hard over her hand, his left hand wrapped in white gauze", 'Su', "his jaw tight, his lips set flat, his brows low, his eyes cold")],
    'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the dark round table.',
    "<su_cozy> lifts her eyes toward the ceiling for a moment, then looks back at <lin_home> and speaks the first line to <lin_home> in a shaking whisper, her eyes glistening, her lips trembling and her brows pulled together. <lin_home> presses her hand harder, shakes his head once and speaks the second line to <su_cozy> in a cold low whisper, his jaw tight, his lips set flat, his brows low and his eyes cold.",
    "苏清月抬眼看了一下天花板，又看回林峰，用发抖的耳语对林峰说出第一句，眼睛含着泪光、嘴唇发颤、眉头拧在一起。林峰把她的手握得更紧，摇了一下头，用冷冷的低声耳语对苏清月说出第二句，下颌绷紧、嘴唇抿平、眉头压低、眼神冰冷。",
    SOUND_DARK, lines=[('su_cozy', "他们，还有救……", 1.2, 'Lin'), ('lin_home', "开门，我们也死。", 4.4, 'Su')], new=True, room={'Su', 'Lin'},
    bg='Between them the little blue flame under the hotpot flickers, and the small grey box stands on the low shelf at frame-right.',
    holds='The frame holds Su and Lin lit faintly from below by the blue flame, the hotpot and the dark room.',
    st={'Su': ('奶白色毛衣，坐在圆桌边，手被林峰握着', '奶白色毛衣，坐在圆桌边，手被林峰握着'), 'Lin': ('灰色棉质家居服，左手缠着白纱布，坐在圆桌边握着她的手', '灰色棉质家居服，左手缠着白纱布，坐在圆桌边握着她的手')})

insert_task('14-06', '06｜插镜：桌边矮架上的小灰盒，那盏灯已经灭了', 3, HOT,
    'Close shot of the low shelf at the right of the dining room, the small grey box in the middle third of the frame, nobody in the scene.',
    "On the low shelf the small grey box with its short antenna has its one small lamp dark and dead, and soft white steam from the hotpot drifts slowly across the front of the frame. Nothing else moves.",
    "矮架上，带着一根短天线的小灰盒，那一盏小灯已经灭了，火锅的白色蒸汽慢慢飘过画面前面。别的什么都不动。",
    breathy('The soft bubbling of the hotpot and a long quiet hush.', '火锅轻轻的咕嘟声和长长的安静。'),
    'The frame holds the small grey box with its dark lamp and a drift of steam, and nobody in the scene.',
    push('the dark lamp on the grey box', '小灰盒上熄灭的灯'))

S.T('14-07', '07｜圆桌边：灯亮了，林峰把牛肉夹进苏清月碗里说吃吧，苏清月问你一点都不怕吗', 12, HOT,
    [P('lin_home', 'right', "sitting at the round table in profile facing frame-left, lifting a slice of cooked beef from the broth with a slotted spoon in his right hand and lowering it toward her bowl, his left hand wrapped in white gauze", 'Su', "his jaw relaxed, a faint calm curve at one corner of his mouth, his brows soft"),
     P('su_cozy', 'left', "sitting at the round table in profile facing frame-right, a small white bowl held in both hands in front of her, her face pale", 'Lin', "her lips parted, her brows lifted")],
    'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the round table.',
    "<lin_home> places the beef into her bowl and speaks the first line to <su_cozy> in a calm warm voice, his jaw relaxed, a faint calm curve at one corner of his mouth and his brows soft. <su_cozy> looks at the bowl, then at him, and speaks the second line to <lin_home> in a soft wondering voice, her lips parted and her brows lifted. <lin_home> answers with the third line to <su_cozy> in a low even voice, then <su_cozy> lowers her eyes, lifts her chopsticks and eats the beef.",
    "林峰把牛肉放进她的碗里，用平静温暖的声音对苏清月说出第一句，下颌放松、嘴角带着一丝平静的弧度、眉毛舒展。苏清月看着碗，又看着他，用轻轻带着疑惑的声音对林峰说出第二句，嘴唇微张、眉毛上扬。林峰用低沉平稳的声音对苏清月答出第三句，然后苏清月垂下眼睛，拿起筷子，把牛肉吃了下去。",
    SOUND_POT,
    lines=[('lin_home', "吃吧，肉煮老了不好吃。", 1.0, 'Su'), ('su_cozy', "你一点都不怕吗？", 4.8, 'Lin'), ('lin_home', "有门，就不怕。", 7.6, 'Su')],
    bg='Between them the copper hotpot steams in the middle of the table, and the open kitchen glows warm at frame-left.',
    holds='The frame holds Su and Lin, the copper hotpot and the plates on the table.', room={'Su', 'Lin'}, new=True,
    st={'Su': ('奶白色毛衣，坐在圆桌边', '奶白色毛衣，坐在圆桌边'), 'Lin': ('灰色棉质家居服，左手缠着白纱布，坐在圆桌边', '灰色棉质家居服，左手缠着白纱布，坐在圆桌边')})

# ---------------------------------------------------------------------------------------------- 第 15 集
b15 = S.episode('剧本第15集｜白雪幽灵', '几天后，主控台上一盏黄灯闪着，墙上的小监控里光伏板被厚雪盖住；缓冲舱里，林峰递给苏清月一把白色的无声铲，她说我跟你一起去；两人穿着白色防寒服从树桩舱口爬出，睫毛上结了霜；他们在光伏板上一点一点推雪，不能扫；远处山坡上出现几个很小的深色人影，林峰把苏清月按进雪堤后面；两人趴着一点点往后挪，说：我们是雪；缓冲舱的圆形舱门锁死，两人靠着门喘气，相视一笑。', 15)

insert_task('15-01', '01｜插镜：主控台上一盏黄灯闪着，墙上的小监控里，黑色的光伏板被厚厚的白雪盖住', 4, CONTROL,
    'Close shot of the control console, the blinking amber lamp and the small wall monitor in the middle third of the frame, nobody in the scene.',
    "On the steel console one amber lamp blinks slowly among the steady green lights, and on the small wall monitor behind it rows of black solar panels lie buried under thick white snow. Nothing else moves.",
    "钢制控制台上，一盏琥珀色的灯在一排稳定的绿灯中缓慢闪烁，后面墙上的小监控里，一排排黑色的太阳能板被厚厚的白雪盖住。别的什么都不动。",
    breathy('A low electric hum from the console and one slow soft beep.', '控制台低低的电流嗡鸣和一声缓慢的轻响。'),
    'The frame holds the console with its blinking amber lamp and the small wall monitor, and nobody in the scene.',
    push('the blinking amber lamp', '闪烁的琥珀灯'))

S.T('15-02', '02｜缓冲舱里：林峰把白色的无声铲递给苏清月，苏清月说我跟你一起去', 12, AIRLOCK2,
    [P('lin_arctic', 'left', "standing in profile facing frame-right in the bulky white polar suit with his hood up, holding a white-handled silent shovel out toward her in his right hand", 'Su', "his jaw tight, his lips set flat, his brows level"),
     P('su_arctic', 'right', "standing in profile facing frame-left in the bulky white polar suit with her hood up, reaching out both gloved hands to take the shovel", 'Lin', "her chin lifted, her lips pressed in a firm line, her brows level")],
    'Medium two-shot, both from the head to the knees, in the middle third of the frame, in the white-tiled airlock.',
    "<su_arctic> speaks the first line to <lin_arctic> in a firm quiet voice, her chin lifted, her lips pressed in a firm line and her brows level, and takes the shovel in both hands. <lin_arctic> speaks the second line to <su_arctic> in a low steady voice, his jaw tight, his lips set flat and his brows level. <su_arctic> gives a small nod and speaks the third line to <lin_arctic>.",
    "苏清月用坚定安静的声音对林峰说出第一句，下巴微抬、嘴唇紧紧抿着、眉毛平直，双手接过了铲子。林峰用低沉稳当的声音对苏清月说出第二句，下颌绷紧、嘴唇抿平、眉毛平直。苏清月轻轻点了点头，对林峰说出第三句。",
    SOUND_AIRLOCK,
    lines=[('su_arctic', "我跟你一起去。", 0.8, 'Lin'), ('lin_arctic', "一点声音都不能有。", 3.6, 'Su'), ('su_arctic', "知道了。", 7.6, 'Lin')],
    bg='Behind them the long steel bench and the shelf of white goggles line the left wall, and the heavy round steel hatch door stands in the right wall.',
    holds='The frame holds Lin and Su in white polar suits, the steel bench and the hatch door.', room={'Lin', 'Su'}, new=True,
    st={'Lin': ('白色极地防寒服，兜帽戴着，手里拿着铲子', '白色极地防寒服，兜帽戴着'), 'Su': ('白色极地防寒服，兜帽戴着', '白色极地防寒服，兜帽戴着，手里拿着铲子')})

S.T('15-03', '03｜树桩舱口边：两人趴在雪里，睫毛结了霜，苏清月低声说睫毛冻住了，林峰让她戴上护目镜', 9, HATCH,
    [P('lin_arctic', 'left', "crouching in the waist-deep snow beside the open hatch in profile facing frame-right, his white goggles already over his eyes, a white shovel in his right hand", 'Su', "his jaw tight, his lips set flat, his brows level"),
     P('su_arctic', 'right', "crouching in the snow in profile facing frame-left, her hood up, frost on her lashes and cheeks, her goggles still pushed up on her forehead, a white shovel in her left hand", 'Lin', "her lips pressed tight against the cold, her brows pulled together")],
    'Medium two-shot, both from the head to the knees, in the middle third of the frame, in the snow beside the hatch.',
    "<su_arctic> speaks the first line to <lin_arctic> in a hushed voice, her lips pressed tight against the cold and her brows pulled together. <lin_arctic> speaks the second line to <su_arctic> in a low voice, his jaw tight, his lips set flat and his brows level. <su_arctic> pulls her goggles down over her eyes with her right hand.",
    "苏清月用压低的声音对林峰说出第一句，嘴唇因寒冷紧紧抿着、眉头拧在一起。林峰用低沉的声音对苏清月说出第二句，下颌绷紧、嘴唇抿平、眉毛平直。苏清月用右手把护目镜拉下来盖住眼睛。",
    breathy('A thin wind across the snow, a soft crunch of boots and slow frosted breaths.', '风掠过雪地细细的声音、靴子轻轻的咯吱和缓慢结着白霜的呼吸。') if False else voiced('A thin wind across the snow, a soft crunch of boots and slow frosted breaths.', '风掠过雪地细细的声音、靴子轻轻的咯吱和缓慢结着白霜的呼吸。'),
    lines=[('su_arctic', "睫毛，都冻住了。", 1.0, 'Lin'), ('lin_arctic', "护目镜，戴上。", 4.2, 'Su')],
    bg='Behind them the camouflaged tree-trunk hatch stands open at frame-left and snow-laden pines fill the background.',
    holds='The frame holds Lin and Su crouched in the snow, the open hatch and snow-laden pines.', room={'Lin', 'Su'}, new=True,
    st={'Lin': ('白色极地防寒服，护目镜戴好', '白色极地防寒服，护目镜戴好'), 'Su': ('白色极地防寒服，兜帽戴着，护目镜推在额头上', '白色极地防寒服，兜帽戴着，护目镜戴好')})

S.T('15-04', '04｜光伏板阵列：两人用白色的铲子一点一点把积雪从板上推下去，一点声音都没有', 10, SOLAR,
    [P('lin_arctic', 'left', "standing at a black solar panel in profile facing frame-right in the bulky white suit with his goggles down, pushing a thick slab of snow slowly off the panel with a white shovel held in both hands", 'obj:the slab of snow sliding off the panel', "his jaw tight, his lips set flat"),
     P('su_arctic', 'right', "standing at the next panel in profile facing frame-right in the bulky white suit with her goggles down, pushing the snow slowly off the panel with a white shovel held in both hands", 'obj:the snow on the panel in front of her', "her lips pressed in a firm line")],
    'Medium two-shot, both from the head to the knees, in the middle third of the frame, at the solar panels.',
    "<lin_arctic> pushes the slab of snow off the panel in one slow smooth sweep so that it slides down in soft pieces without a puff, his jaw tight and his lips set flat. <su_arctic> copies him at the next panel, pushing the snow off in slow smooth strokes, her lips pressed in a firm line.",
    "林峰一下缓慢顺滑地把一整块雪从板上推下去，雪软软地一块块滑落，没有扬起雪雾，下颌绷紧、嘴唇抿平。苏清月在旁边的板上学着他，一下一下缓慢顺滑地把雪推下去，嘴唇紧紧抿着。",
    breathy('A faint hush of snow sliding in soft pieces and slow frosted breaths in a vast silence.', '雪软软地一块块滑落的轻微沙沙声和缓慢结着白霜的呼吸，周围是巨大的寂静。'),
    cam=track('both of them', '两人'),
    bg='Behind them the rows of half-buried solar panels and snow-laden pines stand in the dark, and a wide snow slope rises far at frame-right.',
    holds='The frame holds Lin and Su in white suits, the solar panels, the snow bank and the far slope.', room={'Lin', 'Su'}, new=True,
    st={'Lin': ('白色极地防寒服，护目镜戴好，手里拿着铲子', '白色极地防寒服，护目镜戴好，手里拿着铲子'), 'Su': ('白色极地防寒服，护目镜戴好，手里拿着铲子', '白色极地防寒服，护目镜戴好，手里拿着铲子')})

S.T('15-05', '05｜光伏板边：林峰一把按住苏清月的肩膀，两人一起扑倒在雪堤后面', 5, SOLAR,
    [P('lin_arctic', 'left', "standing at the solar panels in profile facing frame-right, his head turned sharply toward the far snow slope, his right hand already clamped on her shoulder", 'obj:the far snow slope at frame-right', "his jaw clenched, his lips set flat, his brows low"),
     P('su_arctic', 'right', "standing beside him in profile facing frame-right, bent slightly at the waist with a shovel in her hands, his hand on her shoulder", 'obj:the snow in front of her', "her eyes wide behind the goggles, her lips parted")],
    'Medium two-shot, both from the head to the knees, in the middle third of the frame, at the solar panels.',
    "<lin_arctic> presses <su_arctic> down by the shoulder and both of them drop quickly onto their stomachs behind the low snow bank in the foreground and lie flat with the shovels beside them, <lin_arctic> with his jaw clenched and his brows low, <su_arctic> with her lips parted.",
    "林峰按住苏清月的肩膀往下压，两人一起迅速趴到前景低矮的雪堤后面，平平地趴着，铲子放在身边，林峰咬紧下颌、眉头压低，苏清月嘴唇微张。",
    breathy('A sharp soft rustle of heavy cloth, a muffled thump into the snow and fast frosted breaths.', '厚重衣料短促的摩擦声、扑进雪里闷闷的一声和急促结着白霜的呼吸。'),
    dep=True,
    bg='Behind them the rows of half-buried solar panels and snow-laden pines stand in the dark, and a wide snow slope rises far at frame-right.',
    holds='The frame holds Lin and Su, the solar panels, the low snow bank and the far slope.',
    st={'Lin': ('白色极地防寒服，护目镜戴好，手里拿着铲子', '白色极地防寒服，护目镜戴好，趴在雪堤后面'), 'Su': ('白色极地防寒服，护目镜戴好，手里拿着铲子', '白色极地防寒服，护目镜戴好，趴在雪堤后面')})

insert_task('15-06', '06｜插镜：很远的雪坡上，几个很小的深色人影站在雪里，四处张望', 5, SOLAR,
    'Wide shot from behind the low snow bank of the far snow slope, the slope in the middle third of the frame, no one in the foreground.',
    "On the far white snow slope, tiny and dark against the snow, five small figures in patchwork winter clothes stand scattered and still, each holding a long gun and turning slowly to look around. In the foreground only the edge of the low snow bank and a corner of a solar panel show. Nothing else moves.",
    "很远的白色雪坡上，五个很小的、在白雪映衬下发黑的人影，穿着杂牌冬衣，分散着站在那里，每人拿着一支长枪，慢慢转头四处张望。前景只露出低矮雪堤的边缘和一角太阳能板。别的什么都不动。",
    breathy('A long thin howl of wind across the snow and a heavy hush.', '风掠过雪地长长的呼啸和沉重的寂静。'),
    'The frame holds the far snow slope with the five tiny dark figures, the edge of the snow bank and a corner of a solar panel in the foreground.',
    push('the tiny dark figures on the far slope', '远处雪坡上很小的深色人影'))

S.T('15-07', '07｜雪堤后面：两人趴着，苏清月说他们有枪，林峰说我们是雪，一边慢慢往后挪', 11, SOLAR,
    [P('lin_arctic', 'left', "lying flat on his stomach in the snow behind the low snow bank in profile facing frame-right, only his hooded head raised enough to see over the bank, a white shovel beside him", 'obj:the far snow slope at frame-right', "his jaw tight, his lips set flat, his brows low"),
     P('su_arctic', 'right', "lying flat on her stomach beside him in profile facing frame-left, her hooded head turned toward him, her right gloved hand resting on a sheathed knife at her hip", 'Lin', "her lips parted, her brows pulled together")],
    'Medium two-shot, both from the head to the waist, in the middle third of the frame, behind the snow bank.',
    "<su_arctic> speaks the first line to <lin_arctic> in a barely audible whisper, her lips parted and her brows pulled together. <lin_arctic> does not turn his head, keeps his eyes on the far slope and speaks the second line to <su_arctic> in a calm whisper, his jaw tight, his lips set flat and his brows low. Then <lin_arctic> slides his hand along her back and the two of them begin to inch slowly backward through the snow together.",
    "苏清月用几乎听不见的耳语对林峰说出第一句，嘴唇微张、眉头拧在一起。林峰没有转头，眼睛一直看着远处的雪坡，用平静的耳语对苏清月说出第二句，下颌绷紧、嘴唇抿平、眉头压低。然后林峰的手沿着她的背滑过，两人一起在雪里慢慢往后挪。",
    voiced('A thin wind across the snow, the faint crunch of snow under cloth and held frosted breaths.', '风掠过雪地细细的声音、衣料擦过雪的轻轻咯吱和屏住的结霜的呼吸。'),
    lines=[('su_arctic', "他们，有枪。", 1.0, 'Lin'), ('lin_arctic', "别动，我们是雪。", 3.8, 'Su')], new=True, room={'Lin', 'Su'},
    bg='Behind them the rows of half-buried solar panels stand in the dark, and the far snow slope rises at frame-right.',
    holds='The frame holds Lin and Su lying behind the low snow bank, the solar panels and the far slope.',
    st={'Lin': ('白色极地防寒服，护目镜戴好，趴在雪堤后面', '白色极地防寒服，护目镜戴好，趴在雪堤后面'), 'Su': ('白色极地防寒服，护目镜戴好，趴在雪堤后面', '白色极地防寒服，护目镜戴好，趴在雪堤后面')})

S.T('15-08', '08｜缓冲舱里：两人靠在关死的圆形舱门上大口喘气，苏清月说吓死我了，林峰说没开枪就是赢', 9, AIRLOCK2,
    [P('su_arctic', 'center', "standing with her back against the closed round steel hatch door in profile facing frame-right, her hood pushed back and her goggles up, her chest heaving, a white shovel in her left hand", 'Lin', "her cheeks flushed, her lips parted as she pants, her brows lifted"),
     P('lin_arctic', 'right', "standing with his back against the closed round steel hatch door in profile facing frame-left, his hood pushed back and his goggles up, his chest heaving", 'Su', "his jaw loosening, a faint relieved curve at one corner of his mouth, his brows lifted")],
    'Medium two-shot, both from the head to the knees, in the middle third of the frame, in front of the hatch door.',
    "<su_arctic> pants and speaks the first line to <lin_arctic> in a shaky breathless voice, her cheeks flushed, her lips parted and her brows lifted. <lin_arctic> turns his head to her and speaks the second line to <su_arctic> in a low warm voice, his jaw loosening, a faint relieved curve at one corner of his mouth and his brows lifted. <su_arctic> laughs breathlessly.",
    "苏清月喘着气，用发抖带喘的声音对林峰说出第一句，脸颊泛红、嘴唇因喘气微张、眉毛上扬。林峰转头看着她，用低沉温暖的声音对苏清月说出第二句，下颌放松、嘴角带着一丝松了口气的弧度、眉毛上扬。苏清月喘着气笑了出来。",
    SOUND_AIRLOCK,
    lines=[('su_arctic', "吓死我了。", 1.4, 'Lin'), ('lin_arctic', "没开枪，就是赢。", 4.0, 'Su')],
    bg='Behind them the long steel bench with the white boots and the shelf of goggles line the left wall.',
    holds='The frame holds Su and Lin leaning on the closed hatch door, the steel bench and the goggles shelf.', room={'Su', 'Lin'}, new=True,
    st={'Su': ('白色极地防寒服，兜帽放下，护目镜推在额头上，靠着舱门', '白色极地防寒服，兜帽放下，护目镜推在额头上，靠着舱门'), 'Lin': ('白色极地防寒服，兜帽放下，护目镜推在额头上，靠着舱门', '白色极地防寒服，兜帽放下，护目镜推在额头上，靠着舱门')})

# ---------------------------------------------------------------------------------------------- 第 16 集
b16 = S.episode('剧本第16集｜末日里的第一口鲜甜', '地下二层，苏清月一个人拿着小软刷，给番茄的黄色小花一朵一朵刷粉，轻声说今天给你们牵线；几天后，藤蔓上挂着一串红得发亮的樱桃小番茄，她捧着它喊：林峰，红了！他咬下一颗，说：很甜，你的书没白读；两人端着一盘番茄和黄瓜走向楼梯，头顶生长灯里有一盏忽然灭了；主控台边缘亮起一盏黄灯。', 16)

S.T('16-01', '01｜地下二层：苏清月一个人用小软刷给番茄的黄花刷粉，低声说今天给你们牵线', 10, EDEN2,
    [P('su_cozy', 'center', "standing at a tomato row in profile facing frame-right, a small soft brush in her right hand touching the tiny yellow flowers on a tomato vine, her left hand cupping the stem", 'obj:the tiny yellow tomato flowers under the brush', "her lips curved in a sweet smile, her brows soft")],
    'Medium shot, the figure from the head to the knees, in the middle third of the frame, at the tomato row.',
    "<su_cozy> brushes one yellow flower after another with slow light touches, her eyes on the flowers, then murmurs one line to herself in a soft playful voice, talking to nobody, her lips moving softly, then a second short line, her lips curved in a sweet smile and her brows soft. Nobody else is in the room.",
    "苏清月用小软刷轻轻地一朵接一朵碰着黄花，眼睛看着那些花，然后用轻轻带着玩笑的声音自言自语了一句，不是对任何人说的，嘴唇轻轻动着，接着又是一句很短的，嘴角带着温柔的笑、眉毛舒展。房间里没有别人。",
    voiced('A soft hum of grow lamps, the gentle trickle of nutrient water and her hushed murmur.', '生长灯轻轻的嗡鸣、营养液轻轻流淌的声音和她轻轻的自语。'),
    vo=[('su_cozy', "别害羞。", 2.2, 'Su'), ('su_cozy', "今天，我给你们牵线。", 5.0, 'Su')], cam=push1('Su and the flowers', '苏清月和黄色小花'),
    bg='Behind her the long hydroponic channels glow under the pink-violet lamps with tall tomato vines climbing the strings.',
    holds='The frame holds Su alone at the tomato row, the vines and the grow lamps.', room={'Su'}, new=True,
    st={'Su': ('奶白色毛衣，站在番茄架边', '奶白色毛衣，站在番茄架边')})

insert_task('16-02', '02｜插镜：粉紫色的灯光下，藤蔓深处挂着一串红得发亮的樱桃小番茄，上面有水珠', 4, EDEN2,
    'Close shot of a tomato vine, a cluster of red cherry tomatoes in the middle third of the frame, nobody in the scene.',
    "Among the green leaves under the pink-violet light a cluster of plump glossy red cherry tomatoes hangs from the vine with fresh water beads on their skins, and one bead slowly rolls down the nearest tomato. Nothing else moves.",
    "粉紫色的灯光下，绿叶之间挂着一串饱满发亮的红色樱桃小番茄，表皮上凝着新鲜的水珠，最近的一颗上有一颗水珠慢慢滚下来。别的什么都不动。",
    breathy('A soft hum of grow lamps and a faint drip of water.', '生长灯轻轻的嗡鸣和一滴水轻轻落下的声音。'),
    'The frame holds the cluster of red cherry tomatoes among the leaves, and nobody in the scene.',
    push('the cluster of red tomatoes', '那串红番茄'))

S.T('16-03', '03｜地下二层：苏清月捧着刚摘下的一串红番茄，喊林峰红了，说地底下真的种出来了', 10, EDEN2,
    [P('su_cozy', 'left', "standing at the tomato row in profile facing frame-right, cradling a freshly picked cluster of red cherry tomatoes in both palms", 'Lin', "her eyes shining, her lips parted in a sweet smile, her brows lifted"),
     P('lin_home', 'right', "standing in the aisle in profile facing frame-left with his arms loosely folded, his left hand wrapped in a small white bandage", 'Su', "his jaw relaxed, a faint warm curve at one corner of his mouth, his brows soft")],
    'Medium two-shot, both from the head to the knees, in the middle third of the frame, at the tomato row.',
    "<su_cozy> lifts the cluster a little toward <lin_home> and speaks the first line to <lin_home> in a glowing happy voice, then the second line, her eyes shining, her lips parted in a sweet smile and her brows lifted. <lin_home> looks at her and the tomatoes and speaks the third line to <su_cozy> in a low warm voice, a faint warm curve at one corner of his mouth and his brows soft.",
    "苏清月把那串番茄微微举向林峰，用发亮开心的声音对林峰说出第一句，接着说出第二句，眼睛发亮、嘴唇因喜悦微张、眉毛上扬。林峰看着她和番茄，用低沉温暖的声音对苏清月说出第三句，嘴角带着一丝温暖的弧度、眉毛舒展。",
    voiced('A soft hum of grow lamps, the gentle trickle of nutrient water and a small happy laugh.', '生长灯轻轻的嗡鸣、营养液轻轻流淌的声音和一声小小的开心的笑。'),
    lines=[('su_cozy', "林峰，红了！", 0.8, 'Lin'), ('su_cozy', "地底下，真的种出来了！", 2.4, 'Lin'), ('lin_home', "我看见了。", 6.2, 'Su')],
    bg='Behind them the long hydroponic channels glow under the pink-violet lamps with red tomatoes among the vines.',
    holds='The frame holds Su and Lin, the tomato vines and the grow lamps.', room={'Su', 'Lin'}, new=True,
    st={'Su': ('奶白色毛衣，站在番茄架边捧着一串番茄', '奶白色毛衣，站在番茄架边捧着一串番茄'), 'Lin': ('灰色棉质家居服，左手缠着小块白绷带，站在过道里', '灰色棉质家居服，左手缠着小块白绷带，站在过道里')})

S.T('16-04', '04｜地下二层：林峰就着她的手咬下一颗番茄，说很甜，你的书没白读，她红了脸', 11, EDEN2,
    [P('su_cozy', 'left', "standing at the tomato row in profile facing frame-right, holding the cluster of red cherry tomatoes up in her palm toward him", 'Lin', "her lips parted, her cheeks tinted pink, her brows lifted"),
     P('lin_home', 'right', "standing in the aisle in profile facing frame-left, leaning slightly toward her palm with a cherry tomato just bitten in his mouth", 'Su', "his jaw relaxed, his eyes warm, his brows soft")],
    'Medium two-shot, both from the head to the waist, in the middle third of the frame, at the tomato row.',
    "<lin_home> chews slowly, his eyes on her, and speaks the first line to <su_cozy> in a low warm voice, then the second line, his jaw relaxed, his eyes warm and his brows soft. <su_cozy> looks back at him, her lips parted, her cheeks tinted pink and her brows lifted, then lowers her eyes and speaks the third line to <lin_home> softly.",
    "林峰慢慢嚼着，看着她，用低沉温暖的声音对苏清月说出第一句，接着说出第二句，下颌放松、眼神温暖、眉毛舒展。苏清月回看着他，嘴唇微张、脸颊泛起粉红、眉毛上扬，然后垂下眼睛，轻轻对林峰说出第三句。",
    voiced('A crisp small pop of a tomato skin, a soft hum of grow lamps and the gentle trickle of nutrient water.', '番茄皮清脆的一声轻响、生长灯轻轻的嗡鸣和营养液轻轻流淌的声音。'),
    lines=[('lin_home', "很甜。", 3.0, 'Su'), ('lin_home', "你的书，没白读。", 4.6, 'Su'), ('su_cozy', "少贫嘴。", 8.0, 'Lin')], dep=True,
    bg='Behind them the long hydroponic channels glow under the pink-violet lamps with red tomatoes among the vines.',
    holds='The frame holds Su and Lin, the tomato vines and the grow lamps.',
    st={'Su': ('奶白色毛衣，站在番茄架边捧着一串番茄', '奶白色毛衣，站在番茄架边捧着一串番茄'), 'Lin': ('灰色棉质家居服，左手缠着小块白绷带，站在过道里', '灰色棉质家居服，左手缠着小块白绷带，站在过道里')})

S.T('16-05', '05｜地下二层：两人端着一盘番茄和黄瓜走向楼梯，苏清月说晚上凉拌黄瓜，林峰说加一勺辣油', 9, EDEN2,
    [P('su_cozy', 'center', "walking toward the steel staircase in profile facing frame-left, a white plate of red cherry tomatoes and green cucumber slices held in both hands", 'obj:the steel staircase ahead', "her lips curved in a sweet smile, her brows soft"),
     P('lin_home', 'right', "walking beside her in profile facing frame-left, his left hand wrapped in a small white bandage", 'Su', "his jaw relaxed, a faint warm curve at one corner of his mouth, his brows soft")],
    'Medium two-shot, both from the head to the waist, in the middle third of the frame, walking in the aisle.',
    "<su_cozy> walks with the plate and speaks the first line to <lin_home> in a bright happy voice, her lips curved in a sweet smile and her brows soft. <lin_home> walks beside her and speaks the second line to <su_cozy> in a low warm voice, a faint warm curve at one corner of his mouth and his brows soft. The two of them stop at the foot of the steel staircase.",
    "苏清月端着盘子往前走，用明快开心的声音对林峰说出第一句，嘴角带着开心的笑、眉毛舒展。林峰在她身边走着，用低沉温暖的声音对苏清月说出第二句，嘴角带着一丝温暖的弧度、眉毛舒展。两人在钢楼梯脚下停住。",
    voiced('A soft hum of grow lamps, soft footsteps on concrete and the faint clink of the plate.', '生长灯轻轻的嗡鸣、水泥地上轻轻的脚步声和盘子轻轻的碰响。'),
    lines=[('su_cozy', "晚上，凉拌黄瓜？", 1.0, 'Lin'), ('lin_home', "再加一勺辣油。", 3.8, 'Su')],
    cam=('The camera tracks sideways slowly alongside the two of them until they stop at the foot of the steel staircase in the middle third of the frame.', '镜头缓缓横移跟着两人，直到两人停在钢楼梯脚下、占画面中间三分之一。'),
    bg='Ahead of them the steel staircase rises at frame-left and the hydroponic channels glow under the pink-violet lamps behind them.',
    holds='The frame holds Su and Lin walking, the plate of tomatoes and cucumbers and the steel staircase.', room={'Su', 'Lin'}, new=True,
    st={'Su': ('奶白色毛衣，端着一盘番茄和黄瓜', '奶白色毛衣，端着一盘番茄和黄瓜'), 'Lin': ('灰色棉质家居服，左手缠着小块白绷带', '灰色棉质家居服，左手缠着小块白绷带')})

insert_task('16-06', '06｜插镜：长长一排粉紫色的生长灯，中间有一盏灯灭了，旁边的灯都亮着', 3, EDEN2,
    'Wide shot of the long row of pink-violet grow lamps hanging over the channels, the row in the middle third of the frame, nobody in the scene.',
    "Along the long row of hanging pink-violet grow lamps one lamp in the middle is dark while all its neighbours stay lit, and the glow on the leaves below it is dimmer in one patch. Nothing else moves.",
    "长长一排吊着的粉紫色生长灯，中间有一盏是黑的，旁边的灯都亮着，它下面那一小片叶子上的光暗了一块。别的什么都不动。",
    breathy('A soft hum of grow lamps with one low buzz fading away.', '生长灯轻轻的嗡鸣，有一声低低的电流声渐渐消失。'),
    'The frame holds the row of grow lamps with one dark lamp in the middle and the leaves under them, and nobody in the scene.',
    push('the dark lamp in the row', '那排灯里熄灭的一盏'))

insert_task('16-07', '07｜插镜：主控台的边缘，一盏小小的黄灯亮着，旁边是一排绿灯', 4, CONTROL,
    'Close shot of the edge of the control console, one small yellow lamp in the middle third of the frame, nobody in the scene.',
    "At the edge of the steel console one small yellow lamp glows steady beside the long row of green status lights, and the red digital clock on the wall behind it is blurred and dark. Nothing else moves.",
    "钢制控制台的边缘，一盏小小的黄灯稳定地亮着，旁边是一长排绿色的状态灯，后面墙上的红色电子钟模糊而暗。别的什么都不动。",
    breathy('A low electric hum from the console and one thin soft beep.', '控制台低低的电流嗡鸣和一声细细的轻响。'),
    'The frame holds the console edge with its yellow lamp and the green lights, and nobody in the scene.',
    push('the yellow lamp', '那盏黄灯'))

doc = S.finish()
