#!/usr/bin/env python3
"""剧本第 25–26 集（致命催化剂／办公桌上的臣服），合并稿编号 006（2026-10-12）。

写法版本：长镜头＋站位表（第一份按 hh 10-12 09:24 “在新剧情里加你的改正”写的稿）。
改正的内容（对应第 23–24 集 hh 指出的问题，规律 3/12/13、自查清单 46/48/49）：
  · 每个任务先写站位表 B(...)：谁在场、谁在画面里、每个人看着谁、谁对谁说话、谁进谁出、每个人开头/结尾的状态；
    tools/_blocking.py 逐镜检查，不过不交稿。
  · 开场图里每个人都写“眼睛看着谁”（写名字）；每句台词在镜头文字里写“对谁说（to [[asset:X]]）”，X 在画面里。
  · 被打断／被反击的动作和反击的人在同一个任务里，反击的人第一帧就在画面里（赛琳娜扎针→基利安一掌）。
  · “一句话引发的动作”在台词处切开：基利安喊“快跑” → 下一镜莉莉已在门口（站位表 trigger/effect）。
  · 旁观的长老不写成虚化：在画面里、清楚；离开时拍他们夺门而出（25-04），之后才只剩两个人。
  · 8–12 秒一个任务（只有两个一次性事件用 6 秒），每任务最多两句台词、都排在前半段；不用 15 秒。
  · 运镜（“动作＋终点”，已验证 12/13）：25-05 横向跟拍莉莉走过去、26-02 说台词时推近到两张脸；其余固定（自查清单 37：不能全片固定）。

故事填实（剧本第 25–26 集是大纲，补的地方）：
  ① 第 24 集结尾：会议室，长老们沿桌单膝跪着；基利安站着搂着莉莉；赛琳娜跪在他们面前，手里藏着红色针管。
  ② 赛琳娜扎的是基利安不是莉莉（25-01）：观众先看到她跪着瞪基利安，再看她扑起来扎他的手臂，他一掌把她打到墙边，针管摔碎。
  ③ 药是什么、会怎样（25-02）：剧本里一大段独白压成两句——“那是血月，Alpha。”“你会发疯，然后弄碎她！”
  ④ 药效发作（25-03）：红纹爬上脖子、眼睛变金、长出獠牙，他把莉莉往门的方向推开，喊“快跑！”
  ⑤ 其他人怎么离开（25-04）：长老们和赛琳娜夺门而逃，莉莉贴在门边让他们过去，眼睛一直看着基利安。
  ⑥ 她为什么留下（25-05）：她背对着门把门关上、反手锁上（咔哒），他听见锁声回头，她一步步走到他面前。第 25 集停在两人对视上。
  ⑦ 第 26 集：他扑过来把她压在桌上（26-01）→ 低吼“你为什么不跑／我会弄碎你”（26-02）→ 她捧住他的脸吻他，红纹褪去、
     眼睛变回灰色、爪子收回，他把脸埋进她颈窝（26-03，一个镜头里完成状态变化）→ 他抬头“只有你能救我”，把她的手腕按在头顶，
     狂风吹开窗户，窗帘扫过画面（26-04）。
偏离剧本：不拍“用头撞墙”（改成额头抵着墙、拳头砸裂墙板）；她身上没有外套（第 24 集已经落在地上），不拍“脱外套”；
  不拍“指甲划破睡裙肩带”“解皮带扣”（改成爪子抠进桌面），亲密戏不露骨；赛琳娜的独白压成两句。
左右方向（全场固定）：主位椅和墙在画面左边，双开门在画面右边；从左到右：赛琳娜（被打到左边墙）—基利安—莉莉—门。
"""
import copy, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _h3draft import Batch, FOLDER, IMG, breathy, voiced
from _blocking import B, check

BASE = '合并稿/005_第23-24集_会议桌上的独宠到血脉压制_制作稿_追加.json'
OUT = '合并稿/006_第25-26集_致命催化剂到办公桌上的臣服_制作稿_追加'
SRC = json.load(open(os.path.join(FOLDER, BASE), encoding='utf-8'))
b25, b26 = Batch(BASE, SRC['title'], 9200), Batch(BASE, SRC['title'], 9300)

CR = '[[asset:council_room]]'; K = '[[asset:killian]]'; KG = '[[asset:killian_gold]]'
LSV = '[[asset:lily_silver]]'; SEL = '[[asset:selena]]'
LAY_CR = " Fixed stage layout: the long polished dark-wood table runs across the room from frame-left to frame-right; the tall carved high-backed chair at the head of the table is at frame-left; the row of leather chairs lines the far side of the table; the tall dark double doors with brass handles are at frame-right; tall windows with dark drapes are at the back."
END_CR = " Cold grey daylight through the tall windows, the paneled room softly blurred behind."
FIX = ('The camera holds still.', '镜头固定不动。')
NAMES = {'Killian': 'Killian', 'Lily': 'Lily', 'Selena': 'Selena'}
BLOCKS = []          # [(任务编号, 站位表)]，按播放顺序
PROMPTS = {}


