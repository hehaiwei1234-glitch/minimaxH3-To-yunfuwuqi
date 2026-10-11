#!/usr/bin/env python3
"""剧本第 23–24 集（会议桌上的独宠／血脉压制）重写版（2026-10-11，合并稿编号 005）。

hh 10-11 16:05 的三条要求直接落进这批正片：
  ① 长镜头：两人对话、多句台词做成 10–15 秒一个任务（插件上限 15 秒，一个任务可放多句、多个说话人）。
     本批 3 个长镜头：23-04（15 秒：他脱外套裹住她、抱起、三句来回对话）、23-07（10 秒：赛琳娜一个人两句台词，边说边推近）、
     24-02（12 秒：赛琳娜和莉莉各说一句，然后赛琳娜被压跪下）。其余动作镜头仍用 3–6 秒短任务（一次性爆发动作约 1 秒做完，拉长只会定住）。
  ② 种子：第 23 集 9 个任务全用同一个视频种子 9001；第 24 集每个任务各用一个种子（9101–9105，老写法）；
     另加 3 个“对照组”任务：原样复制第 15–18 集里 3 个已跑过的任务（文字、素材、开场图提示词一字不改，承接前段关掉），
     只把种子换成 9001，对着原视频看“固定种子”到底改变了什么。
  ③ 运镜继续用“动作＋终点”写法：23-05 横向跟拍、23-07 推近、24-01 推近到眼睛、24-05 推近到针管，其余固定。

故事填实（技巧文档第十二节）：
  ① 长老为什么出手 → 22 集结尾他刚逼基利安杀她，她推门进来；离门口最近的长老站起来要打她（01）
  ② “瞬移”怎么拍 → 01 的手举到最高，硬切到 02：基利安已经站在她身前、抓着那只手腕（切镜就是瞬移），再一脚把人踹飞
  ③ “怎么没穿鞋”回答 22 集：莉莉光脚跑来，她说“你不见了，所以我跑”（04）
  ④ 赛琳娜是谁、要什么 → 先看她捏碎钢笔（06），再听她喊“那个位置是许给我的”（07），观众就知道她想当狼后
  ⑤ 威压怎么拍 → 先拍玻璃、水壶（没有人，08），再拍莉莉捂胸口（09）
  ⑥ 莉莉为什么会说“跪下” → 她按住基利安的手，眼睛开始泛银光（09），下一集第一个镜头就是银眼睛（24-01）
  ⑦ “跪下”的因果：赛琳娜先喊“跪下，人类”，莉莉用同一个词回她（24-02），一镜到底，她当场被压跪
  ⑧ 注射器的伏笔 → 24 集最后一个镜头，跪着的赛琳娜手伸到裙摆下，抽出一支红色液体的针管
偏离剧本：不拍“撞碎书柜”（会议室里没有书柜，改成撞翻桌尾的椅子）；不拍“膝盖骨断裂”的特写（只有一声脆响）；
  不拍“全场长老各自单膝跪地”的每个人的特写，只拍一个宽景；亲密戏本批没有。
接缝（承接 004 第 22 集末）：莉莉僵在会议室双开门口（画面右边），基利安的主位椅（画面左边）空了。
"""
import copy, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _h3draft import Batch, FOLDER, breathy, voiced

BASE = '合并稿/004_第19-22集_狼王审判到离不开的牢笼_制作稿_追加.json'
OUT = '合并稿/005_第23-24集_会议桌上的独宠到血脉压制_制作稿_追加'
SRC = json.load(open(os.path.join(FOLDER, BASE), encoding='utf-8'))
OLD = json.load(open(os.path.join(FOLDER, '合并稿/002_第15-18集_重写故事_制作稿_追加.json'), encoding='utf-8'))

UNIFIED = 9001
b23, b24 = Batch(BASE, SRC['title'], 9100), Batch(BASE, SRC['title'], 9100)

CR = '[[asset:council_room]]'; K = '[[asset:killian]]'; KG = '[[asset:killian_gold]]'
LS = '[[asset:lily_shirt]]'; LSV = '[[asset:lily_silver]]'; EL = '[[asset:elder]]'; SEL = '[[asset:selena]]'

# ------------------------------------------------------------------------------------------------ 新素材：赛琳娜（只加到 b23，最后用 b23 的 assets）
b23.person('selena', '赛琳娜（长老之女，纯血母狼）',
           "Selena, an elegant, striking adult woman in her late twenties with sleek copper-red hair pulled into a high ponytail, sharp amber eyes with a faint wolfish glint, high cheekbones and full lips painted deep burgundy, wearing a fitted deep-burgundy tailored dress with a high neckline and long sleeves and a small silver wolf-head brooch at the collar, slim silver rings on her fingers. The portrait fixes her identity and clothes, not staging.",
           "赛琳娜，二十八岁左右、优雅而夺目的成年女人，光滑的铜红色头发扎成高马尾，琥珀色的锐利眼睛带一点狼一样的光，颧骨很高，嘴唇涂成深酒红色；穿一件合身的深酒红色高领长袖剪裁连衣裙，领口别一枚小小的银色狼头胸针，手指上戴着细细的银戒指。肖像固定她的长相和衣着，不固定姿势。",
           "A photorealistic half-body portrait of an elegant, striking adult woman in her late twenties with sleek copper-red hair pulled into a high ponytail, sharp amber eyes, high cheekbones and full lips painted deep burgundy, wearing a fitted deep-burgundy tailored dress with a high neckline and long sleeves, a small silver wolf-head brooch at the collar, slim silver rings on her fingers. "
           "She faces the camera with a haughty, composed expression. Soft even studio light, plain neutral gray background, natural skin texture with visible pores.")
