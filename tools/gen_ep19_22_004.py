#!/usr/bin/env python3
"""剧本第 19–22 集（狼王的审判／银毒入骨／血之契约／离不开的牢笼）重写版（2026-10-11，合并稿编号 004）。

写法：先把故事填实、再拆镜头（技巧文档第十二节）；一件事一个镜头、需要时用运镜（第十三节）。
hh 10-11 13:55 说“以后不用额外写测试稿，直接在后续剧情里测”，所以运镜的新写法直接用在正片任务里，
交付说明里标出哪些任务是新写法。

接缝（承接 002 第 18 集末）：18-12 黑狼向左扑出；莉莉跪在仓库左边，流浪狼人在中间偏左，保罗玛丽在门口附近；
仓库的铁门已被炸飞，门洞在画面右边。

大纲缺口和补法：
  ① 流浪狼人怎么死、尸体和匕首 → 不拍穿胸；扑倒＋惨叫被掐断＋匕首特写（毒液，给第 20 集“银毒”埋线）
  ② 黑狼怎么变回人 → 变身用两个镜头：黑雾涌满画面（推近）→ 雾散，拉远看见基利安站着，莉莉跪在脚边
  ③ 他脱外套裹她 → 加一句 “It's me, Lily, I've got you.” 回答 18-11 的 “Is that you, Killian?”
  ④ 莉莉的伤口：观众先看到伤口边缘发黑（基利安没发现，观众比人物知道得多），第 19 集末才咳黑血
  ⑤ “阿贾克斯”是谁、“死斗场”是什么 → 阿贾克斯＝车里那个光头保镖，进来点头；玛丽哭喊 “not the Pit” 让观众明白那是什么地方
  ⑥ 第 20 集没有车：仓库就在庄园后花园，基利安抱着她跑回主楼 → 跑的路上看到黑色血管扩散，医疗室里他才喊出银毒
  ⑦ 狼医“十分钟”之后的反应：基利安的反应特写、掀翻器械、赶人、门被关上，之后才咬手腕
  ⑧ 血契怎么治好她 → 先吸毒血吐进盆里，他低声求她别走，黑色血管退回去，印记发银光，眼睛变银
  ⑨ 反压前后：他先发现她眼睛是银色（一句话），她才翻身；亲密戏全程穿着衣服，只拍表情和手
  ⑩ 第 22 集她为什么跑去书房 → 先拍长老逼他杀她、他拍桌子（和 16 集“长老威胁你”呼应），再拍她醒来发现空床、心口发紧、印记发光、被拉着走
运镜新写法（每个标在说明里）：推近 9 处、拉远 2 处、横向跟拍 2 处，其余固定。
种子 8101–8412（和库里所有稿子不重复）。
"""
import copy, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _h3draft import Batch, FOLDER, breathy, voiced

BASE = '合并稿/002_第15-18集_重写故事_制作稿_追加.json'
OUT = '合并稿/004_第19-22集_狼王审判到离不开的牢笼_制作稿_追加'
SRC = json.load(open(os.path.join(FOLDER, BASE), encoding='utf-8'))

b19, b20, b21, b22 = (Batch(BASE, SRC['title'], s) for s in (8100, 8200, 8300, 8400))

WH = '[[asset:warehouse]]'; GP = '[[asset:garden_path]]'; MR = '[[asset:medical_room]]'; CR = '[[asset:council_room]]'
SD = '[[asset:study_door]]'; BD = '[[asset:bedroom]]'
RG = '[[asset:rogue]]'; WF = '[[asset:black_wolf]]'; PL = '[[asset:paul]]'; MB = '[[asset:mary_black]]'
KG = '[[asset:killian_gold]]'; KGS = '[[asset:killian_gold_shirt]]'; K = '[[asset:killian]]'
LS = '[[asset:lily_shirt]]'; LJ = '[[asset:lily_jacket]]'; LSV = '[[asset:lily_silver]]'
BGD = '[[asset:bodyguard]]'; DOC = '[[asset:doctor]]'; EL = '[[asset:elder]]'

# ------------------------------------------------------------------------------------------------ 新素材（只加到 b19，最后用 b19 的 assets）
b19.scene('medical_room', '地下医疗室',
          "The underground private medical suite of a dark luxurious mansion: white-tiled walls and a pale grey tiled floor, a wide white hospital bed with steel rails and fresh white sheets in the middle of the room with its pillow end at the left, a wheeled instrument trolley with steel trays and glass vials and a glass-fronted medicine cabinet against the left wall, a wheeled heart monitor beside the head of the bed, a heavy steel door with a round wheel handle in the right wall, cold clinical ceiling lights. The reference fixes the layout and decor.",
          "豪华阴沉庄园的地下私人医疗室：白色瓷砖墙面和浅灰色瓷砖地面，房间中间是一张带钢护栏、铺着崭新白床单的宽大病床，枕头一端在左边；左边墙边是带钢托盘和玻璃药瓶的器械推车和玻璃药柜，床头旁是一台带轮子的心电监护仪，右边墙上是一扇带圆形转轮把手的厚重钢门，天花板上是冷冷的医用灯光。参考图固定布局与陈设。",
          "A photorealistic ultra-wide 8:3 cinemascope shot of the underground private medical suite of a dark luxurious mansion: white-tiled walls and a pale grey tiled floor, a wide white hospital bed with steel rails and fresh white sheets in the middle of the room with its pillow end at the left, a wheeled instrument trolley with steel trays and glass vials and a glass-fronted medicine cabinet against the left wall, a wheeled heart monitor beside the head of the bed, a heavy steel door with a round wheel handle in the right wall, cold clinical ceiling lights. "
          "The frame holds the bed, the trolley, the cabinet, the monitor and the steel door.")
b19.scene('council_room', '家族长老会议室',
          "The council room of a dark luxurious mansion: a long polished dark-wood table running across the room from left to right with a row of tall leather chairs along its far side, a tall carved high-backed chair at the head of the table at the left, heavy dark paneled walls with a row of tall windows with dark drapes at the back, a pair of tall dark double doors with large brass handles in the right wall, a dark carpet, cold grey daylight. The reference fixes the layout and decor.",
          "豪华阴沉庄园里的家族长老会议室：一张长长的抛光深色木桌从左到右横过房间，桌子远侧是一排高背皮椅，桌子左端主位是一把高大雕花的高背椅，深色木板墙面，后面是一排挂着深色窗帘的高窗，右边墙上是一对挂着大黄铜把手的高大深色双开门，深色地毯，冷冷的灰色日光。参考图固定布局与陈设。",
          "A photorealistic ultra-wide 8:3 cinemascope shot of the empty council room of a dark luxurious mansion: a long polished dark-wood table running across the room from left to right with a row of tall leather chairs along its far side, a tall carved high-backed chair at the head of the table at the left, heavy dark paneled walls with a row of tall windows with dark drapes at the back, a pair of tall dark double doors with large brass handles in the right wall, a dark carpet, cold grey daylight. "
          "The frame holds the table, the chairs, the windows and the double doors; no people are in the room.")
b19.scene('study_door', '走廊尽头的书房双开门',
          "The upstairs corridor of a dark luxurious mansion in the morning, seen straight on: a long dark-wood paneled wall with amber wall lamps spaced along it, a pale marble floor with a dark runner rug along its length, tall dark double doors with carved panels and large brass handles standing closed at the far right end of the corridor, and the master bedroom's tall single dark-wood door with a brass handle at the far left. The reference fixes the layout and decor.",
          "清晨，阴沉豪华庄园的二楼走廊，正对着看：一道长长的深色木板墙，墙上每隔一段有一盏琥珀色壁灯，浅色大理石地面上顺着走廊铺着深色地毯；走廊最右端是一对雕花、带大黄铜把手的高大深色双开门，关着；最左端是主卧那扇带黄铜把手的高大单开深色木门。参考图固定布局与陈设。",
          "A photorealistic ultra-wide 8:3 cinemascope shot of the upstairs corridor of a dark luxurious mansion in the morning, seen straight on: a long dark-wood paneled wall with amber wall lamps spaced along it, a pale marble floor with a dark runner rug along its length, tall dark double doors with carved panels and large brass handles standing closed at the far right end of the corridor, the master bedroom's tall single dark-wood door with a brass handle at the far left, soft morning light. "
          "The frame holds the paneled wall, the lamps, the rug, the double doors and the bedroom door; no people are in the corridor.")
b19.person('killian_gold_shirt', '基利安（只穿衬衫，金瞳利爪）',
           "Killian, the same very tall, broad-shouldered adult man in his early thirties as in the reference, with short swept-back black hair, a sharp jawline and light stubble, wearing only a white dress shirt with the collar open at the throat and the sleeves rolled to the elbows, a few specks of blood on it, a dark tie pulled loose and hanging, dark trousers and a platinum luxury wristwatch on his left wrist, with no jacket and no waistcoat; his eyes glow a dark gold with narrow vertical pupils, two sharp canine teeth show at the edge of his lips, and long black claws extend from his fingertips. The portrait fixes his identity, clothes and features, not staging.",
           "基利安，和参考图里同一位三十出头、身材极高大、肩膀宽阔的成年男人，黑色短发向后梳，下颌线锋利，有淡淡胡茬；只穿一件白衬衫，领口敞开，袖子卷到手肘，衬衫上有几点血迹，深色领带扯松挂着，深色长裤，左手腕戴铂金豪华腕表，没有外套也没有马甲；眼睛发出暗金色的光，瞳孔是细长的竖瞳，嘴角露出两颗尖利的犬齿，指尖伸出长长的黑色利爪。肖像固定他的长相、衣着和特征，不固定姿势。",
           "A photorealistic half-body portrait of the same man as in the reference image, short swept-back black hair, sharp jawline, light stubble, wearing only a white dress shirt with the collar open and the sleeves rolled to the elbows, a few specks of blood on it, a dark tie pulled loose, a platinum luxury wristwatch on his left wrist, his eyes glowing dark gold with narrow vertical pupils, two sharp canine teeth just visible, long black claws on the fingertips of his hands held at his sides. "
           "He faces the camera with an intense, cold expression. Soft even studio light, plain neutral gray background, natural skin texture with visible pores.", ref='killian')
b19.person('lily_jacket', '莉莉（披着男人黑西装外套，脖子上有血痕）',
           "Lily, the same adult woman in her mid-twenties as in the reference, with long wavy chestnut-brown hair tangled and loose around her shoulders, fair skin and large hazel-green eyes, wearing an oversized white men's cotton dress shirt that falls to mid-thigh, and draped over her shoulders like a cape a man's black suit jacket far too large for her; a thin line of dried blood runs down the left side of her neck; her feet are bare. The portrait fixes her identity and clothes, not staging.",
           "莉莉，和参考图里同一位二十五岁左右的成年女人，栗色长卷发凌乱地披在肩上，皮肤白皙，大大的淡褐绿色眼睛；穿一件肥大的白色男式棉衬衫，下摆到大腿中部，肩上披着一件对她来说大得多的男式黑色西装外套，像披风一样；脖子左侧有一道细细的干掉的血痕；光着脚。肖像固定她的长相和衣着，不固定姿势。",
           "A photorealistic half-body portrait of the same woman as in the reference image, long wavy chestnut-brown hair tangled and loose around her shoulders, large hazel-green eyes, wearing an oversized white men's cotton dress shirt and, draped over her shoulders like a cape, a man's black suit jacket far too large for her; a thin line of dried blood down the left side of her neck. "
           "She faces the camera with a frightened, exhausted expression. Soft even studio light, plain neutral gray background, natural skin texture with visible pores.", ref='lily')
b19.person('lily_silver', '莉莉（银白色的眼睛）',
           "Lily, the same adult woman in her mid-twenties as in the reference, with long wavy chestnut-brown hair loose and tousled around her shoulders, fair skin with a healthy flush, wearing an oversized white men's cotton dress shirt with the collar open at the throat, the left side of her neck smooth and unmarked; her eyes glow a luminous silver-white. The portrait fixes her identity, clothes and eye color, not staging.",
           "莉莉，和参考图里同一位二十五岁左右的成年女人，栗色长卷发松散凌乱地披在肩上，皮肤白皙、脸颊有健康的红晕；穿一件肥大的白色男式棉衬衫，领口敞开，脖子左侧光滑没有任何痕迹；眼睛发出明亮的银白色光。肖像固定她的长相、衣着和眼睛颜色，不固定姿势。",
           "A photorealistic half-body portrait of the same woman as in the reference image, long wavy chestnut-brown hair loose and tousled around her shoulders, a healthy flush on her cheeks, wearing an oversized white men's cotton dress shirt with the collar open, her eyes glowing a luminous silver-white. "
           "She faces the camera with a calm, composed expression. Soft even studio light, plain neutral gray background, natural skin texture with visible pores.", ref='lily')