def T(b, tid, title, dur, chars, assets, img, vis_zh, act_en, act_zh, sound, blk, dep=False, cam=FIX, lines=None):
    s = b.task(title, dur, chars, assets, ['council_room'], img, END_CR + LAY_CR, vis_zh, '0—%d秒，%s' % (dur, cam[1]), None,
               act_en + ' ' + cam[0], act_zh + ' ' + cam[1], sound, lines=lines)
    s['depends_on_previous'] = dep
    BLOCKS.append((tid, blk)); PROMPTS[tid] = s['image_prompt']
    return s


def episode(b, title, summary):
    out = []
    for t in b.tasks:
        out.append((t['title'].split('｜')[1] + '，' + t['visual_zh']).replace('：', '，'))
        for x in t['dialogue']:
            out.append(f"{x['speaker']}：“{x['text']}”")
    return {'title': title, 'summary': summary, 'script': '\n'.join(out), 'segments': b.tasks, 'dialogue_language': 'en'}


ALL3 = {'Killian', 'Lily', 'Selena', 'Elders'}
# 状态用词固定（站位表比对的是字符串）
K_HUMAN = '黑色三件套，灰眼，没变身'
K_SICK = '黑色三件套，灰眼，被扎了左前臂，喘粗气出汗'
K_BEAST = '黑色三件套，金眼獠牙利爪，脖子上红纹'
K_CALM = '黑色三件套，灰眼，獠牙利爪收回，红纹消失'
L_STAND = '白衬衫光脚，银眼，站着'
L_TABLE = '白衬衫光脚，银眼，仰躺在会议桌上'
S_KNEEL = '酒红长裙，跪在地毯上，手里藏着针管'
S_HURT = '酒红长裙，嘴角流血，瘫坐在主位旁的墙边'
E_KNEEL = '沿桌单膝跪着'

# =================================================================================================== 第 25 集：致命催化剂（5 个任务）
T(b25, '25-01', '01｜赛琳娜扑起来把针管扎进基利安的手臂，被他一掌打到墙边', 6,
  ['Selena', 'Killian', 'LilySilver'], ('council_room', 'selena', 'killian', 'lily_silver'),
  "Side-on medium-wide shot, all three people from the head to the knees, in the middle third of the frame, near the head of the long council table. "
  "Selena at frame-left, kneeling on the dark carpet in profile facing frame-right, with sleek copper-red hair in a high ponytail, in the fitted deep-burgundy dress with the silver wolf-head brooch, a slim glass syringe of dark red liquid hidden in her right hand at her side, her amber eyes glaring up at Killian, her lips pressed white, her jaw clenched, her brows low. "
  "Killian at frame-center, standing in three-quarter view turned toward frame-left, in the tailored black three-piece suit, white shirt and dark tie, one arm around Lily's waist, his cold dark-gray eyes on Selena, his lips pressed, his jaw set, his brows low. "
  "Lily at frame-right, standing barefoot pressed against Killian's side within his arm, turned toward frame-left, in the oversized white men's shirt, her chestnut hair loose, her luminous silver-white eyes on Selena, her lips closed, her brows drawn together. "
  "Behind them, along the far side of the table, a row of grey-haired men in black suits kneel on one knee with their heads bowed, clearly visible and in sharp focus. "
  "The frame holds three people in front, Selena, Killian and Lily, with the kneeling men behind the table.",
  "赛琳娜跪在地毯上（画面左），恶狠狠地瞪着基利安；她猛地扑起来，把针管扎进基利安的左前臂，把红色液体推进去；基利安反手一掌把她打飞到主位旁的墙上，针管摔碎；莉莉吓得往他身上一缩；桌后跪着的长老们吓得抬起头。",
  f"A steady side-on medium-wide shot opens from the adopted first frame in {CR}: {SEL} springs up from her knees and drives the syringe into {K}'s left forearm, jamming the plunger down until the dark red liquid empties into him, her lips pulled back in a snarl and her amber eyes on his face; in the same instant {K}'s left hand swings in a brutal backhand that hurls her backward across the carpet toward frame-left, where she slams against the paneled wall beside the tall carved chair, and the glass syringe flies from her hand and shatters on the floor, his jaw clenched and his brows crashing together. {LSV} flinches against his side, her silver eyes going wide on his arm, her lips parting and her brows pulling up. Behind the table the kneeling grey-haired men flinch and lift their heads, their mouths falling open.",
  "一个稳定的侧面中全景，从已采用的开场图继续，场景是会议室：赛琳娜从跪姿猛地扑起来，把针管扎进基利安的左前臂，一下把活塞推到底，暗红色的液体全推进去，她龇着牙，琥珀色的眼睛盯着他的脸；同一瞬间基利安的左手狠狠反手一掌，把她打得向画面左边飞出去，撞在主位旁的木墙板上，玻璃针管从她手里飞出去摔碎在地上，他下颌绷紧，眉头狠狠压下。莉莉吓得往他身上一缩，银色的眼睛瞪大看着他的手臂，嘴唇张开，眉头上扬。桌子后面跪着的长老们一哆嗦，抬起头，张着嘴。",
  breathy("A sharp hiss of breath, the crack of a heavy blow, a body thudding into wood paneling and glass shattering on the floor.",
          "一声急促的吸气、一记重击的闷响、人撞上木墙板的声音和玻璃在地上摔碎的声音。"),
  B(room=ALL3, frame={'Selena': '左', 'Killian': '中', 'Lily': '右', 'Elders': '后'},
    gaze={'Selena': 'Killian', 'Killian': 'Selena', 'Lily': 'Selena', 'Elders': 'obj:floor'},
    interrupt=[('赛琳娜扎针', 'Killian')],
    st_in={'Selena': S_KNEEL, 'Killian': K_HUMAN, 'Lily': L_STAND, 'Elders': E_KNEEL},
    st_out={'Selena': S_HURT, 'Killian': K_SICK, 'Lily': L_STAND, 'Elders': E_KNEEL}))