b23.character('Selena', 'selena',
              "A confident adult female voice, sharp, clear and haughty with a cold, venomous edge, speaking clear American English. Every word is fully voiced and audible; her voice rises into a furious shriek when she is angry.",
              "成年女声，自信、尖锐、清楚而傲慢，带一种冷冷的怨毒，说清楚的美式英语。每个字都正常发声、清晰可辨；生气时声音会拔高成愤怒的尖叫。")

# ------------------------------------------------------------------------------------------------ 场景布局句（和 004 第 22 集一致）
LAY_CR = " Fixed stage layout: the long polished dark-wood table runs across the room from frame-left to frame-right; the tall carved high-backed chair at the head of the table is at frame-left; the row of leather chairs lines the far side of the table; the tall dark double doors with brass handles are at frame-right; tall windows with dark drapes are at the back."
END_CR = " Cold grey daylight through the tall windows, the paneled room softly blurred behind."
FIX = ('The camera holds still.', '镜头固定不动。')


def T(b, title, dur, chars, assets, refs, img, end, vis_zh, dlg, act_en, act_zh, sound, dep=False, cam=FIX, lines=None, seed=None):
    """act_en／act_zh 不含镜头句；cam=(英文镜头句, 中文镜头句)；lines=[(说话人,台词,开口秒),...] 一个任务多句。"""
    s = b.task(title, dur, chars, assets, refs, img, end, vis_zh, '0—%d秒，%s' % (dur, cam[1]), dlg,
               act_en + ' ' + cam[0], act_zh + ' ' + cam[1], sound, lines=lines)
    s['depends_on_previous'] = dep
    if seed is not None:
        s['seed'] = seed
    return s


def episode(b, title, summary):
    lines = []
    for t in b.tasks:
        lines.append((t['title'].split('｜')[1] + '，' + t['visual_zh']).replace('：', '，'))
        for x in t['dialogue']:
            lines.append(f"{x['speaker']}：“{x['text']}”")
    return {'title': title, 'summary': summary, 'script': '\n'.join(lines), 'segments': b.tasks, 'dialogue_language': 'en'}


# =================================================================================================== 第 23 集：会议桌上的独宠（9 个任务，全部固定种子 9001）
# 观众要看懂：长老冲向门口的莉莉要打她 → 基利安已在她身前抓住手腕、一脚踹飞 → 全场僵住 →
# 他脱外套裹住她、抱起、问“怎么没穿鞋”（长镜头，三句来回）→ 抱着她走到主位坐下、让她坐在腿上 →
# 赛琳娜捏碎钢笔（嫉妒）→ 站起来骂（长镜头，两句）→ 威压：玻璃震裂 → 莉莉捂胸口、按住他的手、眼睛泛银光。
# 方向：门在画面右边、主位椅在画面左边；长老从桌尾（右）冲向门口，被踹后向左飞；基利安抱着她向左走到主位。

T(b23, '01｜长老冲向门口，举手要打莉莉', 3, ['Elder', 'LilyShirt'], ('council_room', 'elder', 'lily_shirt'), ['council_room'],
  "Side-on medium two-shot, in the middle third of the frame, at the right end of the grim paneled council room. "
  "Elder at frame-center-left, just risen from his leather chair at the end of the long table, in profile facing frame-right, an old man with swept-back white hair and a deeply lined stern face, in the black three-piece suit with a silver wolf-head lapel pin, one hand gripping the table edge and the other hand beginning to lift, his lips pulled back in a snarl, his brows lowered, his cold pale eyes on Lily. "
  "Lily at frame-right, standing barefoot in the tall open doorway in the oversized white men's shirt, in profile facing frame-left, her chestnut hair tousled, one hand gripping the brass door handle, her lips parted, her brows pulled up, her wide frightened eyes on the elder. "
  "Blurred grey-haired men in dark suits sit along the table behind him. The frame holds exactly two people in focus: Elder and Lily.",
  END_CR + LAY_CR, "离门口最近的长老猛地推开椅子站起来，大步冲向站在门口的莉莉，高高举起手要打她；莉莉吓得缩向门框。",
  None,
  f"A steady side-on medium two-shot opens from the adopted first frame in {CR}: {EL} shoves his chair back and strides across the carpet toward {LS} with his lips curled and his brows low, swinging his open hand up high to strike her; {LS} flinches back against the doorframe, her eyes squeezing shut, her lips parting and her brows pulling up.",
  "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是会议室：长老把椅子往后一推，大步穿过地毯冲向莉莉，嘴唇卷起，眉头压低，高高扬起手掌要打；莉莉缩向门框，眼睛紧紧闭上，嘴唇张开，眉头抬起。",
  breathy("A leather chair scraping back, hard footsteps and a sharp intake of breath.", "皮椅向后刮开的声音、沉重的脚步声和一声倒吸气。"),
  seed=UNIFIED)

