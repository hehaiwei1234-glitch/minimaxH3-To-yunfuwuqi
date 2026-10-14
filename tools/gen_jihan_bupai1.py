#!/usr/bin/env python3
"""《极寒末日：我的隐秘安全屋》补拍包 1（2026-10-14）。必须接在 009（剧本第 1–16 集）之后追加（以 009 的 JSON 为底，style／素材／角色逐字复制）；
追加窗口不要勾“每集／总／任务秒数”。放在 `极寒末日_隐秘安全屋/补拍/`。

起因：hh 看了 009 的第 5–16 集（2026-10-14 09:51–10:00）：降临太短、渲染严寒的凄惨不够；酒窖里苏清月对暴徒几乎没有碰撞（只有 1 秒爆炸声）；
两个人从猜忌到信任缺一个过程；运镜几乎全是固定；对白缺感情；第 10 集 04 号手术后冒出第三个人、场景像正常医院；第 10 集 06 号林峰两个头。
他的要求：只重写他指出的地方，放进“补拍”文件夹，不要整体重写。

三组（每组替换／插入的位置在下面；其余镜头一个字不动）：
  补拍 A（8 个任务，约 52 秒）：替换剧本第 6 集 01、02 号镜头 ——
      正午大街（起重机下降）→ 烧烤摊老板和白领抬头看雾 → 雾墙滚来（起重机上升）→ 人群朝镜头奔跑（镜头倒退）→ 雾锋扫过车流（推近）→
      白领靠着结霜的车颤声叫妈 → 拉远看他已经冻住 → 起重机下降到冰封街面。
  补拍 B（5 个任务，约 35 秒）：替换剧本第 8 集 03 号镜头（08-02 点着酒精瓶之后接 B-01） ——
      钢门被锤得发抖 → 两个暴徒堵在台阶上喊话、苏清月举着燃烧瓶回话 → 瓶子砸向台阶（单独占 6 秒）→ 台阶上的火和空门口 → 苏清月靠着货箱手抖、自言自语。
  补拍 C（5 个任务，约 45 秒）：手术前插一条信任戏（C-01，接在剧本第 10 集 01 号前）；替换第 10 集 04 号（C-02、C-03 两个任务，开场图不指定场景，
      改在文字里写“没有窗、没有门、没有第三个人”）；替换第 10 集 06 号（C-04、C-05：门前说话、门开后的光）。
写法＝009 同一套（一个任务一件慢的事；每人看着谁写进开场图；每句台词对谁说且对象在画面里；运镜写“动作＋终点”；快动作单独占 6 秒任务）。
这次新写的东西：
  · 运镜词汇：起重机下降／上升（A-01、A-03、A-08）、倒退（A-04）、拉远（A-07、B-05、C-02）、横移（A-02、C-01）、推近（其余）；
  · 台词每一句在文字里写明语气（颤、冷、狠、松下来……），人物表情随语气写；
  · 人群（A-01、A-03、A-04）：背景群体不写成虚化，不设有名字的人；
  · C-01…C-03：不指定场景参照图（scene=None），测“多出一个人／场景不对”是不是参照图造成的。
偏离大纲：降临里不拍“瞬间冻住”的过程，只拍雾锋过去的结果（A-05）、白领靠着车坐着不动（A-06、A-07）、冻成冰雕的街（A-08）；
  酒窖里加了一个暴徒“阿瘦”（Lean，手里拿撬棍，有一句台词）；手术前的信任戏、“从你买下我房子那天”是我补的。
H3 方面的风险（交稿时单列、不算我的错）：A-04 人群奔跑（快动作）、A-05 霜的蔓延（状态变化）、A-07 拉远时人会不会多出来、B-02 三人同框、B-03 砸瓶子（快动作）、
  火焰、拉远／起重机下降是第一次用、C-01…C-03 没有场景参照图可能整间屋子换样子、开场图约一成不按文字画。
"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _jihan_base4 import *

BASE_009 = '合并稿/009_第1-16集_合并_重拍低清晰度的1-4集加后12集_制作稿_首批.json'
OUT = '补拍/补拍1_降临_酒窖对峙_手术室信任与伊甸园之门_制作稿_追加'
S = Session(BASE_009, OUT, 60000)


def insert_task(tid, title, dur, scene, framing, act_en, zh, snd, holds, cam, bg=''):
    return S.T(tid, title, dur, scene, [], framing, act_en, zh, snd, cam=cam, holds=holds, room=set(), new=True, bg=bg)


# ---------------------------------------------------------------------------------------------- 补拍 A
bA = S.episode('补拍A｜降临（替换剧本第6集01、02号镜头）', '中午的大街热闹得像平常一样；烧烤摊老板和白领同时抬头看见街尽头的白线；白色雾墙滚过来，人群朝镜头奔跑；雾锋扫过停着的车，车和树都挂上白霜；白领靠着结霜的车坐在路边，颤声叫妈，然后一动不动；整条街冻成了冰蓝色的冰雕街。', 1)

new_person(bA, 'bbq_vendor', '烧烤摊老板（敦实的中年男人，汗湿的白背心，油腻围裙，肩上搭毛巾）', 'man',
           'A stocky Chinese man in his forties with a round sweaty face and small bright eyes, wearing a sweat-stained white tank top and a greasy apron with a towel over one shoulder.',
           '一个四十多岁、敦实的中国男性，圆脸出着汗，眼睛小而亮，穿着被汗浸湿的白色背心和油腻的围裙，肩上搭着一条毛巾。',
           'a round sweaty face, small bright eyes, wearing a sweat-stained white tank top and a greasy apron with a towel over one shoulder', 'a hearty, easy expression', eth='Chinese')
new_person(bA, 'office_guy', '白领（三十多岁，卷袖子的白衬衫，松开的领带，挂着工牌）', 'man',
           'A Chinese office worker in his thirties with neat short black hair and a tired friendly face, wearing a white dress shirt with rolled sleeves, a loosened tie and a lanyard around his neck.',
           '一个三十多岁的中国上班族，黑短发整齐，脸上带着疲惫而和气的神情，穿着卷起袖子的白衬衫，领带松开，脖子上挂着工牌。',
           'neat short black hair, a tired friendly face, wearing a white dress shirt with rolled sleeves, a loosened tie and a lanyard around his neck', 'a relaxed, tired expression', eth='Chinese')
new_person(bA, 'raider_lean', '暴徒阿瘦（精瘦的年轻男人，破迷彩外套，脏围巾遮着口鼻，拿撬棍）', 'man',
           'A wiry Chinese man in his twenties with a gaunt hollow-cheeked face and bloodshot jittery eyes, wearing a torn camouflage jacket with a dirty scarf pulled up over his mouth and nose, holding a steel crowbar.',
           '一个二十多岁、精瘦的中国男性，脸颊凹陷，眼睛布满血丝、神经质地乱转，穿着破旧的迷彩外套，脏围巾拉起来遮住口鼻，手里拿着一根钢撬棍。',
           'a gaunt hollow-cheeked face, bloodshot jittery eyes, wearing a torn camouflage jacket with a dirty scarf pulled up over his mouth and nose', 'a jittery, mean expression', eth='Chinese')
bA.character('Vendor', 'bbq_vendor', VENDOR_EN, VENDOR_ZH)
bA.character('Clerk', 'office_guy', CLERK_EN, CLERK_ZH)
bA.character('Lean', 'raider_lean', LEAN_EN, LEAN_ZH)

STREET_CALM = Scene('street_summer', " Blinding white midday sun glares over the glass towers and the busy lunchtime street.",
                    " Fixed stage layout: a wide boulevard between glass office towers recedes down the middle of the frame, crowded with slow cars and lunchtime crowds on the crosswalks and sidewalks; leafy trees line the sidewalks; a sidewalk barbecue stall sends up a column of smoke at frame-left; at the very far end of the street a thin pale line of haze sits on the horizon.")
STALL = Scene('street_summer', " Blinding white midday sun glares over the glass towers and the lunchtime street.",
              " Fixed stage layout: a sidewalk barbecue stall with a smoking charcoal grill and rows of skewers stands in the foreground at frame-left; the wide boulevard recedes down the middle of the frame between glass office towers with slow cars and lunchtime crowds on the sidewalks; leafy trees line the street; at the far end of the street a low white wall of mist rises on the horizon.")
STREET_RUN = Scene('street_summer', " Blinding white midday sun glares over the glass towers while a towering wall of white mist fills the sky at the far end of the street.",
                   " Fixed stage layout: the wide boulevard between glass office towers recedes down the middle of the frame; a dense tide of office workers, delivery riders and shoppers fills the street and the sidewalks running toward the foreground; stopped cars stand among them; at the far end of the street a towering wall of white mist fills the sky.")
STREET_FRONT = Scene('street_summer', " Blinding white sun glares on the near half of the boulevard while a boiling white front of mist crosses the street behind it.",
                     " Fixed stage layout: the wide boulevard recedes down the middle of the frame; the near half of the street still has green leafy trees and sunlit stopped cars; a boiling white front of mist stands across the middle of the street; everything beyond the front is furred white with frost, dim and grey-blue; nobody is in the street.")
SIDEWALK_FROST = Scene('street_frozen', " Dim grey-blue light and thick white mist drift at street level over the silent boulevard.",
                       " Fixed stage layout: the boulevard recedes down the middle of the frame in thick drifting mist; the parked cars along the curb are furred white with fresh frost; frost-stiffened trees line the sidewalk; a silver sedan stands at the curb at frame-center with a man sitting against its door; the glass towers are furred with frost.")

SOUND_CITY = breathy('The bright din of a busy boulevard at noon: traffic, cicadas, the sizzle of a grill and the indistinct murmur of a crowd.', '中午热闹大街的嘈杂：车流、知了、烤架的滋滋声和人群模糊的低语。')
SOUND_ALARM = breathy('A rising low roar of wind, rattling car windows and a swelling murmur of alarm.', '渐渐变大的低沉风声、汽车玻璃的震动和越来越响的惊慌低语。')
SOUND_RUN = breathy('Pounding footsteps, a rising roar of wind and the breathless gasps of a running crowd.', '密集的奔跑脚步声、越来越大的风吼和人群奔跑时喘不上气的喘息。')
SOUND_HUSH = breathy('A dead hush, a thin wind and the faint tick of ice forming.', '一片死寂，细细的风声和冰层形成时轻轻的嘀嗒声。')
SOUND_PHONE = voiced('A rising low howl of wind, his shaky breath and the faint ticking of frost forming on cloth.', '渐渐变大的低沉风声、他发抖的呼吸声和衣料上结霜时轻轻的嘀嗒声。')

insert_task('A-01', '01｜插镜：正午的大街车水马龙，镜头从高处缓缓降到街面', 6, STREET_CALM,
            'Wide shot from high above the boulevard, the busy street in the middle third of the frame; no named person.',
            "Office workers in short sleeves stream across the crosswalks and along the sidewalks with iced coffees and lunch boxes, cars crawl bumper to bumper under the blazing sun, a sidewalk barbecue stall sends up a lazy column of smoke at frame-left, and far down the street a thin pale line of haze sits on the horizon. Nothing else changes.",
            "穿短袖的上班族端着冰咖啡和饭盒，一股一股地穿过斑马线、走在人行道上，车一辆接一辆地缓缓往前挪，烈日当头，画面左边的烧烤摊升起一缕懒洋洋的烟，街的尽头，地平线上有一条很淡的白线。别的什么都不变。",
            SOUND_CITY, 'The frame holds the busy boulevard with the lunchtime crowds, the crawling cars, the barbecue smoke and the thin pale haze at the far end.',
            descend('the crowded crosswalk and the barbecue stall', '人流拥挤的路口和烧烤摊'),
            bg='The crowds on the crosswalks and sidewalks are sharp and clearly visible.')

S.T('A-02', '02｜街边烧烤摊：老板和白领同时看见街尽头的白色雾墙，一个纳闷，一个发毛', 8, STALL,
    [P('bbq_vendor', 'left', "standing behind the smoking grill in profile facing frame-right, a skewer of meat in his right hand and the towel over his shoulder, his chin lifted and his free arm pointing down the street", 'Office', "his brows knitting, his mouth hanging a little open"),
     P('office_guy', 'center', "standing in front of the stall in profile facing frame-right with a plastic bag of skewers in one hand and an iced coffee in the other, his head turned toward the far end of the street", 'obj:the low white wall of mist at the far end of the street', "his lips parting, his brows drawn together")],
    'Medium two-shot, both from the head to the knees, in the middle third of the frame, at the barbecue stall.',
    "<bbq_vendor> keeps turning a skewer over the coals with a puzzled frown, lifts his chin toward the far end of the street and speaks the first line to <office_guy> in a loud, puzzled voice, his brows knitting and his mouth hanging a little open. <office_guy> lowers his iced coffee, stares at the far end of the street and speaks the second line to <bbq_vendor> in a small, uneasy voice, his lips parting and his brows drawn together, while the people on the sidewalks behind them slow down and stop to look the same way.",
    "烧烤摊老板一边纳闷地皱着眉翻着炭火上的肉串，一边把下巴朝街尽头抬了抬，用洪亮又纳闷的声音对白领说出第一句，眉头拧起、嘴巴微微张着。白领放下手里的冰咖啡，盯着街尽头，用很小、发毛的声音对老板说出第二句，嘴唇微张、眉头拧在一起，他们身后人行道上的人也慢下来，停住脚，朝同一个方向看过去。",
    voiced('The sizzle of the grill, cicadas droning in the heat and the murmur of the lunchtime street.', '烤架的滋滋声、热浪里不停的知了叫和午间街道的嘈杂。'),
    lines=[('bbq_vendor', "哎，你看，那边怎么白了？", 0.8, 'Office'), ('office_guy', "是雾吗？大中午的……", 4.6, 'Bbq')],
    cam=slide('to the right', '右', 'both men stand in the middle third of the frame with the thin white haze of the far horizon visible behind them', '两个人站在画面中间三分之一，身后能看到远处地平线上那一线淡淡的白雾'),
    bg='Behind them the sidewalk crowd and the boulevard are sharp, and a low white wall of mist rises at the far end of the street.',
    holds='The frame holds Bbq and Office at the barbecue stall, the smoking grill and the boulevard behind them.', room={'Bbq', 'Office'}, new=True)

insert_task('A-03', '03｜插镜：街尽头的白色雾墙朝镜头滚过来，路上的人丢下东西，往后退，有人开始跑', 6, STREET,
            'Wide shot from high above the boulevard, the street in the middle third of the frame; no named person.',
            "The towering wall of white mist rolls down the boulevard toward the camera, swallowing the far crosswalk and the first line of parked cars at its foot, while the pedestrians on the sidewalks drop their bags and cups, point at it, back away, and a few turn and start to run.",
            "高耸的白色雾墙沿着大街朝镜头滚过来，吞掉了远处的斑马线和脚下的第一排车，人行道上的行人丢下手里的包和杯子，指着它往后退，有几个人转身开始跑。",
            SOUND_ALARM, 'The frame holds the boulevard with the towering white wall of mist, the stopped cars and the alarmed pedestrians on the sidewalks.',
            rise('the whole boulevard with the towering wall of mist rolling down it', '整条大街和正沿着街滚过来的高耸雾墙'),
            bg='The pedestrians on the sidewalks are sharp and clearly visible.')

insert_task('A-04', '04｜插镜：大街上的人群朝镜头拼命跑，雾墙在他们身后越逼越近', 6, STREET_RUN,
            'Wide low shot at street level, the boulevard in the middle third of the frame; no named person.',
            "A dense crowd of office workers, delivery riders and shoppers sprints down the middle of the boulevard straight toward the camera with bags and phones in their hands and their mouths open, while the towering wall of white mist advances behind them at the far end of the street.",
            "一大群上班族、外卖骑手和购物的人在大街中间朝镜头拼命跑，手里还拿着包和手机，嘴巴张着，高耸的白色雾墙在他们身后的街尽头一点一点逼近。",
            SOUND_RUN, 'The frame holds the boulevard with the running crowd in the foreground and the white wall of mist at the far end, and nobody named.',
            ('The camera retreats slowly backward along the boulevard ahead of the running crowd until the whole street fills the frame.', '镜头在奔跑的人群前面缓缓向后退，直到整条大街占满画面。'),
            bg='The runners are sharp and clearly visible, not blurred.')

insert_task('A-05', '05｜插镜：雾锋从停着的车上慢慢扫过去，被扫过的车和树全挂上了白霜', 6, STREET_FRONT,
            'Wide shot at street level, the boulevard in the middle third of the frame, the front of the mist crossing the street; nobody in the scene.',
            "The boiling white front of the mist moves slowly across the street over the stopped cars, and everything it has passed lies furred white with frost: the windshields are milky, the leaves of the trees are stiff and white, and a layer of ice has climbed the glass of the towers, while the cars and trees in front of it are still green and sunlit. Nothing else moves.",
            "翻滚的白色雾锋慢慢扫过街面上停着的车，被它扫过的东西全挂上了白霜：挡风玻璃一片乳白，行道树的叶子又硬又白，大楼的玻璃上爬满了冰，雾锋前面的车和树还是绿的、还晒着太阳。别的什么都不动。",
            breathy('A long rising howl of wind and the crackle of ice creeping over glass.', '风长长地越来越响的呼啸和冰爬过玻璃时的噼啪声。'),
            'The frame holds the boulevard with the sunlit green half in the foreground, the boiling white front of the mist across the middle of the street and the frosted half beyond it, and nobody in the scene.',
            push1('the edge of the mist', '雾锋的边缘'))

S.T('A-06', '06｜同一条大街：雾刚漫过，白领靠着结霜的车坐在路边，举着手机颤声叫妈', 8, SIDEWALK_FROST,
    [P('office_guy', 'center', "sitting on the curb with his back against the door of a frost-white silver sedan in profile facing frame-right, holding his phone in front of his face in his right hand, his other arm wrapped around his knees, white breath pouring from his mouth and frost forming on his lashes and brows", 'obj:the phone screen in his hand', "his lips trembling, his brows pulled high, his eyes wet")],
    'Medium shot, the figure from the head to the knees, in the middle third of the frame, on the frosted boulevard.',
    "<office_guy> shivers against the car door and stares at the phone screen, then murmurs one short line to himself into the phone in a cracked, trembling voice, talking to nobody, his lips trembling and his brows pulled high, then a second line in a smaller, breaking voice, tears freezing on his lashes. Nobody else is in the frame.",
    "白领缩在车门边发抖，盯着手机屏幕，然后对着手机用破裂发颤的声音低声说了一句很短的话，嘴唇发抖、眉毛高高皱起，接着用更小、更要碎掉的声音又说了一句，眼泪冻在睫毛上。画面里没有别人。",
    SOUND_PHONE, vo=[('office_guy', "喂？妈？", 1.2, 'Office'), ('office_guy', "你听得到吗……", 3.8, 'Office')],
    cam=slide('to the left', '左', 'he sits in the middle third of the frame with the frost-white boulevard behind him', '他坐在画面中间三分之一，身后是白霜覆盖的大街'),
    bg='Behind him the boulevard is lost in thick drifting mist, and the frost-white cars line the curb.',
    holds='The frame holds Office alone sitting against the frost-white sedan, the curb and the misty boulevard.', room={'Office'}, new=True)

S.T('A-07', '07｜插镜：白领的脸已经不动了，镜头拉远，他小小的一个人靠在车门边，整条街一片白', 6, SIDEWALK_FROST,
    [P('office_guy', 'center', "sitting on the curb with his back against the door of the frost-white sedan in profile facing frame-right, his phone slipped into his lap, his head resting back against the door", 'closed', "his face still and calm, a layer of white frost over his lashes, brows and hair", shut='gently closed')],
    'Extreme close-up of his face in the middle third of the frame, on the frosted boulevard.',
    "<office_guy> sits perfectly still against the car door, his eyes gently closed and his face calm under a layer of white frost, his breath no longer clouding. Nobody else is in the frame.",
    "白领一动不动地靠在车门上，眼睛轻轻闭着，脸被一层白霜盖着、平静，嘴里不再冒白气。画面里没有别人。",
    SOUND_HUSH,
    cam=pull('his frost-covered face', '他结满白霜的脸', 'the whole frozen boulevard with the sedan and the small figure sitting at its door', '整条冰封的大街，和靠在车门边的那个小小的身影'),
    bg='The frost-white sedan door is behind his head.',
    holds='The frame holds Office alone, his frost-covered face, and the frost-white car door.', room={'Office'}, new=True)

insert_task('A-08', '08｜插镜：同一条大街彻底冻住了，镜头从高处缓缓降下来，路边的人保持着奔跑的姿势成了冰雕', 7, FROZEN,
            'Wide shot from high above the boulevard, the street in the middle third of the frame; no living person.',
            "The same boulevard lies buried in dim grey-blue light under a thin white mist: the cars are encased in ice, the bare trees are furred with frost, and along both sidewalks and in the middle of the street people stand frozen mid-run in white ice with their arms still swinging. Nothing else moves.",
            "同一条大街，埋在昏暗的灰蓝色光和一层薄薄的白雾里：车被冰裹住，光秃秃的树结满了霜，两边人行道上和街中间的人保持着奔跑、手臂还在摆动的姿势被冻在白色的冰里。别的什么都不动。",
            SOUND_HUSH, 'The frame holds the frozen boulevard with the ice-encased cars, the frost-furred trees and the people frozen mid-run in white ice.',
            descend('the frozen runners in the middle of the street', '街中间保持奔跑姿势的冰雕'))

# ---------------------------------------------------------------------------------------------- 补拍 B
bB = S.episode('补拍B｜酒窖对峙（接在剧本第8集02号之后，替换03号）', '钢门被锤得发抖；门被砸开，两个暴徒堵在台阶上，苏清月举着点着的酒精瓶对着他们；瓶子砸向台阶，火焰腾起，两人被逼出门；台阶上只剩火，苏清月靠着货箱，手在抖。', 2)

SOUND_HAMMER = breathy('Heavy hammer blows booming on steel, rattling bottles and a low wind whistling through the door seam.', '钢门上沉重的锤击闷响、酒瓶的震动和风从门缝里钻进来的低低呼啸。')

insert_task('B-01', '01｜插镜：钢门被锤子一下一下砸得发抖，门上的霜簌簌往下掉', 4, CELLAR,
            'Wide shot from the foot of the steps, the three concrete steps and the heavy steel door in the middle third of the frame; nobody in the scene.',
            "Heavy hammer blows boom against the steel door at the top of the steps; with every blow the door shudders in its frame, flakes of frost and dust shake loose and drift down over the steps, and the wine bottles on the racks tremble. Nothing else moves.",
            "沉重的锤子一下一下砸在台阶顶上的钢门上，每砸一下，门在门框里震一震，霜片和灰尘簌簌地抖落下来、飘在台阶上，酒架上的酒瓶也跟着发颤。别的什么都不动。",
            SOUND_HAMMER, 'The frame holds the three concrete steps, the heavy steel door and the frost-furred wine racks, and nobody in the scene.',
            push1('the shuddering steel door', '发抖的钢门'))

S.T('B-02', '02｜酒窖：门被砸开，两个暴徒堵在台阶上喊话，苏清月举着点着的酒精瓶回话', 11, CELLAR,
    [P('su_down', 'left', "standing in the cellar in profile facing frame-right between the stacked cases, a bottle of burning alcohol held low at her hip in her right hand with a small flame guttering from its neck", 'Brute', "her eyes narrowed, her lips pressed in a thin hard line, her brows low"),
     P('brute_raider', 'center', "standing on the second concrete step in profile facing frame-left, the sledgehammer raised in both hands", 'Su', "his eyes wild, his lips curled under his scarf, his brows lowered"),
     P('raider_lean', 'right', "standing on the top step in the shattered doorway behind him in profile facing frame-left, a steel crowbar held across his chest", 'Brute', "his eyes jittery, a mean grin under his scarf, his brows raised")],
    'Medium-wide shot, all three from the head to the knees, in the middle third of the frame, in the frozen wine cellar.',
    "<brute_raider> raises the hammer and speaks the first line to <su_down> in a savage, hoarse roar, his eyes wild and his lips curled under his scarf. <su_down> lifts the burning bottle slowly to her shoulder and speaks the second line to <brute_raider> in a low voice that shakes at first and hardens as she speaks, her eyes narrowed, her lips pressed in a thin hard line and her brows low. <raider_lean> grins behind the scarf and speaks the third line to <brute_raider> in a shrill, mocking voice, his eyes jittery and his brows raised.",
    "壮实的暴徒举起大锤，用凶狠嘶哑的吼声对苏清月说出第一句，眼睛发狂、嘴唇在围巾下面咧着。苏清月把点着的酒精瓶慢慢举到肩头，用一开始发颤、说着说着变硬的低沉声音对暴徒说出第二句，眼睛眯起、嘴唇抿成一条硬硬的细线、眉头压低。阿瘦在围巾后面咧着嘴笑，用尖利嘲弄的声音对暴徒说出第三句，眼神乱转、眉毛上扬。",
    voiced('The roar of wind through the shattered doorway, the crackle of the small flame and heavy breathing.', '风从被砸开的门口灌进来的呼啸、小火苗的噼啪声和粗重的呼吸声。'),
    lines=[('brute_raider', "出来！吃的，全交出来！", 0.8, 'Su'), ('su_down', "再进一步，我烧死你。", 4.2, 'Brute'), ('raider_lean', "大哥，她手在抖！", 7.6, 'Brute')],
    cam=push('all three of them', '三个人'),
    bg='The heavy steel door hangs shattered open at the top of the steps with black night and blowing snow behind it, and the frost-furred wine racks line the left wall.',
    holds='The frame holds exactly three people, Su, Brute and Raider, the stacked cases, the steps and the shattered door.', room={'Su', 'Brute', 'Raider'}, new=True)

S.T('B-03', '03｜酒窖：苏清月把燃烧瓶砸向台阶，火焰腾起，两个暴徒被逼得连连后退', 6, CELLAR,
    [P('su_down', 'left', "standing in the cellar in profile facing frame-right with her right arm cocked back at her shoulder holding the burning bottle, a flame guttering from its neck", 'Brute', "her eyes narrowed, her lips pressed in a hard line, her brows low"),
     P('brute_raider', 'center', "standing on the second concrete step in profile facing frame-left with the sledgehammer raised in both hands", 'Su', "his eyes wild, his lips curled under his scarf, his brows lowered"),
     P('raider_lean', 'right', "standing on the top step in the shattered doorway behind him in profile facing frame-left, a steel crowbar raised across his chest", 'Su', "his eyes wide, his brows raised, his mouth open under his scarf")],
    'Medium-wide shot, all three from the head to the feet, in the middle third of the frame, in the frozen wine cellar.',
    "<su_down> throws the burning bottle at the steps in one hard sweep of her arm, her eyes on <brute_raider>, and it bursts into a ball of orange flame on the second step. <brute_raider> lets the hammer swing wide and reels back with his arm over his face, and <raider_lean> ducks behind him, and both men stagger backward up the steps and out through the doorway until the doorway is empty, flames licking the steps.",
    "苏清月手臂猛地一挥，把燃烧瓶砸向台阶，眼睛盯着壮实的暴徒，瓶子在第二级台阶上爆成一团橙色的火焰。壮实的暴徒让大锤甩到一边，用手臂挡着脸向后退，阿瘦缩着头躲在他后面，两个人踉踉跄跄地沿着台阶退出门口，直到门口空无一人，火苗舔着台阶。",
    breathy('A roaring whoosh of flame, shattering glass and the howl of wind through the doorway.', '火焰轰然腾起的声音、玻璃碎裂的声音和风从门口灌进来的呼啸。'),
    exit={'Brute', 'Raider'},
    cam=('The camera pulls back slowly from the foot of the steps until the flames, the doorway and Su all fill the frame.', '镜头从台阶脚下缓缓向后拉，直到火焰、门口和苏清月都在画面里。'),
    bg='The heavy steel door hangs shattered open at the top of the steps with black night and blowing snow behind it.',
    holds='The frame holds exactly three people, Su, Brute and Raider, the stacked cases, the steps and the shattered door.', room={'Su', 'Brute', 'Raider'}, new=True)

insert_task('B-04', '04｜插镜：台阶上的火还烧着，空空的门口，雪被风吹进来', 4, CELLAR,
            'Close shot of the three concrete steps and the shattered doorway, the flames on the top steps in the middle third of the frame; nobody in the scene.',
            "Flames lick the top concrete steps and fragments of glass glitter in the fire, the shattered doorway above stands empty and black, and thin streams of snow blow in through it and melt in the heat. Nothing else moves.",
            "火舌舔着最上面的几级台阶，碎玻璃在火里闪光，上面被砸坏的门口空空的、黑洞洞的，细细的雪从门口吹进来，在热气里化掉。别的什么都不动。",
            breathy('The crackle of flames, a thin wind through the doorway and the tick of cooling glass.', '火焰的噼啪声、风从门口吹进来细细的呼啸和玻璃冷却时的嘀嗒声。'),
            'The frame holds the burning steps, the empty shattered doorway and the blowing snow, and nobody in the scene.',
            push1('the flames on the top step', '最上面台阶上的火焰'))

S.T('B-05', '05｜酒窖：苏清月靠着货箱坐在地上，手抖得握不住瓶颈，低声给自己打气', 8, CELLAR,
    [P('su_down', 'center', "sitting on the floor between the stacked cases with her back against a case in profile facing frame-right, the broken neck of the bottle still in her trembling right hand, the firelit steps glowing behind her", 'obj:her own shaking right hand', "her breath shuddering, her lips trembling then pressing together, her brows drawn")],
    'Medium close shot, the figure from the head to the waist, in the middle third of the frame, in the frozen wine cellar.',
    "<su_down> stares at her shaking hand with the broken bottle neck, clenches it shut, and murmurs one short line to herself in a thin shaking voice, talking to nobody, her lips trembling, then a second line in a lower, steadier voice, her lips pressing together and her brows drawn. Nobody else is in the cellar.",
    "苏清月盯着自己握着半截瓶颈、不停发抖的手，把手攥紧，然后用细细发颤的声音自言自语了一句很短的话，不是对任何人说的，嘴唇发抖，接着用更低、更稳的声音又说了一句，嘴唇抿紧、眉头拧着。酒窖里没有别人。",
    voiced('The crackle of the dying flames on the steps, a thin wind through the doorway and her shuddering breath.', '台阶上渐渐变小的火焰的噼啪声、风从门口吹进来细细的呼啸和她发抖的呼吸声。'),
    vo=[('su_down', "手别抖……", 1.6, 'Su'), ('su_down', "我得去找他。", 4.6, 'Su')],
    cam=pull('her shaking hand holding the broken bottle neck', '她颤抖的手和半截瓶颈', 'Su sitting among the stacked cases with the firelit steps behind her', '苏清月坐在货箱之间，身后是映着火光的台阶'),
    bg='Behind her the steps glow orange from the dying flames and the shattered doorway stands empty at the top.',
    holds='The frame holds Su alone sitting between the stacked cases, the firelit steps and the empty doorway.', room={'Su'}, new=True)

# ---------------------------------------------------------------------------------------------- 补拍 C
bC = S.episode('补拍C｜手术室的信任与伊甸园之门（手术前插一条；替换剧本第10集04号、06号）', '手术前，林峰把手术刀刀柄朝她推过去，把手交给她；手术后，苏清月剪断线，林峰夸她手稳，然后拿出协议说签了就是自己人，她问他是不是早就想拉她入伙，他说从你买下我房子那天；然后他带她走到钢门前，推开，粉紫色的光涌出来。', 3)

ROOM_BG = ("The room is a small windowless underground medical room: bare white-tiled walls on every side, no windows, no doors and no other furniture in view; "
           "a steel operating table covered with a sterile blue drape stands between them under a round surgical lamp, an open silver case of instruments stands at frame-left and a plain steel chair stands at frame-right. Hard white light from the round surgical lamp falls on them.")
ROOM_HOLDS = 'The frame holds exactly two people, Su and Lin, and nobody else, with the draped table and the surgical lamp between them.'

S.T('C-01', '01｜手术前（插在剧本第10集01号前）：林峰把手术刀刀柄朝她推过去，说把手交给她，苏清月怀疑，林峰说你带着药穿过了雪原，她接过刀', 12, None,
    [P('su_surgeon', 'left', "standing at the end of the steel table in profile facing frame-right with one white-gloved hand resting on the edge of the blue drape", 'Lin', "her eyes narrowed, her lips pressed in a thin hard line, her brows low"),
     P('lin_white', 'right', "sitting on the plain steel chair in profile facing frame-left, his swollen dark left hand laid palm-down on the blue drape and his right hand sliding a silver scalpel across the drape handle-first toward her", 'Su', "his jaw relaxed, his lips set flat, his brows level, his eyes steady")],
    'Medium two-shot, both from the head to the waist, in the middle third of the frame, in the medical room.',
    "<lin_white> slides the scalpel across the drape handle-first and speaks the first line to <su_surgeon> in a low, calm voice, his jaw relaxed and his eyes steady. <su_surgeon> looks from the scalpel to his face and speaks the second line to <lin_white> in a hard, suspicious voice, her eyes narrowed and her lips pressed in a thin line. <lin_white> speaks the third line to <su_surgeon> in a quiet, sure voice, his brows level. <su_surgeon> exhales, her lips softening, picks up the scalpel and speaks the last line to <lin_white> in a low, tight voice.",
    "林峰把手术刀刀柄朝前沿着蓝布推过去，用低沉平静的声音对苏清月说出第一句，下颌放松、眼睛稳稳的。苏清月看看刀，又看看他的脸，用冷硬怀疑的声音对林峰说出第二句，眼睛眯起、嘴唇抿成一条细线。林峰用安静笃定的声音对苏清月说出第三句，眉毛平直。苏清月呼出一口气，嘴唇松下来，拿起手术刀，用低沉发紧的声音对林峰说出最后一句。",
    SOUND_MED,
    lines=[('lin_white', "刀给你。手，也给你。", 0.8, 'Su'), ('su_surgeon', "你就不怕，我下错刀？", 3.8, 'Lin'), ('lin_white', "你带着药，穿过了雪原。", 6.6, 'Su'), ('su_surgeon', "……别后悔。", 9.4, 'Lin')],
    cam=slide('to the left', '左', 'their two faces and the scalpel on the drape fill the middle third of the frame', '两个人的脸和蓝布上的手术刀占满画面中间三分之一'),
    bg=ROOM_BG, holds=ROOM_HOLDS, room={'Su', 'Lin'}, new=True)

S.T('C-02', '02｜手术后（替换剧本第10集04号的前半）：苏清月剪断线头说好了，林峰取下毛巾，嘶哑地夸她手比他想的稳', 8, None,
    [P('su_surgeon', 'left', "sitting on the stool in profile facing frame-right, small scissors in her right hand just clipping the end of the thread over his neatly stitched left hand wrapped in white gauze, her shoulders dropping", 'Lin', "her lips softening, her brows relaxing"),
     P('lin_white', 'right', "sitting on the plain steel chair in profile facing frame-left, the rolled towel just dropped from his mouth into his right hand, his pale forehead damp with sweat", 'Su', "a faint tired curve at one corner of his mouth, his brows loosening")],
    'Medium two-shot, both from the head to the waist, in the middle third of the frame, in the medical room.',
    "<su_surgeon> clips the end of the thread, sets the scissors down and speaks the first line to <lin_white> in a quiet, tired, relieved voice, her lips softening and her brows relaxing. <lin_white> takes the towel out of his mouth and speaks the second line to <su_surgeon> in a hoarse, low voice with a trace of awed respect, a faint tired curve at one corner of his mouth and his brows loosening.",
    "苏清月剪断线头，放下剪刀，用安静疲惫又松了一口气的声音对林峰说出第一句，嘴唇放松、眉毛舒展。林峰把毛巾从嘴里拿出来，用沙哑低沉、带一点佩服的声音对苏清月说出第二句，嘴角挂着一丝疲倦的弧度、眉头舒展。",
    SOUND_MED,
    lines=[('su_surgeon', "好了。", 0.8, 'Lin'), ('lin_white', "你的手，比我想的稳。", 2.8, 'Su')],
    cam=pull('his neatly stitched left hand wrapped in white gauze on the drape', '他缝合好、缠着白纱布的左手', 'Su and Lin sitting across the table from each other', '隔着桌子对坐的苏清月和林峰'),
    bg=ROOM_BG, holds=ROOM_HOLDS, room={'Su', 'Lin'}, new=True)

S.T('C-03', '03｜手术后（替换剧本第10集04号的后半）：林峰把折好的协议放在她面前，说签了就是自己人，她问是不是早就想拉她入伙，他说从你买下我房子那天', 10, None,
    [P('su_surgeon', 'left', "sitting on the stool in profile facing frame-right, one white-gloved hand resting on the edge of the blue drape and her eyes on his face", 'Lin', "one brow arched, her lips curving wryly"),
     P('lin_white', 'right', "sitting on the plain steel chair in profile facing frame-left, his bandaged left hand resting on the drape and his right hand laying a thin folded paper on the drape in front of her", 'Su', "his jaw relaxed, his lips set flat, his brows level")],
    'Medium two-shot, both from the head to the waist, in the middle third of the frame, in the medical room.',
    "<lin_white> lays the folded paper in front of her and speaks the first line to <su_surgeon> in a low, steady voice, his jaw relaxed and his brows level. <su_surgeon> glances at the paper and speaks the second line to <lin_white> in a dry, half-teasing voice, one brow arched and her lips curving wryly. <lin_white> speaks the third line to <su_surgeon> with a faint warm curve at one corner of his mouth, and <su_surgeon> draws the paper toward her.",
    "林峰把折好的纸放在她面前，用低沉稳当的声音对苏清月说出第一句，下颌放松、眉毛平直。苏清月瞥了一眼那张纸，用干干的、半带逗弄的声音对林峰说出第二句，一边眉毛挑起、嘴角带着一抹玩味的半笑。林峰嘴角带着一丝温暖的弧度对苏清月说出第三句，苏清月把纸拉到自己面前。",
    SOUND_MED,
    lines=[('lin_white', "签了，你就是自己人。", 0.8, 'Su'), ('su_surgeon', "你早就想拉我入伙？", 3.4, 'Lin'), ('lin_white', "从你买下我房子那天。", 5.9, 'Su')],
    cam=push('both of them', '两人'),
    bg=ROOM_BG, holds=ROOM_HOLDS, room={'Su', 'Lin'}, new=True)

S.T('C-04', '04｜钢门前（替换剧本第10集06号的前半）：林峰把手放在门把上，对她说带你去看看我们的伊甸园，她一边好奇一边迟疑', 9, EDENDOOR,
    [P('su_cozy', 'left', "standing in the corridor in profile facing frame-right with her arms folded in the oversized cream sweater", 'Lin', "one brow arched, her lips parted in curiosity"),
     P('lin_home', 'right', "standing beside the steel door in profile facing frame-left, his right hand resting on the door handle and his left hand wrapped in white gauze at his side", 'Su', "his jaw relaxed, a faint pleased curve at one corner of his mouth, his brows lifting")],
    'Medium two-shot, both from the head to the waist, in the middle third of the frame, in the concrete corridor.',
    "<lin_home> speaks the first line to <su_cozy> in a quiet, warm voice, a faint pleased curve at one corner of his mouth. <su_cozy> speaks the second line to <lin_home> in a curious, wary voice, one brow arched and her lips parted. <lin_home> speaks the third line to <su_cozy> in a low, proud voice, his hand tightening on the handle.",
    "林峰用安静温暖的声音对苏清月说出第一句，嘴角带着一丝满意的弧度。苏清月用好奇又有点戒备的声音对林峰说出第二句，一边眉毛挑起、嘴唇微张。林峰用低沉带着骄傲的声音对苏清月说出第三句，握着门把的手收紧。",
    voiced('A low hum from beyond the steel door and soft footsteps on concrete.', '钢门后低低的嗡鸣和混凝土地面上轻轻的脚步声。'),
    lines=[('lin_home', "跟我来。", 0.8, 'Su'), ('su_cozy', "去哪儿？", 3.0, 'Lin'), ('lin_home', "我们的伊甸园。", 4.8, 'Su')],
    cam=push('both of them', '两人'),
    bg='The heavy steel door with the keypad stands at frame-right with a thin line of pink-violet light glowing around its edges.',
    holds='The frame holds exactly two people, Su and Lin, and nobody else, in the concrete corridor beside the steel door with the keypad.', room={'Su', 'Lin'}, new=True)

insert_task('C-05', '05｜插镜（替换剧本第10集06号的后半）：钢门敞开了，粉紫色的光涌出来，铺在走廊的地上', 4, EDENDOOR,
            'Wide shot of the concrete corridor, the open steel door in the middle third of the frame; nobody in the scene.',
            "The heavy steel door stands wide open and a flood of warm pink-violet light pours out of it across the bare concrete floor of the corridor, with a faint green sheen of leaves visible in the glow beyond the doorway. Nothing else moves.",
            "厚重的钢门敞开着，一大片暖暖的粉紫色光从门里涌出来，铺在走廊光秃秃的混凝土地面上，门后的光里隐约有绿叶的光泽。别的什么都不动。",
            breathy('A soft rising hum from beyond the doorway and a hush of awe.', '门后轻轻升起的嗡鸣和敬畏的寂静。'),
            'The frame holds the concrete corridor, the open steel door and the pink-violet light pouring out of it, and nobody in the scene.',
            push1('the open doorway', '敞开的门口'))

doc = S.finish()