T(b25, '25-02', '02｜赛琳娜靠在墙边狂笑：那是血月，你会发疯', 10,
  ['Selena', 'Killian'], ('council_room', 'selena', 'killian'),
  "Side-on medium two-shot, both people from the head to the knees, in the middle third of the frame, at the head of the council table beside the tall carved high-backed chair. "
  "Selena at frame-left, slumped on the carpet with her back against the dark paneled wall beside the tall carved chair, in profile facing frame-right, in the fitted deep-burgundy dress with the silver wolf-head brooch, her copper-red ponytail half loose, a thread of blood at the corner of her mouth, her amber eyes on Killian, her lips curled back in a wild grin, her brows raised. "
  "Killian at frame-right, standing in profile facing frame-left, in the tailored black three-piece suit, white shirt and dark tie, his right hand gripping his left forearm where a bead of blood marks the needle wound, sweat on his temple, his cold dark-gray eyes on Selena, his jaw clenched, his brows low. "
  "Shards of a broken glass syringe and a smear of dark red liquid lie on the carpet between them. "
  "The frame holds exactly two people: Selena and Killian.",
  "赛琳娜瘫坐在主位旁的墙边（画面左），嘴角流血，对着基利安狂笑，说出两句话：那是血月；你会发疯，然后弄碎她。基利安（画面右）捂着被扎的手臂，呼吸越来越粗，盯着她。",
  f"A steady side-on medium two-shot opens from the adopted first frame in {CR}: {SEL} throws her head back against the wall and laughs, then speaks the first line to {K} in a breathless, triumphant voice, her amber eyes on his face and her lips curled back from her teeth; she wipes the blood from her lips with the back of her hand and spits the second line to {K} with a vicious grin, her brows raised. {K}'s breathing turns heavy and ragged, his chest heaving and a vein standing out at his temple, his eyes on her face, his jaw clenched and his brows crashing together.",
  "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是会议室：赛琳娜把头往墙上一靠，大笑起来，然后对着基利安，用喘着气、得意的声音说出第一句，琥珀色的眼睛盯着他的脸，嘴唇咧开露出牙齿；她用手背擦掉嘴上的血，咧着恶毒的笑，对着基利安啐出第二句，眉毛高挑。基利安的呼吸变得沉重而急促，胸口起伏，太阳穴上青筋暴起，眼睛盯着她的脸，下颌绷紧，眉头狠狠压下。",
  voiced("A wild, cracked laugh and ragged, heavy breathing.", "一阵疯狂、破音的笑声和粗重急促的呼吸声。"),
  B(room=ALL3, frame={'Selena': '左', 'Killian': '右'}, gaze={'Selena': 'Killian', 'Killian': 'Selena'},
    says=[('Selena', 'Killian'), ('Selena', 'Killian')],
    st_in={'Selena': S_HURT, 'Killian': K_SICK}, st_out={'Selena': S_HURT, 'Killian': K_SICK}),
  lines=[('Selena', "That was Blood Moon, Alpha.", 1.0), ('Selena', "You'll go mad and break her!", 4.5)])

