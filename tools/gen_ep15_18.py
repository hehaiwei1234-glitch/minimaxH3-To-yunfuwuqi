#!/usr/bin/env python3
"""剧本第 15–18 集（背叛的暗网／印记与离别／银刃之下／暴君的回顾）场景级改编版（2026-10-11，合并稿编号 001）。

做法同马场四集：先问“观众必须看懂哪几件事、每件事由哪个镜头传达、上一镜头为什么引出下一镜头”，再写镜头。
原剧本是大纲，缺口这里补成镜头：
  15 集：保罗为什么发疯（他的公司和莉莉都被抢了）→ 玛丽带来的是谁（观众先看到那个满脸伤疤的人）→ 证据（照片特写）
         → 计划（基利安一走就动手）→ 玛丽的恨 → 猎手的毒匕首（后面“银刀致命”靠它先铺垫）
  16 集：时间地点交代（清晨主卧）→ 咬痕要先拍清楚（趴着、颈后朝镜头）→ 莉莉醒来摸到它
         → 基利安离开的理由、莉莉问“多久”、他的禁令、额头吻、求婚（对话一人一句、来回）→ 车队离开 → 树枝断裂（触发）→ 黑影爬墙
  17 集：翻栏杆捂嘴（过程）→ 闻她→ 银匕首贴脖子（毒、“你的 Alpha 救不了你”）→ 飞机上先拍他闭目平静（交代）
         → 心脏剧痛眼睛变金（触发）→ 怒吼掉头 → 保镖拿起内线电话（命令有人听、有人执行）
  18 集：拖人（在途）→ 推进仓库 → 玛丽见血的反应 → 保罗捏脸 → 扬手 → 铁门飞进来 → 在场的人各有反应
         → 黑狼走出（先让观众认出金色眼睛）→ 流浪狼人吓掉刀 → 莉莉认出他 → 咆哮扑出
方向统一：阳台上莉莉面朝右看车队，树枝声在左边；黑影从左边的花园爬上来；仓库门在右边，狼从右边走出来朝左。
39 个任务、约 183 秒，全部新写。素材／人物／style 以第 11–14 集合并稿为底逐字复制，新增 5 个场景、2 个人物、1 只黑狼。
种子 5501–5811（和库里所有稿子不重复）。写进合并稿编号规矩：文件名开头 001_。
"""
import copy, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _h3draft import Batch, FOLDER, breathy, voiced

BASE = '合并稿/旧合并稿/合并_第11-14集+B_制作稿_追加.json'
OUT = '合并稿/001_第15-18集_场景级改编_制作稿_追加'
SRC = json.load(open(os.path.join(FOLDER, BASE), encoding='utf-8'))

b15, b16, b17, b18 = (Batch(BASE, SRC['title'], s) for s in (5500, 5600, 5700, 5800))

PV = '[[asset:paul_villa]]'; BAL = '[[asset:villa_balcony]]'; GP = '[[asset:garden_path]]'; WH = '[[asset:warehouse]]'
JET = '[[asset:jet_cabin]]'; BD = '[[asset:bedroom]]'
PL = '[[asset:paul]]'; MB = '[[asset:mary_black]]'; RG = '[[asset:rogue]]'; LS = '[[asset:lily_shirt]]'
K = '[[asset:killian]]'; KG = '[[asset:killian_gold]]'; BGD = '[[asset:bodyguard]]'; WF = '[[asset:black_wolf]]'

# ------------------------------------------------------------------------------------------------ 新素材（只加到 b15，最后用 b15 的 assets）
b15.scene('paul_villa', '保罗破败的客厅',
          "The wrecked living room of a bankrupt hillside villa at dawn: a tall bay window with torn curtains and cold pale light at the left, an overturned brown leather sofa and the shards of a smashed glass coffee table in the middle, a wide double doorway into a dim hallway at the right, a smashed wooden cabinet against the back wall, torn papers and broken glass scattered over a dark wooden floor. The reference fixes the layout and decor.",
          "清晨，一栋破产山间别墅里被砸烂的客厅：左边是挂着破窗帘的高大飘窗和冷冷的淡光，中间是翻倒的棕色皮沙发和摔碎的玻璃茶几，右边是通向昏暗走廊的宽双开门，后墙边是被砸坏的木柜，深色木地板上撒满碎纸和碎玻璃。参考图固定布局与陈设。",
          "A photorealistic ultra-wide 8:3 cinemascope shot of the wrecked living room of a bankrupt hillside villa at dawn: a tall bay window with torn curtains and cold pale light at the left, an overturned brown leather sofa and the shards of a smashed glass coffee table in the middle, a wide double doorway into a dim hallway at the right, a smashed wooden cabinet against the back wall, torn papers and broken glass over a dark wooden floor. "
          "The frame holds the window, the sofa, the table shards, the doorway and the cabinet.")
b15.scene('villa_balcony', '别墅二楼阳台（清晨）',
          "The second-floor stone balcony of a dark luxurious hillside mansion on a clear morning: a carved stone balustrade runs along the front; below at the right a gravel driveway leads to tall black iron gates; at the left in the distance a hedge-lined back garden and the rusted corrugated-iron roof of an old warehouse; behind it the dark stone wall and tall glass doors. The reference fixes the layout and decor.",
          "晴朗的清晨，阴沉豪华的山间庄园二楼石质阳台：前面是雕花石栏杆；右下方一条碎石车道通向高大的黑色铁门；左边远处是篱笆围起来的后花园和一座废弃仓库生锈的铁皮屋顶；身后是深色石墙和高大的玻璃门。参考图固定布局与陈设。",
          "A photorealistic ultra-wide 8:3 cinemascope shot of the second-floor stone balcony of a dark luxurious hillside mansion on a clear morning: a carved stone balustrade runs along the front, a gravel driveway at the lower right leads to tall black iron gates, a hedge-lined back garden and the rusted corrugated-iron roof of an old warehouse in the distance at the left, the dark stone wall and tall glass doors behind. "
          "The frame holds the balustrade, the driveway, the gates, the garden and the warehouse roof.")
b15.scene('garden_path', '后花园的碎石小路',
          "A hedge-lined gravel path in the overgrown back garden of a dark mansion on a clear morning: tall dark hedges on both sides, the path running from left to right, at the right a derelict rusted corrugated-iron warehouse with a tall sliding iron door, the mansion's dark stone wall far behind at the left, long soft shadows. The reference fixes the layout and decor.",
          "晴朗的清晨，阴沉庄园荒芜的后花园里一条两边是高大深色篱笆的碎石小路：路从左往右延伸，右边是一座废弃、生锈的铁皮仓库和一扇高大的铁拉门，左边远处是庄园深色的石墙，影子又长又柔。参考图固定布局与陈设。",
          "A photorealistic ultra-wide 8:3 cinemascope shot of a hedge-lined gravel path in the overgrown back garden of a dark mansion on a clear morning: tall dark hedges on both sides, the path running from left to right, a derelict rusted corrugated-iron warehouse with a tall sliding iron door at the right, the mansion's dark stone wall far behind at the left, long soft shadows. "
          "The frame holds the hedges, the path, the warehouse and the far wall.")
b15.scene('warehouse', '废弃仓库内部',
          "The interior of a derelict warehouse: a grey concrete floor, a tall rusted iron double door at the right, stacked wooden crates and steel barrels at the left, concrete pillars in the middle, and shafts of dusty pale light falling from high broken windows at the back. The reference fixes the layout and decor.",
          "一间废弃仓库的内部：灰色水泥地面，右边是一扇高大生锈的铁双开门，左边堆着木箱和铁桶，中间立着水泥柱，后面高处破窗里落下一束束带灰尘的淡光。参考图固定布局与陈设。",
          "A photorealistic ultra-wide 8:3 cinemascope shot of the interior of a derelict warehouse: a grey concrete floor, a tall rusted iron double door at the right, stacked wooden crates and steel barrels at the left, concrete pillars in the middle, shafts of dusty pale light falling from high broken windows at the back. "
          "The frame holds the door, the crates, the pillars and the light shafts.")
b15.scene('jet_cabin', '私人飞机机舱',
          "The cabin of a luxury private jet in flight: cream leather seats and a polished walnut table at the left, a row of oval windows along the right wall showing bright blue sky and white cloud, a wall intercom handset beside the cabin door at the far end, warm soft cabin lighting. The reference fixes the layout and decor.",
          "高空飞行中的豪华私人飞机机舱：左边是奶油色真皮座椅和抛光的胡桃木桌子，右边墙上一排椭圆形舷窗，外面是明亮的蓝天和白云，尽头舱门旁的墙上挂着内线电话听筒，机舱灯光温暖柔和。参考图固定布局与陈设。",
          "A photorealistic ultra-wide 8:3 cinemascope shot of the cabin of a luxury private jet in flight: cream leather seats and a polished walnut table at the left, a row of oval windows along the right wall showing bright blue sky and white cloud, a wall intercom handset beside the cabin door at the far end, warm soft cabin lighting. "
          "The frame holds the seats, the table, the windows and the intercom.")
b15.person('rogue', '流浪狼人（反派猎手）',
           "Rogue, a lean, wiry adult man in his late thirties with long unkempt black hair, a pale hollow face, a thick jagged scar running from his forehead across his left eye down to his jaw, dark stubble and yellowed sharp teeth, wearing a patched black leather jacket over a faded grey shirt, dark trousers and scuffed black boots. The portrait fixes his identity and clothes, not staging.",
           "流浪狼人，三十多岁瘦削精悍的成年男人，长长乱糟糟的黑发，苍白凹陷的脸，一道粗粗的锯齿状伤疤从额头横过左眼一直划到下巴，满脸胡茬，牙齿发黄而尖利，穿打着补丁的黑色皮夹克、褪色的灰衬衫、深色长裤和磨旧的黑靴子。肖像固定他的长相和衣着，不固定姿势。",
           "A photorealistic half-body portrait of a lean, wiry adult man in his late thirties with long unkempt black hair, a pale hollow face, a thick jagged scar running from his forehead across his left eye down to his jaw, dark stubble and yellowed sharp teeth, wearing a patched black leather jacket over a faded grey shirt. "
           "He faces the camera with a cruel, sly expression. Soft even studio light, plain neutral gray background, natural skin texture with visible pores.")