T(b23, '02｜基利安已经站在她身前，抓住手腕，一脚踹飞', 5, ['KillianGold', 'Elder'], ('council_room', 'killian_gold', 'elder'), ['council_room'],
  "Side-on medium two-shot, in the middle third of the frame, in the council room beside the tall open double doors at frame-right. "
  "Killian at frame-center-right, standing in profile facing frame-left, in the tailored black three-piece suit, white shirt and dark tie, his right hand clamped around the wrist of Elder's raised arm at head height, his eyes blazing dark gold, his jaw clenched, his lips pulled back from sharp canine teeth, his brows crashing together. "
  "Elder at frame-center-left, in profile facing frame-right, in the black three-piece suit with the silver wolf-head lapel pin, his raised wrist caught in Killian's grip, his mouth open, his brows jerking up, his pale eyes wide. "
  "The frame holds exactly two people: Killian and Elder.",
  END_CR + LAY_CR, "基利安像瞬移一样已经站在莉莉身前，一把攥住长老举起的手腕，下一秒一脚把他连人带椅子踹飞，撞翻桌尾的一排皮椅。",
  None,
  f"A steady side-on medium two-shot opens from the adopted first frame in {CR}: {KG} flings the elder's wrist away and drives his black leather shoe into {EL}'s chest in one brutal motion, his eyes blazing and his jaw clenched; {EL} is blasted backward off his feet and flies across the carpet to crash into the end of the long table, which skids sideways and topples a row of leather chairs, his mouth open in a grunt and his brows jerking up.",
  "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是会议室：基利安甩开长老的手腕，一个狠狠的动作把黑色皮鞋踹进长老胸口，眼睛喷着金光，下颌咬紧；长老被踹得双脚离地，向后飞过地毯，撞上长桌桌尾，桌子向旁边滑开，一排皮椅被撞翻，他张着嘴发出一声闷哼，眉头猛地抬起。",
  breathy("A sickening crack of a kick, the heavy crash of toppling chairs and a grunt.", "一脚踹中的闷响、皮椅倒下的巨大撞击声和一声闷哼。"),
  seed=UNIFIED)

T(b23, '03｜长老瘫在翻倒的椅子里，全场僵住', 3, ['Elder'], ('council_room', 'elder'), ['council_room'],
  "Medium shot of the elder from the side, in the middle third of the frame, sprawled on his back on the dark carpet among the toppled leather chairs at the end of the long table, in the black three-piece suit with the silver wolf-head lapel pin, one arm flung out, a thread of blood at the corner of his mouth, his lips parted, his brows pulled up, his pale eyes wide and dazed on the ceiling; behind him, softly blurred, grey-haired men in dark suits frozen half out of their leather chairs. The frame holds exactly one person in focus, Elder.",
  END_CR + LAY_CR, "长老瘫在翻倒的椅子堆里咳着血，眼神发直；他身后的长老们全都半站着僵住了。",
  None,
  f"A steady medium shot opens from the adopted first frame in {CR}: {EL} coughs, a thread of blood sliding down his chin, his lips trembling and his brows pulling up, his dazed eyes on the ceiling as a chair rolls over beside him and tips onto its side; behind him the grey-haired men sit rigid, none of them breathing.",
  "一个稳定的中景，从已采用的开场图继续，场景是会议室：长老咳嗽着，一缕血顺着下巴滑下来，嘴唇发抖，眉头抬起，发直的眼睛盯着天花板，旁边一把椅子滚过来翻倒；他身后的长老们僵坐着，谁都不敢呼吸。",
  breathy("A wet cough, a chair rolling over and then a dead, held silence.", "一声带痰的咳嗽、椅子滚动翻倒的声音，然后是屏住呼吸的死寂。"),
  seed=UNIFIED)

# ---- 长镜头 1：15 秒，两个人，三句来回，前 4 秒还有“脱外套→裹住→抱起”的过程动作
T(b23, '04｜他脱下外套裹住她，抱起来：怎么没穿鞋？', 15, ['Killian', 'LilyShirt'], ('council_room', 'killian', 'lily_shirt'), ['council_room'],
  "Side-on medium close-up two-shot, both people from the head to the waist, in the middle third of the frame, at the tall open double doors at frame-right of the council room. "
  "Killian at frame-left, standing in profile facing frame-right, in the tailored black three-piece suit, white shirt and dark tie, his cold dark-gray eyes on Lily's face, his jaw slowly unclenching, his lips pressed together, his brows drawn together, both hands rising to the lapels of his jacket. "
  "Lily at frame-right, standing barefoot in the tall open doorway in profile facing frame-left, in the oversized white men's shirt, her chestnut hair tousled, her wet wide eyes on his face, her lips trembling, her brows pulled up. "
  "The frame holds exactly two people: Killian and Lily.",
  END_CR + LAY_CR, "基利安脱下西装外套，把莉莉整个裹住，一手托背一手托腿把她抱起来，用哄人的温柔声音问她为什么没穿鞋；她小声回答；他又问是不是弄疼了她。",
  None,
  f"A steady side-on medium close-up opens from the adopted first frame in {CR}: {K}'s eyes soften from a cold glare as he shrugs the black jacket off his shoulders and wraps it around {LS}, drawing it closed over her chest with both hands and tucking it under her chin; then he bends, slides one arm behind her back and the other under her knees and lifts her off her bare feet into his arms, her hands gripping his waistcoat, and speaks the first line in a low, tender voice, his brows drawn together and his lips gentle. "
  f"{LS} answers in a small, shaking voice, her wet eyes on his face, her lips trembling and her brows pulled up, her fingers tightening on his shirt. "
  f"Then {K} speaks again, his jaw soft and his brows knitted with worry, his thumb brushing a tear from her cheek.",
  "一个稳定的侧面中近景，从已采用的开场图继续，场景是会议室：基利安的眼神从冰冷的瞪视软下来，他把黑色西装外套从肩上脱下，裹在莉莉身上，用双手把外套在她胸前拢紧、塞到她下巴下面；然后他弯腰，一只手臂托住她的背，另一只手臂托住她的膝弯，把她从光着的脚上抱进怀里，她的手抓着他的马甲，他用低沉温柔的声音说出第一句，眉头皱在一起，嘴唇很柔和。莉莉用细小发抖的声音回答，湿润的眼睛看着他的脸，嘴唇发颤，眉头抬起，手指揪紧他的衬衫。然后基利安又说话了，下颌放松，眉头担忧地拧着，拇指拭去她脸颊上的一滴泪。",
  voiced("The soft rustle of a heavy jacket, a shaky breath and the faint creak of a floorboard.", "厚外套轻轻的摩擦声、一声发抖的呼吸和地板细微的吱嘎声。"),
  lines=[('Killian', "Where are your shoes?", 4.0), ('LilyShirt', "You were gone, so I ran.", 7.2), ('Killian', "Did I hurt you?", 11.0)],
  seed=UNIFIED)