T(b25, '25-03', '03｜药效发作，他把莉莉往门口推开：快跑！', 9,
  ['Killian', 'LilySilver'], ('council_room', 'killian', 'lily_silver'),
  "Side-on medium two-shot, both people from the head to the waist, in the middle third of the frame, beside the long council table. "
  "Killian at frame-left, bent over with both hands gripping the edge of the table, in profile facing frame-right, in the tailored black three-piece suit, white shirt and dark tie, sweat running down his face, thin dark red vein-like lines creeping up the side of his neck, his bloodshot dark-gray eyes on Lily, his lips pulled back from clenched teeth, his brows crashing together. "
  "Lily at frame-right, standing close in profile facing frame-left, in the oversized white men's shirt, both hands reaching for his shoulders, her luminous silver-white eyes on Killian, her lips parted, her brows pulled together. "
  "Behind them, across the table, the row of grey-haired men in black suits still kneel on one knee, their heads lifted, their eyes on Killian and their faces frozen in fear, clearly visible and in sharp focus. "
  "The frame holds two people in front, Killian and Lily, with the kneeling men behind the table.",
  "基利安（画面左）撑着桌子弯着腰，脖子上的红纹往上爬，眼睛变成金色、长出獠牙；莉莉（画面右）伸手去扶他，他抓住她的胳膊把她往门的方向（画面右）狠狠推开，她踉跄几步站住；他对着她吼“快跑，出去！”。桌后跪着的长老们吓得往后缩。",
  f"A steady side-on medium two-shot opens from the adopted first frame in {CR}: the dark red lines crawl up {K}'s neck onto his jaw, his eyes flare a burning gold and his canine teeth lengthen into fangs, his jaw clenched; as {LSV}'s hands touch his shoulders he grabs her by the upper arms and shoves her back hard toward the double doors at frame-right, and she stumbles three steps backward and catches herself, her silver eyes on his face, her lips trembling and her brows pulling up; then he shouts the line to {LSV} in a hoarse, cracking roar, his gold eyes on her face and his lips pulled back from his fangs. Behind the table the kneeling grey-haired men shrink back, their eyes wide.",
  "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是会议室：暗红色的纹路顺着基利安的脖子爬上下颌，他的眼睛燃起金色，犬齿伸长成獠牙，下颌绷紧；莉莉的手刚碰到他的肩膀，他就抓住她的上臂，狠狠把她往画面右边的双开门方向推开，她往后踉跄三步才站稳，银色的眼睛看着他的脸，嘴唇发抖，眉头上扬；然后他对着莉莉用嘶哑、破音的声音吼出那句话，金色的眼睛盯着她的脸，嘴唇咧开露出獠牙。桌子后面跪着的长老们往后缩，眼睛瞪大。",
  voiced("Ragged animal breathing, a low growl rising in his chest, bare feet stumbling on the carpet.", "粗重的野兽般的呼吸声、胸腔里升起的低吼、光脚在地毯上踉跄的声音。"),
  B(room=ALL3, frame={'Killian': '左', 'Lily': '右', 'Elders': '后'},
    gaze={'Killian': 'Lily', 'Lily': 'Killian', 'Elders': 'Killian'},
    says=[('Killian', 'Lily')], trigger='快跑',
    st_in={'Killian': K_SICK, 'Lily': L_STAND, 'Elders': E_KNEEL},
    st_out={'Killian': K_BEAST, 'Lily': L_STAND, 'Elders': E_KNEEL}),
  lines=[('Killian', "Run! Get out of here, Lily!", 3.5)])

T(b25, '25-04', '04｜长老们和赛琳娜夺门而逃，莉莉贴在门边不走', 6,
  ['KillianGold', 'LilySilver', 'Selena'], ('council_room', 'killian_gold', 'lily_silver', 'selena'),
  "Wide side-on shot of the whole council room, in the middle third of the frame, the long polished table running across the room. "
  "Killian at frame-left, at the head of the table beside the tall carved chair, hunched with his back half-turned to the room and one clawed fist pressed against the dark paneled wall, in the tailored black three-piece suit, his gold eyes on his fist against the wall, his lips pulled back from his fangs, his jaw clenched. "
  "Selena at frame-left a few steps from him, pushing herself up off the carpet beside the wall, in the fitted deep-burgundy dress, one hand clutching her side, her amber eyes on the double doors, her lips pressed white, her brows pulled together. "
  "Lily at frame-right, standing barefoot just inside the tall open double doors with her back pressed against one open door, facing into the room in profile facing frame-left, in the oversized white men's shirt, her luminous silver-white eyes on Killian, her lips parted, her brows drawn together. "
  "Along the far side of the table, the grey-haired men in black suits are scrambling up from their knees, clearly visible and in sharp focus, their eyes on the double doors, their mouths open in terror. "
  "The frame holds Killian, Selena, Lily and the scrambling men.",
  "全景：基利安（画面左）背对着屋子、一拳抵在墙上；赛琳娜捂着腰从墙边爬起来；长老们从地上爬起来，顺着长桌冲向画面右边的双开门逃出去，赛琳娜一瘸一拐跟着逃出去；莉莉背贴在敞开的门上让他们过去，眼睛一直看着基利安；基利安一拳砸裂了墙板。最后屋里只剩他们两个。",
  f"A steady wide shot opens from the adopted first frame in {CR}: the grey-haired men scramble to their feet, rush the length of the table and pour out through the open double doors at frame-right, shoving past {LSV}. {SEL} staggers after them clutching her side, her amber eyes on the doors, her lips pressed white and her brows pulled together, and limps out through the doorway. {LSV} stays pressed against the open door, letting them stream past her, her silver eyes never leaving {KG}, her lips parted and her brows drawn together; at frame-left {KG} slams his clawed fist into the paneled wall and the dark wood splits, his jaw clenched and his lips pulled back from his fangs. By the end only {KG} and {LSV} remain in the room.",
  "一个稳定的全景，从已采用的开场图继续，场景是会议室：长老们从地上爬起来，顺着长桌冲过去，从画面右边敞开的双开门挤出去，从莉莉身边擦过；赛琳娜捂着腰踉跄地跟在后面，眼睛盯着门，嘴唇发白，一瘸一拐地出了门；莉莉一直背贴着敞开的门，让他们从身边冲过去，银色的眼睛始终看着基利安，嘴唇张着，眉头紧皱；画面左边，基利安一拳砸在木墙板上，深色的木头裂开，他下颌绷紧，嘴唇咧开露出獠牙。最后屋里只剩基利安和莉莉。",
  breathy("Chairs scraping, a stampede of footsteps on the carpet, a woman's ragged gasping and a heavy blow splitting wood.",
          "椅子刮地的声音、一大片脚步声踩过地毯、一个女人急促的喘息声和一记重拳砸裂木头的声音。"),
  B(room=ALL3, frame={'Killian': '左', 'Selena': '左', 'Lily': '右', 'Elders': '中后'},
    gaze={'Killian': 'obj:fist', 'Selena': 'obj:doors', 'Lily': 'Killian', 'Elders': 'obj:doors'},
    exit={'Selena', 'Elders'}, effect='快跑',
    st_in={'Killian': K_BEAST, 'Selena': S_HURT, 'Lily': L_STAND, 'Elders': E_KNEEL},
    st_out={'Killian': K_BEAST, 'Lily': L_STAND}))