b15.person('mary_black', '玛丽（黑色大衣）',
           "Mary, the same adult woman in her mid-twenties as in the reference, with sleek honey-blonde hair in a tight low bun, flawless makeup, glossy red lips and sharp green eyes, wearing a fitted black wool coat over a black dress, black high heels and a pearl necklace. The portrait fixes her identity and clothes, not staging.",
           "玛丽，和参考图里同一位二十五岁左右的成年女人，光滑的蜜金色头发盘成紧紧的低发髻，妆容精致，红唇亮泽，绿色的眼睛锐利，穿合身的黑色羊毛大衣、里面黑色连衣裙，黑色高跟鞋，戴珍珠项链。肖像固定她的长相和衣着，不固定姿势。",
           "A photorealistic half-body portrait of the same woman as in the reference image, sleek honey-blonde hair in a tight low bun, flawless makeup, glossy red lips and sharp green eyes, wearing a fitted black wool coat over a black dress and a pearl necklace. "
           "She faces the camera with a cold, composed expression. Soft even studio light, plain neutral gray background, natural skin texture with visible pores.",
           ref='mary')
b15.prop('black_wolf', '巨大的纯黑狼',
         "A colossal jet-black wolf the size of a small horse, with thick glossy black fur, a broad powerful chest and heavy shoulders, long white fangs and dark-gold glowing eyes. The portrait fixes the wolf's coat, build and eyes, not staging.",
         "一头巨大的纯黑狼，体型像一匹小马，毛又厚又亮，胸膛宽阔、肩膀厚重，长长的白色獠牙，眼睛是暗金色发光的。肖像固定狼的毛色、体型和眼睛，不固定姿势。",
         "A photorealistic full-body side-profile photograph of a colossal jet-black wolf the size of a small horse, with thick glossy black fur, a broad powerful chest and heavy shoulders, long white fangs and dark-gold glowing eyes, standing on bare ground. "
         "Soft even studio light, plain neutral gray background, natural fur texture, four legs clearly visible.")
b15.character('Rogue', 'rogue',
              "A rough adult male voice, low, gravelly and wheezing with a sly, mocking edge, speaking clear American English. Every word is fully voiced and audible.",
              "粗哑的成年男声，低沉沙砾般带着喘息声，有一种狡猾、嘲弄的味道，说清楚的美式英语。每个字都正常发声、清晰可辨。")
b15.d['characters']['MaryBlack'] = {'image_keys': ['mary_black'], 'voice_description': copy.deepcopy(SRC['characters']['Mary']['voice_description'])}

# ------------------------------------------------------------------------------------------------ 场景布局句
LAY_PV = " Fixed stage layout: the tall bay window with torn curtains and cold pale dawn light is at frame-left; the overturned leather sofa and the shards of the smashed coffee table are in the middle; the wide double doorway to a dim hallway is at frame-right; the smashed wooden cabinet stands against the back wall."
END_PV = " Cold pale dawn light, dust hanging in the air, the wrecked room softly blurred behind."
LAY_BD = " Fixed stage layout: the huge dark-wood bed with charcoal-grey linen fills the left and center of the frame; the tall dark-wood door with a brass handle is at frame-right; the floor-to-ceiling windows with the heavy curtains drawn back are at the back."
END_BD = " Bright warm morning sunlight pours through the open curtains across the bed, soft golden light, the room softly blurred behind."
LAY_BAL = " Fixed stage layout: the carved stone balustrade runs along the front of the balcony; the gravel driveway and the tall black iron gates are at frame-right below; the hedge-lined back garden and the rusted warehouse roof are at frame-left in the distance; the dark stone wall and tall glass doors are behind."
END_BAL = " Soft clear morning sunlight, a pale blue sky, the garden softly blurred in the distance."
LAY_GP = " Fixed stage layout: the gravel path runs from frame-left to frame-right between tall dark hedges; the rusted corrugated-iron warehouse with its tall sliding iron door stands at frame-right; the mansion's dark stone wall is far behind at frame-left."
END_GP = " Soft clear morning light, long shadows across the gravel."
LAY_WH = " Fixed stage layout: the tall rusted iron double door is at frame-right; the stacked wooden crates and steel barrels are at frame-left; concrete pillars stand in the middle and shafts of dusty light fall from the high windows at the back."
END_WH = " Dim, dusty light with pale shafts from the high windows, the warehouse softly blurred behind."
LAY_JET = " Fixed stage layout: the cream leather seats and the walnut table are at frame-left; the row of oval windows with bright blue sky and white cloud runs along the frame-right wall; a wall intercom handset hangs beside the cabin door at the far end."
END_JET = " Warm soft cabin lighting, bright daylight from the windows."


def T(b, title, dur, chars, assets, refs, img, end, vis_zh, dlg, act_en, act_zh, sound, dep=False):
    s = b.task(title, dur, chars, assets, refs, img, end, vis_zh, '0—%d秒，镜头固定。' % dur, dlg, act_en, act_zh, sound)
    s['depends_on_previous'] = dep
    return s


def episode(b, title, summary):
    lines = []
    for t in b.tasks:
        lines.append((t['title'].split('｜')[1] + '，' + t['visual_zh']).replace('：', '，'))
        for x in t['dialogue']:
            lines.append(f"{x['speaker']}：“{x['text']}”")
    return {'title': title, 'summary': summary, 'script': '\n'.join(lines), 'segments': b.tasks, 'dialogue_language': 'en'}


# =================================================================================================== 第 15 集：背叛的暗网
# 观众要看懂：① 保罗破产发疯，恨基利安（公司和莉莉都被抢了）② 玛丽带着一个满脸伤疤的陌生人来
# ③ 玛丽查到了基利安不是人（有照片为证）④ 她雇了猎手 ⑤ 计划：基利安一离开就抓莉莉 ⑥ 玛丽想毁莉莉的脸 ⑦ 猎手有毒匕首、想要莉莉
# 在场名单：保罗、玛丽、流浪狼人（猎手）。保罗和玛丽的对话用双人镜头，猎手在 03 入场、09 单独出现。

T(b15, '01｜保罗在破败的客厅里砸东西', 3, ['PaulOnScreen'], ('paul_villa', 'paul'), ['paul_villa'],
  "Side-on wide-medium shot of Paul alone, from the head to the knees, in profile facing frame-right, in the middle third of the frame, standing in the wrecked living room in the dusty navy blazer over a creased white open-collared shirt, his collar crooked and his hair mussed, "
  "both hands gripping the back of a heavy wooden dining chair raised to shoulder height, his teeth bared, his brows crashing together, his red-rimmed eyes on the smashed wooden cabinet at frame-right. The frame holds exactly one person, Paul.",
  END_PV + LAY_PV, "保罗在破败的客厅里发疯似的把椅子砸向柜子。",
  None,
  f"A steady side-on wide-medium shot opens from the adopted first frame in {PV}: {PL} hurls the heavy wooden chair at the smashed cabinet at frame-right with a roar, the chair exploding into splinters against the wood, his arms dropping and his chest heaving, his teeth bared, his brows crashing together and his eyes red-rimmed. The camera holds still.",
  "一个稳定的侧面宽中景，从已采用的开场图继续，场景是破败的客厅：保罗吼叫着把沉重的木椅砸向画面右边被砸坏的柜子，椅子在木柜上炸成碎片，他的双臂垂下，胸口剧烈起伏，龇着牙，眉头拧在一起，眼眶发红。镜头固定不动。",
  breathy("A heavy crash of splintering wood and a rattle of falling glass.", "木头碎裂的重重一声巨响，和玻璃哗啦掉落的声音。"))

T(b15, '02｜保罗咆哮：他抢了我的公司和莉莉', 6, ['PaulOnScreen'], ('paul_villa', 'paul'), ['paul_villa'],
  "Side-on medium shot of Paul alone, from the head to the waist, in profile facing frame-right, in the middle third of the frame, both fists braced on top of the smashed wooden cabinet at frame-right, the dusty navy blazer hanging crooked, his chest heaving, "
  "his jaw clenched, his lips pulled back from his teeth, his brows crashing together, his red-rimmed wet eyes on the splintered cabinet top in front of him. The frame holds exactly one person, Paul.",
  END_PV + LAY_PV, "保罗双拳撑在烂木柜上，红着眼睛吼出：他抢走了我的公司和莉莉。",
  ('PaulOnScreen', "He took my company and Lily!", 1.0),
  f"A steady side-on medium shot opens from the adopted first frame in {PV}: {PL} shouts in a hoarse, cracking voice and slams his right fist down once on the cabinet top, his jaw clenched, his lips pulled back from his teeth and his red-rimmed wet eyes on the splintered wood. The camera holds still.",
  "一个稳定的侧面中景，从已采用的开场图继续，场景是破败的客厅：保罗用嘶哑发颤的声音吼出来，右拳在柜面上重重砸了一下，下颌咬紧，嘴唇咧开露出牙齿，发红湿润的眼睛盯着破裂的木头。镜头固定不动。",
  voiced("Splinters pattering to the floor and a ragged breath.", "碎木屑噼啪落地的声音和一声粗重的喘息。"), dep=True)