b19.person('elder', '家族长老',
           "Elder, an old man in his sixties with swept-back white hair, a deeply lined stern face, a thin cruel mouth and cold pale eyes, wearing a black three-piece suit with a silver wolf-head lapel pin and a dark grey tie. The portrait fixes his identity and clothes, not staging.",
           "家族长老，六十多岁的老年男人，白发向后梳，脸上皱纹很深而严厉，嘴唇薄而冷酷，眼睛是冷冷的浅色；穿黑色三件套西装，翻领上别着一枚银色狼头胸针，深灰色领带。肖像固定他的长相和衣着，不固定姿势。",
           "A photorealistic half-body portrait of an old man in his sixties with swept-back white hair, a deeply lined stern face, a thin cruel mouth and cold pale eyes, wearing a black three-piece suit with a silver wolf-head lapel pin and a dark grey tie. "
           "He faces the camera with a stern, cold expression. Soft even studio light, plain neutral gray background, natural skin texture with visible pores.")
b19.character('KillianGoldShirt', 'killian_gold_shirt', copy.deepcopy(SRC['characters']['KillianGold']['voice_description']['en']), copy.deepcopy(SRC['characters']['KillianGold']['voice_description']['zh']))
b19.character('LilyJacket', 'lily_jacket', copy.deepcopy(SRC['characters']['LilyShirt']['voice_description']['en']), copy.deepcopy(SRC['characters']['LilyShirt']['voice_description']['zh']))
b19.character('LilySilver', 'lily_silver',
              "A young adult female voice, low, airy and ethereal with a faintly seductive, cold edge, speaking clear American English. Every word is fully voiced and audible.",
              "年轻成年女声，低沉、空灵，带一点冷冷的魅惑，说清楚的美式英语。每个字都正常发声、清晰可辨。")
b19.character('Elder', 'elder',
              "A mature old male voice, dry, hoarse and commanding with a cold, bitter edge, speaking clear American English. Every word is fully voiced and audible.",
              "年老的男声，干涩、沙哑、带命令口气，有一种冷冷的刻薄，说清楚的美式英语。每个字都正常发声、清晰可辨。")

# ------------------------------------------------------------------------------------------------ 场景布局句
LAY_WH = " Fixed stage layout: the open doorway of the warehouse is at frame-right with bright daylight and drifting dust in it, the blown-off rusted iron door lying flat on the concrete floor beside it; the stacked wooden crates and steel barrels are at frame-left; concrete pillars stand in the middle and shafts of dusty light fall from the high windows at the back."
END_WH = " Dim, dusty light with pale shafts from the high windows, dust hanging in the air, the warehouse softly blurred behind."
LAY_GP = " Fixed stage layout: the gravel path runs from frame-left to frame-right between tall dark hedges; the rusted corrugated-iron warehouse with its open doorway stands at frame-right; the mansion's dark stone wall is far behind at frame-left."
END_GP = " Soft clear morning light, long shadows across the gravel."
LAY_MR = " Fixed stage layout: the wide white hospital bed with steel rails stands in the middle of the frame with its pillow end at frame-left; the instrument trolley with steel trays and the glass-fronted cabinet are against the white-tiled wall at frame-left; the heavy steel door with a round wheel handle is at frame-right; the wheeled heart monitor stands beside the head of the bed."
END_MR = " Cold clinical white light from the ceiling, the white-tiled room softly blurred behind."
LAY_CR = " Fixed stage layout: the long polished dark-wood table runs across the room from frame-left to frame-right; the tall carved high-backed chair at the head of the table is at frame-left; the row of leather chairs lines the far side of the table; the tall dark double doors with brass handles are at frame-right; tall windows with dark drapes are at the back."
END_CR = " Cold grey daylight through the tall windows, the paneled room softly blurred behind."
LAY_SD = " Fixed stage layout: the long dark-wood paneled wall with amber wall lamps runs across the frame; the dark runner rug lies along the pale marble floor; the tall dark double doors with large brass handles stand closed at the far right end of the corridor; the master bedroom's tall single door is at the far left."
END_SD = " Soft clear morning light, the paneled corridor softly blurred behind."
LAY_BD = " Fixed stage layout: the huge dark-wood bed with charcoal-grey linen fills the left and center of the frame; the tall dark-wood door with a brass handle is at frame-right; the floor-to-ceiling windows with the heavy curtains drawn back are at the back."
END_BD = " Bright warm morning sunlight pours through the open curtains across the bed, soft golden light, the room softly blurred behind."

FIX = ('The camera holds still.', '镜头固定不动。')


def T(b, title, dur, chars, assets, refs, img, end, vis_zh, dlg, act_en, act_zh, sound, dep=False, cam=FIX):
    """act_en／act_zh 不含镜头句；cam=(英文镜头句, 中文镜头句)，默认固定。"""
    s = b.task(title, dur, chars, assets, refs, img, end, vis_zh, '0—%d秒，%s' % (dur, cam[1]), dlg,
               act_en + ' ' + cam[0], act_zh + ' ' + cam[1], sound)
    s['depends_on_previous'] = dep
    return s


def episode(b, title, summary):
    lines = []
    for t in b.tasks:
        lines.append((t['title'].split('｜')[1] + '，' + t['visual_zh']).replace('：', '，'))
        for x in t['dialogue']:
            lines.append(f"{x['speaker']}：“{x['text']}”")
    return {'title': title, 'summary': summary, 'script': '\n'.join(lines), 'segments': b.tasks, 'dialogue_language': 'en'}

# =================================================================================================== 第 19 集：狼王的审判
# 观众要看懂：黑狼扑倒猎手（死了，只留一把有毒的银匕首）→ 它用尾巴把莉莉护在肚子底下 → 保罗玛丽吓瘫
# → 黑雾涌来、雾散，基利安站在那里（莉莉认出的金眼睛就是他）→ 脱外套裹她，回答她的“是你吗”
# → 观众另外看到她伤口边缘发黑（他没发现）→ 保罗跪求“我是被逼的” → “杀你们脏了我的手” → 阿贾克斯进来，“扔进死斗场”
# → 玛丽哭喊 “not the Pit” → 门口只剩拖痕和一只鞋 → 莉莉咳出黑血。
# 方向：仓库门洞在画面右边；黑狼从右向左扑；保罗玛丽在右边跪着面朝左；基利安在左边面朝右；阿贾克斯从右边门洞进来。

T(b19, '01｜黑狼扑倒流浪狼人，莉莉缩在一旁', 3, ['Rogue', 'LilyShirt'], ('warehouse', 'rogue', 'black_wolf', 'lily_shirt'), ['warehouse'],
  "Wide shot, in the middle third of the frame, inside the warehouse. Rogue at center-left standing in profile facing frame-right, in the patched black leather jacket, the long scar down his left cheek and across his eye, his knees buckling, both arms raised in front of his face, his mouth open in a scream, his brows pulled up, his wide eyes on the wolf; the silver dagger lies on the concrete at his boots. "
  "The colossal jet-black wolf at frame-right in the open doorway, in profile facing frame-left, crouched low with its shoulders bunched to spring, its dark-gold eyes blazing, its fangs bared. "
  "Lily at the far left of the frame kneeling on the concrete in the oversized white men's shirt, her left hand pressed to her neck, her lips parted, her brows pulled up, her wide eyes on the wolf. "
  "The frame holds exactly two people, Rogue and Lily, and one huge black wolf.",
  END_WH + LAY_WH, "黑狼从门洞一跃扑向流浪狼人，把他撞翻在地，尘土炸开；莉莉在左边吓得缩了一下。",
  None,
  f"A steady wide shot opens from the adopted first frame in {WH}: {WF} springs across the concrete in one enormous leap and slams into {RG}'s chest, bearing him flat onto his back in a blast of dust, his mouth stretched wide in a scream that cuts off short and his brows jerking up. {LS} at the far left flinches, her eyes squeezing shut, her lips parting and her brows pulling up.",
  "一个稳定的宽景，从已采用的开场图继续，场景是废弃仓库：黑狼一个巨大的跳跃扑过水泥地，撞在流浪狼人胸口，把他整个人掀翻在地，尘土炸开，他的惨叫被掐断。最左边的莉莉缩了一下，眼睛紧紧闭上，嘴唇张开，眉头抬起。",
  breathy("A thunderous leap, a heavy crash of bodies on concrete and a scream cut off short.", "雷鸣般的一跃、身体砸在水泥地上的重响，和一声被掐断的惨叫。"))

T(b19, '02｜特写：银匕首躺在地上，毒液滴下', 3, [], ('warehouse', 'black_wolf'), ['warehouse'],
  "Low-angle close-up at floor level, in the middle third of the frame: the silver dagger lying on the grey concrete in sharp focus in the foreground, its polished blade catching the pale light, a bead of pale green venom swelling at the tip; far behind it, softly blurred, the huge black wolf's front paw planted beside the still, dark shape of a man in a black leather jacket lying on his back, one open hand on the concrete near the dagger's hilt. No face is in focus and no one stands in the frame.",
  END_WH, "特写：地上那把银匕首，刃尖上一滴淡绿色的毒液正在鼓起来，远处模糊的黑狼爪子旁躺着一动不动的人。",
  None,
  "A close-up opens from the adopted first frame in " + WH + ": the bead of pale green venom swells, slides down the polished steel and drips onto the concrete with a faint hiss, a wisp of smoke curling up where it lands; far behind, the wolf's paw does not move. No face appears.",
  "一个特写，从已采用的开场图继续，场景是废弃仓库：淡绿色的毒液珠越鼓越大，顺着打磨光亮的刀刃滑下，滴在水泥地上发出细细的嘶声，落点冒起一缕烟；远处黑狼的爪子一动不动。画面里没有清晰的脸。",
  breathy("A faint acid hiss and a low rumbling growl far away.", "细微的酸液嘶声和远处低沉的咆哮声。"),
  cam=('The camera pushes in low along the concrete toward the blade until the green bead fills the frame.', '镜头贴着地面往前推近，一直推到绿色毒液珠占满画面。'))

T(b19, '03｜黑狼的尾巴一扫，把莉莉卷到肚子底下', 3, ['LilyShirt'], ('warehouse', 'black_wolf', 'lily_shirt'), ['warehouse'],
  "Side-on medium shot, in the middle third of the frame: the colossal jet-black wolf standing in the middle of the frame in profile facing frame-left, its head lowered, its dark-gold eyes blazing, its long thick black tail lifted high behind it; Lily kneeling on the concrete at frame-right beside its hind legs, in the oversized white men's shirt, her left hand pressed to the cut on her neck, her chestnut hair tangled, her lips parted, her brows pulled up, her wide wet eyes on the wolf's hind leg beside her. The frame holds exactly one person, Lily, and the black wolf.",
  END_WH + LAY_WH, "黑狼的粗尾巴一扫，把莉莉整个卷进自己毛茸茸的肚子底下，挡住了她的视线。",
  None,
  f"A steady side-on medium shot opens from the adopted first frame in {WH}: the wolf's thick black tail sweeps down in a wide arc, curls around {LS} and draws her in against the thick black fur of its belly, so that she is wrapped inside the curve of its body; her face presses into the fur, her eyes squeezing shut, her lips trembling and her brows pulling together.",
  "一个稳定的侧面中景，从已采用的开场图继续，场景是废弃仓库：黑狼粗粗的黑尾巴划出一个大弧扫下来，卷住莉莉，把她拉到自己厚厚的黑毛肚子上，整个人被裹进狼身体的弧线里；她的脸埋进毛里，眼睛紧紧闭上，嘴唇发颤，眉头拧起。",
  breathy("A heavy whoosh of fur, a muffled sob and a deep rumbling growl.", "毛皮扫过的一声沉响、一声闷住的哭泣和低沉的咆哮声。"))