T(b23, '05｜他抱着她走到长桌尽头，坐上主位', 6, ['Killian', 'LilyShirt'], ('council_room', 'killian', 'lily_shirt'), ['council_room'],
  "Wide-medium side-on shot, in the middle third of the frame, in the council room along the long polished table. "
  "Killian at frame-center, walking in profile facing frame-left, in the black waistcoat and white shirt with his sleeves rolled, a dark tie, carrying Lily in both arms against his chest, his cold dark-gray eyes straight ahead toward the tall carved high-backed chair at the head of the table at frame-left, his jaw set, his lips pressed, his brows low. "
  "Lily in his arms, wrapped in his black suit jacket, her bare feet dangling, one arm around his neck, her cheek against his chest, her eyes closed, her lips trembling, her brows pulled together. "
  "Along the far side of the table a row of grey-haired men in dark suits, softly blurred, all staring after him. The frame holds exactly two people in focus: Killian and Lily.",
  END_CR + LAY_CR, "基利安抱着裹在他外套里的莉莉，沿着长桌一路走到尽头，转身坐进高背主位，让她侧坐在自己腿上；长桌后面的长老们全都瞪大眼睛看着。",
  None,
  f"A wide-medium shot opens from the adopted first frame in {CR}: {K} carries {LS} the full length of the table without a glance at anyone, his jaw set and his brows low, reaches the tall carved chair at the head, turns and sits down with her across his lap, settling her head under his chin and tucking the black jacket around her bare feet; {LS} curls into his chest, her eyes closed, her lips trembling and her brows pulling together.",
  "一个宽中景，从已采用的开场图继续，场景是会议室：基利安抱着莉莉走过整张长桌，一眼都不看别人，下颌绷紧，眉头压低，走到画面左边的高背主位，转身坐下，让她侧坐在自己腿上，把她的头按在自己下巴下面，用黑色外套裹住她光着的脚；莉莉蜷进他怀里，眼睛闭着，嘴唇发颤，眉头拧起。",
  breathy("Slow, heavy footsteps on the carpet and the creak of a leather chair taking weight.", "地毯上缓慢沉重的脚步声，和皮椅承重时的吱嘎声。"),
  cam=('The camera tracks sideways at walking pace, keeping them in the middle of the frame while the long table and the staring elders slide past behind them.', '镜头横向跟拍他走路的速度，让他们始终在画面中间，身后的长桌和瞪着眼的长老们一路掠过。'),
  seed=UNIFIED)

T(b23, '06｜赛琳娜捏碎了手里的钢笔', 3, ['Selena'], ('council_room', 'selena'), ['council_room'],
  "Wide-medium side-on shot, in the middle third of the frame, in the council room. "
  "Selena in the near foreground at frame-right, seated at the long table in profile facing frame-left, with sleek copper-red hair in a high ponytail, in the fitted deep-burgundy dress with the silver wolf-head brooch, a black fountain pen gripped in her right hand on the table, her amber eyes narrowed, her jaw tight, her lips pressed white, her brows low. "
  "Far across the room at frame-left, small and softly blurred, a man in a black waistcoat sits in the tall carved chair at the head of the table with a woman curled across his lap. "
  "The frame holds exactly one person in focus, Selena.",
  END_CR + LAY_CR, "赛琳娜坐在长桌右侧，死死盯着远处主位上抱在一起的两个人，手里的钢笔被她越攥越紧。",
  None,
  f"A steady wide-medium shot opens from the adopted first frame in {CR}: {SEL}'s slender fingers close around the fountain pen until its barrel cracks and black ink bursts over her hand and the white papers in front of her, dripping down her wrist, her jaw clenching, her lips pressing white and her nostrils flaring, her amber eyes burning at the two small figures far down the table.",
  "一个稳定的宽中景，从已采用的开场图继续，场景是会议室：赛琳娜纤细的手指攥紧钢笔，直到笔管裂开，黑色墨水喷到她的手上和面前的白纸上，顺着手腕往下滴，下颌绷紧，嘴唇抿得发白，鼻翼翕动，琥珀色的眼睛烧着火，盯着长桌那头远处的两个小小的身影。",
  breathy("A sharp crack of plastic and the slow drip of ink onto paper.", "塑料笔管裂开的一声脆响，和墨水一滴一滴落在纸上的声音。"),
  seed=UNIFIED)