T(b15, '03｜玛丽带着满脸伤疤的陌生人走进来', 4, ['MaryBlack', 'Rogue'], ('paul_villa', 'mary_black', 'rogue'), ['paul_villa'],
  "Side-on medium two-shot, both people from the head to the knees, in the middle third of the frame, just inside the doorway of the wrecked living room, both in profile facing frame-left. "
  "Mary in front at frame-left in a fitted black wool coat over a black dress and black high heels, her honey-blonde hair in a tight low bun, her chin lifted, her lips set in a cold smug smile, her sharp green eyes on the overturned leather sofa at frame-left. "
  "Rogue one step behind her at frame-right, a lean wiry man in a patched black leather jacket, a thick jagged scar down his left cheek and across his eye, his heavy brows lowered, his lips pulled into a cruel half-grin over yellowed teeth, his right hand resting on a sheathed silver dagger at his belt, his narrowed eyes on the shards of the coffee table at frame-left. "
  "The frame holds exactly two people: Mary and Rogue.",
  END_PV + LAY_PV, "玛丽踩着高跟鞋走进来，身后跟着一个满脸伤疤、手按匕首的陌生男人。",
  None,
  f"A steady side-on medium two-shot opens from the adopted first frame in {PV}: {MB} walks slowly across the wreckage, her heels crunching on broken glass, her chin lifted and her cold smug smile widening, her eyes sweeping over the overturned sofa. "
  f"{RG} follows one step behind, his right hand tapping the hilt of the sheathed dagger, his lips curling into a cruel half-grin over his yellowed teeth and his heavy brows low. The camera holds still.",
  "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是破败的客厅：玛丽缓缓走过一地狼藉，高跟鞋踩在碎玻璃上咯吱作响，下巴抬起，冷冷的得意笑容更深，眼睛扫过翻倒的沙发。流浪狼人跟在她身后一步，右手轻轻敲着鞘里匕首的柄，咧开的残忍笑容露出发黄的牙。镜头固定不动。",
  breathy("High heels crunching over broken glass and slow, heavy boot steps.", "高跟鞋踩过碎玻璃的咯吱声和缓慢沉重的靴子声。"))

T(b15, '04｜玛丽举起照片：基利安不是人', 6, ['MaryBlack', 'PaulOnScreen'], ('paul_villa', 'mary_black', 'paul'), ['paul_villa'],
  "Side-on medium two-shot, both people from the head to the waist, in the middle third of the frame, facing each other in profile in the middle of the wrecked living room. "
  "Paul at frame-left in the dusty navy blazer, facing frame-right, his arms hanging, his chest heaving, his lips parted, his brows drawn together, his red-rimmed eyes on the glossy photograph in Mary's hand. "
  "Mary at frame-right in the fitted black wool coat, facing frame-left, her right hand holding a glossy photograph up at chest height toward Paul, her chin lifted, her lips set in a cold smug smile, her sharp green eyes on Paul's face. "
  "The frame holds exactly two people: Paul and Mary.",
  END_PV + LAY_PV, "玛丽把一张照片举到保罗面前，说基利安根本不是人。",
  ('MaryBlack', "Killian isn't even human, Paul.", 1.0),
  f"A steady side-on medium two-shot opens from the adopted first frame in {PV}: {MB} at frame-right speaks in a low, sugary, venomous voice, holding the photograph steady in front of Paul, her cold smug smile widening and her eyes on his face. "
  f"{PL} at frame-left leans closer to the photograph, his lips parting, his brows drawing together and his red-rimmed eyes widening on the print. The camera holds still.",
  "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是破败的客厅：画面右边的玛丽用低沉、甜腻又恶毒的声音说话，把照片稳稳举在保罗面前，冷冷的得意笑容更深，眼睛看着他的脸。画面左边的保罗凑近照片，嘴唇张开，眉头拧起，发红的眼睛盯着相纸越睁越大。镜头固定不动。",
  voiced("Dust settling and a faint creak of floorboards.", "灰尘落定的细微声响和地板轻轻的吱嘎声。"))

T(b15, '05｜照片特写：别墅的墙上有深深的爪痕', 3, [], ('paul_villa',), ['paul_villa'],
  "Close-up of a glossy photograph filling the frame, lying flat on a dark wooden surface in sharp focus, in the middle third of the frame: a night photograph of a dark stone mansion wall with a wide jagged crack running up its length and four deep parallel claw gouges cut into the stone, chunks of plaster fallen on the grass below. No people are in the frame.",
  " Cold pale dawn light, the dark wooden surface softly blurred around the photograph.", "照片特写：一面深色石墙上裂开一道大缝，墙上有四道深深的爪痕。",
  None,
  f"A steady close-up opens from the adopted first frame in {PV}: the glossy photograph lies perfectly flat in sharp focus, the jagged crack and the four deep claw gouges clear in the pale light; its curled corner trembles in a faint draft and a thin trickle of plaster dust slides off the print. No people appear. The camera holds still.",
  "一个稳定的特写，从已采用的开场图继续，场景是破败的客厅：光面照片平平地躺着、对焦清晰，锯齿状的裂缝和四道深深的爪痕在淡淡的光里看得清清楚楚；卷起的一角在微风里轻轻颤动，一缕细细的灰泥粉末从相纸上滑落。画面里没有人出现。镜头固定不动。",
  breathy("A faint rustle of paper in a quiet room.", "安静的房间里纸张轻轻的沙沙声。"))

T(b15, '06｜玛丽：我雇了猎手', 6, ['MaryBlack', 'PaulOnScreen'], ('paul_villa', 'mary_black', 'paul'), ['paul_villa'],
  "Side-on medium two-shot, both people from the head to the waist, in the middle third of the frame, facing each other in profile in the middle of the wrecked living room. "
  "Paul at frame-left in the dusty navy blazer, facing frame-right, his lips parted, his brows pulled up, his eyes wide on Mary's face. "
  "Mary at frame-right in the fitted black wool coat, facing frame-left, the photograph lowered in her left hand, her right hand on her hip, her chin lifted, her lips set in a cold smug smile, her sharp green eyes on Paul's face. "
  "The frame holds exactly two people: Paul and Mary.",
  END_PV + LAY_PV, "玛丽放下照片，说她已经雇了一个猎手。",
  ('MaryBlack', "I hired a hunter, Paul.", 1.0),
  f"A steady side-on medium two-shot opens from the adopted first frame in {PV}: {MB} at frame-right speaks in a sugary, hushed voice, her cold smug smile widening and her chin tilting up. "
  f"{PL} at frame-left looks at her, his brows drawing together and his lips pressing tight. The camera holds still.",
  "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是破败的客厅：画面右边的玛丽用甜腻压低的声音说话，冷冷的得意笑容更深，下巴抬得更高。画面左边的保罗看着她，眉头拧起，嘴唇抿紧。镜头固定不动。",
  voiced("A faint creak of floorboards and a light breeze through the broken window.", "地板轻轻的吱嘎声，和破窗里吹进来的微风。"))

T(b15, '07｜玛丽：他一离开，我们就抓她', 6, ['MaryBlack', 'PaulOnScreen'], ('paul_villa', 'mary_black', 'paul'), ['paul_villa'],
  "Side-on medium two-shot, both people from the head to the waist, in the middle third of the frame, facing each other in profile in the middle of the wrecked living room. "
  "Paul at frame-left in the dusty navy blazer, facing frame-right, his lips pressed tight, his brows drawn together, his narrowed eyes on Mary's face. "
  "Mary at frame-right in the fitted black wool coat, facing frame-left, leaning slightly toward him, her chin lifted, her lips set in a cold smug smile, her sharp green eyes on Paul's face. "
  "The frame holds exactly two people: Paul and Mary.",
  END_PV + LAY_PV, "玛丽凑近保罗，低声说：基利安一离开，就把莉莉抓过来。保罗慢慢点头。",
  ('MaryBlack', "When he leaves, we take her.", 1.0),
  f"A steady side-on medium two-shot opens from the adopted first frame in {PV}: {MB} at frame-right leans toward him and speaks in a low, cold whisper, her smug smile hardening and her eyes on his face. "
  f"{PL} at frame-left nods slowly once, his lips curling into a cruel half-grin and his eyes narrowing. The camera holds still.",
  "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是破败的客厅：画面右边的玛丽凑向他，用低沉冰冷的耳语说话，得意的笑容变硬，眼睛看着他的脸。画面左边的保罗慢慢点了一下头，嘴角扯出残忍的半个笑，眼睛眯起来。镜头固定不动。",
  voiced("A faint creak of floorboards and a light breeze through the broken window.", "地板轻轻的吱嘎声，和破窗里吹进来的微风。"), dep=True)

T(b15, '08｜玛丽：我要毁了她那张脸', 6, ['MaryBlack'], ('paul_villa', 'mary_black'), ['paul_villa'],
  "Medium close-up of Mary alone, from the head to the waist, in profile facing frame-left, in the middle third of the frame, in the fitted black wool coat, the glossy photograph held in her left hand at chest height in front of her, "
  "her lips pressed into a thin cold smug smile, her jaw tight, her sharp green eyes narrowed on the photograph. The frame holds exactly one person, Mary.",
  END_PV + LAY_PV, "玛丽盯着照片，用甜得发毒的声音说要毁了莉莉的脸。",
  ('MaryBlack', "I'll ruin that pretty face.", 1.0),
  f"A steady medium close-up opens from the adopted first frame in {PV}: {MB} speaks in a venomous, sugary voice, her right thumbnail dragging slowly across the surface of the photograph, her thin smug smile widening, her jaw tight and her narrowed eyes on the print. The camera holds still.",
  "一个稳定的中近景，从已采用的开场图继续，场景是破败的客厅：玛丽用甜得发毒的声音说话，右手拇指的指甲慢慢划过照片表面，薄薄的得意笑容越扩越大，下颌绷紧，眯着的眼睛盯着相纸。镜头固定不动。",
  voiced("A slow scrape of a fingernail on glossy paper.", "指甲慢慢划过光面相纸的细微刮擦声。"))

T(b15, '09｜流浪狼人舔着毒匕首', 6, ['Rogue'], ('paul_villa', 'rogue'), ['paul_villa'],
  "Medium close-up of Rogue alone, from the head to the chest, in profile facing frame-left, in the middle third of the frame, in the patched black leather jacket, the long scar down his left cheek and across his eye, "
  "a silver dagger held upright in front of his face in his right hand with a faint green sheen of poison along its blade, his heavy brows lowered, his lips parted, his narrowed eyes on the dagger's tip. The frame holds exactly one person, Rogue.",
  END_PV + LAY_PV, "流浪狼人用舌头舔过匕首上的毒药，说那个有 Luna 血脉的女孩会是他的。",
  ('Rogue', "That Luna girl will be mine.", 1.0),
  f"A steady medium close-up opens from the adopted first frame in {PV}: {RG} draws his tongue slowly along the flat of the blade, then lowers the dagger and speaks in a low, wheezing, sly voice, his lips curling into a cruel grin over yellowed teeth and his narrowed eyes lifting to the tip of the dagger. The camera holds still.",
  "一个稳定的中近景，从已采用的开场图继续，场景是破败的客厅：流浪狼人用舌头慢慢舔过刀刃的平面，然后放低匕首，用低沉、带喘息的狡猾声音说话，嘴唇扯成残忍的笑露出发黄的牙，眯着的眼睛抬起来看着刀尖。镜头固定不动。",
  voiced("A slow wet drag of a tongue on metal and a wheezing breath.", "舌头慢慢舔过金属的湿声，和一声嘶哑的喘息。"))

