#!/usr/bin/env python3
"""剧本第 15–18 集（背叛的暗网／印记与离别／银刃之下／暴君的回顾）重写版（2026-10-11，合并稿编号 002）。

001 版的问题（hh 11:04 指出）：照着大纲逐个镜头还原，只在缝里补几句，故事本身没补实。
这一版先把“观众要看懂什么”想完整，再拆镜头。大纲缺口和补法：
  ① 照片证明基利安不是人 → 删。保罗自己被他单手掐着提起来过（脖子上有淤青），真正缺的是“谁能对付他”
  ② 猎手是谁、凭什么能伤基利安 → 银匕首（银会让怪物流血）＋毒液特写，第 17、20 集的银毒靠它
  ③ 怎么知道他哪天走、抓到人带去哪 → 内线说“他今天走”；猎手说“带去仓库”＋仓库外景提前露一面
  ④ 刚标记完为什么走 → 长老威胁她；他去收拾，是为了保护她
  ⑤ 飞机上的心痛没有铺垫 → 16 集他说“现在我永远感觉得到你”；17 集先拍她后颈印记发金光，再拍他心口痛
  ⑥ 万米高空怎么这么快到 → 飞机改成刚开出山庄不远的车队；他撕掉车门自己先跑，黑狼出场和猎手“怎么这么快”对得上
  ⑦ 保罗为什么扇她 → 他吼“你选了那个怪物，不选我”
15：10 个任务；16：12；17：8；18：12。合计 42 个任务。
方向统一：阳台上莉莉面朝右看车队，树枝声在左边；猎手从左边花园爬上来；仓库门在右边，狼从右边走出来朝左。
素材／人物／style 以第 11–14 集合并稿为底逐字复制，新增 5 个场景（保罗客厅、阳台、花园小路、仓库、车内）＋流浪狼人＋黑玛丽＋黑狼。
种子 6501–6812（和库里所有稿子不重复）。
"""
import copy, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _h3draft import Batch, FOLDER, breathy, voiced

BASE = '合并稿/旧合并稿/合并_第11-14集+B_制作稿_追加.json'
OUT = '合并稿/002_第15-18集_重写故事_制作稿_追加'
SRC = json.load(open(os.path.join(FOLDER, BASE), encoding='utf-8'))

b15, b16, b17, b18 = (Batch(BASE, SRC['title'], s) for s in (6500, 6600, 6700, 6800))

PV = '[[asset:paul_villa]]'; BAL = '[[asset:villa_balcony]]'; GP = '[[asset:garden_path]]'; WH = '[[asset:warehouse]]'
SUV = '[[asset:suv_interior]]'; BD = '[[asset:bedroom]]'
PL = '[[asset:paul]]'; MB = '[[asset:mary_black]]'; RG = '[[asset:rogue]]'; LS = '[[asset:lily_shirt]]'
K = '[[asset:killian]]'; KG = '[[asset:killian_gold]]'; BGD = '[[asset:bodyguard]]'; WF = '[[asset:black_wolf]]'

# ------------------------------------------------------------------------------------------------ 新素材（只加到 b15，最后用 b15 的 assets）
b15.scene('paul_villa', '保罗破败的客厅',
          "The wrecked living room of a bankrupt hillside villa at dawn: a tall bay window with torn curtains and cold pale light at the left, an overturned brown leather sofa and the shards of a smashed glass coffee table in the middle, a wide double doorway into a dim hallway at the right, a smashed wooden cabinet against the back wall with bare walls above it showing pale rectangles where paintings once hung, torn papers and broken glass scattered over a dark wooden floor. The reference fixes the layout and decor.",
          "清晨，一栋破产山间别墅里被砸烂的客厅：左边是挂着破窗帘的高大飘窗和冷冷的淡光，中间是翻倒的棕色皮沙发和摔碎的玻璃茶几，右边是通向昏暗走廊的宽双开门，后墙边是被砸坏的木柜，柜子上方的光墙上留着一块块挂画取走后的浅色方痕，深色木地板上撒满碎纸和碎玻璃。参考图固定布局与陈设。",
          "A photorealistic ultra-wide 8:3 cinemascope shot of the wrecked living room of a bankrupt hillside villa at dawn: a tall bay window with torn curtains and cold pale light at the left, an overturned brown leather sofa and the shards of a smashed glass coffee table in the middle, a wide double doorway into a dim hallway at the right, a smashed wooden cabinet against the back wall with bare walls above it showing pale rectangles where paintings once hung, torn papers and broken glass over a dark wooden floor. "
          "The frame holds the window, the sofa, the table shards, the doorway and the cabinet.")
b15.scene('villa_balcony', '别墅二楼阳台（清晨）',
          "The second-floor stone balcony of a dark luxurious hillside mansion on a clear morning: a carved stone balustrade runs along the front; below at the right a gravel driveway leads to tall black iron gates; at the left in the distance a hedge-lined back garden and the rusted corrugated-iron roof of an old warehouse; behind it the dark stone wall and tall glass doors. The reference fixes the layout and decor.",
          "晴朗的清晨，阴沉豪华的山间庄园二楼石质阳台：前面是雕花石栏杆；右下方一条碎石车道通向高大的黑色铁门；左边远处是篱笆围起来的后花园和一座废弃仓库生锈的铁皮屋顶；身后是深色石墙和高大的玻璃门。参考图固定布局与陈设。",
          "A photorealistic ultra-wide 8:3 cinemascope shot of the second-floor stone balcony of a dark luxurious hillside mansion on a clear morning: a carved stone balustrade runs along the front, a gravel driveway at the lower right leads to tall black iron gates, a hedge-lined back garden and the rusted corrugated-iron roof of an old warehouse in the distance at the left, the dark stone wall and tall glass doors behind. "
          "The frame holds the balustrade, the driveway, the gates, the garden and the warehouse roof.")
b15.scene('garden_path', '后花园的碎石小路',
          "A hedge-lined gravel path in the overgrown back garden of a dark mansion on a clear morning: tall dark hedges on both sides, the path running from left to right, at the right a derelict rusted corrugated-iron warehouse with a tall rusted iron double door, the mansion's dark stone wall far behind at the left, long soft shadows. The reference fixes the layout and decor.",
          "晴朗的清晨，阴沉庄园荒芜的后花园里一条两边是高大深色篱笆的碎石小路：路从左往右延伸，右边是一座废弃、生锈的铁皮仓库和一扇高大生锈的铁双开门，左边远处是庄园深色的石墙，影子又长又柔。参考图固定布局与陈设。",
          "A photorealistic ultra-wide 8:3 cinemascope shot of a hedge-lined gravel path in the overgrown back garden of a dark mansion on a clear morning: tall dark hedges on both sides, the path running from left to right, a derelict rusted corrugated-iron warehouse with a tall rusted iron double door at the right, the mansion's dark stone wall far behind at the left, long soft shadows. "
          "The frame holds the hedges, the path, the warehouse and the far wall.")
b15.scene('warehouse', '废弃仓库内部',
          "The interior of a derelict warehouse: a grey concrete floor, a tall rusted iron double door at the right, stacked wooden crates and steel barrels at the left, concrete pillars in the middle, and shafts of dusty pale light falling from high broken windows at the back. The reference fixes the layout and decor.",
          "一间废弃仓库的内部：灰色水泥地面，右边是一扇高大生锈的铁双开门，左边堆着木箱和铁桶，中间立着水泥柱，后面高处破窗里落下一束束带灰尘的淡光。参考图固定布局与陈设。",
          "A photorealistic ultra-wide 8:3 cinemascope shot of the interior of a derelict warehouse: a grey concrete floor, a tall rusted iron double door at the right, stacked wooden crates and steel barrels at the left, concrete pillars in the middle, shafts of dusty pale light falling from high broken windows at the back. "
          "The frame holds the door, the crates, the pillars and the light shafts.")
b15.scene('suv_interior', '黑色SUV车内（白天）',
          "The interior of a black luxury SUV driving along a pine-lined mountain road in clear daylight, seen from the side: two black leather front seats at the left, a cream leather rear bench at the right, a large side window behind the rear bench showing dark pine trees and a winding grey road, soft daylight on the dark wood trim. The reference fixes the layout and decor.",
          "晴朗白天，一辆黑色豪华SUV行驶在两边是松树的山路上，从侧面看车内：左边是两个黑色真皮前座，右边是奶油色真皮后排座椅，后排座椅后面是一整扇侧窗，窗外是深色松树和蜿蜒的灰色公路，柔和的日光落在深色木饰板上。参考图固定布局与陈设。",
          "A photorealistic ultra-wide 8:3 cinemascope shot of the interior of a black luxury SUV driving along a pine-lined mountain road in clear daylight, seen from the side: two black leather front seats at the left, a cream leather rear bench at the right, a large side window behind the rear bench showing dark pine trees and a winding grey road, soft daylight on the dark wood trim. "
          "The frame holds the front seats, the rear bench and the side window.")
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
LAY_PV = " Fixed stage layout: the tall bay window with torn curtains and cold pale dawn light is at frame-left; the overturned leather sofa and the shards of the smashed coffee table are in the middle; the wide double doorway to a dim hallway is at frame-right; the smashed wooden cabinet stands against the back wall under bare walls with pale rectangles where paintings once hung."
END_PV = " Cold pale dawn light, dust hanging in the air, the wrecked room softly blurred behind."
LAY_BD = " Fixed stage layout: the huge dark-wood bed with charcoal-grey linen fills the left and center of the frame; the tall dark-wood door with a brass handle is at frame-right; the floor-to-ceiling windows with the heavy curtains drawn back are at the back."
END_BD = " Bright warm morning sunlight pours through the open curtains across the bed, soft golden light, the room softly blurred behind."
LAY_BAL = " Fixed stage layout: the carved stone balustrade runs along the front of the balcony; the gravel driveway and the tall black iron gates are at frame-right below; the hedge-lined back garden and the rusted warehouse roof are at frame-left in the distance; the dark stone wall and tall glass doors are behind."
END_BAL = " Soft clear morning sunlight, a pale blue sky, the garden softly blurred in the distance."
LAY_GP = " Fixed stage layout: the gravel path runs from frame-left to frame-right between tall dark hedges; the rusted corrugated-iron warehouse with its tall rusted iron double door stands at frame-right; the mansion's dark stone wall is far behind at frame-left."
END_GP = " Soft clear morning light, long shadows across the gravel."
LAY_WH = " Fixed stage layout: the tall rusted iron double door is at frame-right; the stacked wooden crates and steel barrels are at frame-left; concrete pillars stand in the middle and shafts of dusty light fall from the high windows at the back."
END_WH = " Dim, dusty light with pale shafts from the high windows, the warehouse softly blurred behind."
LAY_SUV = " Fixed stage layout: the two black leather front seats are at frame-left; the cream leather rear bench is at frame-right; the large side window behind the rear bench shows dark pine trees and a winding grey road."
END_SUV = " Soft clear daylight through the windows, the pine forest softly blurred outside."


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