T(b19, '04｜保罗和玛丽吓得瘫在地上往后爬', 3, ['PaulOnScreen', 'MaryBlack'], ('warehouse', 'paul', 'mary_black'), ['warehouse'],
  "Side-on medium two-shot, both people from the head to the waist, in the middle third of the frame, on the concrete floor of the warehouse, both half-sitting and propped on their hands, in profile facing frame-left. "
  "Paul at frame-left in the creased navy blazer, his mouth open in a scream, his brows pulled up, his red-rimmed eyes wide and staring at the concrete in front of him. "
  "Mary at frame-right in the fitted black wool coat, both hands pressed over her mouth, her sharp green eyes wide, her brows lifted, her honey-blonde bun coming loose. "
  "The frame holds exactly two people: Paul and Mary.",
  END_WH + LAY_WH, "保罗和玛丽瘫坐在地上，吓得惨叫，手脚并用往后爬。",
  None,
  f"A steady side-on medium two-shot opens from the adopted first frame in {WH}: {PL} scrambles backward across the concrete on his heels and hands, his mouth stretching wide in a ragged scream and his brows jerking up. {MB} scrambles back beside him, her hands tearing away from her mouth as she shrieks, her green eyes wide and her brows lifted.",
  "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是废弃仓库：保罗和玛丽用脚跟和双手在水泥地上往后蹭，保罗的嘴张得很大发出嘶哑的惨叫，玛丽的手从嘴上扯开尖叫起来，两人浑身发抖、哭个不停。",
  breathy("Two ragged wordless screams and shoes scrabbling on concrete.", "两声嘶哑的、没有字词的惨叫和鞋子在水泥地上蹬踏的声音。"))

T(b19, '05｜黑雾从黑狼身上涌出来', 3, [], ('warehouse', 'black_wolf'), ['warehouse'],
  "Close-up of the colossal jet-black wolf's head and shoulders, in profile facing frame-left, in the middle third of the frame, in the dusty warehouse, its dark-gold eyes blazing, its heavy jaw lowered, its thick black fur bristling with thin wisps of black mist already curling off it. The frame holds exactly one animal and no people.",
  END_WH, "特写：黑狼的头和肩，金色的眼睛发着光，身上已经有一缕缕黑雾往外冒。",
  None,
  "A close-up opens from the adopted first frame in " + WH + ": thick black mist boils up from the wolf's fur and swirls across the frame, its dark-gold eye flaring once through the smoke until the mist swallows the whole picture in darkness. No people appear.",
  "一个特写，从已采用的开场图继续，场景是废弃仓库：浓浓的黑雾从黑狼的毛里翻涌出来，在画面里打着旋，它暗金色的眼睛在烟里亮了一下，然后黑雾把整个画面吞进黑暗。画面里没有人出现。",
  breathy("A deep rumbling growl turning into a low roaring wind and a crackle like distant thunder.", "低沉的咆哮声变成低低的呼啸风声，和远处雷声般的噼啪声。"),
  cam=("The camera pushes in toward the wolf's glowing gold eye while the mist thickens.", '镜头推向黑狼发光的金色眼睛，同时黑雾越来越浓。'))

T(b19, '06｜雾散，基利安站在那里', 4, ['KillianGold', 'LilyShirt'], ('warehouse', 'killian_gold', 'lily_shirt'), ['warehouse'],
  "Extreme close-up in the middle third of the frame: a pair of dark-gold glowing eyes with narrow vertical pupils, set in the dark outline of a man's brow and nose, inside swirling black mist that fills the rest of the frame, the first thin gaps in the mist showing dusty light behind. His brows are low and his eyes are narrowed. The frame holds exactly one person's eyes, Killian's.",
  END_WH, "特写：翻涌的黑雾里，一双发着暗金色光的竖瞳眼睛。",
  None,
  f"A close-up opens from the adopted first frame in {WH}: the black mist thins and drifts away in long tendrils, revealing {KG} standing tall in the middle of the dust in the black three-piece suit, a few specks of blood on his white shirt, his dark-gold eyes with vertical pupils blazing, his chest heaving, his jaw clenched, his lips pulled back from sharp canine teeth, his brows low and long black claws hanging at his sides; {LS} kneels on the concrete at his feet at frame-right, her wide eyes on his face, her lips parted and her brows pulled up.",
  "一个特写，从已采用的开场图继续，场景是废弃仓库：黑雾一缕缕变薄散去，露出站在尘土中间的基利安，穿着黑色三件套西装，白衬衫上有几点血迹，暗金色的竖瞳喷着光，胸口起伏，咬紧牙关，嘴唇咧开露出尖利的犬齿，眉头压得很低，黑色的利爪垂在身侧；莉莉跪在他脚边的画面右边，睁大的眼睛看着他的脸，嘴唇张开，眉头抬起。",
  breathy("A low wind of fading mist, a deep slow breath and a faint crackle.", "渐渐散去的雾气带起的低低风声、一声深深缓慢的呼吸和细微的噼啪声。"),
  dep=True,
  cam=('The camera pulls out from his eyes until Killian is in full view from head to knees, with Lily kneeling at his feet.', '镜头从他的眼睛往后拉，直到看见基利安从头到膝盖的全貌，莉莉跪在他脚边。'))

T(b19, '07｜他脱下外套裹住她：是我，我在', 6, ['KillianGold', 'LilyShirt'], ('warehouse', 'killian_gold', 'lily_shirt'), ['warehouse'],
  "Side-on medium close-up two-shot, both people from the head to the chest, in the middle third of the frame, on the dusty warehouse floor. "
  "Killian at frame-left kneeling on one knee in profile facing frame-right, in the black three-piece suit with blood specks on his white shirt, his dark-gold eyes with vertical pupils on Lily's face, his jaw clenched, his lips pressed together, his brows drawn together, both hands gripping the lapels of his own jacket. "
  "Lily at frame-right kneeling in profile facing frame-left, in the oversized white men's shirt, a thin dried line of blood down the left side of her neck, her chestnut hair tangled, her wet wide eyes on his face, her lips trembling, her brows pulled up. "
  "The frame holds exactly two people: Killian and Lily.",
  END_WH + LAY_WH, "基利安单膝跪下，脱下西装外套裹住莉莉，哑着嗓子说：是我，莉莉，我在。",
  ('KillianGold', "It's me, Lily, I've got you.", 1.0),
  f"A medium close-up opens from the adopted first frame in {WH}: {KG} shrugs the black jacket off his shoulders and wraps it around {LS}, drawing it closed over her chest with both hands, and speaks in a low, rough, shaking voice, his dark-gold eyes on her face and his jaw tight. {LS} clutches the lapel, a tear sliding down her cheek, her lips trembling and her brows pulling up.",
  "一个中近景，从已采用的开场图继续，场景是废弃仓库：基利安把黑色西装外套从肩上脱下来，裹在莉莉身上，用双手把外套在她胸前拢紧，用低沉粗哑发颤的声音说话，暗金色的眼睛看着她的脸，下颌绷紧。莉莉攥住外套的领子，一滴泪滑下脸颊，嘴唇发颤，眉头抬起。",
  voiced("A shaky breath and the soft rustle of cloth.", "一声发抖的呼吸和布料轻轻的摩擦声。"),
  cam=('The camera pushes in toward their two faces until they fill most of the frame.', '镜头推近到两张脸占满大半个画面。'))

T(b19, '08｜特写：她伤口的边缘在发黑', 3, ['LilyJacket'], ('warehouse', 'lily_jacket'), ['warehouse'],
  "Close-up from the side of Lily's neck and shoulder, in the middle third of the frame: the collar of a big black suit jacket on her shoulder, her chestnut hair tangled against her cheek, a thin red cut across the left side of her neck with dried blood around it, her pale face resting against a man's white shirt at the edge of the frame, her eyes closed, her lips pale and parted, her brows soft. The frame holds exactly one person, Lily.",
  END_WH, "特写：莉莉脖子上那道细细的伤口，边缘慢慢变成紫黑色，细细的黑线从伤口往外爬。",
  None,
  f"A close-up opens from the adopted first frame in {WH}: the edges of the thin red cut darken to purple-black and fine black threads begin to creep outward from it beneath {LJ}'s pale skin, while her chest gives a shallow, shuddering rise.",
  "一个特写，从已采用的开场图继续，场景是废弃仓库：那道细细红色伤口的边缘变成紫黑色，细细的黑线开始从伤口顺着莉莉苍白的皮肤下面往外爬，她的胸口浅浅地、发抖地起伏了一下。",
  breathy("A faint hiss like acid and a thin, shaky breath.", "一声像酸液的细微嘶声和一声单薄发抖的呼吸。"),
  cam=('The camera pushes in on the cut until it fills the frame.', '镜头推近到伤口占满画面。'))

T(b19, '09｜保罗跪着哭求：哥哥，我是被逼的', 6, ['PaulOnScreen', 'MaryBlack'], ('warehouse', 'paul', 'mary_black'), ['warehouse'],
  "Side-on medium two-shot, both people from the head to the knees, in the middle third of the frame, both kneeling on the concrete floor of the warehouse in profile facing frame-left. "
  "Paul at frame-left in the creased navy blazer, his hands clasped in front of his chest, tears streaming down his cheeks, his lips trembling, his brows pulled up in a desperate plea, his red-rimmed eyes on the concrete floor. "
  "Mary kneeling beside him at frame-right in the black wool coat, her honey-blonde bun fallen loose, both hands pressed over her mouth, her wet green eyes on the floor, her brows pulled up. "
  "The frame holds exactly two people: Paul and Mary.",
  END_WH + LAY_WH, "保罗和玛丽跪在地上，保罗合着手哭求：哥哥，求你了，我是被逼的！",
  ('PaulOnScreen', "Brother, please, I was forced!", 1.0),
  f"A steady side-on medium two-shot opens from the adopted first frame in {WH}: {PL} bows forward with his clasped hands shaking and pleads in a high, cracking voice, tears streaming down his face, his lips trembling and his brows pulled up; {MB} shakes beside him, her shoulders heaving, her lips pressed behind her hands and her brows pulled up, her wet eyes on the floor.",
  "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是废弃仓库：保罗向前弯下身，合着的双手发抖，用又高又发裂的声音哀求，眼泪淌满脸，嘴唇发颤，眉头抬起；玛丽在他身边发抖，肩膀起伏，湿润的眼睛看着地面。",
  voiced("A ragged sob and the scrape of knees on concrete.", "一声嘶哑的啜泣和膝盖蹭过水泥地的声音。"))

T(b19, '10｜基利安抱着她：杀你们，脏了我的手', 6, ['KillianGoldShirt', 'LilyJacket'], ('warehouse', 'killian_gold_shirt', 'lily_jacket'), ['warehouse'],
  "Side-on medium shot, from the head to the waist, in the middle third of the frame. "
  "Killian standing at frame-center in profile facing frame-right, in the white dress shirt with the collar open and the sleeves rolled to the elbows, a few specks of blood on it, the dark tie hanging loose, carrying Lily against his chest in both arms, his dark-gold eyes with vertical pupils narrowed and cold on the concrete floor ahead of him at frame-right, his jaw clenched, his lips pulled into a thin cruel curl, his brows low. "
  "Lily lies limp in his arms, her head resting on his shoulder, the black suit jacket wrapped around her, her eyes closed, her lips pale, her brows soft. "
  "The frame holds exactly two people: Killian and Lily.",
  END_WH + LAY_WH, "基利安把莉莉抱在怀里站起来，金色的竖瞳冷冷地盯着地上的两个人，说：杀你们，会脏了我的手。",
  ('KillianGoldShirt', "Killing you would dirty my hands.", 1.0),
  f"A steady side-on medium shot opens from the adopted first frame in {WH}: {KGS} speaks in a low, cold, final voice, his dark-gold eyes narrowed, his jaw tight and the thin cruel curl of his lips widening. {LJ} lies limp against his chest, her eyes closed, her lips pale and her brows soft.",
  "一个稳定的侧面中景，从已采用的开场图继续，场景是废弃仓库：基利安用低沉冰冷、不容回旋的声音说话，暗金色的眼睛眯起，薄薄的残忍笑意扩大，把一动不动的莉莉抱在胸口。",
  voiced("Slow cold breathing and a low echo in the empty warehouse.", "缓慢冰冷的呼吸声和空荡荡的仓库里低低的回声。"))

T(b19, '11｜阿贾克斯走进来：把他们扔进死斗场', 6, ['KillianGoldShirt', 'Bodyguard'], ('warehouse', 'killian_gold_shirt', 'lily_jacket', 'bodyguard'), ['warehouse'],
  "Side-on medium two-shot, both men from the head to the waist, in the middle third of the frame, inside the warehouse. "
  "Killian at frame-left in profile facing frame-right, in the white dress shirt with the collar open and the sleeves rolled, holding Lily in both arms against his chest, his dark-gold eyes with vertical pupils cold and fixed on Ajax, his jaw clenched, his lips pressed, his brows low. "
  "Lily lies limp in his arms wrapped in a black suit jacket, her face turned into his shoulder, her eyes closed, her lips pale, her brows soft. "
  "Bodyguard, called Ajax, at frame-right in profile facing frame-left, a tall shaved-headed man in the black suit with a clear earpiece, dust on his shoulders, his stern impassive face, his lips pressed together, his brows level, his eyes on Killian. "
  "The frame holds exactly three people: Killian, Lily in his arms, and Bodyguard.",
  END_WH + LAY_WH, "光头保镖阿贾克斯从门洞走进来站定；基利安下令：阿贾克斯，把他们扔进死斗场。",
  ('KillianGoldShirt', "Ajax, throw them in the Pit.", 1.0),
  f"A steady side-on medium two-shot opens from the adopted first frame in {WH}: {KGS} gives the order in a low, flat, merciless voice, his dark-gold eyes on Ajax, his jaw tight and his brows low. {LJ} lies limp in his arms, her lips pale and her brows soft. {BGD} gives one short nod, his stern face impassive, his lips pressed and his brows level.",
  "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是废弃仓库：基利安用低沉平板、毫不留情的声音下令，暗金色的眼睛看着阿贾克斯；保镖短短点了一下头，严肃的脸毫无表情，嘴唇抿着，眉头平整。",
  voiced("A low echo and the crunch of boots on rubble.", "低低的回声和靴子踩在碎石上的咯吱声。"))