# ---- 长镜头 2：10 秒，一个人，两句台词，边说边推近
T(b23, '07｜赛琳娜站起来骂：那个位置是许给我的', 10, ['Selena'], ('council_room', 'selena'), ['council_room'],
  "Medium shot of Selena alone, from the head to the knees, in the middle third of the frame, standing at the long table in profile facing frame-left, with sleek copper-red hair in a high ponytail, in the fitted deep-burgundy dress with the silver wolf-head brooch, her chair pushed back behind her, black ink dripping from her right hand, her left palm flat on the table, her amber eyes burning, her lips drawn back from her teeth, her jaw trembling, her brows low. "
  "The frame holds exactly one person, Selena.",
  END_CR + LAY_CR, "赛琳娜猛地站起来，沾着墨水的手掌拍在桌上，朝长桌那头的主位尖声骂出第一句，手指狠狠一指，又压低声音毒蛇一样吐出第二句。",
  None,
  f"A medium shot opens from the adopted first frame in {CR}: {SEL} rises sharply to her full height, slams her inky palm onto the table and spits the first line in a shrill, furious voice, her amber eyes blazing and her lips pulled back from her teeth; she jabs a finger along the table, her brows low and her jaw trembling, then speaks again in a lower, venomous hiss, her lip curling and her brows crashing together, her nostrils flaring.",
  "一个中景，从已采用的开场图继续，场景是会议室：赛琳娜猛地站直，把沾着墨水的手掌拍在桌上，用尖利愤怒的声音骂出第一句，琥珀色的眼睛喷着火，嘴唇咧开露出牙齿；她的手指沿着长桌狠狠一指，眉头压低，下颌发抖，然后用更低、毒蛇一样的嘶声说出第二句，嘴唇卷起，眉头猛地拧在一起，鼻翼翕动。",
  voiced("A palm slapping on wood, a furious breath and the squeak of a chair dragged back.", "手掌拍在木头上的声音、一声愤怒的喘息和椅子被拖开的吱嘎声。"),
  cam=('The camera pushes in slowly until Selena fills the frame from the head to the chest.', '镜头慢慢推近，直到赛琳娜从头到胸占满画面。'),
  lines=[('Selena', "That seat was promised to me!", 1.2), ('Selena', "She's not worthy of my shoes!", 5.4)],
  seed=UNIFIED)

T(b23, '08｜玻璃在震动：威压来了', 3, [], ('council_room',), ['council_room'],
  "Medium shot of the council room's tall windows with dark drapes at the back, seen straight on, in the middle third of the frame, with the near edge of the long polished table in the foreground holding a crystal water jug and four glasses, cold grey daylight in the panes. No one is in the frame.",
  END_CR, "会议室的高窗和长桌边的水晶水壶、玻璃杯，一切都在轻轻颤抖，一股看不见的威压正在逼近。",
  None,
  f"A steady medium shot opens from the adopted first frame in {CR}: a low tremor runs through the room, the glasses chatter against the table, the water in the jug shivers into rings and the dark drapes snap sideways in a sudden wind, then a web of cracks races across the tall window panes and the crystal jug bursts. No one appears.",
  "一个稳定的中景，从已采用的开场图继续，场景是会议室：一阵低低的震颤传遍整个房间，玻璃杯在桌面上咯咯作响，水壶里的水抖出一圈圈波纹，深色窗帘在突然刮起的风里向旁边甩开，然后一道道裂纹爬满高窗的玻璃，水晶壶炸开。画面里没有人出现。",
  breathy("A rising low hum, glass chattering and a sharp crack of a pane splitting.", "越来越高的低低嗡鸣、玻璃咯咯作响和一块窗玻璃裂开的一声脆响。"),
  seed=UNIFIED)

T(b23, '09｜莉莉捂住胸口，按住了他抬起的手', 6, ['KillianGold', 'LilyShirt'], ('council_room', 'killian_gold', 'lily_shirt'), ['council_room'],
  "Side-on medium close-up two-shot, both people from the head to the waist, in the middle third of the frame, in the tall carved high-backed chair at the head of the council table. "
  "Killian at frame-left, seated in profile facing frame-right, in the black waistcoat and white shirt with his sleeves rolled, his arm around Lily, his right hand resting on the chair arm, his eyes glowing dark gold on Lily's face, his jaw clenched, his lips pulled back from his canine teeth, his brows crashing together. "
  "Lily at frame-right, curled across his lap in profile facing frame-left, wrapped in his black suit jacket, one hand clawing at her chest, her face drained pale, her chestnut hair stirring in the pressure, her lips parted, her brows pulled up in pain. "
  "The frame holds exactly two people: Killian and Lily.",
  END_CR + LAY_CR, "威压逼到莉莉身上，她捂着胸口喘不上气；基利安的指甲伸了出来，抬手要动手；她的小手突然按住了他的手背，眼睛里泛起一点银光。",
  None,
  f"A steady side-on medium close-up opens from the adopted first frame in {CR}: {LS} gasps, her hand clawing at her chest, her face drained pale, her lips parting and her brows pulling up in pain; {KG}'s long black claws slide from his fingertips as his right hand lifts off the chair arm, his jaw clenching and his lips pulling back from his fangs; then {LS}'s small hand closes over the back of his lifted hand and presses it down against the chair arm, her wet eyes on his face, her lips trembling and her brows pulling together, and a faint silver glint wakes in her eyes.",
  "一个稳定的侧面中近景双人镜头，从已采用的开场图继续，场景是会议室：莉莉喘息着，手抓着胸口，脸色惨白，嘴唇张开，眉头痛苦地抬起；基利安长长的黑色利爪从指尖伸出来，右手从椅子扶手上抬起，下颌咬紧，嘴唇咧开露出獠牙；然后莉莉的小手覆在他抬起的手背上，把它按回椅子扶手上，湿润的眼睛看着他的脸，嘴唇发颤，眉头拧在一起，她眼睛里亮起一点银光。",
  breathy("A ragged gasp, a low growl and the soft crackle of rising pressure.", "一声粗重的喘息、一声低低的咆哮和威压升高时细微的噼啪声。"),
  seed=UNIFIED)