# =================================================================================================== 第 15 集：反派的计划
# 观众要看懂（一环扣一环，后一句回答前一句的疑问）：
#   保罗输光了（公司、未婚妻）→ 玛丽带来一个陌生人 → “能对付他的人？”保罗怕（脖子上有被掐的淤青，呼应第 10 集）
#   → 猎手回答：银（附毒液特写）→ “什么时候动手？”内线说他今天走 → “去哪里？”仓库（先露一次外景）→ 玛丽自己要什么：毁了她的脸
# 在场名单：保罗、玛丽、流浪狼人（猎手）。同一镜头最多 2 人；猎手单独出现 3 次，玛丽单独出现 2 次。

T(b15, '01｜保罗坐在被搬空的家里，攥着订婚戒指', 6, ['PaulOnScreen'], ('paul_villa', 'paul'), ['paul_villa'],
  "Side-on medium shot of Paul alone, from the head to the waist, in profile facing frame-right, in the middle third of the frame, sitting on the dusty floor with his back against the overturned leather sofa, in the creased navy blazer over a white open-collared shirt, a dark purple bruise ringing his throat above the open collar, "
  "his right fist clenched around a small diamond ring held at chest height, his jaw trembling, his lips pulled tight, his brows drawn together, his red-rimmed wet eyes on the ring. The frame holds exactly one person, Paul.",
  END_PV + LAY_PV, "保罗坐在被搬空的家里，脖子上有淤青，手里攥着订婚戒指，哽着嗓子说：他把我的一切都抢走了。",
  ('PaulOnScreen', "He took everything from me!", 1.0),
  f"A steady side-on medium shot opens from the adopted first frame in {PV}: {PL} speaks in a hoarse, cracking voice, squeezing the diamond ring until his knuckles whiten, his jaw trembling, his lips pulled tight, his brows drawn together and a tear sliding from his red-rimmed eyes. The camera holds still.",
  "一个稳定的侧面中景，从已采用的开场图继续，场景是破败的客厅：保罗用嘶哑发裂的声音说话，把钻戒攥得指节发白，下颌发抖，嘴唇紧抿，眉头拧在一起，一滴泪从发红的眼睛里滑下来。镜头固定不动。",
  voiced("A rattling breath and the faint creak of the old floor.", "一声发颤的喘息和旧地板细微的吱嘎声。"))

T(b15, '02｜玛丽带着满脸伤疤的陌生人走进来', 4, ['MaryBlack', 'Rogue'], ('paul_villa', 'mary_black', 'rogue'), ['paul_villa'],
  "Side-on medium two-shot, both people from the head to the knees, in the middle third of the frame, just inside the doorway of the wrecked living room, both in profile facing frame-left. "
  "Mary in front at frame-left in a fitted black wool coat over a black dress and black high heels, her honey-blonde hair in a tight low bun, her chin lifted, her lips set in a cold smug smile, her sharp green eyes sweeping over the overturned sofa. "
  "Rogue one step behind her at frame-right, a lean wiry man in a patched black leather jacket, a thick jagged scar down his left cheek and across his eye, his heavy brows lowered, his lips pulled into a cruel half-grin over yellowed teeth, his right hand resting on a sheathed silver dagger at his belt, his narrowed eyes on the shards of the coffee table at frame-left. "
  "The frame holds exactly two people: Mary and Rogue.",
  END_PV + LAY_PV, "玛丽踩着高跟鞋走进来，身后跟着一个满脸伤疤、手按匕首的陌生男人。",
  None,
  f"A steady side-on medium two-shot opens from the adopted first frame in {PV}: {MB} walks slowly across the wreckage, her heels crunching on broken glass, her chin lifted and her cold smug smile widening. "
  f"{RG} follows one step behind, his right hand tapping the hilt of the sheathed dagger, his lips curling into a cruel half-grin over his yellowed teeth and his heavy brows low. The camera holds still.",
  "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是破败的客厅：玛丽缓缓走过一地狼藉，高跟鞋踩在碎玻璃上咯吱作响，下巴抬起，冷冷的得意笑容更深。流浪狼人跟在她身后一步，右手轻轻敲着鞘里匕首的柄，咧开的残忍笑容露出发黄的牙，眉头压得很低。镜头固定不动。",
  breathy("High heels crunching over broken glass and slow, heavy boot steps.", "高跟鞋踩过碎玻璃的咯吱声和缓慢沉重的靴子声。"))

T(b15, '03｜玛丽：我找到能对付他的人了', 6, ['MaryBlack', 'PaulOnScreen'], ('paul_villa', 'mary_black', 'paul'), ['paul_villa'],
  "Side-on medium two-shot, both people from the head to the waist, in the middle third of the frame, in the middle of the wrecked living room. "
  "Paul at frame-left sitting on the floor against the overturned sofa, in profile facing frame-right, the dark purple bruise around his throat, his face lifted, his lips parted, his brows drawn together, his wet red-rimmed eyes on Mary's face. "
  "Mary at frame-right standing over him in the fitted black wool coat, in profile facing frame-left, her chin lifted, her lips set in a cold smug smile, her sharp green eyes on Paul's face. "
  "The frame holds exactly two people: Paul and Mary.",
  END_PV + LAY_PV, "玛丽站在坐在地上的保罗面前，说她找到了能对付基利安的人。",
  ('MaryBlack', "I found someone to stop him.", 1.0),
  f"A steady side-on medium two-shot opens from the adopted first frame in {PV}: {MB} at frame-right speaks in a low, silky voice, her cold smug smile widening and her green eyes on his face. "
  f"{PL} at frame-left looks up at her, his lips parting, his brows drawing together and a flicker of hope in his wet red-rimmed eyes. The camera holds still.",
  "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是破败的客厅：画面右边的玛丽用低沉丝滑的声音说话，冷冷的得意笑容更深，绿色的眼睛看着他的脸。画面左边的保罗抬头看着她，嘴唇张开，眉头拧起，发红湿润的眼睛里闪过一丝希望。镜头固定不动。",
  voiced("A faint creak of floorboards and a light breeze through the broken window.", "地板轻轻的吱嘎声，和破窗里吹进来的微风。"))

T(b15, '04｜保罗摸着脖子上的淤青：没人能对付那个怪物', 6, ['PaulOnScreen'], ('paul_villa', 'paul'), ['paul_villa'],
  "Side-on medium close-up of Paul alone, from the head to the chest, in profile facing frame-right, in the middle third of the frame, sitting against the overturned leather sofa in the creased navy blazer over a white open-collared shirt, the dark purple bruise ringing his throat clearly visible, "
  "his right hand rising to his bruised throat, his lips trembling, his brows pulled up, his wide wet eyes fixed on the dusty floor. The frame holds exactly one person, Paul.",
  END_PV + LAY_PV, "保罗摸着脖子上的淤青，摇着头说：没人能对付那个怪物。",
  ('PaulOnScreen', "Nobody can stop that monster.", 1.0),
  f"A steady side-on medium close-up opens from the adopted first frame in {PV}: {PL} shakes his head slowly and speaks in a thin, shaking voice, his fingers rubbing the purple bruise at his throat, his lips trembling, his brows pulled up and his wide wet eyes on the floor. The camera holds still.",
  "一个稳定的侧面中近景，从已采用的开场图继续，场景是破败的客厅：保罗慢慢摇着头，用单薄发抖的声音说话，手指揉着脖子上的紫色淤青，嘴唇发颤，眉头抬起，睁大的湿润眼睛盯着地板。镜头固定不动。",
  voiced("A shaky breath and a faint creak of the floorboards.", "一声发抖的呼吸和地板细微的吱嘎声。"))

T(b15, '05｜流浪狼人拔出银匕首：银会让怪物流血', 6, ['Rogue'], ('paul_villa', 'rogue'), ['paul_villa'],
  "Medium close-up of Rogue alone, from the head to the chest, in profile facing frame-left, in the middle third of the frame, in the patched black leather jacket, the long scar down his left cheek and across his eye, "
  "his right hand drawing a silver dagger halfway out of its black leather sheath at his belt so that the polished blade catches the pale light, his heavy brows lowered, his lips curling into a cruel grin over yellowed teeth, his narrowed eyes on the blade. The frame holds exactly one person, Rogue.",
  END_PV + LAY_PV, "流浪狼人把银匕首从鞘里慢慢拔出来，说银会让怪物流血。",
  ('Rogue', "Silver makes monsters bleed.", 1.0),
  f"A steady medium close-up opens from the adopted first frame in {PV}: {RG} slides the silver dagger slowly out of its sheath and speaks in a low, wheezing, sly voice, the blade flashing in the pale light, his lips curling into a cruel grin over his yellowed teeth, his heavy brows low and his narrowed eyes on the blade. The camera holds still.",
  "一个稳定的中近景，从已采用的开场图继续，场景是破败的客厅：流浪狼人把银匕首慢慢从鞘里抽出来，用低沉、带喘息的狡猾声音说话，刀刃在淡光里一闪，他咧开残忍的笑露出发黄的牙，眉头压得很低，眯着的眼睛盯着刀刃。镜头固定不动。",
  voiced("The thin ring of steel leaving a sheath and a wheezing breath.", "钢刃出鞘细细的一声金属声，和一声嘶哑的喘息。"))

