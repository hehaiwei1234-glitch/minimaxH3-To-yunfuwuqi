#!/usr/bin/env python3
"""补拍包 1：给第 1–6 集的“接缝”补 8 个镜头（补1–补5 是 10-09 夜写的；补6–补8 是 10-10 看完第 6 集视频后加的）（2026-10-09 夜，hh 22:56 授权“不连贯的地方需要补的都补一下”）。

基于合并稿（第 5 集＋第 6 集 A＋第 6 集 B）的 JSON（素材、人物逐字复制，F11），只新增一个场景 car_back；
必须在合并稿全部跑完之后追加。8 个任务，种子 3701–3708。
  补1  保罗说 “Sorry. I'll wait outside.”   → 接第 2 集结尾（保罗离场）
  补2  莉莉说 “Fine. I'll sign.”             → 第 3 集结尾（莉莉答应；也让“协议”一词在第 4 集前出现）
  补3  莉莉在轿车后座抱着文件夹             → 第 4 集开头之前（接第 3 集的文件夹道具）
  补4  莉莉提着行李箱站在主卧里             → 第 5 集开头之前（她怎么到卧室的）
  补5  基利安的牙停在她脖子前，金色眼睛褪成黑色 → 第 5 集结尾（剧本第 6 集开头的“闪回”：只留红痕、没咬下去）
  补6  莉莉在宴会厅，左手指尖碰着颈侧的创可贴（左侧脸朝镜头）→ 第 6 集开头（6A 里创可贴一次也没拍到：她两次都面朝右，创可贴在左颈被挡住）
  补7  第 6 集 6A 的 05 号（红酒泼裙）原稿重拍，只换种子 3707 → 原片两侧各有约 8.5% 的黑边
  补8  第 6 集 6A 的 07 号（玛丽特写）原稿重拍，只换种子 3708 → 原片两侧各有约 17% 的黑边
写法已按《自查清单》：每人每任务写了表情、视线目标在画面里、没有画外的人、有台词的任务 6 秒且 ≤6 个单词。
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _h3draft import Batch, FOLDER, silent, voiced

BASE = '合并稿/合并_第5集+第6集A+第6集B_制作稿_追加.json'
OUT = '补拍/补拍包1_接缝补镜头_追加'
SERIES_TITLE = json.load(open(os.path.join(FOLDER, BASE), encoding='utf-8'))['title']

b = Batch(BASE, SERIES_TITLE, 3700)
ZH = []


def T(title, dur, chars, assets, refs, img, end, img_zh, vis_zh, cam_zh, dlg, shot_en, shot_zh, sound):
    s = b.task(title, dur, chars, assets, refs, img, end, vis_zh, cam_zh, dlg, shot_en, shot_zh, sound)
    s['depends_on_previous'] = False
    ZH.append(img_zh)
    return s


# 新场景：轿车后座（空的，没有人）
b.scene('car_back', '轿车后座',
        "The rear seat of a luxury black sedan at dusk: cream leather seat, dark wood trim, a wide side window with cold blue dusk light and warm lights glowing far away. The reference fixes the cabin and the light.",
        "黄昏时一辆豪华黑色轿车的后座：奶油色真皮座椅，深色木饰板，宽大的侧车窗，窗外是冷蓝色的暮光和远处亮着的暖色灯光。参考图固定车内布置和光线。",
        "A photorealistic ultra-wide 8:3 cinemascope shot of the empty rear seat of a luxury black sedan at dusk: a cream leather seat, dark wood trim, a wide side window with cold blue dusk light and warm lights glowing far away, nobody in the car. "
        "The frame holds the seat, the door panel and the side window.")

ROOM = '[[asset:room]]'; LILY = '[[asset:lily]]'; PAU = '[[asset:paul]]'
BEDR = '[[asset:bedroom]]'; CAR = '[[asset:car_back]]'
LC = '[[asset:lily_coat]]'; LS = '[[asset:lily_shirt]]'; KW = '[[asset:killian_wolf]]'

LAYR = " Fixed layout: the heavy dark-wood door is at frame-left; the rack of white gowns is at the back wall at frame-right."
Z_LAYR = "固定布局：厚重的深色木门在画面左边；白色婚纱架在后墙的画面右边。"
END_R = " Warm light from the chandelier and the wall sconces."
Z_END_R = "吊灯和壁灯的暖光。"
LAYB = " Fixed layout: the huge dark-wood bed is against the left wall; the tall dark-wood door is in the right wall; the dark curtains hang at the back."
Z_LAYB = "固定布局：巨大的深色木床靠左边的墙；高大的深色木门在右边的墙上；深色窗帘挂在后面。"
END_B = " Low amber light from the bedside lamps."
Z_END_B = "床头灯低低的琥珀色光。"
END_C = " Cold blue dusk light with warm lights far away. Fixed layout: the side window is at frame-right; the cream leather seat is at frame-left."
Z_END_C = "冷蓝色的暮光，远处有暖色的灯光。固定布局：侧车窗在画面右边；奶油色真皮座椅在画面左边。"

# 补1 保罗：我去外面等（接第 2 集结尾）-----------------------------------------------------------------------
T('补1｜保罗说我去外面等', 6, ['PaulOnScreen'], ('room', 'paul'), ['room'],
  "Medium shot of Paul alone, from the head to the waist, in profile facing frame-left, in the middle third of the frame, in his navy blazer over a white open-collared shirt, "
  "his right hand resting on the brass handle of the heavy dark-wood door at frame-left, his brows drawn together, his lips pressed into a stiff line, his eyes lowered to the brass handle. The frame holds exactly one person, Paul.",
  END_R + LAYR,
  "保罗一个人的中景，头到腰，侧身朝画面左边，在画面中间三分之一，穿藏青色西装外套和白色敞领衬衫，右手搭在画面左边那扇厚重深色木门的黄铜把手上，眉头皱着，嘴唇紧紧抿成一条线，眼睛垂着看着黄铜把手。画面里恰好一个人：保罗。" + Z_END_R + Z_LAYR,
  "保罗站在门边，手搭在把手上，皱着眉，尴尬地低声说他去外面等。", "0—6秒中景，镜头固定。",
  ('PaulOnScreen', "Sorry. I'll wait outside.", 1.0),
  f"A steady medium shot opens from the adopted first frame in {ROOM}: {PAU} in profile facing frame-left, his right hand on the brass door handle, his eyes lowered to the handle. "
  "He speaks in a thin, flustered voice; when he finishes his brows stay drawn together and his lips press into a stiff line. His hand stays on the handle. The camera holds still.",
  "一个稳定的中景，从已采用的开场图继续，场景是试衣间：保罗侧身朝画面左边，右手搭在黄铜门把手上，眼睛垂着看着把手。他用细细的、慌乱的声音说话；说完后，他的眉头仍然皱着，嘴唇抿成一条僵硬的线。他的手一直搭在把手上。镜头固定不动。",
  voiced("A faint hum of the building and the soft rustle of fabric.", "大楼轻轻的嗡嗡声和布料轻轻的摩擦声。"))

# 补2 莉莉：答应（第 3 集结尾）--------------------------------------------------------------------------------
T('补2｜莉莉答应签字', 6, ['Lily'], ('room', 'lily'), ['room'],
  "Medium close-up of Lily alone, waist-up, in profile facing frame-right, in the middle third of the frame, sitting on the carpet with her back against the cream wall in the ivory wedding gown, "
  "a document folder open on her knees and a black pen in her right hand held above the page, her eyes lowered to the page, her eyes glistening with tears, her lower lip trembling, her brows drawn together. The frame holds exactly one person, Lily.",
  END_R + LAYR,
  "莉莉一个人的中近景，腰部以上，侧身朝画面右边，在画面中间三分之一，穿象牙色婚纱，背靠奶油色的墙坐在地毯上，一份文件夹摊开在膝上，右手拿着一支黑色的笔悬在纸页上方，眼睛垂着看着纸页，眼里泛着泪光，下嘴唇发抖，眉头皱着。画面里恰好一个人：莉莉。" + Z_END_R + Z_LAYR,
  "莉莉坐在地上，握着笔，含着泪低声说她签。", "0—6秒莉莉侧面中近景，镜头固定。",
  ('Lily', "Fine. I'll sign.", 1.0),
  f"A steady medium close-up opens from the adopted first frame in {ROOM}: {LILY} in profile facing frame-right on the carpet, the folder open on her knees, the pen above the page, her eyes on the page. "
  "A tear slides down her cheek and she speaks in a small broken voice, her lower lip trembling. The pen stays above the page. The camera holds still.",
  "一个稳定的中近景，从已采用的开场图继续，场景是试衣间：莉莉侧身朝画面右边坐在地毯上，文件夹摊开在膝上，笔悬在纸页上方，眼睛看着纸页。一滴眼泪滑过她的脸颊，她用细小、破碎的声音说话，下嘴唇发抖。笔一直悬在纸页上方。镜头固定不动。",
  voiced("Faint paper rustle and quiet room tone.", "轻轻的纸张摩擦声和安静的房间底噪。"))

# 补3 轿车后座（第 4 集开头之前）-----------------------------------------------------------------------------
T('补3｜车后座抱着文件夹', 6, ['LilyCoat'], ('car_back', 'lily_coat'), ['car_back'],
  "Medium shot of Lily alone, waist-up, seated on the cream leather rear seat at frame-left, in profile facing frame-right, in the middle third of the frame, in the faded grey wool coat, "
  "a document folder pressed flat on her lap under both hands, her lips pressed together, her brows drawn together, her eyes glossy and fixed on the wide side window at frame-right where distant warm lights glow. The frame holds exactly one person, Lily.",
  END_C,
  "莉莉一个人的中景，腰部以上，坐在画面左边的奶油色真皮后座上，侧身朝画面右边，在画面中间三分之一，穿褪色的灰色羊毛大衣，一份文件夹平放在膝上、被双手压着，嘴唇抿紧，眉头皱着，眼睛含着水光，盯着画面右边的宽大侧车窗，窗外有远处暖色的灯光。画面里恰好一个人：莉莉。" + Z_END_C,
  "莉莉坐在车后座，双手压着膝上的文件夹，皱着眉，看着窗外越来越近的灯光。", "0—6秒中景，镜头固定。", None,
  f"A steady medium shot opens from the adopted first frame in {CAR}: {LC} seated at frame-left in profile facing frame-right, both hands pressed on the folder in her lap, her eyes on the side window at frame-right. "
  "She breathes in unsteadily and her fingers tighten on the folder; the warm lights slide slowly across the glass. Her body stays seated. The camera holds still.",
  "一个稳定的中景，从已采用的开场图继续，场景是轿车后座：莉莉坐在画面左边，侧身朝画面右边，双手压在膝上的文件夹上，眼睛看着画面右边的侧车窗。她不稳地吸了一口气，手指攥紧文件夹；暖色的灯光慢慢滑过车窗玻璃。她的身体一直坐着。镜头固定不动。",
  silent("A low steady engine hum and the soft tick of a turn signal.", "低低的、平稳的发动机嗡鸣和转向灯轻轻的嗒嗒声。"))

# 补4 主卧门内（第 5 集开头之前）-----------------------------------------------------------------------------
T('补4｜提着行李箱站在主卧', 6, ['LilyCoat'], ('bedroom', 'lily_coat'), ['bedroom'],
  "Medium shot of Lily alone, full body, standing on the dark rug a few steps inside the room, in profile facing frame-left, in the middle third of the frame, in the faded grey wool coat, "
  "the battered brown leather suitcase in her right hand, her lips pressed together, her eyes wide, her eyes on the huge dark-wood bed at frame-left. The frame holds exactly one person, Lily.",
  END_B + LAYB,
  "莉莉一个人的中景，全身，站在房间里往里几步的深色地毯上，侧身朝画面左边，在画面中间三分之一，穿褪色的灰色羊毛大衣，右手提着那只破旧的棕色皮行李箱，嘴唇抿紧，睁大眼睛，眼睛看着画面左边那张巨大的深色木床。画面里恰好一个人：莉莉。" + Z_END_B + Z_LAYB,
  "莉莉提着旧行李箱站在主卧里，睁大眼睛看着那张大床。", "0—6秒全身中景，镜头固定。", None,
  f"A steady medium shot opens from the adopted first frame in {BEDR}: {LC} standing on the rug in profile facing frame-left, the suitcase in her right hand, her eyes on the huge bed at frame-left. "
  "Her chest rises and falls quickly, her eyes stay wide and her knuckles whiten on the suitcase handle. Her feet stay planted on the rug. The camera holds still.",
  "一个稳定的中景，从已采用的开场图继续，场景是庄园主卧：莉莉站在地毯上，侧身朝画面左边，右手提着行李箱，眼睛看着画面左边那张大床。她的胸口快速起伏，眼睛一直睁大，指节在行李箱提手上攥得发白。她的脚一直钉在地毯上。镜头固定不动。",
  silent("A clock ticking softly and faint wind at the tall windows.", "时钟轻轻的嘀嗒声和高大窗户外隐约的风声。"))

# 补5 咬下去之前停住（第 5 集结尾；剧本第 6 集开头的“闪回”：只留红痕）-----------------------------------------
T('补5｜牙停在脖子前', 6, ['LilyShirt', 'KillianWolf'], ('bedroom', 'lily_shirt', 'killian_wolf'), ['bedroom'],
  "Close side-on two-shot, both people in the middle third of the frame. "
  "Lily at frame-left lies on her back on the charcoal linen of the huge bed in the oversized white shirt, her head tilted back on the pillow, her eyes squeezed shut, her lips parted. "
  "Killian at frame-right leans over her on both arms in the black silk robe, his right hand pinning her left wrist to the mattress, his left hand braced flat on the mattress beside her head, his face an inch from her neck, his jaw clenched, his lips pulled back from sharp teeth, his eyes glowing dark gold. "
  "The frame holds exactly two people: Lily and Killian.",
  END_B + LAYB,
  "侧面的近距离双人镜头，两个人都在画面中间三分之一。莉莉在画面左边，穿宽大的白衬衫，仰面躺在巨大的床的炭灰色床单上，头向后仰在枕头上，紧闭双眼，嘴唇微张。"
  "基利安在画面右边，穿黑色丝绸睡袍，双臂撑着俯在她上方，右手把她的左手腕按在床垫上，左手平撑在她头旁的床垫上，脸离她的脖子只有一英寸，下颌咬紧，嘴唇向后拉开露出尖牙，眼睛发着暗金色的光。"
  "画面里恰好两个人：莉莉和基利安。" + Z_END_B + Z_LAYB,
  "基利安的尖牙停在莉莉的脖子前，咬牙忍住，眼里的金光慢慢褪成黑色，把头抬起一点；莉莉睁开眼睛，脖子侧面留下一道淡淡的红痕。", "0—6秒侧面近景，镜头固定。", None,
  f"A steady close side-on two-shot opens from the adopted first frame in {BEDR}: {KW} leaning over {LS}, his face an inch from her neck, her wrist pinned under his right hand. "
  "His teeth stop short of her skin; his jaw clenches, his lips close over his teeth and the gold in his eyes fades to dark as he draws his head back a few inches. Her eyes open, her lips parted, a faint red mark on the side of her neck. His hands stay where they are. The camera holds still.",
  "一个稳定的侧面近距离双人镜头，从已采用的开场图继续，场景是庄园主卧：基利安俯在莉莉上方，脸离她的脖子一英寸，她的手腕被他的右手按着。他的牙停在离她皮肤还有一点的地方；他咬紧下颌，嘴唇合上盖住牙齿，眼里的金光褪成深色，把头向后抬起几英寸。她睁开眼睛，嘴唇微张，脖子侧面有一道淡淡的红痕。他的手一直留在原处。镜头固定不动。",
  silent("A slow heavy breath of silk against linen and a clock ticking softly.", "丝绸蹭过床单的缓慢沉重的摩擦声，和时钟轻轻的嘀嗒声。"))

# 补6 莉莉颈侧的创可贴（第 6 集开头；6A 里创可贴从没拍到：她两次都面朝画面右边，创可贴贴在左颈被挡住）---------------------
BRM = '[[asset:ballroom]]'; LRD = '[[asset:lily_red]]'
LAYBR = " Fixed stage layout: the wide marble staircase is at frame-left; the long banquet table is at frame-right."
Z_LAYBR = "固定布局：宽阔的大理石楼梯在画面左边；长长的宴会桌在画面右边。"
END_BR = " Warm golden chandelier light, the ballroom softly blurred behind."
Z_END_BR = "温暖的金色吊灯光，宴会厅在后面柔和虚化。"
T('补6｜莉莉颈侧的创可贴', 6, ['LilyRed'], ('ballroom', 'lily_red'), ['ballroom'],
  "Medium close-up of Lily alone, from the head to the chest, in profile facing frame-left so that the left side of her neck faces the camera, in the middle third of the frame, in the floor-length red satin gown with thin straps, "
  "the small beige adhesive bandage clearly visible on the left side of her neck, her left hand raised so that her fingertips rest against the edge of the bandage, her lips pressed together, her brows drawn together, her eyes lowered. The frame holds exactly one person, Lily.",
  END_BR + LAYBR,
  "莉莉一个人的中近景，头到胸口，侧身朝画面左边（所以她的左颈侧朝着镜头），在画面中间三分之一，穿落地红色缎面晚礼服，细肩带，左颈侧那块小小的米色创可贴清清楚楚，她的左手抬起、指尖贴着创可贴的边缘，嘴唇抿紧，眉头皱起，眼睛垂着。画面里恰好一个人：莉莉。" + Z_END_BR + Z_LAYBR,
  "莉莉侧着脸，左手指尖碰着颈侧的创可贴，皱着眉，垂着眼。", "0—6秒莉莉侧面中近景，镜头固定。", None,
  f"A steady medium close-up opens from the adopted first frame in {BRM}: {LRD} in profile facing frame-left, the left side of her neck turned to the camera, the small beige bandage on it, her left fingertips resting against the bandage's edge, her eyes lowered. "
  "She draws a slow breath, her lips pressing tighter and her brows drawing together. Her fingertips stay against the bandage. The camera holds still.",
  "一个稳定的中近景，从已采用的开场图继续，场景是晚宴大厅：莉莉侧身朝画面左边，左颈侧朝着镜头，上面贴着那块小小的米色创可贴，左手指尖贴着创可贴的边缘，眼睛垂着。她缓缓吸一口气，嘴唇抿得更紧，眉头皱起。指尖一直贴着创可贴。镜头固定不动。",
  silent("A string quartet playing softly in the distance and the faint clink of crystal.", "远处弦乐四重奏轻轻的演奏声，和水晶杯轻轻的碰撞声。"))

# 补7、补8：6A 的 05、07 原稿重拍（只换种子和标题；其余一字不动）------------------------------------------------------
import copy as _copy
_base = json.load(open(os.path.join(FOLDER, BASE), encoding='utf-8'))
_6a = [e for e in _base['episodes'] if e['title'].startswith('剧本第6集｜')][0]['segments']
for _idx, _title, _seed, _zh in ((4, '补7｜红酒泼裙重拍', 3707, '（同 6A 的 05 号，原稿一字不改，只换种子）'),
                                 (6, '补8｜玛丽特写重拍', 3708, '（同 6A 的 07 号，原稿一字不改，只换种子）')):
    _s = _copy.deepcopy(_6a[_idx]); _s['title'] = _title; _s['seed'] = _seed; _s['depends_on_previous'] = False
    b.tasks.append(_s); ZH.append(_zh)
b.seed = 3708

b.finish('剧本补拍包｜接缝补镜头', '第 1–6 集接缝补镜头 6 个＋第 6 集两个黑边片重拍 2 个，按剪辑单插进成片', OUT)

# ---- 说明 ------------------------------------------------------------------------------------------------
segs = b.tasks
md = []
md.append("# 补拍包 1：给第 1–5 集补接缝（2026-10-09 夜）\n")
md.append(f"**只粘贴这一个文件：** `{OUT}_全选复制粘贴.txt`（8 个任务，种子 3701–3708）。**必须等你现在在跑的合并稿（第 5 集＋第 6 集 A＋第 6 集 B）全部跑完以后再追加**（追加只能等上一批跑完）。设置照旧：视频/对白共用次数 = 1，对白时间余量 = 0，追加窗口不要勾“每集／总／任务秒数”。**插件里会显示成“第 10 集：剧本补拍包｜接缝补镜头”**（如果你中间又追加了别的，号以屏幕为准）。预计 8 × 7 = 56 分钟（上限推算）。\n")
md.append("## 为什么补这 8 个镜头（见 `补拍/剧情连贯性分析_第1-4集.md`）\n")
md.append("| 补拍 | 补在哪里 | 补的是什么 | 做完怎么算成功 |\n|---|---|---|---|")
md.append("| 补1 | 第 2 集结尾（基利安说完“来接我的未婚妻”、保罗错愕之后） | 保罗在门边尴尬地说 `Sorry. I'll wait outside.`，让“保罗走了”成立 | 保罗一个人，手搭在门把手上，台词清楚，没有多出的人 |")
md.append("| 补2 | 第 3 集结尾 | 莉莉握着笔，含泪说 `Fine. I'll sign.`：**补上“莉莉答应了”，并让“签协议”这个词在第 4 集之前出现** | 莉莉一个人，笔在她手里，台词清楚；眼泪、不笑 |")
md.append("| 补3 | 第 4 集开头之前 | 莉莉在轿车后座，双手压着文件夹，看着窗外的灯：用同一份文件夹把第 3 集和第 4 集接起来 | 车里只有莉莉一个人（不冒司机）；文件夹在她手里 |")
md.append("| 补4 | 第 5 集开头之前 | 莉莉提着旧行李箱站在主卧里：补上“她怎么到了卧室” | 只有莉莉一个人；行李箱在她手里；房间是同一间主卧 |")
md.append("| 补5 | 第 5 集结尾（剧本第 6 集开头的“闪回”） | 基利安的牙停在她脖子前，金色眼睛褪成黑色，把头抬起；她脖子侧面留一道红痕：**让第 6 集里她脖子上的创可贴有来历** | 两个人，每只手有主人；牙没有咬下去；脖子有淡红痕 |")
md.append("| 补6 | 第 6 集开头（接在补5 之后） | 莉莉侧脸、左手指尖碰着颈侧的创可贴：**6A 里创可贴一次都没拍到**（她两次都面朝右，创可贴在左颈被挡住），补6 让观众看见“红痕→创可贴” | 莉莉一个人；创可贴在朝镜头的那一侧、看得清；不笑 |")
md.append("| 补7 | 第 6 集 05 号的位置（替换它） | 红酒泼裙原稿重拍，只换种子：原片两侧各有约 8.5% 黑边 | 没有黑边；红酒泼在玛丽裙上、基利安抓着她手腕（和原片同样的动作） |")
md.append("| 补8 | 第 6 集 07 号的位置（替换它） | 玛丽特写原稿重拍，只换种子：原片两侧各有约 17% 黑边 | 没有黑边；玛丽张着嘴、湿润的眼睛 |\n")
md.append("## 第 1–6 集“最终剪辑顺序”（数字 = 该集碎片文件名里的号；“3-04”= 第 3 集的 04 号；补1…补5 = 本补拍包）\n")
md.append("剧本里第 2 集和第 3 集互相矛盾（保罗看见了基利安／没看见），所以**只能留一条时间线**。我选的是“第 2 集的版本”（保罗看见基利安、被打发走），并把第 3 集里能用的镜头搬了过去。新顺序的两个接缝我已经拿真碎片做过预览（见预览视频）。\n")
md.append("| 集 | 顺序 |\n|---|---|")
md.append("| 第 1 集 | 1、2、3 … 17（不动） |")
md.append("| 第 2 集 | 2-01、2-02、2-03、2-04、**3-04、3-05**（第 3 集的两句气声警告，搬到这里）、2-05、2-06、2-07、2-08、2-09、2-10、2-11、2-12、**补1**、**X1**（第 6 集 B 的 07 号：保罗背对镜头走出门、关门、房间留空；它比 3-07 好，3-07 是在屋内关门。X1 不顺眼就用 3-07） |")
md.append("| 第 3 集 | 3-08（莉莉滑坐在地）、3-09、3-10、3-11、3-12、3-13、**R1**（第 6 集 B 的 10 号：莉莉坐在地上、基利安站着低头看她，两人都在画面里、没有陌生人；它替代 3-14）、**补2** |")
md.append("| 第 4 集 | **补3**、4-01 … 4-10 |")
md.append("| 第 5 集 | **补4**、5-01 … 5-10、**补5**（这样第 5 集结尾不再黑屏卡在“咬下去”，第 6 集开头的创可贴才有来历） |")
md.append("| 第 6 集 | **补6**、6A 的 01、02、03、04、**补7**（替换 6A 的 05）、06、**补8**（替换 6A 的 07）、08 |")
md.append("| **不用的碎片** | 3-01、3-02、3-03、3-06、3-14（共 5 个：保罗“又”进来一次的那几个，和第 2 集矛盾；3-14 是冒出陌生女人的那个）；3-07 留作 X1 不好时的备用；6A 的 05、07（两侧有黑边，补7、补8 替换，补7/补8 若又有黑边就先用原片） |\n")
md.append("## 全部提示词中文全译\n")
for s, zh in zip(segs, ZH):
    dl = '；'.join(f"{x['speaker']}：{x['text']}" for x in s['dialogue']) or '（无台词）'
    md.append(f"### {s['title']}（{s['duration_seconds']} 秒，种子 {s['seed']}，台词：{dl}）\n")
    md.append(f"- **开场图提示词：** {zh}")
    md.append(f"- **视频文字：** {s['shots'][0]['visual_zh']}")
    md.append(f"- **声音：** {s['sound_zh']}\n")
md.append("## 预计会出问题的地方\n")
md.append("- **补3 轿车后座是新场景**：可能冒出司机或第二个人（文字里没写别人，只写了“恰好一个人”）；看开场图。\n- **补2 拿笔的手**：笔和手可能粘在一起或多一只手；看开场图。\n- **补5 压手腕、撑床垫**：两只手各有主人；牙可能还是“咬下去”了，那样补5 就不能用，直接不加。\n- **补1 台词**：念到片尾才结束是常事，验收时听结尾。\n- 补拍的开场图是重新生成的，**脸和房间可能和原来的碎片略有不同**，拼起来看一下，不顺眼的补拍可以不要。\n")
md.append("## 这个补拍包故意避开了什么\n")
md.append("没有新写“人走出画面”的镜头：第 6 集 B 的 X1、X2 已经测过，两个都做成了（人走出去、门关上、房间留空，n=2），所以保罗离开直接用 X1，不再在补拍包里重做。\n")
open(os.path.join(FOLDER, '补拍/补拍包1_说明.md'), 'w', encoding='utf-8').write('\n'.join(md))
print('说明已写')