# =================================================================================================== 第 24 集：血脉压制（5 个任务，每个任务各用一个种子 9101–9105）
# 观众要看懂：莉莉站起来，眼睛是银色 → 赛琳娜喊“跪下，人类”，莉莉用同一个词回她，赛琳娜当场被压跪（长镜头）→
# 所有长老被拉下椅子单膝跪成一排 → 基利安仰头看着她，起身搂住她，对全场宣布“这是你们的女王” →
# 跪着的赛琳娜眼神怨毒，手伸到裙摆下，抽出一支红色液体的针管（伏笔）。

T(b24, '01｜莉莉站起来，眼睛是银色的', 4, ['LilySilver'], ('council_room', 'lily_silver'), ['council_room'],
  "Medium shot of Lily alone, from the head to the knees, in the middle third of the frame, standing beside the tall carved high-backed chair at the head of the council table in profile facing frame-right, a man's black suit jacket slipping off her shoulders, in the oversized white men's shirt, her bare feet on the dark carpet, her chestnut hair stirring around her face, her luminous silver-white eyes level, her lips closed, her brows smooth, her chin lifted. "
  "The frame holds exactly one person, Lily.",
  END_CR + LAY_CR, "莉莉从基利安怀里慢慢站起来，黑色外套从肩上滑落，眼睛变成明亮的银白色，头发被无形的风吹得飘起来。",
  None,
  f"A medium shot opens from the adopted first frame in {CR}: {LSV} rises to her full height, the black jacket sliding from her shoulders to the carpet, her chestnut hair lifting around her face in an unseen wind, her lips closed and her brows smooth, her luminous silver-white eyes glowing brighter.",
  "一个中景，从已采用的开场图继续，场景是会议室：莉莉站直身子，黑色外套从肩上滑落到地毯上，栗色头发被看不见的风吹得在脸边飘起，嘴唇闭着，眉头平整，明亮的银白色眼睛越来越亮。",
  breathy("A low resonant hum, the soft whisper of a jacket falling and a slow even breath.", "低低的共鸣嗡声、外套落地的轻响和一声缓慢平稳的呼吸。"),
  cam=('The camera pushes in from the medium shot until her silver eyes fill the frame.', '镜头从中景推近，直到她银白色的眼睛占满画面。'))

# ---- 长镜头 3：12 秒，两个人，两句来回（同一个词），然后动作：赛琳娜被压跪
T(b24, '02｜赛琳娜：跪下，人类！莉莉：跪下。', 12, ['Selena', 'LilySilver'], ('council_room', 'selena', 'lily_silver'), ['council_room'],
  "Side-on medium two-shot, both people from the head to the knees, in the middle third of the frame, in the council room on either side of the corner of the long polished table. "
  "Lily at frame-left, standing beside the tall carved high-backed chair in profile facing frame-right, in the oversized white men's shirt, her chestnut hair stirring around her face, her luminous silver-white eyes level, her lips closed, her brows smooth. "
  "Selena at frame-right, standing behind the table in profile facing frame-left, with sleek copper-red hair in a high ponytail, in the fitted deep-burgundy dress with the silver wolf-head brooch, black ink on her right hand, her amber eyes blazing, her lips drawn back from her teeth, her jaw tight, her brows low. "
  "The frame holds exactly two people: Lily and Selena.",
  END_CR + LAY_CR, "赛琳娜指着莉莉喊“跪下，人类”；莉莉银色的眼睛纹丝不动，用同一个词轻轻回她；赛琳娜突然被一座看不见的山压住，膝盖咔的一声重重砸在地上，头抬不起来。",
  None,
  f"A steady side-on medium two-shot opens from the adopted first frame in {CR}: {SEL} jabs a finger at {LSV} and spits the first line, her lips drawn back and her brows low; {LSV} answers with a single quiet word, her silver eyes level, her lips barely moving and her brows smooth, and the tall windows behind them shiver as her voice carries a strange, bell-like resonance; at once {SEL}'s eyes go wide, a sickening crack of bone sounds and she is slammed down onto both knees on the carpet as if an invisible mountain has landed on her shoulders, her mouth open in a silent scream, her brows jerking up, her head forced down and unable to lift, her hands pressed flat on the floor.",
  "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是会议室：赛琳娜用手指指着莉莉，吐出第一句，嘴唇咧开，眉头压低；莉莉用一个轻轻的词回答，银色的眼睛纹丝不动，嘴唇几乎没动，眉头平整，她的声音带着一种奇异的钟声一样的共鸣，身后的高窗跟着颤动；赛琳娜的眼睛一下子睁大，一声让人牙酸的骨头脆响，她像被一座看不见的山压在肩上，双膝重重砸在地毯上，嘴张着发出无声的尖叫，眉头猛地抬起，头被压得抬不起来，双手按在地上。",
  voiced("A resonant, bell-like echo behind a single word, a sharp crack of bone and the heavy thud of knees on carpet.", "一个词后面钟声一样的回响、骨头裂开的一声脆响和膝盖砸在地毯上的重重一声。"),
  lines=[('Selena', "Get on your knees, human!", 1.0), ('LilySilver', "Kneel.", 5.0)])