T(b15, '06｜特写：匕首刃上滴下一滴绿色毒液', 3, [], ('paul_villa',), ['paul_villa'],
  "Close-up of a black-gloved hand in a patched black leather sleeve holding a silver dagger upright, point up, in the middle third of the frame, the polished blade in sharp focus with a bead of pale green venom swelling at its edge near the tip, the dusty living room floor softly blurred far below. Only the hand and forearm are in the frame; no face appears.",
  " Cold pale dawn light, dust drifting in the air.", "特写：一只戴黑手套的手握着银匕首，刃口上一滴淡绿色的毒液正在鼓起来。",
  None,
  f"A steady close-up opens from the adopted first frame in {PV}: the bead of pale green venom swells, slides slowly down the polished edge of the silver dagger and drips toward the dusty floor, leaving a faint hissing wisp of smoke behind it; the black-gloved fingers tighten once on the hilt. No face appears. The camera holds still.",
  "一个稳定的特写，从已采用的开场图继续，场景是破败的客厅：淡绿色的毒液珠越鼓越大，慢慢顺着银匕首打磨光亮的刃口滑下，朝积灰的地板滴落，身后留下一缕细细的嘶嘶作响的烟；戴黑手套的手指在刀柄上握紧了一下。画面里没有脸出现。镜头固定不动。",
  breathy("A faint hiss like acid dripping and the creak of leather.", "一声像酸液滴落的细微嘶声和皮革的吱嘎声。"))

T(b15, '07｜玛丽看着手机：我的内线说他今天就走', 6, ['MaryBlack'], ('paul_villa', 'mary_black'), ['paul_villa'],
  "Medium close-up of Mary alone, from the head to the waist, in profile facing frame-left, in the middle third of the frame, in the fitted black wool coat, a smartphone with a softly glowing screen held in her left hand at chest height, "
  "her red lips set in a cold smug smile, her jaw relaxed, her sharp green eyes narrowed on the phone screen. The frame holds exactly one person, Mary.",
  END_PV + LAY_PV, "玛丽看着手机屏幕，说她的内线报信，基利安今天就走。",
  ('MaryBlack', "My spy says he leaves today.", 1.0),
  f"A steady medium close-up opens from the adopted first frame in {PV}: {MB} lifts the glowing phone a little higher and speaks in a low, silky voice, her cold smug smile widening, her jaw relaxed and her narrowed green eyes on the screen. The camera holds still.",
  "一个稳定的中近景，从已采用的开场图继续，场景是破败的客厅：玛丽把发亮的手机举高了一点，用低沉丝滑的声音说话，冷冷的得意笑容更深，下颌放松，眯起的绿眼睛盯着屏幕。镜头固定不动。",
  voiced("A soft electronic chime and a faint creak of the floorboards.", "一声轻轻的电子提示音和地板细微的吱嘎声。"))

T(b15, '08｜流浪狼人收刀：我把她带去仓库', 6, ['Rogue'], ('paul_villa', 'rogue'), ['paul_villa'],
  "Medium close-up of Rogue alone, from the head to the chest, in profile facing frame-left, in the middle third of the frame, in the patched black leather jacket, the long scar down his left cheek and across his eye, "
  "the silver dagger held low in his right hand with its point resting against his open left palm, his heavy brows lowered, his lips pulled into a cruel grin over yellowed teeth, his narrowed eyes on the dagger. The frame holds exactly one person, Rogue.",
  END_PV + LAY_PV, "流浪狼人把匕首插回鞘里，说他会把她带去仓库。",
  ('Rogue', "I'll bring her to the warehouse.", 1.0),
  f"A steady medium close-up opens from the adopted first frame in {PV}: {RG} slides the dagger back into its sheath with a sharp click and speaks in a low, wheezing, sly voice, his lips curling into a cruel grin over his yellowed teeth, his heavy brows low and his narrowed eyes on the sheath. The camera holds still.",
  "一个稳定的中近景，从已采用的开场图继续，场景是破败的客厅：流浪狼人“咔”的一声把匕首插回鞘里，用低沉、带喘息的狡猾声音说话，咧开残忍的笑露出发黄的牙，眉头压得很低，眯着的眼睛盯着刀鞘。镜头固定不动。",
  voiced("A sharp metallic click and a wheezing breath.", "一声清脆的金属咔嗒声和一声嘶哑的喘息。"))

T(b15, '09｜后花园的小路和废弃仓库', 3, [], ('garden_path',), ['garden_path'],
  "Wide shot of the hedge-lined gravel path in the overgrown back garden, in the middle third of the frame: the rusted corrugated-iron warehouse with its tall rusted iron double door closed at frame-right, tall dark hedges on both sides, the mansion's dark stone wall far behind at frame-left, the gravel empty. No people are in the frame.",
  END_GP + LAY_GP, "后花园里一条空荡荡的碎石小路，尽头是锈迹斑斑的废弃仓库。",
  None,
  f"A steady wide shot opens from the adopted first frame in {GP}: a faint breeze stirs the dark hedges and dry leaves drift slowly across the empty gravel toward the closed iron double door of the warehouse at frame-right. No people appear. The camera holds still.",
  "一个稳定的宽景，从已采用的开场图继续，场景是后花园的小路：一阵微风吹动深色的篱笆，干枯的落叶慢慢飘过空荡荡的碎石路，飘向画面右边仓库紧闭的铁双开门。画面里没有人出现。镜头固定不动。",
  breathy("A low wind through dry hedges and a distant creak of rusted metal.", "穿过干枯篱笆的低低风声和远处生锈金属的吱嘎声。"))

T(b15, '10｜玛丽：我还要毁了她那张漂亮的脸', 6, ['MaryBlack'], ('paul_villa', 'mary_black'), ['paul_villa'],
  "Medium close-up of Mary alone, from the head to the waist, in profile facing frame-left, in the middle third of the frame, in the fitted black wool coat, the smartphone lowered in her left hand, her red-lacquered right fingertips resting against her own cheek, "
  "her lips set in a thin cold smug smile, her jaw tight, her sharp green eyes narrowed. The frame holds exactly one person, Mary.",
  END_PV + LAY_PV, "玛丽用甜得发毒的声音说，她还要毁了莉莉那张漂亮的脸。",
  ('MaryBlack', "And I'll ruin her pretty face.", 1.0),
  f"A steady medium close-up opens from the adopted first frame in {PV}: {MB} speaks in a sugary, venomous voice, her red-lacquered fingertips tapping slowly against her own cheek, her thin cold smug smile widening, her jaw tight and her sharp green eyes narrowed. The camera holds still.",
  "一个稳定的中近景，从已采用的开场图继续，场景是破败的客厅：玛丽用甜得发毒的声音说话，涂着红指甲的指尖在自己的脸颊上慢慢敲着，薄薄的冷冷得意的笑容越扩越大，下颌绷紧，绿色的眼睛眯着。镜头固定不动。",
  voiced("A slow tap of fingernails and a faint creak of the floorboards.", "指甲慢慢敲击的轻响和地板细微的吱嘎声。"))

# =================================================================================================== 第 16 集：印记和离别
# 观众要看懂：清晨 → 她后颈有了印记（给 17 集的“感应”提前埋线）→ 她问“你对我做了什么” → 他答：“现在我永远感觉得到你”
# → 他为什么要走（长老威胁她）→ 她怕被留下 → 禁令 → 额头吻 → 求婚 → 车队开出铁门（她一个人了）
# → 树枝咔嚓（猎手在花园里踩断）→ 她猛地转头（变灵敏的耳朵）→ 黑影爬墙。
CL16 = ("Side-on medium close-up two-shot, both people from the head to the chest, in the middle third of the frame. "
        "Killian at frame-left in profile facing frame-right, in the tailored black three-piece suit, white shirt and dark tie, sitting on the edge of the bed, {K}. "
        "Lily at frame-right on the bed propped on her left forearm, her face turned toward him in profile facing frame-left, in the oversized white shirt, her chestnut hair swept forward over her left shoulder, {L}. "
        "The frame holds exactly two people: Killian and Lily.")

T(b16, '01｜清晨，她颈后的新月印记', 3, ['LilyShirt'], ('bedroom', 'lily_shirt'), ['bedroom'],
  "Close-up from slightly above and from the side of Lily's head, neck and shoulders as she lies on her stomach, her face turned toward frame-right on the pillow, her long chestnut hair swept forward over her left shoulder so that the back of her neck is bare, the collar of the oversized white shirt low on her shoulders; "
  "on the center of her bare nape, in the middle third of the frame, a dark-red crescent-moon mark in an ornate, tattoo-like pattern, the skin around it slightly flushed. Her eyes are closed, her lips softly parted, her brows relaxed. The frame holds exactly one person, Lily.",
  END_BD + LAY_BD, "清晨的阳光里，莉莉趴着睡，颈后有一枚暗红色、像图腾一样的新月印记。",
  None,
  f"A steady close-up opens from the adopted first frame in {BD}: the dark-red crescent mark on {LS}'s nape gleams in the warm sunlight as her slow breath lifts her shoulders, a loose strand of chestnut hair sliding across her cheek, her lips softly parted and her brows relaxed. The camera holds still.",
  "一个稳定的特写，从已采用的开场图继续，场景是主卧：莉莉颈后的暗红色新月印记在暖暖的阳光里发亮，她缓慢的呼吸让肩膀轻轻起伏，一缕散落的栗色头发滑过脸颊，嘴唇轻轻张开，眉头舒展。镜头固定不动。",
  breathy("Soft birdsong outside and the quiet rustle of linen.", "窗外轻轻的鸟叫声和亚麻床单的轻响。"))