T(b25, '25-05', '05｜莉莉关上门、反手锁上，一步步走到他面前', 10,
  ['KillianGold', 'LilySilver'], ('council_room', 'killian_gold', 'lily_silver'),
  "Wide side-on shot of the empty council room, in the middle third of the frame, the long polished table between the two people. "
  "Killian at frame-left, at the head of the table beside the tall carved chair, standing with his forehead pressed against the cracked dark paneled wall and one clawed fist against the splintered wood, in the tailored black three-piece suit, thin dark red lines on his neck, his eyes squeezed shut, his lips pulled back from his fangs, his jaw clenched. "
  "Lily at frame-right, standing barefoot with her back against the tall double doors, which stand a little open behind her, facing into the room in profile facing frame-left, in the oversized white men's shirt, both hands behind her on the brass handles, her luminous silver-white eyes on Killian, her lips pressed together, her brows drawn together with resolve. "
  "The frame holds exactly two people: Killian and Lily.",
  "屋里只剩两个人。莉莉（画面右）背靠着门，眼睛看着基利安，反手把两扇门关上，再反手拧上铜锁，“咔哒”一声；基利安（画面左）额头抵着裂开的墙，听见锁声停住，慢慢转过头看她，眼睛是金色的；莉莉离开门口，沿着长桌一步步走过去，停在桌头，离他几步远，抬着下巴看着他。",
  f"A wide shot opens from the adopted first frame in {CR}: {LSV} pulls both doors shut behind her without taking her silver eyes off {KG}, reaches behind her back and turns the brass lock with a loud click, her lips pressed together and her brows drawn together; at the click {KG} goes still, lifts his forehead from the wall and slowly turns his head toward her, his eyes burning gold, his jaw clenched and his lips pulled back from his fangs; {LSV} steps away from the doors and walks slowly along the table toward him, her eyes on his face, until she stops beside the head of the table a few steps from him, her chin lifted and her lips pressed together.",
  "一个全景，从已采用的开场图继续，场景是会议室：莉莉的银色眼睛一直看着基利安，反手把两扇门在身后关上，再把手伸到背后拧上铜锁，“咔哒”一声响，她抿着嘴，眉头紧皱；锁一响，基利安停住不动，额头离开墙，慢慢把头转向她，眼睛燃着金色，下颌绷紧，嘴唇咧开露出獠牙；莉莉离开门口，沿着长桌慢慢朝他走过去，眼睛看着他的脸，一直走到桌头、离他几步远的地方停下，抬着下巴，抿着嘴。",
  breathy("The heavy doors thudding shut, the sharp click of a lock, ragged animal breathing and soft bare footsteps on the carpet.",
          "厚重的门关上的闷响、锁“咔哒”一声、粗重的野兽般的呼吸声和光脚踩在地毯上的轻响。"),
  B(room={'Killian', 'Lily'}, frame={'Killian': '左', 'Lily': '右'}, gaze={'Killian': 'closed', 'Lily': 'Killian'},
    st_in={'Killian': K_BEAST, 'Lily': L_STAND}, st_out={'Killian': K_BEAST, 'Lily': L_STAND}),
  cam=('The camera tracks sideways with Lily as she walks along the table, until she stops a few steps from Killian with both of them in the middle of the frame.',
       '镜头跟着莉莉横向移动，直到她停在离基利安几步远的地方、两人都在画面中间。'))