# =================================================================================================== 第 16 集：印记与离别
# 观众要看懂：① 清晨、主卧 ② 莉莉颈后多了新月咬痕（咬痕朝镜头）③ 她醒来，摸到它，感觉到自己变了（听觉变灵）
# ④ 基利安要走（理由：处理欧洲的长老）⑤ 莉莉问多久 ⑥ 他的禁令：别出别墅 ⑦ 额头吻、“回来就结婚” ⑧ 车队离开，莉莉在阳台
# ⑨ 树枝断裂（触发）⑩ 黑影爬墙。对话 05–09 用同一个双人构图、一人一句、来回。
BD16 = ('bedroom', 'lily_shirt')

T(b16, '01｜清晨，主卧', 3, ['LilyShirt'], ('bedroom', 'lily_shirt'), ['bedroom'],
  "Side-on wide shot of Lily alone, in the middle third of the frame, lying on her stomach on the huge dark-wood bed in the oversized white men's shirt, the charcoal-grey duvet pulled up to her waist, her head turned toward frame-right on the pillow, "
  "her long chestnut hair loose over her left shoulder, her eyes closed, her lips softly parted, her brows relaxed. Tangled sheets and pillows lie around her. The frame holds exactly one person, Lily.",
  END_BD + LAY_BD, "清晨的阳光洒在主卧的床上，莉莉趴在凌乱的被子里睡着。",
  None,
  f"A steady wide shot opens from the adopted first frame in {BD}: golden morning sunlight slides slowly across the bed and over {LS}, who breathes slowly in her sleep, her lips softly parted and her brows relaxed. A light breeze stirs the curtain at the back. The camera holds still.",
  "一个稳定的宽景，从已采用的开场图继续，场景是主卧：金色的晨光慢慢滑过床面，滑过莉莉，她在睡梦里均匀地呼吸，嘴唇轻轻张开，眉头舒展。一阵微风吹动后面的窗帘。镜头固定不动。",
  breathy("Soft birdsong outside and the quiet rustle of linen.", "窗外轻轻的鸟叫声和亚麻床单的轻响。"))

T(b16, '02｜特写：她颈后的新月咬痕', 3, ['LilyShirt'], ('bedroom', 'lily_shirt'), ['bedroom'],
  "Close-up from slightly above and from the side of Lily's head, neck and shoulders as she lies on her stomach, her face turned toward frame-right on the pillow, her long chestnut hair swept forward over her left shoulder so that the back of her neck is bare, the collar of the oversized white shirt low on her shoulders; "
  "on the center of her bare nape, in the middle third of the frame, a dark-red crescent-moon mark in an ornate, tattoo-like pattern, the skin around it slightly flushed. Her eyes are closed, her lips softly parted, her brows relaxed. The frame holds exactly one person, Lily.",
  END_BD + LAY_BD, "特写：莉莉颈后有一枚暗红色、像图腾一样的新月咬痕。",
  None,
  f"A steady close-up opens from the adopted first frame in {BD}: the dark-red crescent mark on {LS}'s nape gleams in the warm sunlight as her slow breath lifts her shoulders, a loose strand of chestnut hair sliding across her cheek, her lips softly parted and her brows relaxed. The camera holds still.",
  "一个稳定的特写，从已采用的开场图继续，场景是主卧：莉莉颈后的暗红色新月印记在暖暖的阳光里发亮，她缓慢的呼吸让肩膀轻轻起伏，一缕散落的栗色头发滑过脸颊，嘴唇轻轻张开，眉头舒展。镜头固定不动。",
  breathy("Soft breathing and a faint rustle of linen.", "轻轻的呼吸声和亚麻床单细微的响声。"), dep=True)

T(b16, '03｜莉莉醒来，摸到颈后的印记', 4, ['LilyShirt'], ('bedroom', 'lily_shirt'), ['bedroom'],
  "Side-on medium shot of Lily alone, from the head to the waist, in the middle third of the frame, lying on her stomach on the bed propped on her left forearm, her face turned toward frame-right, in the oversized white shirt, her chestnut hair swept forward over her left shoulder, "
  "her eyes just opening, her lips parted, her brows drawn together, the crescent mark visible on her bare nape. The frame holds exactly one person, Lily.",
  END_BD + LAY_BD, "莉莉醒来，右手摸到颈后的印记，偏着头像在听什么，眼睛睁大。",
  None,
  f"A steady side-on medium shot opens from the adopted first frame in {BD}: {LS} blinks her eyes wide open and her right hand rises slowly to the back of her neck until her fingertips touch the crescent mark; she tilts her head as if listening, her lips parting, her brows drawing together and her eyes widening. The camera holds still.",
  "一个稳定的侧面中景，从已采用的开场图继续，场景是主卧：莉莉眨着眼睛睁大，右手慢慢抬到后颈，指尖碰到新月印记；她偏着头，像是在听什么，嘴唇张开，眉头拧起，眼睛越睁越大。镜头固定不动。",
  breathy("Birdsong that sounds unusually crisp and clear, and a soft intake of breath.", "格外清脆清晰的鸟叫声，和一声轻轻的吸气。"), dep=True)

T(b16, '04｜基利安坐在床边抚摸咬痕', 4, ['Killian', 'LilyShirt'], ('bedroom', 'killian', 'lily_shirt'), ['bedroom'],
  "Side-on medium two-shot, both people from the head to the waist, in the middle third of the frame, on and beside the huge dark-wood bed. "
  "Killian in the center sitting on the edge of the bed in profile facing frame-right, in the tailored black three-piece suit, white shirt and dark tie, his right hand raised, the tips of his fingers resting on Lily's bare nape, his heavy eyes on the crescent mark, his lips softly closed, his jaw relaxed, his brows level. "
  "Lily at frame-right lying on her stomach on the bed propped on her forearms, her face turned toward him in profile facing frame-left, in the oversized white shirt, her chestnut hair swept forward over her left shoulder, her eyes half closed, her lips parted, her brows soft. "
  "The frame holds exactly two people: Killian and Lily.",
  END_BD + LAY_BD, "基利安穿着高定西装坐在床边，指尖轻轻抚过她颈后的咬痕。",
  None,
  f"A steady side-on medium two-shot opens from the adopted first frame in {BD}: the fingertips of {K} trace slowly along the crescent mark on {LS}'s nape, his heavy eyes on the mark and his lips softly closed. She shivers under his touch, her eyes drifting half shut and her lips parting. The camera holds still.",
  "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是主卧：基利安的指尖慢慢描过莉莉颈后的新月印记，沉沉的眼睛看着印记，嘴唇轻轻闭着。她在他的触碰下轻轻一颤，眼睛慢慢半闭，嘴唇微张。镜头固定不动。",
  breathy("The faint rustle of linen and slow breathing.", "亚麻床单轻轻的响声和缓慢的呼吸声。"))

CL16 = ("Side-on medium close-up two-shot, both people from the head to the chest, in the middle third of the frame. "
        "Killian at frame-left in profile facing frame-right, in the tailored black three-piece suit, white shirt and dark tie, sitting on the edge of the bed, {K}. "
        "Lily at frame-right propped on her forearms on the bed, her face turned toward him in profile facing frame-left, in the oversized white shirt, her chestnut hair swept forward over her left shoulder, {L}. "
        "The frame holds exactly two people: Killian and Lily.")

T(b16, '05｜基利安：我要去处理欧洲的长老', 6, ['Killian', 'LilyShirt'], ('bedroom', 'killian', 'lily_shirt'), ['bedroom'],
  CL16.format(K="his eyes on her face, his lips set, his jaw tight, his brows level", L="her eyes on his face, her lips parted, her brows pulled up"),
  END_BD + LAY_BD, "基利安看着她，用低沉冷静的声音说要去惩罚欧洲的长老。",
  ('Killian', "I must punish the European elders.", 1.0),
  f"A steady side-on medium close-up opens from the adopted first frame in {BD}: {K} speaks in a low, calm, cold voice, his eyes on her face and his jaw tight. {LS} listens, her brows drawing together and her lips parting. The camera holds still.",
  "一个稳定的侧面中近景，从已采用的开场图继续，场景是主卧：基利安用低沉平静又冰冷的声音说话，眼睛看着她的脸，下颌绷紧。莉莉听着，眉头拧起，嘴唇张开。镜头固定不动。",
  voiced("A light morning breeze and a faint creak of the bed.", "轻轻的晨风和床垫细微的吱嘎声。"), dep=True)

T(b16, '06｜莉莉：你要去多久？', 6, ['Killian', 'LilyShirt'], ('bedroom', 'killian', 'lily_shirt'), ['bedroom'],
  CL16.format(K="his eyes on her face, his lips flat, his jaw tight, his brows level", L="her glossy eyes on his face, her lips trembling, her brows pulled up"),
  END_BD + LAY_BD, "莉莉用担心的小声音问：你要去多久？",
  ('LilyShirt', "Will you be gone long?", 1.0),
  f"A steady side-on medium close-up opens from the adopted first frame in {BD}: {LS} asks in a small, worried voice, her glossy eyes on his face, her brows pulling up and her lips trembling. {K}'s jaw tightens as he looks at her. The camera holds still.",
  "一个稳定的侧面中近景，从已采用的开场图继续，场景是主卧：莉莉用小小的、担心的声音问，湿亮的眼睛看着他的脸，眉头抬起，嘴唇发颤。基利安看着她，下颌绷紧。镜头固定不动。",
  voiced("A light morning breeze and a faint creak of the bed.", "轻轻的晨风和床垫细微的吱嘎声。"), dep=True)