T(b16, '02｜莉莉醒来摸到印记：你对我做了什么？', 6, ['Killian', 'LilyShirt'], ('bedroom', 'killian', 'lily_shirt'), ['bedroom'],
  CL16.format(K="his eyes on her face, his lips set, his jaw relaxed, his brows level",
              L="her right hand pressed to the back of her neck, her glossy wide eyes on his face, her lips trembling, her brows pulled up"),
  END_BD + LAY_BD, "莉莉醒来，一手按着颈后的印记，惊慌地问坐在床边的基利安：你对我做了什么？",
  ('LilyShirt', "What did you do to me?", 1.0),
  f"A steady side-on medium close-up opens from the adopted first frame in {BD}: {LS} asks in a small, shaking voice, her right hand pressed to the back of her neck, her glossy wide eyes on his face, her lips trembling and her brows pulled up. {K} watches her calmly, his lips set and his jaw relaxed. The camera holds still.",
  "一个稳定的侧面中近景，从已采用的开场图继续，场景是主卧：莉莉用小小发抖的声音问，右手按在后颈上，湿亮的眼睛睁大看着他的脸，嘴唇发颤，眉头抬起。基利安平静地看着她，嘴唇抿着，下颌放松。镜头固定不动。",
  voiced("A light morning breeze and a faint creak of the bed.", "轻轻的晨风和床垫细微的吱嘎声。"))

T(b16, '03｜基利安抚过印记：现在我永远感觉得到你', 6, ['Killian', 'LilyShirt'], ('bedroom', 'killian', 'lily_shirt'), ['bedroom'],
  CL16.format(K="his right fingertips resting on the crescent mark on her nape, his heavy eyes on the mark, his lips set, his jaw relaxed, his brows level",
              L="her glossy eyes on his face, her lips parted, her brows pulled up"),
  END_BD + LAY_BD, "基利安的指尖抚过她颈后的印记，低声说：现在我永远感觉得到你。",
  ('Killian', "Now I'll always feel you.", 1.0),
  f"A steady side-on medium close-up opens from the adopted first frame in {BD}: the fingertips of {K} trace slowly along the crescent mark on her nape as he speaks in a low, husky voice, his heavy eyes on the mark, his lips set and his jaw relaxed. {LS} shivers under his touch, her eyes drifting half shut and her lips parting. The camera holds still.",
  "一个稳定的侧面中近景，从已采用的开场图继续，场景是主卧：基利安的指尖慢慢描过她颈后的印记，用低沉沙哑的声音说话，沉沉的眼睛看着印记，嘴唇抿着，下颌放松。莉莉在他的触碰下轻轻一颤，眼睛慢慢半闭，嘴唇微张。镜头固定不动。",
  voiced("The faint rustle of linen and slow breathing.", "亚麻床单轻轻的响声和缓慢的呼吸声。"), dep=True)

T(b16, '04｜基利安：长老们威胁你，我去收拾他们', 6, ['Killian', 'LilyShirt'], ('bedroom', 'killian', 'lily_shirt'), ['bedroom'],
  CL16.format(K="his dark eyes fixed on her face, his lips set, his jaw tight, his brows level",
              L="her eyes on his face, her lips parted, her brows drawn together"),
  END_BD + LAY_BD, "基利安看着她，用低沉冰冷的声音说，长老们威胁她，他要去收拾他们。",
  ('Killian', "Elders threaten you. I'll silence them.", 1.0),
  f"A steady side-on medium close-up opens from the adopted first frame in {BD}: {K} speaks in a low, cold, even voice, his dark eyes fixed on her face, his jaw tight and his lips hard. {LS} listens, her brows drawing together and her lips parting. The camera holds still.",
  "一个稳定的侧面中近景，从已采用的开场图继续，场景是主卧：基利安用低沉冰冷平稳的声音说话，深色的眼睛一直盯着她的脸，下颌绷紧，嘴唇紧闭。莉莉听着，眉头渐渐拧起，嘴唇张开。镜头固定不动。",
  voiced("A light morning breeze and a faint creak of the bed.", "轻轻的晨风和床垫细微的吱嘎声。"), dep=True)

T(b16, '05｜莉莉：你把我一个人留在这？', 6, ['Killian', 'LilyShirt'], ('bedroom', 'killian', 'lily_shirt'), ['bedroom'],
  CL16.format(K="his eyes on her face, his lips flat, his jaw tight, his brows level",
              L="her glossy eyes on his face, her lips trembling, her brows pulled up"),
  END_BD + LAY_BD, "莉莉用担心的小声音问：你把我一个人留在这？",
  ('LilyShirt', "You're leaving me here alone?", 1.0),
  f"A steady side-on medium close-up opens from the adopted first frame in {BD}: {LS} asks in a small, worried voice, her glossy eyes on his face, her brows pulling up and her lips trembling. {K}'s jaw tightens as he looks at her. The camera holds still.",
  "一个稳定的侧面中近景，从已采用的开场图继续，场景是主卧：莉莉用小小的、担心的声音问，湿亮的眼睛看着他的脸，眉头抬起，嘴唇发颤。基利安看着她，下颌绷紧。镜头固定不动。",
  voiced("A light morning breeze and a faint creak of the bed.", "轻轻的晨风和床垫细微的吱嘎声。"), dep=True)

T(b16, '06｜基利安：我回来之前不准出门', 6, ['Killian', 'LilyShirt'], ('bedroom', 'killian', 'lily_shirt'), ['bedroom'],
  CL16.format(K="his eyes dark and fixed on her face, his lips set, his jaw tight, his brows level",
              L="her eyes on his face, her lips pressed together, her brows pulled up"),
  END_BD + LAY_BD, "基利安用不容反驳的低声命令她：我回来之前，不准踏出别墅。",
  ('Killian', "Don't step outside until I return.", 1.0),
  f"A steady side-on medium close-up opens from the adopted first frame in {BD}: {K} lifts his left hand and cups her jaw, speaking in a low, steely voice, his dark eyes fixed on her face. {LS} gives one small nod, her lips pressing together. The camera holds still.",
  "一个稳定的侧面中近景，从已采用的开场图继续，场景是主卧：基利安抬起左手托住她的下颌，用低沉如钢的声音说话，深色的眼睛一直盯着她的脸。莉莉轻轻点了一下头，嘴唇抿紧。镜头固定不动。",
  voiced("A light morning breeze and a faint creak of the bed.", "轻轻的晨风和床垫细微的吱嘎声。"), dep=True)

T(b16, '07｜他吻在她额头上', 4, ['Killian', 'LilyShirt'], ('bedroom', 'killian', 'lily_shirt'), ['bedroom'],
  CL16.format(K="leaning down toward her, his lips an inch above her forehead, his eyes lowered on her face, his jaw relaxed, his brows level",
              L="her eyes closing, her lips parted, her brows soft"),
  END_BD + LAY_BD, "基利安低下头，在莉莉的额头上印下一个长长的吻，睁开眼时眼神里是病态的占有欲。",
  None,
  f"A steady side-on medium close-up opens from the adopted first frame in {BD}: {K} lowers his head and presses a long kiss to {LS}'s forehead, his eyes closing and his brows soft; then his eyes open slowly, dark with a possessive gleam, his jaw tight and his face still close to hers. Her eyes close and her lips part. The camera holds still.",
  "一个稳定的侧面中近景，从已采用的开场图继续，场景是主卧：基利安低下头，在莉莉的额头上印下一个长长的吻，眼睛闭上；然后他慢慢睁开眼，深色的眼睛里带着占有欲的光，脸仍贴得很近。她的眼睛闭上，嘴唇微张。镜头固定不动。",
  breathy("A soft sound of a kiss and slow breathing.", "轻轻的一声吻声和缓慢的呼吸声。"), dep=True)

T(b16, '08｜基利安：等我回来，我们就结婚', 6, ['Killian', 'LilyShirt'], ('bedroom', 'killian', 'lily_shirt'), ['bedroom'],
  CL16.format(K="his dark eyes on her face, his lips set, his jaw tight, his brows level",
              L="her glossy eyes on his face, her lips parted, her brows pulled up"),
  END_BD + LAY_BD, "基利安用拇指擦过她的脸颊，低声说：等我回来，我们就结婚。",
  ('Killian', "When I'm back, we marry.", 1.0),
  f"A steady side-on medium close-up opens from the adopted first frame in {BD}: {K}'s thumb brushes slowly along her cheek as he speaks in a low, husky, possessive voice, his jaw tight, his brows low and his dark eyes on her face. {LS} looks up at him, her glossy eyes widening and her lips parting. The camera holds still.",
  "一个稳定的侧面中近景，从已采用的开场图继续，场景是主卧：基利安的拇指慢慢擦过她的脸颊，用低沉沙哑、带着占有欲的声音说话，深色的眼睛看着她的脸。莉莉抬头看着他，湿亮的眼睛睁大，嘴唇微张。镜头固定不动。",
  voiced("A light morning breeze and a faint creak of the bed.", "轻轻的晨风和床垫细微的吱嘎声。"), dep=True)

T(b16, '09｜莉莉在阳台上，看着车队开出铁门', 4, ['LilyShirt'], ('villa_balcony', 'lily_shirt'), ['villa_balcony'],
  "Side-on medium shot of Lily alone, from the head to the knees, in the middle third of the frame, standing at the stone balustrade of the second-floor balcony in profile facing frame-right, in the oversized white men's shirt, her chestnut hair loose and stirring in the breeze, both hands resting on the stone rail, "
  "her lips parted, her brows soft, her wistful eyes on the last of three black SUVs rolling through the open tall black iron gates at frame-right below. The frame holds exactly one person, Lily.",
  END_BAL + LAY_BAL, "莉莉站在二楼阳台，看着最后一辆黑色车子驶出铁门，铁门在车后关上。",
  None,
  f"A steady side-on medium shot opens from the adopted first frame in {BAL}: the last black SUV rolls out through the iron gates at frame-right and the heavy gates swing shut behind it, and {LS}'s right hand rises to the back of her neck, her lips parting and her soft, wistful eyes on the closed gates. The camera holds still.",
  "一个稳定的侧面中景，从已采用的开场图继续，场景是二楼阳台：最后一辆黑色车子从画面右边的铁门驶出去，沉重的铁门在车后合拢；莉莉的右手抬到后颈，嘴唇微张，柔柔的、若有所思的眼睛看着关上的铁门。镜头固定不动。",
  breathy("A distant car engine fading away and the clang of heavy gates closing.", "远处渐渐远去的引擎声和沉重铁门合上的哐当声。"))