# =================================================================================================== 第 26 集：办公桌上的臣服（4 个任务）
T(b26, '26-01', '01｜他扑过来，把莉莉压在会议桌上', 8,
  ['KillianGold', 'LilySilver'], ('council_room', 'killian_gold', 'lily_silver'),
  "Side-on medium-wide two-shot, both people from the head to the knees, in the middle third of the frame, beside the head of the long polished council table, which is strewn with papers and leather folders. "
  "Killian at frame-left, standing hunched a few steps from Lily with his back near the cracked paneled wall, in profile facing frame-right, in the tailored black three-piece suit, thin dark red lines on his neck, long black claws at his fingertips, his gold eyes on Lily, his lips pulled back from his fangs, his brows crashing together. "
  "Lily at frame-right, standing barefoot beside the edge of the table in profile facing frame-left, in the oversized white men's shirt, her luminous silver-white eyes on Killian, her lips pressed together, her chin lifted, her brows drawn together. "
  "The frame holds exactly two people: Killian and Lily.",
  "接第 25 集结尾：两人在桌头对视。基利安（画面左）猛扑过来，搂住她的腰，把她仰面按倒在会议桌上，手臂把桌上的文件扫落一地；他双手撑在她肩膀两侧，喘着粗气，金色的眼睛盯着她；莉莉仰躺在桌上，双手抵着他的胸口，看着他。",
  f"A steady side-on medium-wide two-shot opens from the adopted first frame in {CR}: {KG} lunges across the gap, seizes {LSV} by the waist and lays her back across the polished table in one motion, his arm sweeping a spill of papers and folders off the table onto the floor; he braces over her with his clawed hands planted on the table on either side of her shoulders, his chest heaving, his gold eyes on her face and his lips pulled back from his fangs. {LSV} lies back on the table with her hands against his chest, her silver eyes on his face, her lips parted and her brows smooth.",
  "一个稳定的侧面中全景双人镜头，从已采用的开场图继续，场景是会议室：基利安扑过来，一把搂住莉莉的腰，一个动作就把她仰面放倒在光亮的长桌上，手臂把桌上的一摊文件和皮夹扫到地上；他俯在她上方，带爪子的双手撑在她肩膀两侧的桌面上，胸口剧烈起伏，金色的眼睛盯着她的脸，嘴唇咧开露出獠牙。莉莉仰躺在桌上，双手抵着他的胸口，银色的眼睛看着他的脸，嘴唇微张，眉头舒展。",
  breathy("A rush of movement, papers and folders slapping onto the floor, a heavy thud on wood and ragged animal breathing.",
          "一阵急促的动作声、文件和皮夹拍落在地上的声音、一声砸在木头上的闷响和粗重的野兽般的呼吸声。"),
  B(room={'Killian', 'Lily'}, frame={'Killian': '左', 'Lily': '右'}, gaze={'Killian': 'Lily', 'Lily': 'Killian'},
    st_in={'Killian': K_BEAST, 'Lily': L_STAND}, st_out={'Killian': K_BEAST, 'Lily': L_TABLE}))

T(b26, '26-02', '02｜他压着她低吼：你为什么不跑', 10,
  ['KillianGold', 'LilySilver'], ('council_room', 'killian_gold', 'lily_silver'),
  "Side-on medium close-up two-shot, both people from the head to the chest, in the middle third of the frame, over the polished council table. "
  "Killian at frame-left, leaning over her and braced on his clawed hands on the table, his face above hers, in the tailored black three-piece suit, thin dark red lines on his neck, his gold eyes on Lily, his lips pulled back from his fangs, his brows crashing together. "
  "Lily at frame-right, lying on her back across the table with her chestnut hair spread over the dark wood, in the oversized white men's shirt, her luminous silver-white eyes on Killian, her lips parted, her brows smooth. "
  "The frame holds exactly two people: Killian and Lily.",
  "近一点的双人镜头：基利安（画面左）俯在她上方，爪子抠进桌面划出白痕，对着她低吼两句：你为什么不跑；我会弄碎你。莉莉（画面右）仰躺着，不挣扎，眼神慢慢变软，看着他。",
  f"A side-on medium close-up opens from the adopted first frame in {CR}: {KG}'s claws dig into the polished wood beside her shoulders, gouging pale scratches, and he speaks the first line to {LSV} in a low animal growl, his gold eyes on her face and his brows crashing together; his breath shudders and he speaks the second line to {LSV} in a cracked, pleading rasp, his lips trembling over his fangs. {LSV} lies still without struggling, her silver eyes softening on his face, her lips parted and her brows smooth.",
  "一个侧面中近景，从已采用的开场图继续，场景是会议室：基利安的爪子抠进她肩膀旁边光亮的木头里，划出几道白痕，他对着莉莉用低沉的野兽般的声音说出第一句，金色的眼睛盯着她的脸，眉头狠狠压下；他的呼吸一颤，又对着莉莉用破碎、近乎哀求的沙哑声音说出第二句，嘴唇在獠牙上发抖。莉莉一动不动地躺着，没有挣扎，银色的眼睛在看着他的时候慢慢变软，嘴唇微张，眉头舒展。",
  voiced("A low animal growl, ragged shuddering breaths and claws scraping wood.", "低沉的野兽般的低吼、颤抖急促的呼吸声和爪子刮木头的声音。"),
  B(room={'Killian', 'Lily'}, frame={'Killian': '左', 'Lily': '右'}, gaze={'Killian': 'Lily', 'Lily': 'Killian'},
    says=[('Killian', 'Lily'), ('Killian', 'Lily')],
    st_in={'Killian': K_BEAST, 'Lily': L_TABLE}, st_out={'Killian': K_BEAST, 'Lily': L_TABLE}),
  dep=True, lines=[('KillianGold', "Why didn't you run?", 1.0), ('KillianGold', "I'll break you, Lily.", 4.5)],
  cam=('The camera pushes in until both of their faces fill the frame.', '镜头推近，直到两人的脸占满画面。'))