T(b16, '07｜基利安：我回来之前不准出门', 6, ['Killian', 'LilyShirt'], ('bedroom', 'killian', 'lily_shirt'), ['bedroom'],
  CL16.format(K="his eyes dark and fixed on her face, his lips set, his jaw tight, his brows level", L="her eyes on his face, her lips pressed together, her brows pulled up"),
  END_BD + LAY_BD, "基利安用不容反驳的低声命令她：我回来之前，不准踏出别墅。",
  ('Killian', "Don't step outside until I return.", 1.0),
  f"A steady side-on medium close-up opens from the adopted first frame in {BD}: {K} lifts his left hand and cups her jaw, speaking in a low, steely voice, his dark eyes fixed on her face. {LS} gives one small nod, her lips pressing together. The camera holds still.",
  "一个稳定的侧面中近景，从已采用的开场图继续，场景是主卧：基利安抬起左手托住她的下颌，用低沉如钢的声音说话，深色的眼睛一直盯着她的脸。莉莉轻轻点了一下头，嘴唇抿紧。镜头固定不动。",
  voiced("A light morning breeze and a faint creak of the bed.", "轻轻的晨风和床垫细微的吱嘎声。"), dep=True)

T(b16, '08｜他吻在她额头上', 4, ['Killian', 'LilyShirt'], ('bedroom', 'killian', 'lily_shirt'), ['bedroom'],
  CL16.format(K="leaning down toward her, his lips an inch above her forehead, his eyes lowered on her face, his jaw relaxed, his brows level", L="her eyes closing, her lips parted, her brows soft"),
  END_BD + LAY_BD, "基利安低下头，在莉莉的额头上印下一个长长的吻，睁开眼时眼神里是病态的占有欲。",
  None,
  f"A steady side-on medium close-up opens from the adopted first frame in {BD}: {K} lowers his head and presses a long kiss to {LS}'s forehead, his eyes closing and his brows soft; then his eyes open slowly, dark with a possessive gleam, his jaw tight and his face still close to hers. Her eyes close and her lips part. The camera holds still.",
  "一个稳定的侧面中近景，从已采用的开场图继续，场景是主卧：基利安低下头，在莉莉的额头上印下一个长长的吻，眼睛闭上；然后他慢慢睁开眼，深色的眼睛里带着占有欲的光，脸仍贴得很近。她的眼睛闭上，嘴唇微张。镜头固定不动。",
  breathy("A soft sound of a kiss and slow breathing.", "轻轻的一声吻声和缓慢的呼吸声。"), dep=True)

T(b16, '09｜基利安：等我回来，我们就结婚', 6, ['Killian', 'LilyShirt'], ('bedroom', 'killian', 'lily_shirt'), ['bedroom'],
  CL16.format(K="his dark eyes on her face, his lips set, his jaw tight, his brows level", L="her glossy eyes on his face, her lips parted, her brows pulled up"),
  END_BD + LAY_BD, "基利安用拇指擦过她的脸颊，低声说：等我回来，我们就结婚。",
  ('Killian', "When I'm back, we marry.", 1.0),
  f"A steady side-on medium close-up opens from the adopted first frame in {BD}: {K}'s thumb brushes slowly along her cheek as he speaks in a low, husky, possessive voice, his jaw tight, his brows low and his dark eyes on her face. {LS} looks up at him, her glossy eyes widening and her lips parting. The camera holds still.",
  "一个稳定的侧面中近景，从已采用的开场图继续，场景是主卧：基利安的拇指慢慢擦过她的脸颊，用低沉沙哑、带着占有欲的声音说话，深色的眼睛看着她的脸。莉莉抬头看着他，湿亮的眼睛睁大，嘴唇微张。镜头固定不动。",
  voiced("A light morning breeze and a faint creak of the bed.", "轻轻的晨风和床垫细微的吱嘎声。"), dep=True)

T(b16, '10｜莉莉在阳台看着车队离开', 4, ['LilyShirt'], ('villa_balcony', 'lily_shirt'), ['villa_balcony'],
  "Side-on medium shot of Lily alone, from the head to the knees, in the middle third of the frame, standing at the stone balustrade of the second-floor balcony in profile facing frame-right, in the oversized white men's shirt, her chestnut hair loose and stirring in the breeze, both hands resting on the stone rail, "
  "her lips parted, her brows soft, her wistful eyes on the line of black SUVs rolling along the gravel driveway toward the tall black iron gates at frame-right. The frame holds exactly one person, Lily.",
  END_BAL + LAY_BAL, "莉莉站在二楼阳台，目送一队黑色车子驶向铁门。",
  None,
  f"A steady side-on medium shot opens from the adopted first frame in {BAL}: the black SUVs roll slowly along the gravel driveway toward the open iron gates at frame-right, and {LS}'s right hand rises to the back of her neck, her lips parting and her soft, wistful eyes following the cars. The camera holds still.",
  "一个稳定的侧面中景，从已采用的开场图继续，场景是二楼阳台：黑色的车子沿着碎石车道慢慢驶向画面右边敞开的铁门，莉莉的右手抬到后颈，嘴唇微张，柔柔的、若有所思的眼睛追着车子。镜头固定不动。",
  breathy("Distant car engines fading away and a light breeze.", "远处渐渐远去的引擎声和轻轻的风声。"))

T(b16, '11｜树枝断裂，她猛地回头', 4, ['LilyShirt'], ('villa_balcony', 'lily_shirt'), ['villa_balcony'],
  "Side-on medium shot of Lily alone, from the head to the knees, in the middle third of the frame, standing at the stone balustrade of the second-floor balcony in profile facing frame-right, in the oversized white men's shirt, her chestnut hair loose, both hands resting on the stone rail, "
  "her lips parted, her brows soft, her eyes on the black iron gates at frame-right. The hedge-lined back garden and the rusted warehouse roof are in the distance at frame-left. The frame holds exactly one person, Lily.",
  END_BAL + LAY_BAL, "一声树枝断裂的脆响，莉莉猛地回头看向左边的后花园。",
  None,
  f"A steady side-on medium shot opens from the adopted first frame in {BAL}: a sharp crack of a breaking branch sounds, and {LS} turns only her head toward frame-left, her eyes going wide on the hedge-lined garden and the rusted warehouse roof, her brows pulling up and her lips parting. The camera holds still.",
  "一个稳定的侧面中景，从已采用的开场图继续，场景是二楼阳台：一声树枝断裂的脆响，莉莉只是把头转向画面左边，睁大的眼睛看着篱笆围起来的后花园和生锈的仓库屋顶，眉头抬起，嘴唇张开。镜头固定不动。",
  breathy("A sharp crack of a breaking branch, then a hush.", "一声清脆的树枝断裂声，然后是一片寂静。"), dep=True)

T(b16, '12｜黑影顺着墙壁爬上来', 4, ['Rogue'], ('rogue',), [],
  "Wide shot looking up the dark stone wall of the mansion from the garden below, in the middle third of the frame: Rogue, a lean man in a patched black leather jacket, climbing the wall hand over hand through thick ivy, his gloved fingers gripping the stone ledges, "
  "his scarred face turned upward, his lips pulled back from yellowed teeth, his narrowed eyes on the stone balustrade of the balcony at the top of the frame. The frame holds exactly one person, Rogue.",
  " Soft clear morning sunlight, a pale blue sky behind the roofline.", "流浪狼人顺着墙上的藤蔓飞快地往阳台爬。",
  None,
  f"A steady wide shot opens from the adopted first frame: {RG} climbs up the stone wall hand over hand through the ivy, his gloved fingers hooking the ledges and his boots scrabbling at the stone, his lips pulled back from his yellowed teeth and his narrowed eyes fixed on the balustrade above; loose ivy leaves flutter down. The camera holds still.",
  "一个稳定的宽景，从已采用的开场图继续：流浪狼人顺着墙上的藤蔓双手交替往上爬，戴手套的手指钩住石头的凹处，靴子在石墙上蹬着，嘴唇咧开露出发黄的牙，眯起的眼睛盯着上面的栏杆；散落的藤叶飘落下来。镜头固定不动。",
  breathy("Scrabbling boots on stone and the rustle of ivy.", "靴子在石头上蹬踏的声音和藤叶的沙沙声。"))

# =================================================================================================== 第 17 集：银刃之下
# 观众要看懂：① 他翻上阳台抓住她 ② 他要什么（她的味道，“难怪基利安把你藏起来”）③ 银匕首、毒、“你的 Alpha 救不了你”
# ④ 基利安在飞机上（平静）→ ⑤ 心脏剧痛、眼睛变金（感应）→ ⑥ 怒吼掉头 → ⑦ 保镖执行。
# 03 的匕首贴脖子是原因，05 的心痛是结果，中间只隔一个“飞机上平静”的交代镜头。

T(b17, '01｜黑影翻过栏杆，捂住她的嘴', 4, ['Rogue', 'LilyShirt'], ('villa_balcony', 'rogue', 'lily_shirt'), ['villa_balcony'],
  "Side-on medium-wide two-shot, both people from the head to the knees, in the middle third of the frame, on the second-floor stone balcony. "
  "Lily at frame-right standing at the stone balustrade in profile facing frame-left, in the oversized white men's shirt, her chestnut hair loose, her right hand at the back of her neck, her lips parted, her brows pulled up, her wide eyes on the garden hedges at frame-left. "
  "Rogue at frame-left on the far side of the balustrade, his gloved hands gripping the top of the stone rail and his head and shoulders risen above it, in the patched black leather jacket, the long scar down his left cheek, his lips pulled back from yellowed teeth, his narrowed eyes on Lily. "
  "The frame holds exactly two people: Lily and Rogue.",
  END_BAL + LAY_BAL, "流浪狼人一下翻过栏杆，捂住莉莉的嘴，把她按在栏杆上。",
  None,
  f"A steady side-on medium-wide two-shot opens from the adopted first frame in {BAL}: {RG} vaults over the stone balustrade in one motion and lands close in front of her, his lips pulled back from his yellowed teeth. His left hand clamps over her mouth and his right arm locks across her collarbone, slamming her back against the stone rail. {LS}'s eyes go wide, her brows pull up and a muffled cry escapes behind his hand. The camera holds still.",
  "一个稳定的侧面中宽双人镜头，从已采用的开场图继续，场景是二楼阳台：流浪狼人一下翻过石栏杆，落在莉莉面前，左手捂住她的嘴，右臂横卡在她的锁骨上，把她狠狠按在石栏杆上，她的眼睛睁大，眉头抬起，一声闷叫从他的手底下漏出来。镜头固定不动。",
  breathy("A scuff of boots landing on stone and a muffled cry.", "靴子落在石头上的一声摩擦，和一声被堵住的闷叫。"))