T(b16, '10｜猎手躲在花园里，一脚踩断树枝', 4, ['Rogue'], ('garden_path', 'rogue'), ['garden_path'],
  "Side-on wide-medium shot of Rogue alone, from the head to the boots, in profile facing frame-left, in the middle third of the frame, crouching low on the gravel path beside a tall dark hedge, in the patched black leather jacket, the long scar down his left cheek and across his eye, his gloved right hand resting on the hilt of the sheathed silver dagger, a dry twig lying under his right boot, "
  "his heavy brows lowered, his lips pulled back from yellowed teeth in a cruel grin, his narrowed eyes on the mansion's dark stone wall far at frame-left. The frame holds exactly one person, Rogue.",
  END_GP + LAY_GP, "流浪狼人蹲在后花园的篱笆边，一脚踩断了地上的枯树枝，立刻僵住。",
  None,
  f"A steady side-on wide-medium shot opens from the adopted first frame in {GP}: {RG} shifts his weight forward and his boot comes down on the dry twig, which snaps with a sharp crack; he freezes at once, his lips tightening over his yellowed teeth, his heavy brows low and his narrowed eyes fixed on the far wall. The camera holds still.",
  "一个稳定的侧面宽中景，从已采用的开场图继续，场景是后花园的小路：流浪狼人身体往前一压，靴子踩在枯树枝上，“咔嚓”一声脆响；他立刻僵住，嘴唇收紧盖住发黄的牙，眉头压低，眯着的眼睛死死盯着远处的墙。镜头固定不动。",
  breathy("A sharp crack of a dry twig, then a held breath and a hush.", "枯树枝清脆的一声断裂，然后是屏住的呼吸和一片寂静。"))

T(b16, '11｜树枝断裂，她猛地回头', 4, ['LilyShirt'], ('villa_balcony', 'lily_shirt'), ['villa_balcony'],
  "Side-on medium shot of Lily alone, from the head to the knees, in the middle third of the frame, standing at the stone balustrade of the second-floor balcony in profile facing frame-right, in the oversized white men's shirt, her chestnut hair loose, both hands resting on the stone rail, "
  "her lips parted, her brows soft, her eyes on the closed black iron gates at frame-right. The hedge-lined back garden and the rusted warehouse roof are in the distance at frame-left. The frame holds exactly one person, Lily.",
  END_BAL + LAY_BAL, "一声很远的树枝断裂声，莉莉猛地回头看向左边的后花园。",
  None,
  f"A steady side-on medium shot opens from the adopted first frame in {BAL}: a faint, distant crack of a breaking branch sounds, and {LS} turns only her head toward frame-left, her eyes going wide on the hedge-lined garden and the rusted warehouse roof, her brows pulling up and her lips parting. The camera holds still.",
  "一个稳定的侧面中景，从已采用的开场图继续，场景是二楼阳台：传来一声很远、很轻的树枝断裂声，莉莉只是把头转向画面左边，睁大的眼睛看着篱笆围起来的后花园和生锈的仓库屋顶，眉头抬起，嘴唇张开。镜头固定不动。",
  breathy("A faint, distant crack of a breaking branch, then a hush.", "很远、很轻的一声树枝断裂声，然后是一片寂静。"))

T(b16, '12｜黑影顺着墙壁爬上来', 4, ['Rogue'], ('rogue',), [],
  "Wide shot looking up the dark stone wall of the mansion from the garden below, in the middle third of the frame: Rogue, a lean man in a patched black leather jacket, climbing the wall hand over hand through thick ivy, his gloved fingers gripping the stone ledges, "
  "his scarred face turned upward, his lips pulled back from yellowed teeth, his narrowed eyes on the stone balustrade of the balcony at the top of the frame. The frame holds exactly one person, Rogue.",
  " Soft clear morning sunlight, a pale blue sky behind the roofline.", "流浪狼人顺着墙上的藤蔓飞快地往阳台爬。",
  None,
  f"A steady wide shot opens from the adopted first frame: {RG} climbs up the stone wall hand over hand through the ivy, his gloved fingers hooking the ledges and his boots scrabbling at the stone, his lips pulled back from his yellowed teeth and his narrowed eyes fixed on the balustrade above; loose ivy leaves flutter down. The camera holds still.",
  "一个稳定的宽景，从已采用的开场图继续：流浪狼人顺着墙上的藤蔓双手交替往上爬，戴手套的手指钩住石头的凹处，靴子在石墙上蹬着，嘴唇咧开露出发黄的牙，眯起的眼睛盯着上面的栏杆；散落的藤叶飘落下来。镜头固定不动。",
  breathy("Scrabbling boots on stone and the rustle of ivy.", "靴子在石头上蹬踏的声音和藤叶的沙沙声。"))

# =================================================================================================== 第 17 集：银刃之下
# 观众要看懂：猎手翻上阳台抓住她 → 他闻出她是 Luna → 银匕首（有毒，已经划出血）→ 另一边：基利安在车里很平静
# → 她后颈的印记发金光（他能感觉到她的原因）→ 他心口痛、眼睛变金 → “停车！” → 车门被撕掉，他已经跑了。
# 原大纲是万米高空的飞机，这里改成刚开出山庄不远的车队：他赶回来才快得合理，猎手那句“你怎么这么快”才成立。

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

T(b17, '02｜他嗅着她：你闻起来是纯正的 Luna', 6, ['Rogue', 'LilyShirt'], ('villa_balcony', 'rogue', 'lily_shirt'), ['villa_balcony'],
  PIN17.format(L="Rogue's left hand clamped over her mouth, her wide eyes wet with tears, her brows pulled up, her chest heaving, both hands gripping his wrist",
               R="his scarred face lowered beside her hair, his nostrils flared, his eyes half closed, his lips curling into a greedy grin over yellowed teeth"),
  END_BAL + LAY_BAL, "流浪狼人贪婪地嗅着她的头发，说她闻起来是纯正的 Luna；莉莉拼命挣扎。",
  ('Rogue', "You smell like pure Luna.", 1.0),
  f"A steady side-on medium close-up opens from the adopted first frame in {BAL}: {RG} breathes in deeply beside her hair, his eyes half closing and his lips curling into a greedy grin, and speaks in a low, wheezing, sly voice. {LS} fights against his hold, her wet eyes wide and her brows pulled up, her hands dragging at his wrist. The camera holds still.",
  "一个稳定的侧面中近景，从已采用的开场图继续，场景是二楼阳台：流浪狼人在她的头发边深深吸了一口气，眼睛半闭，贪婪的笑容更大，用低沉、带喘息的狡猾声音说话。莉莉拼命挣扎，湿润的眼睛睁大，眉头抬起，双手拽着他的手腕。镜头固定不动。",
  voiced("A wheezing breath and the scuff of bare feet on stone.", "一声嘶哑的喘息和光脚蹭在石头上的摩擦声。"), dep=True)

T(b17, '03｜银匕首贴上她的脖子：乖乖跟我走', 6, ['Rogue', 'LilyShirt'], ('villa_balcony', 'rogue', 'lily_shirt'), ['villa_balcony'],
  PIN17.format(L="her chin lifted away from the blade, her lips pressed tight and trembling, her brows pulled up, tears on her lashes, her wide eyes on the dagger",
               R="his left arm locked across her collarbone and his right hand holding a silver dagger with a faint green sheen of poison, its flat laid against the left side of her throat, a thin red line of blood already running down her neck, his lips pulled into a cruel grin, his narrowed eyes on her face"),
  END_BAL + LAY_BAL, "流浪狼人把淬了毒的银匕首压在她脖子上，血已经淌下来，他说：乖乖跟我走，不然我割深一点。",
  ('Rogue', "Come quietly, or I cut deeper.", 1.0),
  f"A steady side-on medium close-up opens from the adopted first frame in {BAL}: {RG} presses the edge of the silver dagger harder against {LS}'s throat and speaks in a low, savage whisper, his lips curled into a cruel grin; the thin line of red blood along the blade widens and runs down her neck. She freezes, her chin lifting, her lips trembling and her wide eyes brimming with tears. The camera holds still.",
  "一个稳定的侧面中近景，从已采用的开场图继续，场景是二楼阳台：流浪狼人把银匕首的刃口更用力地压在莉莉的喉咙上，用低沉凶狠的耳语说话，嘴角扯出残忍的笑；刀刃上那道细细的血线变宽，淌下她的脖子。她僵住了，下巴抬起，嘴唇发颤，睁大的眼睛里蓄满泪水。镜头固定不动。",
  voiced("A thin metallic hiss of a blade on skin and a shaky breath.", "刀刃贴着皮肤细细的金属嘶声，和一声发抖的呼吸。"), dep=True)

T(b17, '04｜车队里的基利安，平静地靠在后座', 4, ['Killian'], ('suv_interior', 'killian'), ['suv_interior'],
  "Side-on medium shot of Killian alone, from the head to the knees, in the middle third of the frame, sitting on the cream leather rear bench at frame-right in profile facing frame-left, in the tailored black three-piece suit, white shirt and dark tie, his right arm resting along the seat back, his left hand relaxed on his thigh, "
  "his lips softly closed, his jaw relaxed, his brows level, his calm dark-gray eyes on the headrest of the front seat in front of him. The frame holds exactly one person, Killian.",
  END_SUV + LAY_SUV, "疾驶的黑色SUV里，基利安靠在后座上，神情平静。",
  None,
  f"A steady side-on medium shot opens from the adopted first frame in {SUV}: dark pine trunks slide past the large side window as {K} sits calmly, his chest rising and falling slowly, his lips softly closed, his jaw relaxed and his brows level. The camera holds still.",
  "一个稳定的侧面中景，从已采用的开场图继续，场景是行驶的黑色SUV车内：深色的松树树干从大侧窗外一棵棵滑过，基利安平静地坐着，胸口缓慢起伏，嘴唇轻轻闭着，下颌放松，眉头平整。镜头固定不动。",
  breathy("The low steady hum of an engine and tires on asphalt.", "发动机低沉平稳的嗡鸣和轮胎碾过柏油路的声音。"))