T(b19, '12｜玛丽尖叫：不要，别扔去死斗场', 6, ['MaryBlack', 'PaulOnScreen'], ('warehouse', 'mary_black', 'paul'), ['warehouse'],
  "Side-on medium close-up two-shot, both people from the head to the chest, in the middle third of the frame, kneeling on the concrete in profile facing frame-left. "
  "Mary in front at frame-left in the black wool coat, her honey-blonde hair wild, her head thrown back and her mouth wide open in a scream, tears streaming down her face, her eyes squeezed shut, her brows pulled up. "
  "Paul behind her at frame-right in the creased navy blazer, both hands pressed over his face, his shoulders shaking, his brows pulled together above his fingers. "
  "The frame holds exactly two people: Mary and Paul.",
  END_WH + LAY_WH, "玛丽仰着头尖叫：不，别扔我们去死斗场，求你了！保罗捂着脸哭。",
  ('MaryBlack', "No, not the Pit, please!", 1.0),
  f"A steady side-on medium close-up two-shot opens from the adopted first frame in {WH}: {MB} screams the plea in a shrill, cracking voice, tears running down her face, her mouth wide and her brows pulled up. {PL} crumples beside her, his hands pressed over his face, his lips pressed tight and his brows pulled together, his shoulders heaving.",
  "一个稳定的侧面中近景双人镜头，从已采用的开场图继续，场景是废弃仓库：玛丽用又尖又发裂的声音喊出求饶，眼泪淌满脸；保罗在她身边瘫软下去，双手捂着脸，肩膀起伏。",
  voiced("A shrill echoing scream and a ragged sob.", "一声尖利回响的尖叫和一声嘶哑的啜泣。"))

T(b19, '13｜门洞边只剩拖痕和一只鞋', 3, [], ('warehouse',), ['warehouse'],
  "Wide shot of the warehouse floor near the open doorway, in the middle third of the frame: long drag marks scraped through the dust across the grey concrete toward the bright open doorway at frame-right, one brown leather loafer lying on its side beside them, the blown-off rusted iron door lying flat beside the doorway, pale dust drifting in the light shafts. No people are in the frame.",
  END_WH + LAY_WH, "仓库的地上，几道拖痕一直通向门洞，旁边孤零零一只皮鞋；尖叫声越来越远。",
  None,
  "A steady wide shot opens from the adopted first frame in " + WH + ": two screams grow fainter and fainter somewhere beyond the open doorway at frame-right until they are gone, while the dust drifts slowly down through the light and the lost loafer lies still. No people appear.",
  "一个稳定的宽景，从已采用的开场图继续，场景是废弃仓库：两声尖叫在画面右边门洞外越来越远，直到消失，灰尘在光束里慢慢落下，那只掉了的皮鞋一动不动。画面里没有人出现。",
  breathy("Two wordless screams growing fainter, then a hush and a low wind.", "两声没有字词的尖叫越来越远，然后是一片寂静和低低的风声。"))

T(b19, '14｜莉莉咳出黑血，眼睛合上', 6, ['KillianGoldShirt', 'LilyJacket'], ('warehouse', 'killian_gold_shirt', 'lily_jacket'), ['warehouse'],
  "Side-on medium close-up two-shot, both people from the head to the chest, in the middle third of the frame, inside the warehouse. "
  "Killian at frame-center in profile facing frame-right, in the white dress shirt with the collar open, holding Lily against his chest in both arms, his dark-gold eyes on her face, his jaw clenched, his lips pressed, his brows drawn together. "
  "Lily in his arms, her head resting back over his left arm, in the oversized white men's shirt with the black suit jacket around her, her face turned up toward him, her eyes half closed, her lips pale and parted, her brows soft. "
  "The frame holds exactly two people: Killian and Lily.",
  END_WH + LAY_WH, "莉莉在他怀里猛地咳出一口黑血，头往后一垂；基利安慌了，喊她别睡。",
  ('KillianGoldShirt', "Lily, stay with me!", 1.5),
  f"A steady side-on medium close-up opens from the adopted first frame in {WH}: {LJ}'s body jerks and she coughs, and dark, almost black blood wells from her lips and runs down her chin onto his white shirt; her eyes roll half shut and her head sags back over his arm. {KGS}'s dark-gold eyes snap wide, his jaw dropping, his brows crashing together, and he cries out hoarsely.",
  "一个稳定的侧面中近景，从已采用的开场图继续，场景是废弃仓库：莉莉的身体猛地一抽，咳了起来，深得几乎发黑的血从她嘴里涌出，顺着下巴淌到他的白衬衫上；她的眼睛翻成半闭，头往后垂在他的手臂上。基利安暗金色的眼睛猛地睁大，下巴掉下来，眉头拧在一起，嘶哑地喊出声。",
  voiced("A wet, rattling cough and a sharp gasp.", "一声湿湿的、带着杂音的咳嗽和一声急促的抽气。"))

# =================================================================================================== 第 20 集：银毒入骨
# 原大纲写“回程的车内”，但仓库就在庄园后花园，没有车：基利安抱着她跑回主楼。
# 观众要看懂：黑色血管在扩散（路上先看到）→ 进医疗室放下她 → 他认出是银毒 → 狼医跪下说“只剩十分钟”
# → 他的反应 → 掀翻器械 → 赶人、门被关上 → 低声誓言 → 咬自己手腕 → 喂血 → 吻伤口。
# 方向：他从仓库向左跑回主楼；医疗室的钢门在画面右边，他从右边进来向左走。

T(b20, '01｜基利安抱着她跑过后花园', 4, ['KillianGoldShirt', 'LilyJacket'], ('garden_path', 'killian_gold_shirt', 'lily_jacket'), ['garden_path'],
  "Side-on wide-medium shot, from the head to the knees, in the middle third of the frame, on the gravel path between the tall dark hedges. "
  "Killian at frame-center in profile facing frame-left, in the white dress shirt with the collar open and the sleeves rolled, a few specks of blood on it, carrying Lily in both arms against his chest, his dark-gold eyes ahead on the mansion's dark stone wall far at frame-left, his jaw clenched, his lips pressed, his brows crashing together. "
  "Lily lies limp in his arms, her head resting on his shoulder, the black suit jacket wrapped around her, a smear of dark blood at the corner of her pale lips, her eyes closed, her brows soft. The rusted warehouse with its open doorway stands behind him at frame-right. "
  "The frame holds exactly two people: Killian and Lily.",
  END_GP + LAY_GP, "基利安抱着莉莉，在后花园的小路上拔腿狂奔，朝庄园主楼的方向跑。",
  None,
  f"A wide-medium shot opens from the adopted first frame in {GP}: {KGS} breaks into a hard run along the gravel toward frame-left, gravel spraying under his shoes, his jaw clenched and his brows crashing together. {LJ}'s head bounces against his shoulder and her loose hair swings, her lips pale and her brows soft.",
  "一个宽中景，从已采用的开场图继续，场景是后花园的小路：基利安沿着碎石路朝画面左边拔腿狂奔，碎石在鞋底下飞溅，莉莉的头在他肩上颠着，披散的头发甩动。",
  breathy("Pounding footsteps on gravel and a harsh, rapid breath.", "碎石路上急促沉重的脚步声和粗重飞快的喘息声。"),
  cam=('The camera tracks sideways with him at running pace, keeping him in the middle of the frame as the hedges stream past behind.', '镜头横向跟拍他奔跑，让他始终在画面中间，身后的篱笆一路掠过。'))

T(b20, '02｜特写：黑色血管在她脖子上蔓延', 3, ['LilyJacket'], ('garden_path', 'lily_jacket'), ['garden_path'],
  "Close-up from slightly above and from the side of Lily's neck and shoulder, in the middle third of the frame: the collar of a big black suit jacket on her shoulder, a thin cut across the left side of her neck with dark, almost black threads of veins beginning to branch out beneath her pale skin, her chestnut hair tangled, her face pale, her eyes closed, her lips parted with a smear of dark blood, her brows soft; blurred dark hedges far behind. The frame holds exactly one person, Lily.",
  END_GP, "特写：莉莉脖子上的伤口，黑色的血管像墨水一样在皮肤下往锁骨、往心口爬。",
  None,
  f"A close-up opens from the adopted first frame in {GP}: fine black veins branch out from the cut and crawl beneath {LJ}'s pale skin across her collarbone toward her chest like spreading ink, while her chest gives a shallow shuddering rise and her head rocks with his running steps.",
  "一个特写，从已采用的开场图继续，场景是后花园的小路：细细的黑色血管从伤口分叉，在莉莉苍白的皮肤下面像蔓延的墨水一样爬过锁骨，朝胸口去，她的胸口浅浅地、发抖地起伏，头随着他奔跑的脚步轻轻晃动。",
  breathy("A faint hiss like acid, pounding footsteps and a thin, shaky breath.", "一声像酸液的细微嘶声、沉重的脚步声和一声单薄发抖的呼吸。"),
  cam=('The camera pushes in on her neck until the black veins fill most of the frame.', '镜头推近到黑色血管占满大半个画面。'))

T(b20, '03｜他冲进医疗室，把她放到病床上', 4, ['KillianGoldShirt', 'LilyJacket'], ('medical_room', 'killian_gold_shirt', 'lily_jacket'), ['medical_room'],
  "Side-on wide-medium shot, both from the head to the feet, in the middle third of the frame, in the underground medical room. "
  "Killian just inside the heavy steel door at frame-right, in profile facing frame-left, in the white dress shirt with the collar open and the sleeves rolled, carrying Lily in both arms, his dark-gold eyes on the white hospital bed in the middle of the room at frame-left, his jaw clenched, his lips pressed, his brows crashing together. "
  "Lily lies limp in his arms, her head hanging back over his arm and her bare feet dangling, the black suit jacket wrapped around her, her eyes closed, her face deathly pale, her lips parted, her brows soft. "
  "The frame holds exactly two people: Killian and Lily.",
  END_MR + LAY_MR, "基利安抱着莉莉冲进地下医疗室，三大步走到病床边，把她放下。",
  None,
  f"A steady side-on wide-medium shot opens from the adopted first frame in {MR}: {KGS} crosses the tiled floor in three long strides, his jaw clenched and his brows crashing together, and lays her down on the white hospital bed. {LJ} sinks into the pillow, her chestnut hair spilling out, her lips pale and her brows soft, while his hands linger on her shoulders and his lips press hard.",
  "一个稳定的侧面宽中景，从已采用的开场图继续，场景是地下医疗室：基利安三个大步走过瓷砖地面，把莉莉放到白色病床上，她的头陷进枕头，栗色头发散开；他的手在她肩上停了一下，嘴唇抿得发白，眉头拧在一起。",
  breathy("Heavy running steps on tile, a soft thud on the mattress and a ragged breath.", "瓷砖上沉重奔跑的脚步声、床垫上一声轻响和一声粗重的喘息。"))