PIN17 = ("Side-on medium close-up two-shot, both people from the head to the chest, in the middle third of the frame, at the stone balustrade. "
         "Lily at frame-right, pinned back against the stone rail in the oversized white men's shirt, {L}. "
         "Rogue directly behind her at frame-left in the patched black leather jacket, the long scar down his left cheek, {R}. "
         "The frame holds exactly two people: Lily and Rogue.")

T(b17, '02｜他嗅着她：难怪他把你藏起来', 6, ['Rogue', 'LilyShirt'], ('villa_balcony', 'rogue', 'lily_shirt'), ['villa_balcony'],
  PIN17.format(L="Rogue's left hand clamped over her mouth, her wide eyes wet with tears, her brows pulled up, her chest heaving, both hands gripping his wrist",
               R="his scarred face lowered beside her hair, his nostrils flared, his eyes half closed, his lips curling into a greedy grin over yellowed teeth"),
  END_BAL + LAY_BAL, "流浪狼人贪婪地嗅着她的头发，说难怪基利安把她藏得这么深；莉莉拼命挣扎。",
  ('Rogue', "No wonder he hides you.", 1.0),
  f"A steady side-on medium close-up opens from the adopted first frame in {BAL}: {RG} breathes in deeply beside her hair, his eyes half closing and his lips curling into a greedy grin, and speaks in a low, wheezing, sly voice. {LS} fights against his hold, her wet eyes wide and her brows pulled up, her hands dragging at his wrist. The camera holds still.",
  "一个稳定的侧面中近景，从已采用的开场图继续，场景是二楼阳台：流浪狼人在她的头发边深深吸了一口气，眼睛半闭，贪婪的笑容更大，用低沉、带喘息的狡猾声音说话。莉莉拼命挣扎，湿润的眼睛睁大，眉头抬起，双手拽着他的手腕。镜头固定不动。",
  voiced("A wheezing breath and the scuff of bare feet on stone.", "一声嘶哑的喘息和光脚蹭在石头上的摩擦声。"), dep=True)

T(b17, '03｜银匕首贴上她的脖子', 6, ['Rogue', 'LilyShirt'], ('villa_balcony', 'rogue', 'lily_shirt'), ['villa_balcony'],
  PIN17.format(L="her chin lifted away from the blade, her lips pressed tight and trembling, her brows pulled up, tears on her lashes, her wide eyes on the dagger",
               R="his left arm locked across her collarbone and his right hand holding a silver dagger with a faint green sheen of poison, its flat laid against the left side of her throat, his lips pulled into a cruel grin, his narrowed eyes on her face"),
  END_BAL + LAY_BAL, "流浪狼人把淬了毒的银匕首压在她脖子上，说她的 Alpha 现在救不了她。",
  ('Rogue', "Your Alpha can't save you now.", 1.0),
  f"A steady side-on medium close-up opens from the adopted first frame in {BAL}: {RG} presses the edge of the silver dagger against {LS}'s throat and speaks in a low, savage whisper, his lips curled into a cruel grin; a thin line of red blood wells up along the blade and runs down her neck. She freezes, her chin lifting, her lips trembling and her wide eyes brimming with tears. The camera holds still.",
  "一个稳定的侧面中近景，从已采用的开场图继续，场景是二楼阳台：流浪狼人把银匕首的刃口压在莉莉的喉咙上，用低沉凶狠的耳语说话；一道细细的红色血线沿着刀刃渗出，淌下她的脖子。她僵住了，下巴抬起，嘴唇发颤，睁大的眼睛里蓄满泪水。镜头固定不动。",
  voiced("A thin metallic hiss of a blade on skin and a shaky breath.", "刀刃贴着皮肤细细的金属嘶声，和一声发抖的呼吸。"), dep=True)

T(b17, '04｜万米高空的飞机上，基利安闭着眼睛', 4, ['Killian'], ('jet_cabin', 'killian'), ['jet_cabin'],
  "Side-on medium shot of Killian alone, from the head to the knees, in the middle third of the frame, reclined in a cream leather seat at frame-left in profile facing frame-right, in the tailored black three-piece suit, white shirt and dark tie, his hands folded on his lap, "
  "his eyes closed, his lips softly closed, his jaw relaxed, his brows level. Oval windows show bright blue sky and white cloud along the frame-right wall. The frame holds exactly one person, Killian.",
  END_JET + LAY_JET, "万米高空的私人飞机里，基利安靠在座椅上闭着眼睛，神情平静。",
  None,
  f"A steady side-on medium shot opens from the adopted first frame in {JET}: {K} sits calmly with his eyes closed, his chest rising and falling slowly, his lips softly closed and his brows level; white cloud drifts past the oval windows at frame-right. The camera holds still.",
  "一个稳定的侧面中景，从已采用的开场图继续，场景是私人飞机机舱：基利安平静地坐着，闭着眼睛，胸口缓慢起伏，嘴唇轻轻闭着，眉头平整；白云从画面右边的椭圆舷窗外飘过。镜头固定不动。",
  breathy("The low steady hum of jet engines and slow breathing.", "喷气发动机低沉平稳的嗡鸣和缓慢的呼吸声。"))

T(b17, '05｜他的心脏猛地一痛，眼睛变成金色', 3, ['KillianGold'], ('jet_cabin', 'killian_gold'), ['jet_cabin'],
  "Side-on medium close-up of Killian alone, from the head to the chest, in profile facing frame-right, in the middle third of the frame, reclined in the cream leather seat in the tailored black three-piece suit, his eyes closed, his lips softly closed, his brows just beginning to draw together, his hands folded on his lap. "
  "Oval windows show bright blue sky along the frame-right wall. The frame holds exactly one person, Killian.",
  END_JET + LAY_JET, "基利安心口一阵剧痛，猛地睁眼，眼睛变成暗金色，指尖长出黑色的爪。",
  None,
  f"A steady side-on medium close-up opens from the adopted first frame in {JET}: {KG}'s body jolts and his right hand clamps over his heart, black claws extending from his fingertips; his eyes snap open, glowing dark gold, his jaw clenching, his lips pulling back from sharp canine teeth and his brows crashing together. The camera holds still.",
  "一个稳定的侧面中近景，从已采用的开场图继续，场景是私人飞机机舱：基利安的身体猛地一震，右手按住心口，指尖伸出黑色的爪；他的眼睛猛地睁开，发出暗金色的光，下颌咬紧，嘴唇咧开露出尖利的犬齿，眉头拧在一起。镜头固定不动。",
  breathy("A sharp gasp and the hum of jet engines.", "一声猛烈的抽气和喷气发动机的嗡鸣。"))

T(b17, '06｜他怒吼：掉头！', 6, ['KillianGold'], ('jet_cabin', 'killian_gold'), ['jet_cabin'],
  "Side-on medium close-up of Killian alone, from the head to the chest, in profile facing frame-right, in the middle third of the frame, in the cream leather seat in the tailored black three-piece suit, his right hand clutching his chest with long black claws, "
  "his eyes glowing dark gold, his teeth bared, his jaw clenched, his brows crashing together. The oval window at frame-right behind him is clear and shows bright blue sky. The frame holds exactly one person, Killian.",
  END_JET + LAY_JET, "基利安怒吼着下令掉头，身后的舷窗被震出蛛网般的裂纹。",
  ('KillianGold', "Turn this plane around!", 1.0),
  f"A steady side-on medium close-up opens from the adopted first frame in {JET}: {KG} roars the order in a raw, thunderous voice, his mouth wide and his glowing gold eyes blazing, his claws digging into his chest; behind him the oval window at frame-right splits with a spreading spiderweb crack in the glass. The camera holds still.",
  "一个稳定的侧面中近景，从已采用的开场图继续，场景是私人飞机机舱：基利安用粗哑如雷的声音吼出命令，嘴张得很大，发光的金色眼睛怒火燃烧，爪子抠进胸口；他身后画面右边的椭圆舷窗里，玻璃裂开蛛网一样越扩越大的裂纹。镜头固定不动。",
  voiced("A thunderous roar and the sharp crack of splitting glass.", "雷鸣般的怒吼和玻璃裂开的一声脆响。"), dep=True)

T(b17, '07｜保镖抓起内线电话', 6, ['Bodyguard'], ('jet_cabin', 'bodyguard'), ['jet_cabin'],
  "Side-on medium shot of Bodyguard alone, from the head to the waist, in profile facing frame-left, in the middle third of the frame, standing in the aisle of the jet cabin, the cream leather seats at frame-right, the wall intercom handset beside the cabin door at frame-left, "
  "his right hand lifting the handset to his ear, his left hand braced on a seat back, his stern face gone pale, his lips parted, his brows pulled up, his wide eyes on the handset. The frame holds exactly one person, Bodyguard.",
  END_JET + LAY_JET, "保镖抓起内线电话，对机长大喊掉头。",
  ('Bodyguard', "Turn back now, Captain!", 1.0),
  f"A steady side-on medium shot opens from the adopted first frame in {JET}: {BGD} presses the intercom handset to his ear and shouts the order into it in a flat, urgent voice, his lips tight, his brows pulled up and his eyes wide on the handset; the cabin shudders around him. The camera holds still.",
  "一个稳定的侧面中景，从已采用的开场图继续，场景是私人飞机机舱：保镖把内线电话听筒按在耳边，用平板急促的声音对着话筒下令，嘴唇抿紧，眉头抬起，睁大眼睛盯着听筒；机舱在他周围发着抖。镜头固定不动。",
  voiced("A shuddering rattle of the cabin and the hum of engines.", "机舱发抖的格格声和发动机的嗡鸣。"))