T(b26, '26-03', '03｜她捧住他的脸吻他，他一点点安静下来', 10,
  ['KillianGold', 'LilySilver'], ('council_room', 'killian_gold', 'lily_silver'),
  "Side-on close-up two-shot, both people from the head to the shoulders, in the middle third of the frame, over the polished council table. "
  "Killian at frame-left, leaning low over her, in the tailored black three-piece suit, thin dark red lines on his neck, his gold eyes on Lily, his lips pulled back from his fangs, his jaw clenched, his brows crashing together. "
  "Lily at frame-right, lying on her back across the table, in the oversized white men's shirt, both hands rising toward his face, her luminous silver-white eyes on Killian, her lips parted, her brows smooth. "
  "The frame holds exactly two people: Killian and Lily.",
  "特写：莉莉（画面右）捧住他的脸，抬头吻他；一层淡淡的银光从她手上漫到他脸上和脖子上，他脖子上的红纹褪去，眼睛从金色变回灰色，獠牙和爪子收回，绷紧的肩膀松下来；他结束这个吻，把脸埋进她的颈窝，闭上眼，喉咙里发出一声委屈的呜咽，她抚着他的头发。",
  f"A steady side-on close-up opens from the adopted first frame in {CR}: {LSV} cups {KG}'s face in both hands, lifts her head and kisses him, her eyes closing. A faint silver shimmer spreads from her hands over his face and neck: {KG}'s dark red lines fade away, the gold drains from his eyes back to dark gray, his fangs and claws slide back and his rigid shoulders loosen, his brows softening; {KG} breaks the kiss and lowers his face into the curve of her neck, his eyes closing and his lips trembling, a low broken whimper in his throat; {LSV} strokes his hair, her eyes closed and her lips soft.",
  "一个稳定的侧面特写，从已采用的开场图继续，场景是会议室：莉莉双手捧住基利安的脸，抬起头吻他，眼睛闭上；一层淡淡的银光从她手上漫到他的脸和脖子上，他脖子上的暗红纹路慢慢褪去，眼里的金色退回深灰色，獠牙和爪子缩回去，绷紧的肩膀松了下来，眉头也舒展开；他结束这个吻，把脸埋进她的颈窝，闭上眼睛，嘴唇发抖，喉咙里发出一声低低的、破碎的呜咽，莉莉抚着他的头发，闭着眼，嘴唇柔软。",
  breathy("Ragged breathing slowing and softening, a faint airy shimmer of sound and a low broken whimper.", "急促的呼吸慢慢平缓变轻、一点轻轻的空灵声响和一声低低的、破碎的呜咽。"),
  B(room={'Killian', 'Lily'}, frame={'Killian': '左', 'Lily': '右'}, gaze={'Killian': 'Lily', 'Lily': 'Killian'},
    st_in={'Killian': K_BEAST, 'Lily': L_TABLE}, st_out={'Killian': K_CALM, 'Lily': L_TABLE}),
  dep=True)