T(b20, '04｜基利安认出是银毒，喊医生', 6, ['KillianGoldShirt', 'LilyJacket'], ('medical_room', 'killian_gold_shirt', 'lily_jacket'), ['medical_room'],
  "Side-on medium close-up two-shot, both people from the head to the chest, in the middle third of the frame, in the underground medical room. "
  "Lily lying on her back on the white pillow in the middle of the frame, her head at frame-left and her body running toward frame-right, the black jacket open at her collar, fine black veins branching from the thin cut on the left side of her neck across her collarbone, her eyes closed, her lips pale and parted, her brows soft. "
  "Killian standing at the head of the bed at frame-left, bent over her, in profile facing frame-right, in the white dress shirt with the loosened dark tie hanging, one hand flat on the pillow beside her head, his dark-gold eyes wide and fixed on the black veins on her neck, his jaw clenching, his lips pulled back from his canine teeth, his brows crashing together. "
  "The frame holds exactly two people: Killian and Lily.",
  END_MR + LAY_MR, "基利安看着她脖子上的黑色血管，脸色骤变，喊道：这是银毒，快叫医生！",
  ('KillianGoldShirt', "It's silver poison, get the doctor!", 1.0),
  f"A steady side-on medium close-up two-shot opens from the adopted first frame in {MR}: {KGS} shouts in a raw, cracking voice, his dark-gold eyes locked on the black veins on her neck, his jaw clenching and his brows crashing together, his claws digging into the pillow. {LJ} lies motionless, her lips pale and her brows soft, a shallow breath lifting her chest.",
  "一个稳定的侧面中近景双人镜头，从已采用的开场图继续，场景是地下医疗室：基利安用粗哑发裂的声音喊，暗金色的眼睛死死盯着她脖子上的黑色血管，爪子抠进枕头；莉莉一动不动，浅浅的呼吸让胸口起伏。",
  voiced("A sharp ragged breath and the beep of a heart monitor.", "一声尖锐粗重的呼吸和心电监护仪的滴声。"))

T(b20, '05｜狼医跪下：她只剩十分钟', 6, ['Doctor'], ('medical_room', 'doctor'), ['medical_room'],
  "Side-on medium shot of Doctor alone, from the head to the knees, in the middle third of the frame, in profile facing frame-left, standing at the foot of the white hospital bed (its steel rail and white sheet at frame-left), in the long white doctor's coat, his stethoscope swinging, a silver tray of syringes in his shaking hands, his gray hair disordered, his lips trembling, his brows pulled up, his wide terrified eyes on the white sheet of the bed. The frame holds exactly one person, Doctor.",
  END_MR + LAY_MR, "狼医捧着针剂冲到床边，看了一眼伤口，腿一软跪下，颤声说：她只剩十分钟了，Alpha！",
  ('Doctor', "She has ten minutes, Alpha!", 1.0),
  f"A steady side-on medium shot opens from the adopted first frame in {MR}: {DOC}'s knees give out and he drops onto both knees on the tiled floor as the tray of syringes clatters away, and he gasps the words in a thin, cracking, terrified voice, his lips trembling, his brows pulled up and his wide eyes on the bed.",
  "一个稳定的侧面中景，从已采用的开场图继续，场景是地下医疗室：狼医的腿一软，双膝跪在瓷砖地上，一盘针剂哐啷滑出去，他用单薄发裂、吓坏了的声音喘着说话，嘴唇发颤，眉头抬起，睁大的眼睛看着病床。",
  voiced("A clatter of metal on tile and a trembling gasp.", "金属掉在瓷砖上的哐啷声和一声发抖的喘息。"))

T(b20, '06｜基利安的脸：愤怒退去，只剩绝望', 3, ['KillianGoldShirt'], ('medical_room', 'killian_gold_shirt'), ['medical_room'],
  "Medium close-up of Killian alone, from the head to the chest, in the middle third of the frame, in profile facing frame-right, standing at the bedside in the white dress shirt with the loosened dark tie, his head bowed, his dark-gold eyes lowered toward the white sheet at the bottom of the frame, his jaw trembling, his lips pressed into a hard line, his brows knitting upward in anguish, his eyes glistening. The frame holds exactly one person, Killian.",
  END_MR, "特写：基利安听完“十分钟”，脸上的怒气一点点退掉，下巴发抖，眼睛湿了。",
  None,
  f"A close-up opens from the adopted first frame in {MR}: the fury drains from {KGS}'s face and his jaw begins to tremble, his lips pressing into a hard line, his brows knitting upward and his dark-gold eyes glistening and unblinking.",
  "一个近景，从已采用的开场图继续，场景是地下医疗室：基利安脸上的怒气一点点退去，下巴开始发抖，嘴唇抿成一条硬线，眉头往上拧，暗金色的眼睛湿了，一眨不眨。",
  breathy("A slow shuddering breath and the faint beep of a heart monitor.", "一声缓慢发抖的呼吸和心电监护仪细微的滴声。"),
  cam=('The camera pushes in toward his face until his eyes fill the top half of the frame.', '镜头推近到他的眼睛占满画面上半部分。'))

T(b20, '07｜他一把掀翻器械推车', 3, ['KillianGoldShirt', 'Doctor'], ('medical_room', 'killian_gold_shirt', 'doctor'), ['medical_room'],
  "Side-on wide-medium shot, in the middle third of the frame, in the underground medical room. "
  "Killian standing at frame-center in profile facing frame-left, in the white dress shirt with the loosened tie, his right arm drawn back, his dark-gold eyes blazing, his jaw clenched, his lips pulled back from sharp teeth, his brows crashing together; the wheeled instrument trolley loaded with steel trays and glass vials beside him at frame-left. "
  "Doctor kneeling on the tiles at frame-right in the white coat, his hands raised in front of his face, his lips parted, his brows pulled up, his wide eyes on Killian. The white hospital bed is behind them at the back of the room. "
  "The frame holds exactly two people: Killian and Doctor.",
  END_MR + LAY_MR, "基利安一臂扫过器械推车，托盘和药瓶飞出去砸在墙上；狼医抱着头缩起来。",
  None,
  f"A steady side-on wide-medium shot opens from the adopted first frame in {MR}: {KGS} sweeps his arm across the trolley, his jaw clenched and his brows crashing together, and the trays, vials and instruments fly across the room and smash against the tiled wall in a spray of glass. {DOC} flinches with his arms flung over his head, his lips parted and his brows pulled up.",
  "一个稳定的侧面宽中景，从已采用的开场图继续，场景是地下医疗室：基利安一条手臂横扫过推车，托盘、药瓶和器械飞过房间砸在瓷砖墙上，玻璃碎成一片，狼医双臂抱头缩了一下。",
  breathy("A violent crash of metal and shattering glass.", "金属的猛烈撞击声和玻璃碎裂声。"))

T(b20, '08｜他吼：全都滚出去', 6, ['KillianGoldShirt'], ('medical_room', 'killian_gold_shirt'), ['medical_room'],
  "Side-on medium close-up of Killian alone, from the head to the waist, in the middle third of the frame, in profile facing frame-right, in the white dress shirt with the loosened tie, his right arm extended and his claws pointing at the heavy steel door with the round wheel handle at frame-right, his dark-gold eyes blazing on the door, his mouth open in a roar, his jaw clenched, his brows crashing together. The frame holds exactly one person, Killian.",
  END_MR + LAY_MR, "基利安伸手指着钢门，怒吼着让所有人滚出去。",
  ('KillianGoldShirt', "Get out, all of you, now!", 1.0),
  f"A steady side-on medium close-up opens from the adopted first frame in {MR}: {KGS} roars the order in a raw, thunderous voice, his arm outstretched and his dark-gold eyes blazing at the door, his mouth wide, his jaw clenched and his brows crashing together.",
  "一个稳定的侧面中近景，从已采用的开场图继续，场景是地下医疗室：基利安用粗哑如雷的声音怒吼着下令，手臂伸直，暗金色的眼睛对着门喷火。",
  voiced("A thunderous roar echoing off the white tiles.", "雷鸣般的怒吼在白瓷砖墙上回响。"))

T(b20, '09｜狼医逃出去，钢门重重关上', 3, ['Doctor'], ('medical_room', 'doctor'), ['medical_room'],
  "Side-on wide shot of the heavy steel door with the round wheel handle in the right wall of the medical room, in the middle third of the frame: Doctor in the long white doctor's coat stumbling toward the open door at frame-right, half-turned, his stethoscope swinging, his lips parted, his brows pulled up, his wide terrified eyes on the door handle; the foot of the white hospital bed at the far left. The frame holds exactly one person, Doctor.",
  END_MR + LAY_MR, "狼医连滚带爬冲出钢门，门在他身后“砰”地关死。",
  None,
  f"A steady side-on wide shot opens from the adopted first frame in {MR}: {DOC} scrambles through the doorway into the dark hallway beyond, his lips parted and his brows pulled up, and the heavy steel door swings shut behind him with a deep boom, shaking dust from the ceiling; the doorway is left shut and empty.",
  "一个稳定的侧面宽景，从已采用的开场图继续，场景是地下医疗室：狼医连滚带爬冲出门洞，跑进外面昏暗的走廊，沉重的钢门在他身后“砰”地合上，震得天花板落下灰尘；门口留下一扇关死的空门。",
  breathy("Scrambling shoes, a deep metallic boom and a hush.", "慌乱的鞋声、一声深沉的金属闷响，然后一片寂静。"))

T(b20, '10｜他贴着她低声发誓：连死神也带不走你', 6, ['KillianGoldShirt', 'LilyJacket'], ('medical_room', 'killian_gold_shirt', 'lily_jacket'), ['medical_room'],
  "Side-on close two-shot, both people from the head to the shoulders, in the middle third of the frame, in the underground medical room. "
  "Lily lying on her back on the white pillow, her head in the middle of the frame, the black jacket open at her collar, the black veins visible on her neck, her eyes closed, her lips pale and parted, her brows soft. "
  "Killian bent very close over her at frame-left, in profile facing frame-right, his forehead almost touching hers, one hand cupping her cheek, his dark-gold eyes glistening and fixed on her face, his jaw trembling, his lips pressed, his brows drawn up in anguish. "
  "The frame holds exactly two people: Killian and Lily.",
  END_MR + LAY_MR, "屋里只剩他们两个；基利安贴近她的脸，颤声发誓：连死神也不能把你带走。",
  ('KillianGoldShirt', "Not even death can take you.", 1.0),
  f"A steady side-on close two-shot opens from the adopted first frame in {MR}: {KGS} whispers the vow in a trembling, savage voice, his thumb brushing slowly across her cheek, his dark-gold eyes glistening, his jaw trembling. {LJ} lies still, her lips pale and her brows soft, a shallow breath lifting her chest.",
  "一个稳定的侧面近景双人镜头，从已采用的开场图继续，场景是地下医疗室：基利安用发抖又凶狠的声音低声发誓，拇指慢慢擦过她的脸颊，暗金色的眼睛湿亮；莉莉一动不动，浅浅的呼吸让胸口起伏。",
  voiced("A trembling whisper and the slow beep of a heart monitor.", "发抖的低语和心电监护仪缓慢的滴声。"))

T(b20, '11｜他咬破自己的手腕', 3, ['KillianGoldShirt'], ('medical_room', 'killian_gold_shirt'), ['medical_room'],
  "Close-up of Killian alone, from the head to the chest, in the middle third of the frame, in profile facing frame-right, in the white dress shirt with the sleeve rolled to the elbow, his left forearm raised to his mouth, his lips pulled back from two long sharp canine teeth hovering over the inside of his left wrist, his dark-gold eyes fixed on his wrist, his jaw tight, his brows drawn down. The frame holds exactly one person, Killian.",
  END_MR, "特写：基利安把左手腕举到嘴边，獠牙对准手腕，狠狠咬下去，血涌出来。",
  None,
  f"A steady close-up opens from the adopted first frame in {MR}: {KGS} sinks his fangs into his own wrist with a hard bite, his eyes squeezing shut and his brows crashing together; dark red blood wells up and runs down his forearm.",
  "一个稳定的特写，从已采用的开场图继续，场景是地下医疗室：基利安用獠牙狠狠咬进自己的手腕，眼睛紧闭，眉头拧在一起，深红色的血涌出来，顺着小臂淌下。",
  breathy("A sharp wet crunch and a hard exhale through the teeth.", "一声尖锐的湿湿的咬合声和牙缝里一口用力呼出的气。"))

T(b20, '12｜他把流血的手腕按到她嘴边', 4, ['KillianGoldShirt', 'LilyJacket'], ('medical_room', 'killian_gold_shirt', 'lily_jacket'), ['medical_room'],
  "Side-on close two-shot, both from the head to the shoulders, in the middle third of the frame. "
  "Lily lying on her back on the white pillow at frame-center, her head tilted back, the black jacket open at her collar, black veins on her neck, her eyes closed, her lips pale and parted, her brows soft. "
  "Killian at frame-left bent over her in profile facing frame-right, his right hand under her jaw tilting her face up, his left wrist with a fresh bleeding bite held over her parted lips, his dark-gold eyes fixed on her face, his jaw tight, his lips pressed, his brows drawn down. "
  "The frame holds exactly two people: Killian and Lily.",
  END_MR + LAY_MR, "基利安托起她的下巴，把流着血的手腕按在她嘴唇上，让血流进她嘴里。",
  None,
  f"A steady side-on close two-shot opens from the adopted first frame in {MR}: {KGS} presses his bleeding wrist to {LJ}'s lips, dark red blood running into her mouth and down her chin; her throat moves in a small swallow and her brows draw together faintly, while his dark-gold eyes stay locked on her face.",
  "一个稳定的侧面近景双人镜头，从已采用的开场图继续，场景是地下医疗室：基利安把流血的手腕按在莉莉的嘴唇上，深红色的血流进她嘴里，沿下巴淌下；她的喉咙轻轻动了一下，眉头微微拧起，他暗金色的眼睛一直盯着她的脸。",
  breathy("A faint swallow and the slow beep of a heart monitor.", "一声轻轻的吞咽声和心电监护仪缓慢的滴声。"))