# =================================================================================================== 第 18 集：暴君的回顾
# 观众要看懂：① 莉莉被拖到废弃仓库（在途）② 保罗和玛丽在那里等着 ③ 玛丽见血的得意 ④ 保罗羞辱、扬手
# ⑤ 铁门被炸飞（谁？）⑥ 在场的人各有反应（保罗和玛丽后退）⑦ 巨大黑狼走出来（金色眼睛对上飞机上那双）
# ⑧ 流浪狼人吓掉刀、叫出名字 ⑨ 莉莉认出他 ⑩ 咆哮扑出。

T(b18, '01｜狼人把莉莉拖向废弃仓库', 4, ['Rogue', 'LilyShirt'], ('garden_path', 'rogue', 'lily_shirt'), ['garden_path'],
  "Side-on wide-medium two-shot, both people from the head to the knees, in the middle third of the frame, on the gravel path between the tall dark hedges, both in profile facing frame-right, the rusted warehouse ahead at frame-right. "
  "Rogue at frame-left in the patched black leather jacket, his left hand gripping Lily's right upper arm and his right hand holding the silver dagger low at his side, his lips pulled into a cruel grin, his narrowed eyes on the warehouse door at frame-right. "
  "Lily at frame-right of him in the oversized white men's shirt, stumbling forward barefoot on the gravel, a thin line of blood down the left side of her neck, her chestnut hair tangled, her lips pressed together and trembling, her brows pulled up, her wet eyes on the gravel. "
  "The frame holds exactly two people: Rogue and Lily.",
  END_GP + LAY_GP, "流浪狼人拽着脖子在流血的莉莉，穿过后花园的小路，拖向仓库。",
  None,
  f"A steady side-on wide-medium two-shot opens from the adopted first frame in {GP}: {RG} drags her along the gravel path toward the warehouse door at frame-right, his lips curled into a cruel grin. {LS} stumbles barefoot over the stones, blood trickling down her neck, her lips trembling and her brows pulled up. The camera holds still.",
  "一个稳定的侧面宽中双人镜头，从已采用的开场图继续，场景是后花园的小路：流浪狼人拽着莉莉沿碎石路拖向画面右边的仓库门，残忍的笑容更大；她光着的脚在石子上踉跄，血顺着脖子淌下来，嘴唇发颤。镜头固定不动。",
  breathy("Boots and bare feet scuffing over gravel and a shaky breath.", "靴子和光脚在碎石上拖行的摩擦声，和一声发抖的呼吸。"))

T(b18, '02｜他把她推进仓库', 4, ['Rogue', 'LilyShirt'], ('warehouse', 'rogue', 'lily_shirt'), ['warehouse'],
  "Side-on wide-medium two-shot, both people from the head to the knees, in the middle third of the frame, inside the warehouse. "
  "Rogue at frame-right standing by the tall rusted iron double door in the patched black leather jacket, his right arm still extended from a shove, the silver dagger in his left hand, his lips pulled into a cruel grin, his narrowed eyes on Lily. "
  "Lily at frame-left in the oversized white men's shirt, stumbling forward barefoot onto the concrete floor, both hands reaching for the floor, a thin line of blood down the left side of her neck, her lips parted, her brows pulled up, her wide eyes on the concrete. "
  "The frame holds exactly two people: Rogue and Lily.",
  END_WH + LAY_WH, "流浪狼人把莉莉一把推进仓库，她摔倒在水泥地上。",
  None,
  f"A steady side-on wide-medium two-shot opens from the adopted first frame in {WH}: {LS} stumbles forward and drops onto her hands and knees on the concrete, her chestnut hair falling around her face, her lips parting and her brows pulling up. {RG} stands over her by the door, his lips curling into a cruel grin and his narrowed eyes on her. The camera holds still.",
  "一个稳定的侧面宽中双人镜头，从已采用的开场图继续，场景是废弃仓库：莉莉踉跄向前，双手双膝摔在水泥地上，栗色的头发垂在脸边，嘴唇张开，眉头抬起。流浪狼人站在门边俯视着她，残忍的笑容更大。镜头固定不动。",
  breathy("A hard thud of knees on concrete and a sharp gasp.", "膝盖重重磕在水泥地上的闷响，和一声急促的抽气。"))

T(b18, '03｜玛丽看见血，兴奋大笑', 6, ['MaryBlack', 'LilyShirt'], ('warehouse', 'mary_black', 'lily_shirt'), ['warehouse'],
  "Side-on medium two-shot, both people from the head to the knees, in the middle third of the frame, on the concrete floor of the warehouse. "
  "Mary at frame-left standing in the fitted black wool coat, her hands clasped at her chest, her lips parted in a gleeful laugh, her chin lifted, her sharp green eyes bright and wide on Lily's bleeding neck. "
  "Lily at frame-right kneeling on the concrete in the oversized white men's shirt, her left hand pressed to the bleeding side of her neck with blood between her fingers, her head bowed, her lips pressed tight, her brows pulled together, tears on her cheeks, her eyes on the floor. "
  "The frame holds exactly two people: Mary and Lily.",
  END_WH + LAY_WH, "玛丽看着莉莉脖子上的血，兴奋地笑着说：看那么多血！",
  ('MaryBlack', "Look at all that blood!", 1.0),
  f"A steady side-on medium two-shot opens from the adopted first frame in {WH}: {MB} at frame-left speaks in a gleeful, sugary voice, her lips curled into a delighted grin, her eyes bright on Lily's bleeding neck and her chin tilting up. {LS} at frame-right presses her hand harder against her neck, her head sinking lower, her lips trembling and tears running down her cheeks. The camera holds still.",
  "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是废弃仓库：画面左边的玛丽用兴奋甜腻的声音说话，眼睛亮亮地盯着莉莉流血的脖子，下巴抬起。画面右边的莉莉把手更用力地按在脖子上，头垂得更低，嘴唇发颤，眼泪顺着脸颊流下来。镜头固定不动。",
  voiced("A gleeful laugh echoing in the empty warehouse and a faint drip of water.", "空荡荡的仓库里回响的兴奋笑声，和细微的滴水声。"))

T(b18, '04｜保罗捏住她的脸羞辱她', 6, ['PaulOnScreen', 'LilyShirt'], ('warehouse', 'paul', 'lily_shirt'), ['warehouse'],
  "Side-on medium two-shot, both people from the head to the knees, in the middle third of the frame, on the concrete floor of the warehouse. "
  "Paul at frame-left standing in the dusty navy blazer, bending forward, his right hand gripping Lily's cheeks and chin, his lips pulled back from his teeth, his brows crashing together, his red-rimmed eyes on her face. "
  "Lily at frame-right kneeling in the oversized white men's shirt, her face lifted in his grip, her wet eyes on his face, her lips pressed tight and trembling, her brows pulled up, blood on the side of her neck. "
  "The frame holds exactly two people: Paul and Lily.",
  END_WH + LAY_WH, "保罗弯下腰狠狠捏住莉莉的脸，咬着牙嘲讽她。",
  ('PaulOnScreen', "Not so proud now, are you?", 1.0),
  f"A steady side-on medium two-shot opens from the adopted first frame in {WH}: {PL} at frame-left squeezes her face hard and spits the words in a furious, sneering voice, his lips pulled back from his bared teeth, his brows crashing together and his eyes burning on hers. {LS} at frame-right glares back at him, her wet eyes unflinching, her lips trembling and her brows pulling together. The camera holds still.",
  "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是废弃仓库：画面左边的保罗狠狠捏住她的脸，用暴怒带嘲讽的声音把话吐出来，龇着牙，眼睛喷火地盯着她。画面右边的莉莉湿润的眼睛毫不退缩地瞪回去，嘴唇发颤，眉头拧起。镜头固定不动。",
  voiced("A cold draft whistling through the empty warehouse.", "冷风吹过空荡荡的仓库的呼啸声。"))

T(b18, '05｜保罗扬起手要打下去', 3, ['PaulOnScreen', 'LilyShirt'], ('warehouse', 'paul', 'lily_shirt'), ['warehouse'],
  "Side-on medium two-shot, both people from the head to the knees, in the middle third of the frame, on the concrete floor of the warehouse. "
  "Paul at frame-left standing in the dusty navy blazer, his right arm drawn back with the open palm at shoulder height, his jaw clenched, his lips pulled back from his teeth, his red-rimmed eyes blazing on Lily's face. "
  "Lily at frame-right kneeling in the oversized white men's shirt, her face lifted, her eyes squeezed shut, her lips pressed tight, her brows pulled together, blood on the side of her neck. "
  "The frame holds exactly two people: Paul and Lily.",
  END_WH + LAY_WH, "保罗把手高高扬起，莉莉闭紧眼睛等着挨打。",
  None,
  f"A steady side-on medium two-shot opens from the adopted first frame in {WH}: {PL} swings his arm back and raises his open right hand high, his jaw clenched, his brows crashing together and his eyes blazing; {LS}'s eyes squeeze shut and her lips press tight as she braces. The camera holds still.",
  "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是废弃仓库：保罗把手臂往后一甩，张开的右手高高扬起，龇着牙，眼睛喷火；莉莉的眼睛紧紧闭上，嘴唇抿紧，咬牙等着。镜头固定不动。",
  breathy("A sharp intake of breath and the faint creak of the old building.", "一声急促的吸气和旧建筑细微的吱嘎声。"), dep=True)

T(b18, '06｜铁门被炸飞', 3, [], ('warehouse',), ['warehouse'],
  "Wide shot of the warehouse interior in the middle third of the frame: the tall rusted iron double door at frame-right closed, shafts of dusty pale light falling across the concrete floor, the stacked crates and steel barrels at frame-left, concrete pillars in the middle. No people are in the frame.",
  END_WH + LAY_WH, "一声巨响，仓库的铁门整扇炸飞进来，砸在地上，烟尘滚滚。",
  None,
  f"A steady wide shot opens from the adopted first frame in {WH}: with a tremendous boom the rusted iron double door bursts inward off its hinges and slams flat onto the concrete floor toward frame-left in a roaring cloud of dust and flying rust, the shafts of light turning thick with smoke. No people appear. The camera holds still.",
  "一个稳定的宽景，从已采用的开场图继续，场景是废弃仓库：随着一声巨响，生锈的铁双开门整扇从合页上炸开，朝画面左边重重拍在水泥地上，烟尘和锈屑滚滚而起，一束束光变得浓烟滚滚。画面里没有人出现。镜头固定不动。",
  breathy("A thunderous boom of tearing metal, a screech and a crash of iron on concrete.", "撕裂金属的一声雷鸣般的巨响、一阵刺耳的尖啸，和铁板砸在水泥地上的轰响。"))