T(b26, '26-04', '04｜他抬起头：只有你能救我；狂风吹开窗户，窗帘扫过画面', 10,
  ['Killian', 'LilySilver'], ('council_room', 'killian', 'lily_silver'),
  "Side-on close-up two-shot, both people from the head to the shoulders, in the middle third of the frame, over the polished council table, the tall windows with dark drapes behind them. "
  "Killian at frame-left, lifting his face from the curve of her neck and leaning over her, in the tailored black three-piece suit, his wet, pleading dark-gray eyes on Lily, his lips parted, his brows drawn together. "
  "Lily at frame-right, lying on her back across the table with her chestnut hair spread over the dark wood, in the oversized white men's shirt, her luminous silver-white eyes on Killian, her lips parted, her brows softly raised. "
  "The frame holds exactly two people: Killian and Lily.",
  "基利安（画面左）从她颈窝里抬起头，眼睛已经是灰色，湿漉漉地哀求着，对着她低声说“只有你能救我，莉莉”；然后他握住她的两只手腕按在她头顶的桌面上；她呼吸一滞，看着他。一阵狂风吹开身后的窗户，深色的窗帘卷进屋里，扫过画面，直到整个画面被深色的布盖住。",
  f"A steady side-on close-up opens from the adopted first frame in {CR}: {K} speaks the line to {LSV} in a hoarse, desperate whisper, his dark-gray eyes on her face and his brows drawn together; then he takes both her wrists and presses them above her head onto the table, his lips parted; {LSV}'s breath catches, her silver eyes on his face and her lips parting. A sudden gust bursts the tall windows open behind them and the dark drapes whip into the room and sweep across the view until dark fabric fills the frame.",
  "一个稳定的侧面特写，从已采用的开场图继续，场景是会议室：基利安对着莉莉用沙哑、绝望的低声说出那句话，深灰色的眼睛看着她的脸，眉头紧皱；然后他握住她的两只手腕，按在她头顶的桌面上，嘴唇微张；莉莉的呼吸一滞，银色的眼睛看着他的脸，嘴唇张开。一阵狂风猛地吹开他们身后的高窗，深色的窗帘卷进屋里，扫过画面，直到深色的布占满整个画面。",
  voiced("A hoarse whisper, a sudden howl of wind, windows banging open and heavy drapes snapping.", "一声沙哑的低语、突然呼啸的风声、窗户被吹开撞响和厚重窗帘猎猎作响。"),
  B(room={'Killian', 'Lily'}, frame={'Killian': '左', 'Lily': '右'}, gaze={'Killian': 'Lily', 'Lily': 'Killian'},
    says=[('Killian', 'Lily')],
    st_in={'Killian': K_CALM, 'Lily': L_TABLE}, st_out={'Killian': K_CALM, 'Lily': L_TABLE}),
  lines=[('Killian', "Only you can save me, Lily.", 1.5)])

# 种子：第 25 集 9201–9205，第 26 集 9301–9304（Batch 自动编号）
# =================================================================================================== 站位表检查（不过不交稿）
problems = check(BLOCKS, NAMES, PROMPTS)
if problems:
    print('站位表检查没过：'); [print('  ✗', p) for p in problems]; sys.exit(1)
print(f'站位表检查通过：{len(BLOCKS)} 个任务')

doc = copy.deepcopy(b25.d)
doc['episodes'] = [
    episode(b25, '剧本第25集｜致命催化剂（站位表写法）',
            '赛琳娜扑起来把一支红色针管扎进基利安的手臂，被他一掌打到墙边；她狂笑着说那是“血月”，他会发疯、弄碎莉莉；药效发作，他把莉莉推开喊“快跑”；长老们和赛琳娜夺门而逃；莉莉却关上门、反手锁上，一步步走到他面前。'),
    episode(b26, '剧本第26集｜办公桌上的臣服（站位表写法）',
            '他扑过来把莉莉压在会议桌上，低吼“你为什么不跑，我会弄碎你”；她捧住他的脸吻他，红纹褪去、眼睛变回灰色，他把脸埋进她颈窝；他抬起头说“只有你能救我”，狂风吹开窗户，窗帘扫过画面。'),
]

seen = set()
folder = os.path.join(FOLDER, '合并稿')
for sub in ('', '旧合并稿'):
    dd_dir = os.path.join(folder, sub)
    if not os.path.isdir(dd_dir): continue
    for fn in os.listdir(dd_dir):
        if fn.endswith('.json') and not fn.startswith('006_'):
            try:
                dd = json.load(open(os.path.join(dd_dir, fn), encoding='utf-8'))
                for e in dd['episodes']:
                    for s in e['segments']:
                        seen.add(s['seed'])
            except Exception:
                pass
mine = [s['seed'] for e in doc['episodes'] for s in e['segments']]
clash = sorted(x for x in set(mine) if x in seen)
assert len(set(mine)) == len(mine), '本稿内种子重复'
print('与库里已有种子重复：', clash if clash else '无')

txt = json.dumps(doc, ensure_ascii=False, indent=1)
open(os.path.join(FOLDER, OUT + '.json'), 'w', encoding='utf-8').write(txt)
open(os.path.join(FOLDER, OUT + '_全选复制粘贴.txt'), 'w', encoding='utf-8').write(txt)
n = sum(len(e['segments']) for e in doc['episodes']); sec = sum(s['duration_seconds'] for e in doc['episodes'] for s in e['segments'])
print(f'{len(doc["episodes"])} 集、{n} 个任务、约 {sec} 秒；文件 {len(txt.encode())/1024:.0f} KB → {OUT}')
for e in doc['episodes']:
    print('  ', e['title'], len(e['segments']), '个任务', sum(s['duration_seconds'] for s in e['segments']), '秒')