T(b20, '13｜他低头吻上她脖子上的黑色伤口', 3, ['KillianGoldShirt', 'LilyJacket'], ('medical_room', 'killian_gold_shirt', 'lily_jacket'), ['medical_room'],
  "Side-on close two-shot, both from the head to the shoulders, in the middle third of the frame. "
  "Lily lying on her back on the white pillow at frame-center, her head tilted back, blood smeared on her lips, the black jacket open at her collar, black veins around the cut on her neck, her eyes closed, her brows soft. "
  "Killian at frame-left bending toward her neck in profile facing frame-right, his lowered wrist stained dark red, his dark-gold eyes fixed on the cut, his jaw tight, his lips parting, his brows drawn down. "
  "The frame holds exactly two people: Killian and Lily.",
  END_MR + LAY_MR, "他低下头，嘴唇贴上她脖子上那道发黑的伤口。",
  None,
  f"A steady side-on close two-shot opens from the adopted first frame in {MR}: {KGS} lowers his head and presses his lips to the black-veined cut on {LJ}'s neck; her head tilts back on the pillow, her lips parting and her brows drawing together, and the black veins beside the cut shiver.",
  "一个稳定的侧面近景双人镜头，从已采用的开场图继续，场景是地下医疗室：基利安低下头，嘴唇贴在莉莉脖子上那道爬满黑色血管的伤口上；她的头往后仰在枕头上，嘴唇张开，眉头拧起，伤口旁的黑色血管颤了一下。",
  breathy("A soft low sound and a slow breath.", "一声轻轻的低低的响声和缓慢的呼吸声。"), dep=True)

# =================================================================================================== 第 21 集：血之契约
# 观众要看懂：他吸出毒血吐掉（先去毒）→ 低声求她别走（时间在过）→ 黑色血管退回去 → 印记发银光（血契起作用）
# → 眼睛变银 → 他先发现“你的眼睛是银色的” → 她翻身把他按住 → “你的血好甜” → 他理智崩断。
# 亲密戏全程穿衣，只拍表情和手；最后停在他的眼睛上，不拍后面。

T(b21, '01｜他吸出毒血，吐进铁盆', 4, ['KillianGoldShirt', 'LilyJacket'], ('medical_room', 'killian_gold_shirt', 'lily_jacket'), ['medical_room'],
  "Side-on close two-shot, both from the head to the shoulders, in the middle third of the frame, in the underground medical room. "
  "Lily lying on her back on the white pillow with her head tilted back and to the right, her eyes closed, her lips smeared with dark red, black veins around the cut on the left side of her neck, her brows soft. "
  "Killian bent over her at frame-left in profile facing frame-right, his lips pressed to the cut on her neck, his eyes closed, his jaw tight, his brows drawn together. A small steel basin stands on a tray on the bedside table at frame-right. "
  "The frame holds exactly two people: Killian and Lily.",
  END_MR + LAY_MR, "基利安用嘴吸出她伤口里的毒血，抬头吐进床边的铁盆里。",
  None,
  f"A steady side-on close two-shot opens from the adopted first frame in {MR}: {KGS} draws back with dark, inky blood on his lips, turns his head and spits it into the steel basin at frame-right with a splash, then wipes his mouth with the back of his hand, his dark-gold eyes blazing, his jaw clenched and his brows low, and lowers his mouth to her neck again. {LJ} lies unmoving, her lips smeared with dark red and her brows soft.",
  "一个稳定的侧面近景双人镜头，从已采用的开场图继续，场景是地下医疗室：基利安抬起头，嘴唇上沾着墨黑的血，扭头“噗”地吐进画面右边的铁盆里，用手背擦了一下嘴，暗金色的眼睛喷着光，下颌绷紧，眉头压低，然后又低头贴上她的脖子；莉莉一动不动。",
  breathy("A wet draw of breath, a splash and a heavy exhale.", "一声湿湿的吸气、一声水花声和一口沉重的呼气。"))

T(b21, '02｜他额头抵着她的额头：不准你离开我', 6, ['KillianGoldShirt', 'LilyJacket'], ('medical_room', 'killian_gold_shirt', 'lily_jacket'), ['medical_room'],
  "Side-on close two-shot, both from the head to the shoulders, in the middle third of the frame, in the underground medical room. "
  "Lily lying on her back on the white pillow, black veins still faintly visible around the cut on her neck, dark blood smeared on her pale lips, her eyes closed, her brows soft. "
  "Killian bent over her at frame-left in profile facing frame-right, his forehead pressed to hers, one hand cupping her cheek, his eyes shut, his jaw trembling, his lips pressed, his brows drawn up in anguish. "
  "The frame holds exactly two people: Killian and Lily.",
  END_MR + LAY_MR, "毒血吐完了，他额头抵着她的额头，颤着声音说：不准你离开我。",
  ('KillianGoldShirt', "Don't you dare leave me.", 1.0),
  f"A steady side-on close two-shot opens from the adopted first frame in {MR}: {KGS} whispers in a shaking, raw voice, his forehead pressed to hers and his thumb stroking her cheek, his jaw trembling and his brows drawn up in anguish; {LJ} lies still, her lips pale and parted.",
  "一个稳定的侧面近景双人镜头，从已采用的开场图继续，场景是地下医疗室：基利安用发抖粗哑的声音低声说话，额头抵着她的额头，拇指轻轻抚着她的脸颊，下颌发颤，眉头痛苦地抬起；莉莉一动不动，嘴唇苍白微张。",
  voiced("A raw whisper and the slow beep of a heart monitor.", "粗哑的低语和心电监护仪缓慢的滴声。"), dep=True)

T(b21, '03｜黑色血管退回伤口，皮肤恢复', 3, ['LilyJacket', 'KillianGoldShirt'], ('medical_room', 'lily_jacket', 'killian_gold_shirt'), ['medical_room'],
  "Close-up of Lily's neck and collarbone from slightly above and the side, in the middle third of the frame: fine black veins branching from the cut on the left side of her neck across her collarbone, her pale skin damp, the collar of the black jacket at the edge of the frame, the white pillow beneath her chestnut hair, her eyes closed, her lips pale, her brows soft. At the very top edge of the frame the dark hair of Killian's bowed head, his eyes shut, his jaw tight, his brows drawn together. The frame holds exactly two people: Lily, and Killian at the edge.",
  END_MR, "特写：她脖子上的黑色血管像墨水被抽回去一样退回伤口，皮肤恢复了血色。",
  None,
  f"A close-up opens from the adopted first frame in {MR}: the black veins on {LJ}'s neck retreat like ink drawn back into the cut, fading from her collarbone to her neck until her skin is smooth and pale and the cut closes to a thin pink line; at the edge of the frame {KGS}'s dark head stays bowed at her shoulder, his eyes shut, his jaw tight and his brows drawn together.",
  "一个特写，从已采用的开场图继续，场景是地下医疗室：莉莉脖子上的黑色血管像墨水被抽回伤口一样往回退，从锁骨退到脖子，直到皮肤变得光滑苍白，伤口收成一条细细的粉红线；画面边缘，基利安黑色的头仍然低在她肩边，眼睛闭着，下颌绷紧，眉头拧着。",
  breathy("A soft fading hiss and a slow, steadier breath.", "渐渐消失的轻轻嘶声和一声缓慢、平稳了一点的呼吸。"),
  cam=('The camera pulls out from her neck until both of them are in view.', '镜头从她的脖子往后拉，直到两个人都入画。'))

T(b21, '04｜特写：颈后的新月印记亮起银光', 3, ['LilySilver'], ('medical_room', 'lily_silver'), ['medical_room'],
  "Close-up from behind and slightly to the left of Lily's head, neck and shoulders, in the middle third of the frame, as she lies on her side on the white pillow facing away, her chestnut hair swept forward over her left shoulder so that her nape is bare, the collar of the oversized white shirt low on her shoulders; on the center of her nape the dark-red crescent-moon mark in an ornate tattoo-like pattern, her skin flushed and smooth, her cheek just visible against the pillow with her eyes closed, her lips softly parted, her brows relaxed. The frame holds exactly one person, Lily.",
  END_MR, "特写：莉莉颈后的新月印记亮起一阵耀眼的银色光芒，把白枕头照得发亮。",
  None,
  f"A steady close-up opens from the adopted first frame in {MR}: the crescent mark on {LSV}'s nape flares with a dazzling silver light that pulses once and again, throwing a cold silver glow across the white pillow and the tiles, as her shoulders draw in a deep breath.",
  "一个稳定的特写，从已采用的开场图继续，场景是地下医疗室：莉莉颈后的新月印记亮起耀眼的银光，闪一下，再闪一下，把冷冷的银色光芒洒在白枕头和瓷砖上，她的肩膀深深吸了一口气。",
  breathy("A rising crystalline hum and one deep heartbeat.", "渐渐升高的清脆嗡鸣声和一下深沉的心跳。"))

T(b21, '05｜特写：她猛地睁开眼睛，眼睛是银色的', 4, ['LilySilver'], ('medical_room', 'lily_silver'), ['medical_room'],
  "Close-up of Lily's face on the white pillow, in the middle third of the frame, seen from the front slightly from the side, her eyes closed, her chestnut hair spilling across the pillow, a healthy flush on her cheeks, her lips softly parted, her brows relaxed; the left side of her neck smooth and unmarked. The frame holds exactly one person, Lily.",
  END_MR, "特写：莉莉的眼皮一颤，猛地睁开，眼睛变成了发光的银白色。",
  None,
  f"A close-up opens from the adopted first frame in {MR}: {LSV}'s eyelids tremble and then snap open on luminous silver-white irises that glow faintly in the cold light; she draws a deep gasping breath, her lips parting and her brows pulling together.",
  "一个特写，从已采用的开场图继续，场景是地下医疗室：莉莉的眼皮颤了颤，然后猛地睁开，露出在冷光里微微发亮的银白色虹膜；她深深吸了一口气，嘴唇张开，眉头拧起。",
  breathy("A deep gasping breath and a faint crystalline ring.", "一声深深的喘息和一声清脆的嗡鸣。"),
  cam=('The camera pushes in until her silver eyes fill the width of the frame.', '镜头推近到银白色的眼睛占满画面宽度。'))

T(b21, '06｜基利安愣住：莉莉，你的眼睛是银色的', 6, ['KillianGoldShirt', 'LilySilver'], ('medical_room', 'killian_gold_shirt', 'lily_silver'), ['medical_room'],
  "Side-on medium close-up two-shot, both people from the head to the chest, in the middle third of the frame, in the underground medical room. "
  "Killian at frame-left in profile facing frame-right, lifting his head from her neck, dark blood at the corner of his lips, in the white dress shirt, his dark-gold eyes wide and fixed on her face, his jaw slack, his lips parted, his brows pulled up in shock. "
  "Lily at frame-right lying on the white pillow, propped slightly on her elbow, in the oversized white shirt, her chestnut hair spilling, her luminous silver-white eyes fixed on his face, her lips parted, her brows soft. "
  "The frame holds exactly two people: Killian and Lily.",
  END_MR + LAY_MR, "基利安抬起头，看着她银色的眼睛，愣愣地低声说：莉莉，你的眼睛是银色的。",
  ('KillianGoldShirt', "Lily, your eyes are silver.", 1.0),
  f"A steady side-on medium close-up two-shot opens from the adopted first frame in {MR}: {KGS} whispers in a hushed, awed voice, his dark-gold eyes wide on her face, his jaw slack and his brows pulled up; {LSV} looks up at him with calm silver eyes, her lips parting slowly and her brows soft.",
  "一个稳定的侧面中近景双人镜头，从已采用的开场图继续，场景是地下医疗室：基利安用压低的、惊叹的声音说话，暗金色的眼睛睁大看着她的脸，下巴松开，眉头抬起；莉莉用平静的银色眼睛看着他，嘴唇慢慢张开，眉头柔和。",
  voiced("A hushed breath and a faint crystalline ring.", "一声压低的呼吸和清脆的嗡鸣声。"))