T(b17, '05｜特写：她后颈的印记亮起金光', 3, ['LilyShirt'], ('villa_balcony', 'lily_shirt'), ['villa_balcony'],
  "Close-up from behind and slightly to the left of Lily's head, neck and shoulders, in the middle third of the frame, her long chestnut hair swept forward over her left shoulder so that her nape is bare, the collar of the oversized white men's shirt low on her shoulders; "
  "on the center of her nape the dark-red crescent-moon mark in an ornate, tattoo-like pattern, a thin red line of blood running down the side of her neck, her chin lifted and her jaw trembling, the stone balustrade softly blurred beyond her. The frame holds exactly one person, Lily.",
  END_BAL + LAY_BAL, "特写：莉莉后颈的新月印记亮起一阵金色的光，她的下巴在发抖。",
  None,
  f"A steady close-up opens from the adopted first frame in {BAL}: the crescent mark on {LS}'s nape flares with a warm golden glow that pulses once, then again, brightening and fading as her shoulders shake and her jaw trembles. The camera holds still.",
  "一个稳定的特写，从已采用的开场图继续，场景是二楼阳台：莉莉后颈的新月印记亮起一阵温暖的金光，闪一下，再闪一下，忽亮忽暗，她的肩膀在发抖，下颌在颤。镜头固定不动。",
  breathy("A deep heartbeat thump, once and again, and a trembling breath.", "一下深沉的心跳声，又一下，和一声发抖的呼吸。"))

T(b17, '06｜基利安心口剧痛，眼睛变成金色', 3, ['KillianGold'], ('suv_interior', 'killian_gold'), ['suv_interior'],
  "Side-on medium close-up of Killian alone, from the head to the chest, in profile facing frame-left, in the middle third of the frame, sitting on the cream leather rear bench at frame-right in the tailored black three-piece suit, his eyes closed, his lips softly closed, his brows just beginning to draw together, his hands resting on his lap. "
  "The large side window behind the bench shows dark pine trees. The frame holds exactly one person, Killian.",
  END_SUV + LAY_SUV, "基利安心口一阵剧痛，猛地睁眼，眼睛变成暗金色，指尖长出黑色的爪。",
  None,
  f"A steady side-on medium close-up opens from the adopted first frame in {SUV}: {KG}'s body jolts and his right hand clamps over his heart, black claws extending from his fingertips; his eyes snap open, glowing dark gold, his jaw clenching, his lips pulling back from sharp canine teeth and his brows crashing together. The camera holds still.",
  "一个稳定的侧面中近景，从已采用的开场图继续，场景是行驶的黑色SUV车内：基利安的身体猛地一震，右手按住心口，指尖伸出黑色的爪；他的眼睛猛地睁开，发出暗金色的光，下颌咬紧，嘴唇咧开露出尖利的犬齿，眉头拧在一起。镜头固定不动。",
  breathy("A sharp gasp and the hum of an engine.", "一声猛烈的抽气和发动机的嗡鸣。"))

T(b17, '07｜他怒吼：停车！', 6, ['KillianGold', 'Bodyguard'], ('suv_interior', 'killian_gold', 'bodyguard'), ['suv_interior'],
  "Side-on medium two-shot, both people from the head to the waist, in the middle third of the frame, inside the black SUV. "
  "Bodyguard at frame-left in the black leather front passenger seat, in the black suit with the clear earpiece, turned toward the back seat in profile facing frame-right, his stern face startled, his lips parted, his brows pulled up, his wide eyes on Killian. "
  "Killian at frame-right on the cream leather rear bench in profile facing frame-left, in the tailored black three-piece suit, his right hand clutching his chest with long black claws, his eyes glowing dark gold, his teeth bared, his jaw clenched, his brows crashing together. "
  "The frame holds exactly two people: Bodyguard and Killian.",
  END_SUV + LAY_SUV, "基利安怒吼着让停车，侧窗被震出蛛网般的裂纹，前座的保镖吓得一激灵。",
  ('KillianGold', "Stop the car!", 1.0),
  f"A steady side-on medium two-shot opens from the adopted first frame in {SUV}: {KG} roars the order in a raw, thunderous voice, his mouth wide and his glowing gold eyes blazing, his claws digging into his chest; behind him the large side window splits with a spreading spiderweb crack in the glass. "
  f"{BGD} flinches hard, his lips parting, his brows jerking up and his wide eyes locked on Killian. The camera holds still.",
  "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是行驶的黑色SUV车内：基利安用粗哑如雷的声音吼出命令，嘴张得很大，发光的金色眼睛怒火燃烧，爪子抠进胸口；他身后的大侧窗里，玻璃裂开蛛网一样越扩越大的裂纹。保镖猛地一缩，嘴唇张开，眉头一跳，睁大的眼睛死死盯着基利安。镜头固定不动。",
  voiced("A thunderous roar, the sharp crack of splitting glass and a screech of brakes.", "雷鸣般的怒吼、玻璃裂开的一声脆响和刹车的尖啸。"))

T(b17, '08｜后座空了，车门被撕掉，保镖愣住', 4, ['Bodyguard'], ('suv_interior', 'bodyguard'), ['suv_interior'],
  "Side-on medium shot of Bodyguard alone, from the head to the waist, in the middle third of the frame, inside the stopped black SUV, in the front passenger seat at frame-left, turned around toward the rear bench in profile facing frame-right, in the black suit with the clear earpiece, "
  "his stern face frozen, his lips parted, his brows pulled up, his wide eyes on the empty cream leather rear bench at frame-right, whose rear door hangs wide open, wrenched off its upper hinge, daylight and pine trunks showing through the gap. The frame holds exactly one person, Bodyguard.",
  END_SUV + LAY_SUV, "后座空了，车门被撕得歪在一边，保镖愣愣地看着空座位。",
  None,
  f"A steady side-on medium shot opens from the adopted first frame in {SUV}: the wrenched rear door swings slowly on its broken hinge over the empty cream leather bench, pine needles drifting in through the gap, while {BGD} stares at the empty seat, his lips parting, his brows pulling up and his wide eyes unblinking. The camera holds still.",
  "一个稳定的侧面中景，从已采用的开场图继续，场景是停下的黑色SUV车内：被撕坏的后车门在断裂的合页上慢慢晃着，挂在空空的奶油色后座上方，松针从缺口飘进来；保镖愣愣地盯着空座位，嘴唇张开，眉头抬起，睁大的眼睛一眨不眨。镜头固定不动。",
  breathy("A shriek of tires fading into silence, a creaking hinge and a sharp breath.", "刹车的尖啸渐渐消失，合页吱呀作响，和一声急促的抽气。"))

# =================================================================================================== 第 18 集：仓库和黑狼
# 观众要看懂：猎手把流血的莉莉拖过花园（在途）→ 保罗和玛丽早就在仓库里等着（15 集说好的）→ 她被推进去 → 玛丽见血兴奋
# → 保罗为什么恨她（“你选了那个怪物，不选我”）→ 扬手 → 铁门被炸飞 → 各人反应 → 黑狼走出（金眼睛＝17 集车里那双）
# → 猎手吓掉刀：“你怎么这么快”→ 莉莉认出他 → 咆哮扑出。

T(b18, '01｜狼人把流血的莉莉拖过后花园', 4, ['Rogue', 'LilyShirt'], ('garden_path', 'rogue', 'lily_shirt'), ['garden_path'],
  "Side-on wide-medium two-shot, both people from the head to the knees, in the middle third of the frame, on the gravel path between the tall dark hedges, both in profile facing frame-right, the rusted warehouse ahead at frame-right. "
  "Rogue at frame-left in the patched black leather jacket, his left hand gripping Lily's right upper arm and his right hand holding the silver dagger low at his side, his lips pulled into a cruel grin, his narrowed eyes on the warehouse door at frame-right. "
  "Lily at frame-right of him in the oversized white men's shirt, stumbling forward barefoot on the gravel, a thin line of blood down the left side of her neck, her chestnut hair tangled, her lips pressed together and trembling, her brows pulled up, her wet eyes on the gravel. "
  "The frame holds exactly two people: Rogue and Lily.",
  END_GP + LAY_GP, "流浪狼人拽着脖子在流血的莉莉，穿过后花园的小路，拖向仓库。",
  None,
  f"A steady side-on wide-medium two-shot opens from the adopted first frame in {GP}: {RG} drags her along the gravel path toward the warehouse door at frame-right, his lips curled into a cruel grin. {LS} stumbles barefoot over the stones, blood trickling down her neck, her lips trembling and her brows pulled up. The camera holds still.",
  "一个稳定的侧面宽中双人镜头，从已采用的开场图继续，场景是后花园的小路：流浪狼人拽着莉莉沿碎石路拖向画面右边的仓库门，残忍的笑容更大；她光着的脚在石子上踉跄，血顺着脖子淌下来，嘴唇发颤。镜头固定不动。",
  breathy("Boots and bare feet scuffing over gravel and a shaky breath.", "靴子和光脚在碎石上拖行的摩擦声，和一声发抖的呼吸。"))