T(b18, '07｜保罗和玛丽被吓得后退', 3, ['PaulOnScreen', 'MaryBlack'], ('warehouse', 'paul', 'mary_black'), ['warehouse'],
  "Side-on medium two-shot, both people from the head to the waist, in the middle third of the frame, standing side by side on the concrete floor, both in profile facing frame-right toward the dust at the doorway at frame-right. "
  "Paul at frame-left in the dusty navy blazer, his right arm still raised, his lips parted, his brows pulled up, his red-rimmed eyes wide on the dust cloud. "
  "Mary at frame-right in the fitted black wool coat, her hands rising to her mouth, her lips parted, her brows lifted, her sharp green eyes wide on the dust cloud. "
  "The frame holds exactly two people: Paul and Mary.",
  END_WH + LAY_WH, "保罗和玛丽被巨响吓得踉跄后退，一个举手挡脸，一个捂住嘴。",
  None,
  f"A steady side-on medium two-shot opens from the adopted first frame in {WH}: {PL} staggers back and flings his raised hand up to shield his face, his mouth falling open; {MB} stumbles back with her hands pressed to her mouth, her brows lifting and her eyes widening on the roiling dust. The camera holds still.",
  "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是废弃仓库：保罗踉跄后退，扬着的手一下举起来挡住脸，嘴巴张开；玛丽踉跄后退，双手捂住嘴，眉头扬起，眼睛看着翻滚的烟尘越睁越大。镜头固定不动。",
  breathy("Scraping shoes, a sharp gasp and settling dust.", "鞋底拖地的声音、一声急促的抽气和灰尘落定的声音。"))

T(b18, '08｜黑狼从烟尘里走出来', 4, [], ('warehouse', 'black_wolf'), ['warehouse'],
  "Wide shot, in the middle third of the frame, of a colossal jet-black wolf the size of a small horse standing in the doorway at frame-right in a thick cloud of dust, in profile facing frame-left, its thick black fur bristling, its dark-gold glowing eyes fixed on the concrete floor ahead of it at frame-left, "
  "its lips curled back from long white fangs; the broken iron door lies flat on the floor in front of it. The frame holds exactly one animal, the black wolf, and no people.",
  END_WH + LAY_WH, "一头巨大的纯黑狼从烟尘里慢慢走出来，眼睛是暗金色的。",
  None,
  f"A steady wide shot opens from the adopted first frame in {WH}: {WF} walks slowly out of the dust toward frame-left, its massive shoulders rolling, its claws clicking on the concrete and its dark-gold eyes blazing, its fangs bared as the dust swirls around its legs. No people appear. The camera holds still.",
  "一个稳定的宽景，从已采用的开场图继续，场景是废弃仓库：巨大的黑狼从尘土里朝画面左边慢慢走出来，厚重的肩膀一起一伏，爪子在水泥地上咔嗒作响，暗金色的眼睛喷着光，龇着獠牙，尘土在它的腿边打着旋。画面里没有人出现。镜头固定不动。",
  breathy("A deep rumbling growl and the slow click of claws on concrete.", "低沉的咆哮声和爪子慢慢敲在水泥地上的咔嗒声。"))

T(b18, '09｜流浪狼人吓得刀掉在地上', 6, ['Rogue'], ('warehouse', 'rogue', 'black_wolf'), ['warehouse'],
  "Side-on wide-medium shot, in the middle third of the frame, inside the warehouse. Rogue at frame-left standing in profile facing frame-right, in the patched black leather jacket, the silver dagger slipping from his shaking right hand, his knees buckling, his lips trembling, his brows pulled up, his eyes wide and fixed on the wolf's head. "
  "The colossal jet-black wolf at frame-right in profile facing frame-left, its head lowered, its dark-gold eyes blazing at Rogue, its fangs bared, in a haze of dust. The frame holds exactly one person, Rogue, and one huge black wolf.",
  END_WH + LAY_WH, "流浪狼人吓得匕首脱手，腿一软，哆嗦着问：你怎么来得这么快？",
  ('Rogue', "How did you get here, Killian?", 1.0),
  f"A steady side-on wide-medium shot opens from the adopted first frame in {WH}: {RG}'s trembling hand opens and the silver dagger clatters to the concrete; his knees buckle as he stammers in a cracking, terrified voice, his lips trembling and his eyes wide on the gold eyes of {WF}. The wolf takes one slow step closer, growling. The camera holds still.",
  "一个稳定的侧面宽中景，从已采用的开场图继续，场景是废弃仓库：流浪狼人发抖的手一松，银匕首哐啷掉在水泥地上；他双腿发软，用发颤、惊恐的声音结结巴巴地说话，嘴唇哆嗦，睁大的眼睛盯着黑狼的金色眼睛。黑狼往前慢慢逼近一步，低低地咆哮。镜头固定不动。",
  voiced("The ring of a dagger on concrete and a low rumbling growl.", "匕首掉在水泥地上的一声脆响和低沉的咆哮声。"))

T(b18, '10｜莉莉认出了那双金色的眼睛', 6, ['LilyShirt'], ('warehouse', 'lily_shirt', 'black_wolf'), ['warehouse'],
  "Side-on wide-medium shot, in the middle third of the frame, inside the warehouse. Lily at frame-left kneeling on the concrete in the oversized white men's shirt, her left hand pressed to her bleeding neck, her face lifted, her lips parted, her brows pulled up, her tear-streaked wide eyes fixed on the wolf's gold eyes. "
  "The colossal jet-black wolf at frame-right in profile facing frame-left, standing over the fallen iron door, its head lowered, its dark-gold eyes blazing. The frame holds exactly one person, Lily, and one huge black wolf.",
  END_WH + LAY_WH, "莉莉跪在地上，捂着流血的脖子，认出了那双金色的眼睛，轻声问：是你吗？",
  ('LilyShirt', "Is that you, Killian?", 1.0),
  f"A steady side-on wide-medium shot opens from the adopted first frame in {WH}: {LS} whispers in a trembling voice, her wide wet eyes locked on the gold eyes of {WF} and her lips trembling; the wolf's fierce gaze softens for an instant as it looks at her, its growl dying away. The camera holds still.",
  "一个稳定的侧面宽中景，从已采用的开场图继续，场景是废弃仓库：莉莉用发颤的声音轻轻地问，湿润睁大的眼睛直直盯着黑狼的金色眼睛，嘴唇发颤；黑狼凶狠的目光在看着她的那一瞬软了一下，低吼声渐渐消去。镜头固定不动。",
  voiced("A low fading growl and a shaky breath.", "渐渐低下去的咆哮声和一声发抖的呼吸。"))

T(b18, '11｜黑狼咆哮着扑出去', 3, [], ('warehouse', 'black_wolf'), ['warehouse'],
  "Side-on close-up of the colossal jet-black wolf's head and shoulders, in profile facing frame-left, in the middle third of the frame, in a haze of dust, its dark-gold eyes blazing, its upper lip curled back from long white fangs, its thick black fur bristling. The frame holds exactly one animal, the black wolf, and no people.",
  END_WH + LAY_WH, "黑狼仰头一声震天的咆哮，然后猛地向左扑了出去。",
  None,
  f"A steady side-on close-up opens from the adopted first frame in {WH}: {WF} throws its head back and unleashes a thunderous roar with its jaws stretched wide, then lunges forward toward frame-left in one violent leap, the dust blasting outward. No people appear. The camera holds still.",
  "一个稳定的侧面特写，从已采用的开场图继续，场景是废弃仓库：黑狼仰起头，张大嘴发出一声雷鸣般的咆哮，然后猛地向画面左边一跃而出，尘土向四周炸开。画面里没有人出现。镜头固定不动。",
  breathy("A thunderous roar that shakes the walls and a heavy impact.", "震得墙壁发抖的雷鸣般的咆哮，和一声沉重的撞击。"))

# =================================================================================================== 合成一份
doc = copy.deepcopy(b15.d)
doc['episodes'] = [
    episode(b15, '剧本第15集｜背叛的暗网（场景级改编）', '破产的保罗发疯，玛丽带着伤疤猎手来，照片证明基利安不是人，计划：他一走就抓莉莉。'),
    episode(b16, '剧本第16集｜印记与离别（场景级改编）', '清晨主卧颈后的新月印记，基利安交代去欧洲、禁止她出门、求婚，车队离开，树枝断裂，黑影爬墙。'),
    episode(b17, '剧本第17集｜银刃之下（场景级改编）', '猎手翻上阳台抓住莉莉，银匕首划破脖子；飞机上的基利安心口剧痛、眼睛变金、怒吼掉头。'),
    episode(b18, '剧本第18集｜暴君的回顾（场景级改编）', '莉莉被拖进仓库，保罗扬手要打，铁门炸飞，巨大黑狼走出来，咆哮扑出。'),
]
txt = json.dumps(doc, ensure_ascii=False, indent=1)
open(os.path.join(FOLDER, OUT + '.json'), 'w', encoding='utf-8').write(txt)
open(os.path.join(FOLDER, OUT + '_全选复制粘贴.txt'), 'w', encoding='utf-8').write(txt)
n = sum(len(e['segments']) for e in doc['episodes']); sec = sum(s['duration_seconds'] for e in doc['episodes'] for s in e['segments'])
print(f'{len(doc["episodes"])} 集、{n} 个任务、约 {sec} 秒；文件 {len(txt.encode())/1024:.0f} KB → {OUT}')
for e in doc['episodes']:
    print('  ', e['title'], len(e['segments']), '个任务', sum(s['duration_seconds'] for s in e['segments']), '秒')