T(b21, '07｜她抓住他的衣领，翻身把他按在床上', 4, ['KillianGoldShirt', 'LilySilver'], ('medical_room', 'killian_gold_shirt', 'lily_silver'), ['medical_room'],
  "Side-on medium two-shot, both people from the head to the waist, in the middle third of the frame, on the white hospital bed. "
  "Killian at frame-left, bending over Lily with one hand flat on the mattress beside her head, in profile facing frame-right, in the white dress shirt, his dark-gold eyes wide, his lips parted, his brows pulled up. "
  "Lily at frame-right lying on her back, in the oversized white shirt with the collar open, her chestnut hair spilling, both hands gripping the collar of his shirt, her luminous silver-white eyes cold and fixed on his, her lips set, her brows level. "
  "The frame holds exactly two people: Killian and Lily.",
  END_MR + LAY_MR, "莉莉揪住基利安的衣领，一翻身，竟然把一米九的他按倒在病床上。",
  None,
  f"A steady side-on medium two-shot opens from the adopted first frame in {MR}: {LSV} pulls on his collar and rolls him over in one smooth, powerful motion, flipping {KGS} onto his back on the white bed, and ends kneeling above him with both his wrists pinned to the mattress beside his head, her hair falling around her face and her silver eyes fixed on his; his dark-gold eyes widen, his lips part and his brows pull up.",
  "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是地下医疗室：莉莉揪着他的衣领，一个流畅有力的翻身，把基利安掀倒在白色病床上，她跪在他上方，把他的两只手腕按在头两边的床垫上，头发垂在脸边，银色的眼睛盯着他的眼睛；他暗金色的眼睛睁大，嘴唇张开，眉头抬起。",
  breathy("A rustle of linen, a sharp breath and the creak of the bed.", "亚麻床单的摩擦声、一声急促的吸气和床架的吱嘎声。"), dep=True)

T(b21, '08｜她用指尖抹过他嘴角的血：你的血好甜', 6, ['LilySilver', 'KillianGoldShirt'], ('medical_room', 'lily_silver', 'killian_gold_shirt'), ['medical_room'],
  "Side-on close two-shot, both people from the head to the shoulders, in the middle third of the frame, on the white hospital bed. "
  "Killian lying on his back on the white pillow with his head at frame-left, in the white dress shirt, his dark-gold eyes wide and fixed on her, his lips parted with a smear of dark blood at the corner, his jaw slack, his brows pulled up. "
  "Lily kneeling above him at frame-right, in the oversized white shirt, her chestnut hair falling forward around both their faces, her right fingertip resting on the blood at the corner of his lips, her luminous silver-white eyes half lidded and fixed on his mouth, a faint coy smile on her lips, her brows soft. "
  "The frame holds exactly two people: Lily and Killian.",
  END_MR + LAY_MR, "莉莉俯身看着他，指尖抹过他嘴角的血，用空灵的声音说：你的血，好甜。",
  ('LilySilver', "Your blood tastes so sweet.", 1.0),
  f"A close two-shot opens from the adopted first frame in {MR}: {LSV} speaks in a low, airy, ethereal voice, her fingertip sliding along the blood at the corner of his lips and her silver eyes half lidded; {KGS} lies utterly still beneath her, his dark-gold eyes wide, his lips parted and his brows pulled up.",
  "一个近景双人镜头，从已采用的开场图继续，场景是地下医疗室：莉莉用低沉空灵的声音说话，指尖划过他嘴角的血，银色的眼睛半垂；基利安一动不动地躺在她下面，暗金色的眼睛睁大，嘴唇张开，眉头抬起。",
  voiced("A low airy whisper and the faint rustle of linen.", "低低的空灵耳语和亚麻床单轻轻的摩擦声。"), dep=True,
  cam=('The camera pushes in toward their two faces until they fill most of the frame.', '镜头推近到两张脸占满大半个画面。'))

T(b21, '09｜他的喉结滚动，理智彻底崩断', 3, ['KillianGoldShirt'], ('medical_room', 'killian_gold_shirt'), ['medical_room'],
  "Close-up of Killian alone lying on his back on the white pillow, in the middle third of the frame, his head tilted back, his dark-gold eyes wide, his lips parted, his jaw slack, his brows pulled up, silver light flickering across his face. The frame holds exactly one person, Killian.",
  END_MR, "特写：基利安仰躺着，喉结用力滚动，眼睛里的金光越来越亮，最后一根理智的弦断了。",
  None,
  f"A steady close-up opens from the adopted first frame in {MR}: {KGS} swallows hard, his throat working; his dark-gold eyes flare brighter, his pupils narrowing to slits, and his jaw tightens and his lips press together as his control visibly breaks, his brows crashing together.",
  "一个稳定的特写，从已采用的开场图继续，场景是地下医疗室：基利安用力吞咽，喉结滚动；暗金色的眼睛越来越亮，瞳孔缩成细线，下颌绷紧，嘴唇抿住，他的理智眼看着崩断，眉头拧在一起。",
  breathy("A hard swallow and one slow, shaking breath.", "一声用力的吞咽和一口缓慢发抖的呼吸。"))

# =================================================================================================== 第 22 集：离不开的牢笼
# 观众要看懂：第二天早晨 → 伤口好了 → 他不在 → 她心慌发作 → 跑出去（光脚）
# 另一边：长老逼他杀她，他拍桌子（呼应 16 集“长老威胁你”）→ 她循着印记的牵引跑过走廊 → 推开门 → 所有人回头 → 他的椅子空了。
# 方向：卧室门在画面右边；走廊里她从左向右跑，书房双开门在右端；会议室的门在画面右边，他坐在左边主位。

T(b22, '01｜第二天早晨的主卧，地上是凌乱的衣服', 3, ['LilyShirt'], ('bedroom', 'lily_shirt'), ['bedroom'],
  "Wide shot of the master bedroom in bright morning sunlight, in the middle third of the frame: the huge dark-wood bed with rumpled charcoal-grey linen at frame-left, Lily asleep on the pillow with only her tousled chestnut hair, her closed eyes, her softly parted lips and her relaxed brows showing above the sheet; on the dark rug in the foreground a man's black three-piece suit jacket crumpled, a loosened dark tie and a white dress shirt with torn sleeves lying where they fell. The frame holds exactly one person, Lily, asleep.",
  END_BD + LAY_BD, "第二天早晨，阳光洒满主卧，地上扔着皱成一团的外套和撕破的衬衫，莉莉还睡在床上。",
  None,
  f"A wide shot opens from the adopted first frame in {BD}: bright sunlight glows across the rumpled linen as {LS} sleeps, her shoulders rising and falling with slow breaths, her lips softly parted and her brows relaxed, dust motes drifting in the golden light.",
  "一个宽景，从已采用的开场图继续，场景是主卧：明亮的阳光洒在皱巴巴的亚麻床单上，莉莉睡着，肩膀随着缓慢的呼吸起伏，金色的光里飘着灰尘。",
  breathy("Soft birdsong and the quiet rustle of linen.", "轻轻的鸟叫声和亚麻床单的轻响。"),
  cam=('The camera glides forward low over the floor past the crumpled jacket and torn shirt toward the bed.', '镜头贴着地板往前滑，经过皱成一团的外套和撕破的衬衫，朝床靠近。'))

T(b22, '02｜莉莉醒来，摸到脖子上光滑的皮肤', 4, ['LilyShirt'], ('bedroom', 'lily_shirt'), ['bedroom'],
  "Close-up of Lily's face on the pillow in bright morning sunlight, seen from the side, in profile facing frame-right, in the middle third of the frame, her eyes closed, her chestnut hair tousled across her cheek, her lips softly parted, her brows relaxed; the left side of her neck smooth and unmarked beneath her jaw. The frame holds exactly one person, Lily.",
  END_BD + LAY_BD, "莉莉醒来，眼睛恢复了原来的颜色，伸手摸脖子，伤口完全愈合了，只剩光滑的皮肤。",
  None,
  f"A steady close-up opens from the adopted first frame in {BD}: {LS}'s eyelids flutter open on her large hazel-green eyes, and she draws a slow breath; her right hand rises and her fingertips touch the left side of her neck where the cut was, finding only smooth, unbroken skin, her brows pulling together in confusion and her lips parting.",
  "一个稳定的特写，从已采用的开场图继续，场景是主卧：莉莉的眼皮颤动着睁开，露出淡褐绿色的大眼睛，慢慢吸了一口气；她的右手抬起来，指尖碰到脖子左侧原来有伤口的地方，只摸到光滑完整的皮肤，眉头困惑地拧起，嘴唇张开。",
  breathy("Soft birdsong and a slow breath.", "轻轻的鸟叫声和一声缓慢的呼吸。"))

T(b22, '03｜她伸手摸到旁边空了的、冰凉的枕头', 4, ['LilyShirt'], ('bedroom', 'lily_shirt'), ['bedroom'],
  "Side-on medium shot of Lily alone, from the head to the waist, in the middle third of the frame, propped on her left elbow in the huge bed in the oversized white men's shirt, in profile facing frame-right, her chestnut hair tousled; beside her the other half of the bed, a dented charcoal-grey pillow and the linen thrown back, empty; her wide eyes on the dented pillow, her lips parted, her brows pulled up. The frame holds exactly one person, Lily.",
  END_BD + LAY_BD, "床的另一半是空的；她摸了摸枕头，是凉的，一下子慌了，手按住心口。",
  None,
  f"A steady side-on medium shot opens from the adopted first frame in {BD}: {LS} reaches out and lays her hand flat on the dented pillow, which is cold, and her face crumples, her lips trembling and her brows pulling up; her other hand flies to her chest and presses hard, her breath coming short and fast.",
  "一个稳定的侧面中景，从已采用的开场图继续，场景是主卧：莉莉伸手按在凹下去的枕头上，枕头是凉的，她的脸皱了起来，嘴唇发颤，眉头抬起；另一只手猛地按住胸口，用力压着，呼吸又短又快。",
  breathy("A short ragged breath and the rustle of linen.", "一声短促粗重的呼吸和亚麻床单的摩擦声。"))

T(b22, '04｜她喘不上气：基利安，你在哪', 6, ['LilyShirt'], ('bedroom', 'lily_shirt'), ['bedroom'],
  "Side-on medium close-up of Lily alone, from the head to the waist, in the middle third of the frame, sitting on the edge of the huge bed in profile facing frame-right, in the oversized white men's shirt, her chestnut hair tousled, one hand pressed hard to her chest and the other gripping the charcoal linen, her wide wet eyes on the tall dark-wood door with the brass handle at frame-right, her lips trembling, her brows pulled up. The frame holds exactly one person, Lily.",
  END_BD + LAY_BD, "莉莉坐在床边，一手按着胸口，喘不上气，对着门口颤着声音喊：基利安，你在哪？",
  ('LilyShirt', "Killian, where are you?", 1.0),
  f"A steady side-on medium close-up opens from the adopted first frame in {BD}: {LS} gasps for air and calls out in a thin, shaking voice, her hand pressed to her chest, her wide wet eyes on the door, her lips trembling and her brows pulled up, a wave of nausea doubling her forward.",
  "一个稳定的侧面中近景，从已采用的开场图继续，场景是主卧：莉莉大口喘气，用单薄发抖的声音喊，手按着胸口，湿润睁大的眼睛看着门，嘴唇发颤，眉头抬起，一阵恶心让她弯下腰。",
  voiced("A ragged gasp and the creak of the bed.", "一声粗重的喘息和床架的吱嘎声。"))

T(b22, '05｜她光着脚冲出卧室', 4, ['LilyShirt'], ('bedroom', 'lily_shirt'), ['bedroom'],
  "Side-on wide-medium shot of Lily alone, from the head to the feet, in the middle third of the frame, standing barefoot beside the huge bed at frame-left in the oversized white men's shirt, her chestnut hair tousled, one hand on her chest, her wide eyes on the tall dark-wood door with the brass handle at frame-right, her lips parted, her brows pulled up. The frame holds exactly one person, Lily.",
  END_BD + LAY_BD, "莉莉光着脚冲向门口，一把拉开门跑了出去，房间里空了。",
  None,
  f"A steady side-on wide-medium shot opens from the adopted first frame in {BD}: {LS} bolts across the room, her lips parted and her brows pulled up, yanks the door open and runs out, her bare feet slapping on the wood; the door swings wide behind her and the room is left empty.",
  "一个稳定的侧面宽中景，从已采用的开场图继续，场景是主卧：莉莉冲过房间，一把拉开门跑了出去，光脚拍在木地板上；门在她身后大敞着，房间里空了。",
  breathy("Bare feet slapping on wood and a door banging open.", "光脚拍在木地板上的声音和门被撞开的声音。"))