T(b18, '02｜仓库里，保罗和玛丽早就在等', 4, ['PaulOnScreen', 'MaryBlack'], ('warehouse', 'paul', 'mary_black'), ['warehouse'],
  "Side-on medium two-shot, both people from the head to the knees, in the middle third of the frame, standing side by side on the concrete floor of the warehouse, both in profile facing frame-right toward the closed tall rusted iron double door at frame-right. "
  "Paul at frame-left in the creased navy blazer, his arms folded, his lips pressed tight, his brows drawn together, his red-rimmed eyes on the door. "
  "Mary at frame-right in the fitted black wool coat, her right heel tapping on the concrete, her chin lifted, her lips set in a thin cold smug smile, her sharp green eyes on the door. "
  "The frame holds exactly two people: Paul and Mary.",
  END_WH + LAY_WH, "仓库里，保罗和玛丽并排站着等；听到门外的脚步声，两个人同时抬起头。",
  None,
  f"A steady side-on medium two-shot opens from the adopted first frame in {WH}: faint footsteps crunch on gravel outside the door. {MB} stops tapping her heel, her head lifting, her cold smug smile widening and her green eyes bright. {PL}'s arms unfold, his lips parting, his brows lifting and his red-rimmed eyes widening with hungry eagerness. The camera holds still.",
  "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是废弃仓库：门外传来碎石上轻轻的脚步声。玛丽停下了敲地的脚跟，头抬起来，冷冷的得意笑容更深，绿眼睛发亮。保罗抱着的手臂放下来，嘴唇张开，眉头扬起，发红的眼睛带着贪婪的急切越睁越大。镜头固定不动。",
  breathy("Faint footsteps on gravel outside and the creak of an old building.", "门外碎石上轻轻的脚步声和旧建筑的吱嘎声。"))

T(b18, '03｜他把她推进仓库，关上铁门', 4, ['Rogue', 'LilyShirt'], ('warehouse', 'rogue', 'lily_shirt'), ['warehouse'],
  "Side-on wide-medium two-shot, both people from the head to the knees, in the middle third of the frame, inside the warehouse. "
  "Rogue at frame-right standing in the opening of the tall rusted iron double door with daylight spilling in behind him, in the patched black leather jacket, his right arm still extended from a shove, the silver dagger in his left hand, his lips pulled into a cruel grin, his narrowed eyes on Lily. "
  "Lily at frame-left in the oversized white men's shirt, stumbling forward barefoot onto the concrete floor, both hands reaching for the floor, a thin line of blood down the left side of her neck, her lips parted, her brows pulled up, her wide eyes on the concrete. "
  "The frame holds exactly two people: Rogue and Lily.",
  END_WH + LAY_WH, "流浪狼人把莉莉一把推进仓库，她摔倒在水泥地上，他把铁门拉上。",
  None,
  f"A steady side-on wide-medium two-shot opens from the adopted first frame in {WH}: {LS} stumbles forward and drops onto her hands and knees on the concrete, her chestnut hair falling around her face, her lips parting and her brows pulling up. {RG} drags the tall iron double door shut behind him with a heavy clang, his lips curling into a cruel grin and his narrowed eyes on her. The camera holds still.",
  "一个稳定的侧面宽中双人镜头，从已采用的开场图继续，场景是废弃仓库：莉莉踉跄向前，双手双膝摔在水泥地上，栗色的头发垂在脸边，嘴唇张开，眉头抬起。流浪狼人在身后“哐当”一声把高大的铁双开门拉上，残忍的笑容更大，眯着的眼睛盯着她。镜头固定不动。",
  breathy("A hard thud of knees on concrete, a sharp gasp and the heavy clang of an iron door.", "膝盖重重磕在水泥地上的闷响、一声急促的抽气，和铁门沉重的哐当声。"))

T(b18, '04｜玛丽看见血，兴奋大笑', 6, ['MaryBlack', 'LilyShirt'], ('warehouse', 'mary_black', 'lily_shirt'), ['warehouse'],
  "Side-on medium two-shot, both people from the head to the knees, in the middle third of the frame, on the concrete floor of the warehouse. "
  "Mary at frame-right standing in the fitted black wool coat, her hands clasped at her chest, her lips parted in a gleeful laugh, her chin lifted, her sharp green eyes bright and wide on Lily's bleeding neck. "
  "Lily at frame-left kneeling on the concrete in the oversized white men's shirt, her left hand pressed to the bleeding side of her neck with blood between her fingers, her head bowed, her lips pressed tight, her brows pulled together, tears on her cheeks, her eyes on the floor. "
  "The frame holds exactly two people: Mary and Lily.",
  END_WH + LAY_WH, "玛丽看着莉莉脖子上的血，兴奋地笑着说：看那么多血！",
  ('MaryBlack', "Look at all that blood!", 1.0),
  f"A steady side-on medium two-shot opens from the adopted first frame in {WH}: {MB} at frame-right speaks in a gleeful, sugary voice, her lips curled into a delighted grin, her eyes bright on Lily's bleeding neck and her chin tilting up. {LS} at frame-left presses her hand harder against her neck, her head sinking lower, her lips trembling and tears running down her cheeks. The camera holds still.",
  "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是废弃仓库：画面右边的玛丽用兴奋甜腻的声音说话，眼睛亮亮地盯着莉莉流血的脖子，下巴抬起。画面左边的莉莉把手更用力地按在脖子上，头垂得更低，嘴唇发颤，眼泪顺着脸颊流下来。镜头固定不动。",
  voiced("A gleeful laugh echoing in the empty warehouse and a faint drip of water.", "空荡荡的仓库里回响的兴奋笑声，和细微的滴水声。"))

T(b18, '05｜保罗捏住她的脸：你选了那个怪物，不选我', 6, ['PaulOnScreen', 'LilyShirt'], ('warehouse', 'paul', 'lily_shirt'), ['warehouse'],
  "Side-on medium two-shot, both people from the head to the knees, in the middle third of the frame, on the concrete floor of the warehouse. "
  "Paul at frame-right standing in the creased navy blazer, bending forward, his right hand gripping Lily's cheeks and chin, his lips pulled back from his teeth, his brows crashing together, his red-rimmed wet eyes on her face. "
  "Lily at frame-left kneeling in the oversized white men's shirt, her face lifted in his grip, her wet eyes on his face, her lips pressed tight and trembling, her brows pulled up, blood on the side of her neck. "
  "The frame holds exactly two people: Paul and Lily.",
  END_WH + LAY_WH, "保罗弯下腰狠狠捏住莉莉的脸，红着眼睛吼：你选了那个怪物，不选我！",
  ('PaulOnScreen', "You chose that monster over me!", 1.0),
  f"A steady side-on medium two-shot opens from the adopted first frame in {WH}: {PL} at frame-right squeezes her face hard and spits the words in a furious, cracking voice, his lips pulled back from his bared teeth, his brows crashing together and his wet eyes burning on hers. {LS} at frame-left glares back at him, her wet eyes unflinching, her lips trembling and her brows pulling together. The camera holds still.",
  "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是废弃仓库：画面右边的保罗狠狠捏住她的脸，用暴怒又发裂的声音把话吐出来，龇着牙，眉头拧在一起，湿润的眼睛喷火地盯着她。画面左边的莉莉湿润的眼睛毫不退缩地瞪回去，嘴唇发颤，眉头拧起。镜头固定不动。",
  voiced("A cold draft whistling through the empty warehouse.", "冷风吹过空荡荡的仓库的呼啸声。"))

T(b18, '06｜保罗扬起手要打下去', 3, ['PaulOnScreen', 'LilyShirt'], ('warehouse', 'paul', 'lily_shirt'), ['warehouse'],
  "Side-on medium two-shot, both people from the head to the knees, in the middle third of the frame, on the concrete floor of the warehouse. "
  "Paul at frame-right standing in the creased navy blazer, his right arm drawn back with the open palm at shoulder height, his jaw clenched, his lips pulled back from his teeth, his red-rimmed eyes blazing on Lily's face. "
  "Lily at frame-left kneeling in the oversized white men's shirt, her face lifted, her eyes squeezed shut, her lips pressed tight, her brows pulled together, blood on the side of her neck. "
  "The frame holds exactly two people: Paul and Lily.",
  END_WH + LAY_WH, "保罗把手高高扬起，莉莉闭紧眼睛等着挨打。",
  None,
  f"A steady side-on medium two-shot opens from the adopted first frame in {WH}: {PL} swings his arm back and raises his open right hand high, his jaw clenched, his brows crashing together and his eyes blazing; {LS}'s eyes squeeze shut and her lips press tight as she braces. The camera holds still.",
  "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是废弃仓库：保罗把手臂往后一甩，张开的右手高高扬起，咬紧牙关，眉头拧在一起，眼睛喷火；莉莉的眼睛紧紧闭上，嘴唇抿紧，咬牙等着。镜头固定不动。",
  breathy("A sharp intake of breath and the faint creak of the old building.", "一声急促的吸气和旧建筑细微的吱嘎声。"), dep=True)

T(b18, '07｜铁门被炸飞', 3, [], ('warehouse',), ['warehouse'],
  "Wide shot of the warehouse interior in the middle third of the frame: the tall rusted iron double door at frame-right closed, shafts of dusty pale light falling across the concrete floor, the stacked crates and steel barrels at frame-left, concrete pillars in the middle. No people are in the frame.",
  END_WH + LAY_WH, "一声巨响，仓库的铁门整扇炸飞进来，砸在地上，烟尘滚滚。",
  None,
  f"A steady wide shot opens from the adopted first frame in {WH}: with a tremendous boom the rusted iron double door bursts inward off its hinges and slams flat onto the concrete floor toward frame-left in a roaring cloud of dust and flying rust, the shafts of light turning thick with smoke. No people appear. The camera holds still.",
  "一个稳定的宽景，从已采用的开场图继续，场景是废弃仓库：随着一声巨响，生锈的铁双开门整扇从合页上炸开，朝画面左边重重拍在水泥地上，烟尘和锈屑滚滚而起，一束束光变得浓烟滚滚。画面里没有人出现。镜头固定不动。",
  breathy("A thunderous boom of tearing metal, a screech and a crash of iron on concrete.", "撕裂金属的一声雷鸣般的巨响、一阵刺耳的尖啸，和铁板砸在水泥地上的轰响。"))