T(b24, '03｜所有长老被拉下椅子，单膝跪成一排', 5, ['Selena'], ('council_room', 'selena', 'elder'), ['council_room'],
  "Wide shot of the council room from the end of the long polished table, in the middle third of the frame. "
  "In the near foreground at frame-right, Selena already on both knees on the carpet in profile facing frame-left, her head forced down, her copper-red ponytail hanging, her lips pressed white and her brows pulled together. "
  "Behind the long table, Elder and a dozen other grey-haired men in black three-piece suits with silver wolf-head pins sit upright in their leather chairs, their lips pressed, their brows low, their jaws tight. "
  "The frame holds Selena in the foreground and the row of seated men behind the table.",
  END_CR + LAY_CR, "宽景：赛琳娜已经跪在前景里；桌后一排长老坐得笔直，突然一个接一个被无形的力量从椅子上拉下来，单膝跪地，椅子翻倒。",
  None,
  f"A steady wide shot opens from the adopted first frame in {CR}: one after another {EL} and the other grey-haired men are dragged off their leather chairs as if by an invisible hand, their lips parting and their brows jerking up, and drop to one knee on the carpet with a hand pressed to the floor, chairs toppling behind them, until every elder along the table kneels in a row with his head bowed; {SEL} stays on her knees in the foreground, her head forced down, her lips pressed white and her brows pulled together.",
  "一个稳定的宽景，从已采用的开场图继续，场景是会议室：长老们一个接一个像被一只看不见的手从皮椅上拽下来，嘴唇张开，眉头猛地抬起，单膝砸在地毯上，一只手按着地面，椅子在身后翻倒，直到桌边每一位长老都低着头跪成一排；赛琳娜在前景里一直跪着，头被压得低低的。",
  breathy("A rolling wave of cracking joints, chairs toppling and bodies dropping heavily onto carpet.", "一阵接一阵的关节脆响、椅子倒下的声音和身体重重砸在地毯上的声音。"))

T(b24, '04｜他起身搂住她：这就是你们的女王', 8, ['Killian', 'LilySilver'], ('council_room', 'killian', 'lily_silver'), ['council_room'],
  "Side-on medium close-up two-shot, both people from the head to the waist, in the middle third of the frame, in front of the tall carved high-backed chair at the head of the council table. "
  "Killian at frame-left, seated in the chair in profile facing frame-right, in the black waistcoat and white shirt with his sleeves rolled, his cold dark-gray eyes on Lily's face, his lips parted, his brows lifted, a look of fierce reverent pride. "
  "Lily at frame-right, standing in profile facing frame-left beside the chair, in the oversized white men's shirt, her luminous silver-white eyes level, her lips closed, her brows smooth, her chin lifted. "
  "Behind them at frame-left, softly blurred, the row of kneeling grey-haired men. The frame holds exactly two people in focus: Killian and Lily.",
  END_CR + LAY_CR, "基利安坐在椅子上仰头看着她，眼神里全是近乎病态的骄傲；他站起来，一把搂住她的腰，把她拉进怀里，对着跪了一地的人宣布。",
  None,
  f"A steady side-on medium close-up opens from the adopted first frame in {CR}: {K} gazes up at {LSV} with fierce worship, then rises to his full height and hooks one arm around her waist, drawing her into his side, his jaw set and his lips firm, and says the line to the kneeling room in a deep, quiet, carrying voice, his brows low. {LSV} stands calm in his arm, her silver eyes level, her lips closed and her brows smooth.",
  "一个稳定的侧面中近景，从已采用的开场图继续，场景是会议室：基利安仰头看着莉莉，眼神里满是狂热的崇拜，然后站起来，一只手臂搂住她的腰，把她拉到自己身侧，下颌绷紧，嘴唇坚定，用低沉安静却传得很远的声音对着跪着的满屋人说出那句话，眉头压低。莉莉在他臂弯里站得很平静，银色的眼睛平视，嘴唇闭着，眉头平整。",
  voiced("A slow rustle of cloth and the hush of a room holding its breath.", "布料缓慢的摩擦声和满屋人屏住呼吸的寂静。"),
  lines=[('Killian', "Meet your queen.", 4.0)])