T(b22, '06｜会议室里，长老要杀她', 6, ['Elder', 'KillianGold'], ('council_room', 'elder', 'killian_gold'), ['council_room'],
  "Side-on medium two-shot, in the middle third of the frame, in the grim paneled council room. "
  "Elder standing at frame-right in profile facing frame-left, an old man with swept-back white hair and a deeply lined stern face, in the black three-piece suit with a silver wolf-head lapel pin, his bony finger stabbing down at the long polished table, his lips pulled into a snarl, his brows lowered, his cold pale eyes on Killian. "
  "Killian seated at frame-left at the head of the long table in the tall carved chair, in profile facing frame-right, in the tailored black three-piece suit, white shirt and dark tie, his hands gripping the chair arms, his eyes glowing dark gold, his jaw clenching, his lips pressed, his brows low. "
  "Blurred grey-haired men in dark suits sit along the table behind them. The frame holds exactly two people in focus: Elder and Killian.",
  END_CR + LAY_CR, "另一边的会议室里，白发长老拍着桌子说：那个人类女孩必须死，Alpha！基利安的眼睛已经发金。",
  ('Elder', "The human girl must die, Alpha!", 1.0),
  f"A steady side-on medium two-shot opens from the adopted first frame in {CR}: {EL} speaks in a dry, hoarse, commanding voice, stabbing his finger at the table, his lip curled and his brows low; {KG} listens, his jaw clenching harder, his lips pressed into a white line and his brows lowering.",
  "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是阴沉的会议室：长老用干涩沙哑、命令式的声音说话，手指戳着桌面，嘴唇卷起，眉头压低；基利安听着，下颌越咬越紧，嘴唇抿成一条白线，眉头越压越低。",
  voiced("A dry creak of leather chairs.", "皮椅干涩的吱嘎声。"))

T(b22, '07｜基利安拍碎桌面：碰她的人都得死', 6, ['KillianGold', 'Elder'], ('council_room', 'killian_gold', 'elder'), ['council_room'],
  "Side-on medium two-shot, in the middle third of the frame, in the council room. "
  "Killian now on his feet at frame-left behind the long table, in profile facing frame-right, in the black three-piece suit, one palm slammed flat on the polished table, his other fist clenched, his eyes blazing dark gold, his mouth open in a roar, his jaw clenched, his brows crashing together. "
  "Elder at frame-right flinching back in the black three-piece suit with the silver wolf-head pin, his lips parted, his brows pulled up, his pale eyes wide on Killian. "
  "Blurred grey-haired men in dark suits sit rigid along the table behind them. The frame holds exactly two people in focus: Killian and Elder.",
  END_CR + LAY_CR, "基利安猛地站起来，一掌拍在桌上，怒吼：谁碰她，谁就得死！",
  ('KillianGold', "Anyone who touches her dies!", 1.0),
  f"A steady side-on medium two-shot opens from the adopted first frame in {CR}: {KG} roars the words in a deep, thunderous voice, his palm slammed on the polished table and a crack running through the wood, his eyes blazing, his jaw clenched and his brows crashing together. {EL} flinches backward, his lips parting and his brows pulling up.",
  "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是会议室：基利安用低沉如雷的声音吼出这句话，手掌砸在抛光的桌面上，木头上裂开一道缝，眼睛喷着金光；长老向后一缩，嘴唇张开，眉头抬起。",
  voiced("A crack of splitting wood and a thunderous roar.", "木头裂开的脆响和雷鸣般的怒吼。"), dep=True)

T(b22, '08｜她光着脚在走廊里狂奔', 4, ['LilyShirt'], ('study_door', 'lily_shirt'), ['study_door'],
  "Side-on wide-medium shot of Lily alone, from the head to the feet, in the middle third of the frame, running barefoot along the pale marble floor and dark runner rug of the corridor in profile facing frame-right, in the oversized white men's shirt, her chestnut hair streaming, one hand pressed to her chest, her wide eyes on the tall dark double doors at the far right end of the corridor, her lips parted, her brows pulled up. The frame holds exactly one person, Lily.",
  END_SD + LAY_SD, "莉莉光着脚在长长的走廊里狂奔，朝走廊尽头的双开门跑去。",
  None,
  f"A wide-medium shot opens from the adopted first frame in {SD}: {LS} runs barefoot along the corridor toward the doors at frame-right, her chestnut hair streaming and her hand pressed to her chest, her lips parted and her brows pulled up, her breath ragged.",
  "一个宽中景，从已采用的开场图继续，场景是走廊：莉莉光着脚沿走廊朝画面右边的双开门奔跑，栗色头发向后飞，手按着胸口，呼吸又乱又重。",
  breathy("Bare feet slapping on marble and a ragged, panicked breath.", "光脚拍在大理石地面上的声音和一声慌乱粗重的喘息。"),
  cam=('The camera tracks sideways with her at running pace, keeping her in the middle of the frame while the paneled wall and amber lamps stream past behind.', '镜头横向跟拍她奔跑，让她始终在画面中间，身后的木板墙和琥珀色壁灯一路掠过。'))

T(b22, '09｜她停在门前，颈后的印记在发光', 3, ['LilyShirt'], ('study_door', 'lily_shirt'), ['study_door'],
  "Medium shot from behind and slightly to the left of Lily, from the head to the knees, in the middle third of the frame, standing still on the marble floor of the corridor in the oversized white men's shirt, her chestnut hair swept forward over her left shoulder so that her nape is bare, the dark-red crescent-moon mark on her nape, her right hand pressed to her chest, her shoulders heaving, her cheek just visible in profile with her lips parted and her brows pulled up; ahead of her at the far end of the corridor the tall dark double doors with large brass handles, closed. The frame holds exactly one person, Lily.",
  END_SD + LAY_SD, "莉莉在双开门前停下来，颈后的印记发出淡淡的金光，她听见了门里的什么。",
  None,
  f"A steady medium shot opens from the adopted first frame in {SD}: the crescent mark on {LS}'s nape glows a soft warm gold and her heaving shoulders slowly still; her head lifts toward the doors, her lips parting and her brows pulling up, and she takes one step toward them.",
  "一个稳定的中景，从已采用的开场图继续，场景是走廊：莉莉颈后的新月印记发出柔和温暖的金光，起伏的肩膀慢慢平静下来；她抬头朝着那扇门，嘴唇张开，眉头抬起，向前迈了一步。",
  breathy("A soft warm hum, a slowing breath and one heartbeat.", "一声柔和温暖的嗡鸣、渐渐平缓的呼吸和一下心跳。"))

T(b22, '10｜双开门被推开，所有长老同时回头', 4, ['KillianGold', 'LilyShirt'], ('council_room', 'killian_gold', 'lily_shirt'), ['council_room'],
  "Wide shot of the council room seen from the side, in the middle third of the frame: the long polished dark-wood table running across the frame with a dozen grey-haired men in black three-piece suits seated along it, all facing frame-left toward the head of the table, their lips pressed and their brows lowered; "
  "Killian standing at the head of the table at frame-left in the black three-piece suit, one palm flat on the table, his eyes blazing gold, his mouth open mid-roar, his brows crashing together; the tall dark double doors at frame-right still closed.",
  END_CR + LAY_CR, "会议室里的所有人正对着基利安，双开门忽然被推开，莉莉站在门口。",
  None,
  f"A steady wide shot opens from the adopted first frame in {CR}: the tall double doors at frame-right burst open and {LS} stands in the doorway barefoot in the oversized white shirt, one hand on the brass handle, her chest heaving, her wide eyes on the room, her lips parted and her brows pulled up; every elder's head snaps toward the doorway with cold, murderous stares, and {KG}'s roar cuts off as his head turns, his gold eyes widening and his brows pulling up.",
  "一个稳定的宽景，从已采用的开场图继续，场景是会议室：画面右边的高大双开门被猛地推开，莉莉光着脚穿着肥大的白衬衫站在门口，一只手扶着黄铜把手，胸口起伏，睁大的眼睛看着屋里，嘴唇张开，眉头抬起；每一位长老同时扭头看向门口，目光冰冷带着杀气，基利安的怒吼戛然而止，他转过头，金色的眼睛睁大，眉头抬起。",
  breathy("A boom of doors flung open and a sudden dead silence.", "双开门被撞开的一声巨响，然后是死一般的寂静。"))

T(b22, '11｜莉莉僵在门口', 4, ['LilyShirt'], ('council_room', 'lily_shirt'), ['council_room'],
  "Side-on medium shot of Lily alone, from the head to the knees, in the middle third of the frame, standing barefoot in the tall open doorway at frame-right, in the oversized white men's shirt, her chestnut hair tousled, one hand gripping the brass handle of the open door, her wide frightened eyes on the long polished table and the row of dark-suited men blurred at frame-left, her lips parted, her brows pulled up. The frame holds exactly one person in focus, Lily.",
  END_CR + LAY_CR, "莉莉被十几双冷冰冰的眼睛盯着，吓得僵在门口，往后退了半步。",
  None,
  f"A steady side-on medium shot opens from the adopted first frame in {CR}: {LS} freezes in the doorway, her hand slipping from the handle to her chest, her lips trembling and her brows pulling up, her bare toes curling against the threshold as she takes half a step back.",
  "一个稳定的侧面中景，从已采用的开场图继续，场景是会议室：莉莉僵在门口，手从把手上滑到胸口，嘴唇发颤，眉头抬起，光着的脚趾蜷在门槛上，她往后退了半步。",
  breathy("A held breath and the faint creak of the door.", "屏住的呼吸和门轴细微的吱嘎声。"))

T(b22, '12｜主位的椅子空了', 3, [], ('council_room',), ['council_room'],
  "Medium shot of the tall carved high-backed chair at the head of the long polished table, in the middle third of the frame, empty and turned slightly outward, a leather folder and loose papers on the table in front of it, the blurred figures of grey-haired men in dark suits sitting rigid along the table behind it. No one sits in the chair.",
  END_CR, "基利安的高背椅空了，椅子还在转，桌上的文件被风吹得乱飞。",
  None,
  f"A steady medium shot opens from the adopted first frame in {CR}: the empty chair rocks and spins slowly in the sudden stillness while the loose papers on the table flutter and slide off the edge, a rush of wind rolling through the room; the men behind it stare at the vacant seat. No one sits in the chair.",
  "一个稳定的中景，从已采用的开场图继续，场景是会议室：空椅子在突然的寂静里晃动、慢慢转着，桌上的散页文件被吹得乱飞、滑下桌沿，一阵风滚过房间；椅子后面的人呆呆盯着空座位。椅子上没有人。",
  breathy("A rush of wind, fluttering paper and the slow creak of a spinning chair.", "一阵风声、纸页翻飞的声音和椅子慢慢转动的吱嘎声。"))

# =================================================================================================== 合成一份
doc = copy.deepcopy(b19.d)
doc['episodes'] = [
    episode(b19, '剧本第19集｜狼王的审判（重写）', '黑狼扑杀猎手，留下一把有毒的银匕首；尾巴护住莉莉；黑雾里变回人，基利安脱外套裹她，回答她“是你吗”；保罗跪求，基利安下令把他们扔进死斗场；莉莉咳出黑血。'),
    episode(b20, '剧本第20集｜银毒入骨（重写）', '基利安抱着她跑回主楼；黑色血管扩散，他认出银毒；狼医说只剩十分钟；他赶走所有人，咬破手腕喂血，吻上伤口。'),
    episode(b21, '剧本第21集｜血之契约（重写）', '他吸出毒血、低声求她别走；黑色血管退回，印记发银光，眼睛变银；她翻身按住他，说“你的血好甜”，他理智崩断。'),
    episode(b22, '剧本第22集｜离不开的牢笼（重写）', '第二天她醒来发现空床，心慌发作，光脚跑出去；另一边长老要杀她、基利安拍桌；她循着印记跑到会议室推开门，所有人回头，他的椅子空了。'),
]
txt = json.dumps(doc, ensure_ascii=False, indent=1)
open(os.path.join(FOLDER, OUT + '.json'), 'w', encoding='utf-8').write(txt)
open(os.path.join(FOLDER, OUT + '_全选复制粘贴.txt'), 'w', encoding='utf-8').write(txt)
n = sum(len(e['segments']) for e in doc['episodes']); sec = sum(s['duration_seconds'] for e in doc['episodes'] for s in e['segments'])
print(f'{len(doc["episodes"])} 集、{n} 个任务、约 {sec} 秒；文件 {len(txt.encode())/1024:.0f} KB → {OUT}')
for e in doc['episodes']:
    print('  ', e['title'], len(e['segments']), '个任务', sum(s['duration_seconds'] for s in e['segments']), '秒')