T(b18, '08｜保罗和玛丽被吓得后退', 3, ['PaulOnScreen', 'MaryBlack'], ('warehouse', 'paul', 'mary_black'), ['warehouse'],
  "Side-on medium two-shot, both people from the head to the waist, in the middle third of the frame, standing side by side on the concrete floor, both in profile facing frame-right toward the dust at the doorway at frame-right. "
  "Paul at frame-left in the creased navy blazer, his right arm still raised, his lips parted, his brows pulled up, his red-rimmed eyes wide on the dust cloud. "
  "Mary at frame-right in the fitted black wool coat, her hands rising to her mouth, her lips parted, her brows lifted, her sharp green eyes wide on the dust cloud. "
  "The frame holds exactly two people: Paul and Mary.",
  END_WH + LAY_WH, "保罗和玛丽被巨响吓得踉跄后退，一个举手挡脸，一个捂住嘴。",
  None,
  f"A steady side-on medium two-shot opens from the adopted first frame in {WH}: {PL} staggers back and flings his raised hand up to shield his face, his mouth falling open. {MB} stumbles back with her hands pressed to her mouth, her brows lifting and her eyes widening on the roiling dust. The camera holds still.",
  "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是废弃仓库：保罗踉跄后退，扬着的手一下举起来挡住脸，嘴巴张开。玛丽踉跄后退，双手捂住嘴，眉头扬起，眼睛看着翻滚的烟尘越睁越大。镜头固定不动。",
  breathy("Scraping shoes, a sharp gasp and settling dust.", "鞋底拖地的声音、一声急促的抽气和灰尘落定的声音。"))

T(b18, '09｜黑狼从烟尘里走出来', 4, [], ('warehouse', 'black_wolf'), ['warehouse'],
  "Wide shot, in the middle third of the frame, of a colossal jet-black wolf the size of a small horse standing in the doorway at frame-right in a thick cloud of dust, in profile facing frame-left, its thick black fur bristling, its dark-gold glowing eyes fixed on the concrete floor ahead of it at frame-left, "
  "its lips curled back from long white fangs; the broken iron door lies flat on the floor in front of it. The frame holds exactly one animal, the black wolf, and no people.",
  END_WH + LAY_WH, "一头巨大的纯黑狼从烟尘里慢慢走出来，眼睛是暗金色的。",
  None,
  f"A steady wide shot opens from the adopted first frame in {WH}: {WF} walks slowly out of the dust toward frame-left, its massive shoulders rolling, its claws clicking on the concrete and its dark-gold eyes blazing, its fangs bared as the dust swirls around its legs. No people appear. The camera holds still.",
  "一个稳定的宽景，从已采用的开场图继续，场景是废弃仓库：巨大的黑狼从尘土里朝画面左边慢慢走出来，厚重的肩膀一起一伏，爪子在水泥地上咔嗒作响，暗金色的眼睛喷着光，龇着獠牙，尘土在它的腿边打着旋。画面里没有人出现。镜头固定不动。",
  breathy("A deep rumbling growl and the slow click of claws on concrete.", "低沉的咆哮声和爪子慢慢敲在水泥地上的咔嗒声。"))

T(b18, '10｜流浪狼人吓得刀掉在地上：你怎么这么快就到了', 6, ['Rogue'], ('warehouse', 'rogue', 'black_wolf'), ['warehouse'],
  "Side-on wide-medium shot, in the middle third of the frame, inside the warehouse. Rogue at frame-left standing in profile facing frame-right, in the patched black leather jacket, the silver dagger slipping from his shaking right hand, his knees buckling, his lips trembling, his brows pulled up, his eyes wide and fixed on the wolf's head. "
  "The colossal jet-black wolf at frame-right in profile facing frame-left, its head lowered, its dark-gold eyes blazing at Rogue, its fangs bared, in a haze of dust. The frame holds exactly one person, Rogue, and one huge black wolf.",
  END_WH + LAY_WH, "流浪狼人吓得匕首脱手，腿一软，哆嗦着问：你怎么这么快就到了，基利安？",
  ('Rogue', "How are you here already, Killian?", 1.0),
  f"A steady side-on wide-medium shot opens from the adopted first frame in {WH}: {RG}'s trembling hand opens and the silver dagger clatters to the concrete; his knees buckle as he stammers in a cracking, terrified voice, his lips trembling and his eyes wide on the gold eyes of {WF}. The wolf takes one slow step closer, growling. The camera holds still.",
  "一个稳定的侧面宽中景，从已采用的开场图继续，场景是废弃仓库：流浪狼人发抖的手一松，银匕首哐啷掉在水泥地上；他双腿发软，用发颤、惊恐的声音结结巴巴地说话，嘴唇哆嗦，睁大的眼睛盯着黑狼的金色眼睛。黑狼往前慢慢逼近一步，低低地咆哮。镜头固定不动。",
  voiced("The ring of a dagger on concrete and a low rumbling growl.", "匕首掉在水泥地上的一声脆响和低沉的咆哮声。"))

T(b18, '11｜莉莉认出了那双金色的眼睛', 6, ['LilyShirt'], ('warehouse', 'lily_shirt', 'black_wolf'), ['warehouse'],
  "Side-on wide-medium shot, in the middle third of the frame, inside the warehouse. Lily at frame-left kneeling on the concrete in the oversized white men's shirt, her left hand pressed to her bleeding neck, her face lifted, her lips parted, her brows pulled up, her tear-streaked wide eyes fixed on the wolf's gold eyes. "
  "The colossal jet-black wolf at frame-right in profile facing frame-left, standing over the fallen iron door, its head lowered, its dark-gold eyes blazing. The frame holds exactly one person, Lily, and one huge black wolf.",
  END_WH + LAY_WH, "莉莉跪在地上，捂着流血的脖子，认出了那双金色的眼睛，轻声问：是你吗？",
  ('LilyShirt', "Is that you, Killian?", 1.0),
  f"A steady side-on wide-medium shot opens from the adopted first frame in {WH}: {LS} whispers in a trembling voice, her wide wet eyes locked on the gold eyes of {WF} and her lips trembling; the wolf's fierce gaze softens for an instant as it looks at her, its growl dying away. The camera holds still.",
  "一个稳定的侧面宽中景，从已采用的开场图继续，场景是废弃仓库：莉莉用发颤的声音轻轻地问，湿润睁大的眼睛直直盯着黑狼的金色眼睛，嘴唇发颤；黑狼凶狠的目光在看着她的那一瞬软了一下，低吼声渐渐消去。镜头固定不动。",
  voiced("A low fading growl and a shaky breath.", "渐渐低下去的咆哮声和一声发抖的呼吸。"))

T(b18, '12｜黑狼咆哮着扑出去', 3, [], ('warehouse', 'black_wolf'), ['warehouse'],
  "Side-on close-up of the colossal jet-black wolf's head and shoulders, in profile facing frame-left, in the middle third of the frame, in a haze of dust, its dark-gold eyes blazing, its upper lip curled back from long white fangs, its thick black fur bristling. The frame holds exactly one animal, the black wolf, and no people.",
  END_WH + LAY_WH, "黑狼仰头一声震天的咆哮，然后猛地向左扑了出去。",
  None,
  f"A steady side-on close-up opens from the adopted first frame in {WH}: {WF} throws its head back and unleashes a thunderous roar with its jaws stretched wide, then lunges forward toward frame-left in one violent leap, the dust blasting outward. No people appear. The camera holds still.",
  "一个稳定的侧面特写，从已采用的开场图继续，场景是废弃仓库：黑狼仰起头，张大嘴发出一声雷鸣般的咆哮，然后猛地向画面左边一跃而出，尘土向四周炸开。画面里没有人出现。镜头固定不动。",
  breathy("A thunderous roar that shakes the walls and a heavy impact.", "震得墙壁发抖的雷鸣般的咆哮，和一声沉重的撞击。"))

# =================================================================================================== 合成一份
doc = copy.deepcopy(b15.d)
doc['episodes'] = [
    episode(b15, '剧本第15集｜反派的计划（重写）', '保罗输光了一切，玛丽带来猎手；银匕首和毒液；内线说基利安今天就走；计划：抓走莉莉带去仓库，玛丽要毁她的脸。'),
    episode(b16, '剧本第16集｜印记与离别（重写）', '清晨颈后的新月印记；莉莉问“你对我做了什么”，基利安说现在永远感觉得到她；长老威胁她所以他要走；禁令、额头吻、求婚；车队开出铁门；猎手踩断树枝，莉莉猛回头，黑影爬墙。'),
    episode(b17, '剧本第17集｜银刃之下（重写）', '猎手翻上阳台，闻出她是 Luna，银匕首划出血；车里的基利安平静，她后颈印记发金光，他心口剧痛眼睛变金，吼停车，撕掉车门先跑了。'),
    episode(b18, '剧本第18集｜暴君的回顾（重写）', '莉莉被拖进仓库，保罗玛丽等着；玛丽见血大笑，保罗骂她选了怪物、扬手要打；铁门炸飞，黑狼走出，猎手吓掉刀，莉莉认出金眼睛，黑狼咆哮扑出。'),
]
txt = json.dumps(doc, ensure_ascii=False, indent=1)
open(os.path.join(FOLDER, OUT + '.json'), 'w', encoding='utf-8').write(txt)
open(os.path.join(FOLDER, OUT + '_全选复制粘贴.txt'), 'w', encoding='utf-8').write(txt)
n = sum(len(e['segments']) for e in doc['episodes']); sec = sum(s['duration_seconds'] for e in doc['episodes'] for s in e['segments'])
print(f'{len(doc["episodes"])} 集、{n} 个任务、约 {sec} 秒；文件 {len(txt.encode())/1024:.0f} KB → {OUT}')
for e in doc['episodes']:
    print('  ', e['title'], len(e['segments']), '个任务', sum(s['duration_seconds'] for s in e['segments']), '秒')