T(b24, '05｜跪着的赛琳娜，手摸向裙摆下', 4, ['Selena'], ('council_room', 'selena'), ['council_room'],
  "Medium close-up of Selena alone, from the head to the waist, in the middle third of the frame, kneeling on the dark carpet in profile facing frame-left, her head forced down with her copper-red ponytail fallen over one shoulder, in the fitted deep-burgundy dress with the silver wolf-head brooch, her amber eyes glaring up under her brows with pure venom, her lips pulled back from her teeth, her jaw clenched, her right hand sliding down toward the hem of her dress. "
  "The frame holds exactly one person, Selena.",
  END_CR + LAY_CR, "赛琳娜跪在地上，头被压着，眼神怨毒到了极点，右手悄悄摸向裙摆下面，抽出一支装着暗红色液体的针管。",
  None,
  f"A steady medium close-up opens from the adopted first frame in {CR}: {SEL}'s right hand slips under the hem of her dress, her amber eyes still burning, her lips curling back from her teeth and her brows low; the hand draws out a slim glass syringe full of dark red liquid, and the red glints in the grey light as her fingers close around it.",
  "一个稳定的中近景，从已采用的开场图继续，场景是会议室：赛琳娜的右手悄悄滑进裙摆下面，琥珀色的眼睛依旧烧着火，嘴唇从牙齿上卷起，眉头压低；那只手抽出一支细细的、装满暗红色液体的玻璃针管，红色在灰白的光里一闪，她的手指握紧。",
  breathy("A slow heavy breath, the whisper of fabric and a faint glassy click.", "一声缓慢沉重的呼吸、布料的轻响和玻璃一声轻轻的磕碰。"),
  cam=('The camera pushes in until the red liquid in the syringe fills the frame.', '镜头推近，直到针管里的红色液体占满画面。'))

# 第 24 集每个任务各用自己的种子（老写法）
for i, s in enumerate(b24.tasks):
    s['seed'] = 9101 + i

# =================================================================================================== 对照组：原样复制 3 个已经跑过的任务，只换种子
bc = Batch(BASE, SRC['title'], 9100)
PICK = [('剧本第16集', '02｜'), ('剧本第17集', '01｜'), ('剧本第18集', '04｜')]
orig_tag = {'剧本第16集': '16集02号', '剧本第17集': '17集01号', '剧本第18集': '18集04号'}
for k, (ep_prefix, tprefix) in enumerate(PICK, start=1):
    ep = [e for e in OLD['episodes'] if e['title'].startswith(ep_prefix)][0]
    seg = copy.deepcopy([s for s in ep['segments'] if s['title'].startswith(tprefix)][0])
    assert seg['depends_on_previous'] is False
    old_seed = seg['seed']
    name = seg['title'].split('｜')[1]
    seg['title'] = '%02d｜对照（原%s，原种子%d）%s' % (k, orig_tag[ep_prefix], old_seed, name)
    seg['seed'] = UNIFIED
    bc.tasks.append(seg)

# =================================================================================================== 合成一份
doc = copy.deepcopy(b23.d)
doc['episodes'] = [
    episode(b23, '剧本第23集｜会议桌上的独宠（重写，长镜头测试，全集固定种子9001）',
            '长老冲向门口要打莉莉，基利安像瞬移一样出现，一脚踹飞；他脱外套裹住她、抱起，问她怎么没穿鞋；抱着她坐上主位；赛琳娜捏碎钢笔、站起来骂；威压震裂玻璃；莉莉按住他的手，眼睛泛银光。'),
    episode(b24, '剧本第24集｜血脉压制（重写，长镜头测试，每个任务各用一个种子）',
            '莉莉站起来，眼睛是银色的；赛琳娜喊“跪下，人类”，莉莉用同一个词回她，赛琳娜被压跪；所有长老单膝跪成一排；基利安搂住她：“这是你们的女王”；跪着的赛琳娜抽出一支红色液体的针管。'),
    episode(bc, '对照组｜同一批任务换成固定种子9001（不进成片）',
            '原样复制第16集02号、第17集01号、第18集04号三个已经跑过的任务，只把种子换成9001，用来和原视频对比。'),
]

# 种子：和库里所有稿子不重复（固定种子 9001 本批内重复是故意的；对照组沿用 9001）
seen = set()
folder = os.path.join(FOLDER, '合并稿')
for fn in os.listdir(folder):
    if fn.endswith('.json') and not fn.startswith('005_'):
        try:
            dd = json.load(open(os.path.join(folder, fn), encoding='utf-8'))
            for e in dd['episodes']:
                for s in e['segments']:
                    seen.add(s['seed'])
        except Exception:
            pass
old_dir = os.path.join(folder, '旧合并稿')
if os.path.isdir(old_dir):
    for fn in os.listdir(old_dir):
        if fn.endswith('.json'):
            try:
                dd = json.load(open(os.path.join(old_dir, fn), encoding='utf-8'))
                for e in dd['episodes']:
                    for s in e['segments']:
                        seen.add(s['seed'])
            except Exception:
                pass
mine = [s['seed'] for e in doc['episodes'] for s in e['segments']]
clash = sorted(x for x in set(mine) if x in seen)
print('与库里已有种子重复：', clash if clash else '无')

txt = json.dumps(doc, ensure_ascii=False, indent=1)
open(os.path.join(FOLDER, OUT + '.json'), 'w', encoding='utf-8').write(txt)
open(os.path.join(FOLDER, OUT + '_全选复制粘贴.txt'), 'w', encoding='utf-8').write(txt)
n = sum(len(e['segments']) for e in doc['episodes']); sec = sum(s['duration_seconds'] for e in doc['episodes'] for s in e['segments'])
print(f'{len(doc["episodes"])} 集、{n} 个任务、约 {sec} 秒；文件 {len(txt.encode())/1024:.0f} KB → {OUT}')
for e in doc['episodes']:
    print('  ', e['title'], len(e['segments']), '个任务', sum(s['duration_seconds'] for s in e['segments']), '秒')
