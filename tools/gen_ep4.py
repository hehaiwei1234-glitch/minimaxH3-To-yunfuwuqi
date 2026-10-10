#!/usr/bin/env python3
"""第 4 集“羊入虎口”——按 8 条通用规律重写，并附两份对比测试稿（2026-10-09 18:xx）。

  A 版 = 正式版：10 个任务，5–6 秒短片段，承接前段只在“同一批人、同一地点”时打开。
  B 版 = 对比测试：长片段（10/12/15 秒）、一个任务两句台词、片内切镜、现成开场图（opening_frame_key）。
  C 版 = 对比测试：续接（continuity='continue'），只有 3 个任务；需要所选视频工作流带“续接节点”，否则插件会拒绝导入，所以单独放一份。
B、C 以 A 的 JSON 为底（素材、角色逐字相同，手册 F11），不新增素材。B、C 是实验，不进成片。

写法依据 docs/H3通用规律.md 的 8 条：只写想要的（不写 Nobody / No hands / not）；不写程度词；开场图里写清人数、位置、手；
每个动作和声音都有看得见的来源；一个任务一句台词（B 版有意违反，用来测）；提示词里不转述台词。
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _h3draft import Batch, FOLDER, silent, voiced

BASE = '第03集/第03集_制作稿_追加.json'
OUT_A = '第04集/第04集_制作稿_追加'
OUT_B = '第04集/第04集B_对比测试_长片段与现成开场图'
OUT_C = '第04集/第04集C_对比测试_续接'
SERIES_TITLE = json.load(open(os.path.join(FOLDER, BASE), encoding='utf-8'))['title']

V = '[[asset:villa_front]]'; LC = '[[asset:lily_coat]]'; KR = '[[asset:killian_robe]]'; BU = '[[asset:butler]]'
LAY_S = " Fixed stage layout: the black Maybach is at frame-left; the mansion's entrance steps and the balcony above them are at frame-right."
LAY_LK = LAY_S + " Lily is always at frame-left of Killian."
LAY_LB = LAY_S + " Lily is always at frame-left of the butler."
LAY_BAL = " Fixed stage layout: the stone balustrade runs along the bottom of the frame; the tall black iron gates and the dark pine trees stand far behind."
END = " Cold blue dusk light with warm lamps glowing in the mansion's windows."
Z_END = "冷蓝的暮色，庄园的窗里亮着暖灯。"
Z_S = "固定布局：黑色迈巴赫在画面左边；庄园的入口台阶和台阶上方的阳台在画面右边。"
Z_LK = Z_S + "莉莉始终在基利安左边。"
Z_LB = Z_S + "莉莉始终在管家左边。"
Z_BAL = "固定布局：石栏杆横在画面下方；高大的黑色铁门和深色松树在很远的后面。"


class Rec:
    """每份稿子的记录：开场图中文全译、承接标记。"""
    def __init__(self, base, seed0):
        self.b = Batch(base, SERIES_TITLE, seed0)
        self.zh = []

    def T(self, flag, title, dur, chars, assets, refs, img, end, img_zh, vis_zh, cam_zh, dlg, shot_en, shot_zh, sound, **kw):
        s = self.b.task(title, dur, chars, assets, refs, img, end, vis_zh, cam_zh, dlg, shot_en, shot_zh, sound, **kw)
        if not kw.get('cont'):
            s['depends_on_previous'] = flag
        self.zh.append(img_zh)
        return s


# ======================================================================================================
# A 版：正式版
# ======================================================================================================
A = Rec(BASE, 3300)
b = A.b

# ---- 新素材、新角色（庄园门前图的提示词去掉了 “No people / not any people” 这类否定写法）----------------------
b.scene('villa_front', '半山庄园门前',
        ("The gravel forecourt of a gloomy luxurious hillside mansion at dusk: a dark stone facade with tall narrow windows, a wide flight of stone entrance steps on the right, "
         "a second-floor stone balcony with a balustrade above the entrance, tall black iron gates and dark pine trees behind, a black Maybach sedan parked on the gravel on the left, "
         "cold blue dusk light with warm lamps glowing in the windows. The reference fixes the layout and decor."),
        ("黄昏时阴森奢华的半山庄园门前碎石场地：深色石头外墙配高窄窗，右边是宽阔的石头台阶，台阶上方二楼有一座带栏杆的石头阳台，后面是高大的黑色铁门和深色松树，"
         "左边碎石地上停着一辆黑色迈巴赫轿车，冷蓝的暮色里窗内亮着暖灯。参考图固定布局与陈设。"),
        ("A photorealistic ultra-wide 8:3 cinemascope shot of the gravel forecourt of a gloomy luxurious hillside mansion at dusk: a dark stone facade with tall narrow windows, a wide flight of stone entrance steps on the right, "
         "a second-floor stone balcony with a balustrade above the entrance, tall black iron gates and dark pine trees behind, a black Maybach sedan parked on the gravel on the left, "
         "cold blue dusk light with warm lamps in the windows. The frame holds the mansion, the gravel, the car and the pines."))
b.person('butler', '老管家',
         ("The butler, an elderly man in his sixties with neatly combed silver hair, a lined, dignified face and kind pale-blue eyes, wearing a black tailcoat, white shirt, grey waistcoat, black tie and white gloves. "
          "The portrait fixes his identity and clothes, not staging."),
         "老管家，六十多岁的老人，银发梳得整齐，脸上有皱纹、端庄，眼睛是温和的浅蓝色，穿黑色燕尾服、白衬衫、灰色马甲、黑领带，戴白手套。人物图固定身份与衣服，不固定站位。",
         ("A photorealistic half-body portrait of an elderly man in his sixties with neatly combed silver hair, a lined, dignified face and kind pale-blue eyes, wearing a black tailcoat, white shirt, grey waistcoat, black tie and white gloves. "
          "He faces the camera with a calm, courteous expression. Soft even studio light, plain neutral gray background, natural skin texture with visible pores."))
b.person('lily_coat', '莉莉（旅途装）',
         ("Lily, the same adult woman in her mid-twenties as in the reference, with long wavy chestnut-brown hair pulled into a low loose ponytail held by a small silver hair clip, fair skin and large hazel-green eyes, "
          "now wearing a faded grey wool coat over a plain navy dress, tired but proud. The portrait fixes her identity and clothes, not staging."),
         "莉莉，和参考图是同一个二十五岁左右的成年女性，栗棕色长卷发低低地扎成松散的马尾，用一枚小银发卡固定，白皙皮肤、浅褐绿色大眼睛，这次穿褪色的灰色羊毛外套配朴素的藏青连衣裙，疲惫却倔强。人物图固定身份与衣服，不固定站位。",
         ("A photorealistic half-body portrait of the same woman as in the reference image, long wavy chestnut-brown hair pulled into a low loose ponytail held by a small silver hair clip, "
          "wearing a faded grey wool coat over a plain navy dress. She faces the camera with a tired but proud expression. Soft even studio light, plain neutral gray background, natural skin texture with visible pores."),
         ref='lily')
b.person('killian_robe', '基利安（黑丝绸睡袍）',
         ("Killian, the same very tall, broad-shouldered adult man in his early thirties as in the reference, with short swept-back black hair, a sharp jawline, light stubble and cold dark-gray eyes, "
          "now wearing a black silk robe tied at the waist over dark trousers, the collar open at the base of the throat, a platinum luxury wristwatch on his left wrist. The portrait fixes his identity and clothes, not staging."),
         "基利安，和参考图是同一个三十出头、身材极高、肩膀宽阔的成年男性，黑色短发向后梳，下颌线锋利，有浅胡茬，眼睛是冷冽的深灰色，这次穿黑色真丝睡袍，腰间系带，里面是深色长裤，领口开到喉咙下方，左腕戴铂金色名表。人物图固定身份与衣服，不固定站位。",
         ("A photorealistic half-body portrait of the same man as in the reference image, short swept-back black hair, sharp jawline, light stubble and cold dark-gray eyes, "
          "wearing a black silk robe tied at the waist, the collar open at the base of the throat, a platinum luxury wristwatch on his left wrist. He faces the camera with a cold, composed expression. "
          "Soft even studio light, plain neutral gray background, natural skin texture with visible pores."),
         ref='killian')
b.character('Butler', 'butler',
            "An elderly adult male voice, courteous, measured and warm, speaking clear American English at ordinary conversational volume with careful politeness.",
            "年迈的成年男声，彬彬有礼、不急不缓、带着温和，说清楚的美式英语，正常交谈音量，措辞谨慎有礼。")
b.character('LilyCoat', 'lily_coat',
            "A young adult female voice, light and slightly breathy, speaking clear American English. Every word is fully voiced and audible, tight and shaky with nerves, alarm and wounded pride.",
            "年轻成年女声，轻而略带气息，说清楚的美式英语。每个字都正常发声、清晰可辨，声音紧绷发颤，带着紧张、惊慌和受伤的自尊。")
b.character('KillianRobe', 'killian_robe',
            "A mature adult male voice in a deep chest register, low and unhurried with a husky edge, speaking clear American English in a quiet, controlled, menacing tone. He never shouts, and every word is fully voiced and audible.",
            "成熟成年男声，深沉的胸腔音，低缓不急，带沙哑质感，说清楚的美式英语。语气安静、克制、带压迫感，从不喊叫，每个字都正常发声、清晰可辨。")

VIL = ('villa_front',)

# 01 ------------------------------------------------------------------------------------------------
A.T(False, '01｜驶入庄园', 5, [], VIL, ['villa_front'],
    "Wide shot of the gravel forecourt of the dark hillside mansion at dusk, the open gravel in the middle third of the frame, the black Maybach in the left third, stopped on the gravel with its headlights on, the mansion's entrance steps and the balcony above them in the right third. The frame holds the forecourt, the car and the mansion.",
    END,
    "黄昏时阴森的半山庄园门前碎石场地的广角镜头：开阔的碎石地在画面中间三分之一，黑色迈巴赫在画面左三分之一，停在碎石地上，车灯亮着；庄园的入口台阶和台阶上方的阳台在画面右三分之一。画面里是庄园门前、汽车和庄园。" + Z_END,
    "黄昏，黑色迈巴赫开进阴森的半山庄园，慢慢停在碎石地上。画面里只有汽车和庄园。", "0—5秒庄园门前全景，镜头固定。", None,
    f"A steady wide shot opens from the adopted first frame in {V}: the black Maybach rolling the last few metres across the gravel in the left third of the frame and coming to a stop, its headlights lighting the stones, the dark mansion with its entrance steps in the right third. The frame holds the car and the mansion. The camera holds still.",
    "一个稳定的广角镜头，从已采用的开场图继续，场景是庄园门前：黑色迈巴赫在画面左三分之一的碎石地上滑完最后几米，停下，车灯照亮碎石，深色庄园和入口台阶在画面右三分之一。画面里是汽车和庄园。镜头固定不动。",
    silent("A low engine idling down to silence and tyres crunching slowly on gravel.", "低沉的引擎声渐渐熄灭，轮胎在碎石上缓慢碾过。"))

# 02 ------------------------------------------------------------------------------------------------
A.T(True, '02｜旧行李箱', 6, ['LilyCoat'], ('villa_front', 'lily_coat'), ['villa_front'],
    "Medium shot of Lily alone, full body, standing on the gravel beside the open rear door of the black Maybach at frame-left, in profile facing frame-right, centered in the middle third of the frame, in the faded grey wool coat, "
    "a battered brown leather suitcase in her right hand, her eyes on the mansion's entrance steps at frame-right. The frame holds exactly one person, Lily.",
    END + LAY_S,
    "莉莉一个人的中景，全身，站在碎石地上，旁边是画面左边那辆黑色迈巴赫敞开的后车门，侧身朝画面右边，在画面中间三分之一，穿褪色的灰色羊毛外套，右手提着一只破旧的棕色皮行李箱，眼睛看着画面右边庄园的入口台阶。画面里恰好一个人：莉莉。" + Z_END + Z_S,
    "莉莉一个人站在车旁，提着旧行李箱，看着右边庄园的入口。", "0—6秒莉莉侧面中景，镜头固定。", None,
    f"A steady medium shot opens from the adopted first frame in {V}: {LC} alone on the gravel in profile facing frame-right, the battered suitcase in her right hand, her eyes on the mansion's entrance steps at frame-right. "
    "Wind stirs her hair and her knuckles whiten on the suitcase handle. Her feet stay planted on the gravel. The camera holds still.",
    "一个稳定的中景，从已采用的开场图继续，场景是庄园门前：莉莉一个人站在碎石地上，侧身朝画面右边，右手提着旧行李箱，眼睛看着画面右边庄园的入口台阶。风吹动她的头发，握着行李箱把手的指节发白。她的脚稳稳站在碎石上。镜头固定不动。",
    silent("Cold wind in the pine trees and a faint creak of leather.", "冷风吹过松林的声音，皮革轻轻的吱呀声。"))

# 03 ------------------------------------------------------------------------------------------------
A.T(False, '03｜老管家', 6, ['Butler', 'LilyCoat'], ('villa_front', 'butler', 'lily_coat'), ['villa_front'],
    "Medium two-shot, waist-up, in profile, both people centered in the middle third of the frame. Lily stands at frame-left in profile facing frame-right in the faded grey wool coat, the battered brown suitcase on the gravel at her feet; "
    "the elderly butler in his black tailcoat and white gloves stands at frame-right facing her, his hands clasped in front of him, his eyes on her face. The frame holds exactly two people: Lily and the butler.",
    END + LAY_LB,
    "侧面的中景双人镜头，腰部以上，两个人都在画面中间三分之一。莉莉在画面左边，侧身朝画面右边，穿褪色的灰色羊毛外套，破旧的棕色行李箱放在她脚边的碎石地上；老管家穿黑色燕尾服、戴白手套，站在画面右边面对她，双手交叠在身前，眼睛看着她的脸。画面里恰好两个人：莉莉和管家。" + Z_END + Z_LB,
    "老管家站在莉莉面前，双手交叠，恭敬地开口。莉莉愣愣地看着他。", "0—6秒侧面中景，两人居中，莉莉在左、管家在右，镜头固定。",
    ('Butler', "Madam, your room is ready.", 1.0),
    f"A steady medium two-shot in profile opens from the adopted first frame in {V}: {LC} at frame-left, the suitcase at her feet; {BU} at frame-right facing her, his gloved hands clasped in front of him. "
    "He speaks with courteous, measured politeness, his eyes on her face. She stares at him, startled. His hands stay clasped. The camera holds still.",
    "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是庄园门前：莉莉在画面左边，行李箱放在脚边；管家在画面右边面对她，戴着白手套的双手交叠在身前。他有礼、不急不缓地说话，眼睛看着她的脸。她吃惊地看着他。他的手一直交叠。镜头固定不动。",
    voiced("Cold wind and a faint rustle of cloth.", "冷风声和轻微的衣料沙沙声。"))

# 04 ------------------------------------------------------------------------------------------------
A.T(False, '04｜我不是女主人', 6, ['LilyCoat'], ('villa_front', 'lily_coat'), ['villa_front'],
    "Medium close-up of Lily alone, chest-up, in profile facing frame-right, centered in the middle third of the frame, in the faded grey wool coat, her brows drawn together and her lips parted, "
    "her eyes on an old man standing at frame-right, just outside the frame. The frame holds exactly one person, Lily.",
    END + LAY_S,
    "莉莉一个人的中近景，胸部以上，侧身朝画面右边，在画面中间三分之一，穿褪色的灰色羊毛外套，眉头皱起、嘴唇微张，眼睛看着站在画面右边、画面之外的老人。画面里恰好一个人：莉莉。" + Z_END + Z_S,
    "莉莉慌乱地看着右边画面外的管家，开口纠正。", "0—6秒莉莉侧面中近景，镜头固定。",
    ('LilyCoat', "I'm not the lady of the house!", 0.8),
    f"A steady medium close-up opens from the adopted first frame in {V}: {LC} in profile facing frame-right, her eyes on the old man at frame-right, just outside the frame. "
    "She speaks in a flustered, shaky voice, her eyes wide. Her shoulders rise with a quick breath. The camera holds still.",
    "一个稳定的中近景，从已采用的开场图继续，场景是庄园门前：莉莉侧身朝画面右边，眼睛看着画面右边、画面之外的老人。她慌乱地、声音发颤地说话，眼睛睁大。她的肩膀随着急促的呼吸抬起。镜头固定不动。",
    voiced("Cold wind and a faint rustle of cloth.", "冷风声和轻微的衣料沙沙声。"))

# 05 ------------------------------------------------------------------------------------------------
A.T(False, '05｜二楼的基利安', 6, ['KillianRobe'], ('villa_front', 'killian_robe'), ['villa_front'],
    "Medium shot of Killian alone, waist-up, standing at the stone balustrade of the second-floor balcony, centered in the middle third of the frame, in profile facing frame-left, in the black silk robe tied at the waist, "
    "a crystal whiskey tumbler in his right hand, his eyes lowered on a woman standing below at frame-left, just outside the frame, his face cold and unreadable. The frame holds exactly one person, Killian.",
    END + LAY_BAL,
    "基利安一个人的中景，腰部以上，站在二楼阳台的石栏杆边，在画面中间三分之一，侧身朝画面左边，穿腰间系带的黑色真丝睡袍，右手端着水晶威士忌杯，眼睛垂下看着站在楼下画面左边、画面之外的女人，脸冷淡、看不出情绪。画面里恰好一个人：基利安。" + Z_END + Z_BAL,
    "基利安穿着黑色真丝睡袍，端着威士忌，站在二楼阳台上，冷冷地低头看着楼下画面外的莉莉，开口。", "0—6秒基利安侧面中景，镜头固定。",
    ('KillianRobe', "She is. Take her to my bedroom.", 1.0),
    f"A steady medium shot opens from the adopted first frame in {V}: {KR} in profile facing frame-left at the stone balustrade, the whiskey tumbler in his right hand, his eyes lowered on the woman below at frame-left, just outside the frame. "
    "He speaks slowly, his voice low and cold. The glass stays in his hand. The camera holds still.",
    "一个稳定的中景，从已采用的开场图继续，场景是庄园二楼阳台：基利安侧身朝画面左边站在石栏杆边，右手端着威士忌杯，眼睛垂下看着楼下画面左边、画面之外的女人。他慢慢地开口，声音低而冷。酒杯一直在手里。镜头固定不动。",
    voiced("Cold wind and a faint clink of ice in the glass.", "冷风声和杯中冰块轻轻的碰撞声。"))

# 06 ------------------------------------------------------------------------------------------------
A.T(False, '06｜协议里没说', 6, ['LilyCoat'], ('villa_front', 'lily_coat'), ['villa_front'],
    "Medium close-up of Lily alone, chest-up, in profile facing frame-right, centered in the middle third of the frame, in the faded grey wool coat, her chin lifted, her eyes wide and fixed on a man on the balcony above at frame-right, just outside the frame, "
    "her lips parted. The frame holds exactly one person, Lily.",
    END + LAY_S,
    "莉莉一个人的中近景，胸部以上，侧身朝画面右边，在画面中间三分之一，穿褪色的灰色羊毛外套，下巴抬起，睁大眼睛盯着阳台上、画面右上方画面之外的男人，嘴唇微张。画面里恰好一个人：莉莉。" + Z_END + Z_S,
    "莉莉抬起头，瞪大眼睛看着右上方画面外阳台上的基利安，说话。", "0—6秒莉莉侧面中近景，镜头固定。",
    ('LilyCoat', "My bedroom? The contract never said that!", 0.8),
    f"A steady medium close-up opens from the adopted first frame in {V}: {LC} in profile facing frame-right, her chin lifted, her eyes fixed on the man above at frame-right, just outside the frame. "
    "She speaks sharply, her voice shaking with alarm and anger. Her head and lips move. The camera holds still.",
    "一个稳定的中近景，从已采用的开场图继续，场景是庄园门前：莉莉侧身朝画面右边，下巴抬起，眼睛盯着画面右上方、画面之外的男人。她尖声说话，声音因惊慌和愤怒而发颤。她的头和嘴唇在动。镜头固定不动。",
    voiced("Cold wind.", "冷风声。"))

# 07 ------------------------------------------------------------------------------------------------
A.T(False, '07｜阳台空了', 5, [], VIL, ['villa_front'],
    "Medium shot of the second-floor stone balcony above the entrance steps, the stone balustrade centered in the middle third of the frame, a crystal whiskey tumbler with amber whiskey standing on the balustrade. The frame holds the balcony, the balustrade and the glass.",
    END + LAY_BAL,
    "二楼石头阳台的中景，阳台在入口台阶上方，石栏杆在画面中间三分之一，一只盛着琥珀色威士忌的水晶杯放在栏杆上。画面里是阳台、栏杆和酒杯。" + Z_END + Z_BAL,
    "二楼阳台上已经没有人了，石栏杆上只留着那只威士忌酒杯。", "0—5秒空阳台中景，镜头固定。", None,
    f"A steady medium shot opens from the adopted first frame in {V}: the stone balcony, the whiskey tumbler standing on the balustrade. "
    "The glass stays still. Cold wind stirs the dark pine trees behind. The frame holds the balcony and the pines. The camera holds still.",
    "一个稳定的中景，从已采用的开场图继续，场景是二楼阳台：石头阳台，威士忌酒杯放在栏杆上。酒杯一动不动。冷风吹动后面的深色松树。画面里是阳台和松树。镜头固定不动。",
    silent("Cold wind in the pine trees, then a sudden low rush of air.", "冷风吹过松林，然后一阵突然的低沉气流声。"))

# 08–10 的开场图与文字（A 版：构图逐段变化；B/C 版里同一动作用别的连接方式）-----------------------------------------
PIN_MED = ("Medium two-shot, waist-up, in profile, both people centered in the middle third of the frame. Lily stands at frame-left with her back flat against the black door of the Maybach, her hands pressed flat against the car door behind her, "
           "her eyes wide and fixed on Killian's face, her battered suitcase on the gravel at her feet; Killian stands at frame-right facing her, very close, in the black silk robe, his right forearm braced on the car roof above and beside her head, "
           "his whole right arm in the frame, his left hand at his side, his eyes lowered on her face. The frame holds exactly two people: Lily and Killian.")
PIN_MED_ZH = ("侧面的中景双人镜头，腰部以上，两个人都在画面中间三分之一。莉莉在画面左边，后背平贴在黑色迈巴赫的车门上，双手平按在身后的车门上，睁大眼睛盯着基利安的脸，破旧的行李箱放在她脚边的碎石地上；"
              "基利安在画面右边面对她，靠得很近，穿黑色真丝睡袍，右前臂撑在她头旁上方的车顶上，整条右臂都在画面里，左手垂在身侧，眼睛垂下看着她的脸。画面里恰好两个人：莉莉和基利安。")
# 08 ------------------------------------------------------------------------------------------------
A.T(False, '08｜你抵押的全部', 6, ['LilyCoat', 'KillianRobe'], ('villa_front', 'lily_coat', 'killian_robe'), ['villa_front'],
    PIN_MED, END + LAY_LK, PIN_MED_ZH + Z_END + Z_LK,
    "基利安已经站在莉莉面前，把她逼到车门上，一只手撑在车顶，低头看着她，开口。", "0—6秒侧面中景，两人居中，莉莉在左、基利安在右，镜头固定。",
    ('KillianRobe', "Read it again. You pledged everything.", 1.0),
    f"A steady medium two-shot in profile opens from the adopted first frame in {V}: {LC} with her back against the car door, her eyes wide and fixed on {KR}'s face; {KR} close in front of her, his right forearm braced on the car roof. "
    "He speaks low and slowly, his eyes on her face. She stays pressed against the door. The camera holds still.",
    "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是庄园门前：莉莉背靠车门，睁大眼睛盯着基利安的脸；基利安紧贴在她面前，右前臂撑在车顶上。他低声缓慢地说话，眼睛看着她的脸。她一直贴在车门上。镜头固定不动。",
    voiced("Cold wind and a faint creak of the car body.", "冷风声和车身轻微的吱呀声。"))

# 09 ------------------------------------------------------------------------------------------------
A.T(True, '09｜抽走发卡', 6, ['LilyCoat', 'KillianRobe'], ('villa_front', 'lily_coat', 'killian_robe'), ['villa_front'],
    "Tight side-profile two-shot of heads and shoulders, both people centered in the middle third of the frame. Lily at frame-left has her back against the black car door, her low ponytail held by a small silver hair clip, "
    "her hands pressed flat against the car door behind her, her eyes fixed on Killian's face; Killian at frame-right faces her very close, his right hand raised to the silver clip behind her ear, his whole right forearm in the frame, his eyes on her face. "
    "The frame holds exactly two people: Lily and Killian.",
    END + LAY_LK,
    "头肩的侧面近景双人镜头，两个人都在画面中间三分之一。莉莉在画面左边，后背贴着黑色车门，低马尾上别着一枚小银发卡，双手平按在身后的车门上，眼睛盯着基利安的脸；基利安在画面右边，靠得很近面对她，右手抬到她耳后的银发卡处，整条右前臂都在画面里，眼睛看着她的脸。画面里恰好两个人：莉莉和基利安。" + Z_END + Z_LK,
    "基利安伸手把莉莉发间的发卡抽走，她的长发散落下来。", "0—6秒侧面近景，两人头肩居中，莉莉在左、基利安在右，镜头固定。", None,
    f"A steady tight side-profile two-shot opens from the adopted first frame in {V}: {KR}'s right hand at the silver clip in {LC}'s hair, her eyes fixed on his face. "
    "He draws the clip out between two fingers and her long hair falls loose around her shoulders. Her eyes stay on his. The camera holds still.",
    "一个稳定的侧面近景双人镜头，从已采用的开场图继续，场景是庄园门前：基利安的右手在莉莉发间的银发卡上，她的眼睛盯着他的脸。他用两根手指把发卡抽出来，她的长发散落在肩上。她的目光一直停在他眼睛上。镜头固定不动。",
    silent("A tiny click of the clip and the soft rustle of hair falling.", "发卡轻轻的咔哒声和头发散落的沙沙声。"))

# 10 ------------------------------------------------------------------------------------------------
A.T(True, '10｜颈窝', 6, ['LilyCoat', 'KillianRobe'], ('villa_front', 'lily_coat', 'killian_robe'), ['villa_front'],
    "Tight side-profile two-shot of heads and shoulders, both people centered in the middle third of the frame. Killian's face at frame-right is lowered into the curve of Lily's neck, his eyes closed, "
    "his right hand resting on the black car door beside her head, his whole right forearm in the frame; Lily at frame-left has her long loose chestnut hair around her shoulders, her eyes wide, her head turned toward frame-left, "
    "her hands pressed flat against the car door behind her. The frame holds exactly two people: Lily and Killian.",
    END + LAY_LK,
    "头肩的侧面近景双人镜头，两个人都在画面中间三分之一。基利安在画面右边，脸低下埋进莉莉的颈窝，闭着眼睛，右手放在她头旁的黑色车门上，整条右前臂都在画面里；莉莉在画面左边，栗棕色的长发松散地披在肩上，睁大眼睛，头转向画面左边，双手平按在身后的车门上。画面里恰好两个人：莉莉和基利安。" + Z_END + Z_LK,
    "基利安低头埋进莉莉的颈窝，深深吸了一口气，再睁开眼，眼神变得极其危险。（成片里在这里切断）", "0—6秒侧面近景，两人头肩居中，莉莉在左、基利安在右，镜头固定。", None,
    f"A steady tight side-profile two-shot opens from the adopted first frame in {V}: {KR}'s face lowered into the curve of {LC}'s neck, his eyes closed, her loose hair around her shoulders. "
    "He draws one long slow breath, then his eyes open, dark and intent, his face still against her neck. She stays pressed against the door. The camera holds still.",
    "一个稳定的侧面近景双人镜头，从已采用的开场图继续，场景是庄园门前：基利安的脸埋在莉莉的颈窝里，闭着眼，她的长发散在肩上。他慢慢吸了一口长气，然后睁开眼，眼神深沉而危险，脸仍贴在她的颈边。她一直贴在车门上。镜头固定不动。",
    silent("Faint rustle of hair and cloth, then quiet.", "头发和衣料轻轻的沙沙声，然后安静。"))

A_SUMMARY = ('黑色迈巴赫驶入阴森的半山庄园，莉莉提着旧行李箱下车。老管家称她“女主人”，她慌乱地纠正；二楼阳台上的基利安说“她就是”，要她住进他的卧室。'
             '她抗议协议里没写，他却转眼出现在她面前，把她逼到车门上，说她抵押的是“全部”，抽走她的发卡，低头埋进她的颈窝。')
A.b.finish('第4集｜羊入虎口', A_SUMMARY, OUT_A)

# ======================================================================================================
# B 版：长片段 + 一个任务两句台词 + 片内切镜 + 现成开场图（对比测试，不进成片）
# ======================================================================================================
B = Rec(OUT_A + '.json', 3350)

# B00 现成开场图 --------------------------------------------------------------------------------------
B.T(False, '00｜庄园全景（现成开场图）', 5, [], (), [],
    "Wide shot of the gravel forecourt of the dark hillside mansion at dusk, the open gravel in the middle third of the frame, the black Maybach in the left third, the mansion's entrance steps and the balcony above them in the right third. The frame holds the forecourt, the car and the mansion.",
    END,
    "黄昏时阴森的半山庄园门前碎石场地的广角镜头：开阔的碎石地在画面中间三分之一，黑色迈巴赫在画面左三分之一，庄园的入口台阶和台阶上方的阳台在画面右三分之一。画面里是庄园门前、汽车和庄园。" + Z_END + "（这个任务不生成开场图，直接用素材图“半山庄园门前”当第一帧，这段话不会被使用。）",
    "庄园门前的全景，风吹动松树，窗里的灯光闪动。", "0—5秒庄园门前全景，镜头固定。", None,
    f"A steady wide shot opens from the adopted first frame in {V}: the dark hillside mansion at dusk, the black Maybach parked on the gravel in the left third of the frame, the entrance steps and the balcony above them in the right third. "
    "Wind moves the dark pine branches behind the mansion and the lamps in the windows flicker. The frame holds the car and the mansion. The camera holds still.",
    "一个稳定的广角镜头，从已采用的开场图继续，场景是庄园门前：黄昏时阴森的庄园，黑色迈巴赫停在画面左三分之一的碎石地上，入口台阶和台阶上方的阳台在画面右三分之一。风吹动庄园后面深色的松树枝，窗里的灯光闪动。画面里是汽车和庄园。镜头固定不动。",
    silent("Cold wind in the pine trees and a faint electrical hum from the lamps.", "冷风吹过松林，灯里轻微的电流嗡嗡声。"),
    frame='villa_front')

# B01 10 秒、一次切镜、无台词（对比 A 的 01+02）---------------------------------------------------------
B.T(False, '01｜驶入并站定（10秒一次切镜）', 10, ['LilyCoat'], ('villa_front', 'lily_coat'), ['villa_front'],
    "Wide shot of the gravel forecourt of the dark hillside mansion at dusk, the open gravel in the middle third of the frame, the black Maybach in the left third, stopped on the gravel with its headlights on, the mansion's entrance steps and the balcony above them in the right third. The frame holds the forecourt, the car and the mansion.",
    END,
    "（和 A 版 01 号的开场图相同）黄昏时阴森的半山庄园门前碎石场地的广角镜头：开阔的碎石地在画面中间三分之一，黑色迈巴赫在画面左三分之一，停在碎石地上，车灯亮着；庄园的入口台阶和台阶上方的阳台在画面右三分之一。画面里是庄园门前、汽车和庄园。" + Z_END,
    "黑色迈巴赫开进庄园停下；切镜后莉莉一个人站在车旁，提着旧行李箱，看着右边庄园的入口。", "0—4.5秒庄园全景；4.5—10秒莉莉侧面中景；镜头都固定。", None,
    None, None,
    silent("A low engine idling down to silence and tyres crunching slowly on gravel, then cold wind in the pine trees.", "低沉的引擎声渐渐熄灭，轮胎在碎石上缓慢碾过，然后冷风吹过松林。"),
    shots=[(0, 4.5,
            f"A steady wide shot opens from the adopted first frame in {V}: the black Maybach rolling the last few metres across the gravel in the left third of the frame and coming to a stop, its headlights lighting the stones, the dark mansion with its entrance steps in the right third. The frame holds the car and the mansion. The camera holds still.",
            "一个稳定的广角镜头，从已采用的开场图继续，场景是庄园门前：黑色迈巴赫在画面左三分之一的碎石地上滑完最后几米，停下，车灯照亮碎石，深色庄园和入口台阶在画面右三分之一。画面里是汽车和庄园。镜头固定不动。", []),
           (4.5, 10,
            f"A steady medium shot of the same forecourt: {LC} alone on the gravel beside the open rear door of the black Maybach at frame-left, in profile facing frame-right, the battered suitcase in her right hand, her eyes on the mansion's entrance steps at frame-right. "
            "Behind her the dark stone facade, the balcony above the entrance steps, the tall black iron gates and the dark pines. Wind stirs her hair and her knuckles whiten on the suitcase handle. Her feet stay planted on the gravel. The camera holds still.",
            "一个稳定的中景，同一个庄园门前：莉莉一个人站在碎石地上，旁边是画面左边那辆黑色迈巴赫敞开的后车门，侧身朝画面右边，右手提着旧行李箱，眼睛看着画面右边庄园的入口台阶。她身后是深色石头外墙、入口台阶上方的阳台、高大的黑色铁门和深色松树。风吹动她的头发，握着行李箱把手的指节发白。她的脚稳稳站在碎石上。镜头固定不动。", [])])

# B02 10 秒、一个任务两位说话人（对比 A 的 03+04）---------------------------------------------------------
B.T(False, '02｜管家和莉莉（一个任务两句话）', 10, ['Butler', 'LilyCoat'], ('villa_front', 'butler', 'lily_coat'), ['villa_front'],
    "Medium two-shot, waist-up, in profile, both people centered in the middle third of the frame. Lily stands at frame-left in profile facing frame-right in the faded grey wool coat, the battered brown suitcase on the gravel at her feet; "
    "the elderly butler in his black tailcoat and white gloves stands at frame-right facing her, his hands clasped in front of him, his eyes on her face. The frame holds exactly two people: Lily and the butler.",
    END + LAY_LB,
    "（和 A 版 03 号的开场图相同）侧面的中景双人镜头，腰部以上，两个人都在画面中间三分之一。莉莉在画面左边，侧身朝画面右边，穿褪色的灰色羊毛外套，破旧的棕色行李箱放在她脚边的碎石地上；老管家穿黑色燕尾服、戴白手套，站在画面右边面对她，双手交叠在身前，眼睛看着她的脸。画面里恰好两个人：莉莉和管家。" + Z_END + Z_LB,
    "老管家先开口，莉莉愣了一下，再慌乱地回答。", "0—10秒侧面中景，两人居中，莉莉在左、管家在右，镜头固定。", None,
    None, None,
    voiced("Cold wind and a faint rustle of cloth.", "冷风声和轻微的衣料沙沙声。"),
    lines=[('Butler', "Madam, your room is ready.", 1.0), ('LilyCoat', "I'm not the lady of the house!", 5.2)],
    shots=[(0, 10,
            f"A steady medium two-shot in profile opens from the adopted first frame in {V}: {LC} at frame-left, the suitcase at her feet; {BU} at frame-right facing her, his gloved hands clasped in front of him. "
            "He speaks first with courteous, measured politeness, his eyes on her face. She stares at him, startled, then answers in a flustered, shaky voice, her eyes wide. His hands stay clasped. The camera holds still.",
            "一个稳定的侧面中景双人镜头，从已采用的开场图继续，场景是庄园门前：莉莉在画面左边，行李箱放在脚边；管家在画面右边面对她，戴着白手套的双手交叠在身前。他先有礼、不急不缓地说话，眼睛看着她的脸。她吃惊地看着他，然后慌乱地、声音发颤地回答，眼睛睁大。他的手一直交叠。镜头固定不动。", [0, 1])])

# B03 12 秒、阳台→回头、一次切镜、两位说话人（对比 A 的 05+06）----------------------------------------------
B.T(False, '03｜阳台上说，莉莉回话（12秒一次切镜）', 12, ['KillianRobe', 'LilyCoat'], ('villa_front', 'killian_robe', 'lily_coat'), ['villa_front'],
    "Medium shot of Killian alone, waist-up, standing at the stone balustrade of the second-floor balcony, centered in the middle third of the frame, in profile facing frame-left, in the black silk robe tied at the waist, "
    "a crystal whiskey tumbler in his right hand, his eyes lowered on a woman standing below at frame-left, just outside the frame, his face cold and unreadable. The frame holds exactly one person, Killian.",
    END + LAY_BAL,
    "（和 A 版 05 号的开场图相同）基利安一个人的中景，腰部以上，站在二楼阳台的石栏杆边，在画面中间三分之一，侧身朝画面左边，穿腰间系带的黑色真丝睡袍，右手端着水晶威士忌杯，眼睛垂下看着站在楼下画面左边、画面之外的女人，脸冷淡、看不出情绪。画面里恰好一个人：基利安。" + Z_END + Z_BAL,
    "基利安在阳台上开口；切镜后莉莉抬头瞪着他，回话。", "0—5.5秒基利安侧面中景；5.5—12秒莉莉侧面中近景；镜头都固定。", None,
    None, None,
    voiced("Cold wind and a faint clink of ice in the glass.", "冷风声和杯中冰块轻轻的碰撞声。"),
    lines=[('KillianRobe', "She is. Take her to my bedroom.", 0.8), ('LilyCoat', "My bedroom? The contract never said that!", 6.3)],
    shots=[(0, 5.5,
            f"A steady medium shot opens from the adopted first frame in {V}: {KR} in profile facing frame-left at the stone balustrade, the whiskey tumbler in his right hand, his eyes lowered on the woman below at frame-left, just outside the frame. "
            "He speaks slowly, his voice low and cold. The glass stays in his hand. The camera holds still.",
            "一个稳定的中景，从已采用的开场图继续，场景是庄园二楼阳台：基利安侧身朝画面左边站在石栏杆边，右手端着威士忌杯，眼睛垂下看着楼下画面左边、画面之外的女人。他慢慢地开口，声音低而冷。酒杯一直在手里。镜头固定不动。", [0]),
           (5.5, 12,
            f"A steady medium close-up of the forecourt below: {LC} alone in profile facing frame-right, her chin lifted, her eyes fixed on the man on the balcony above at frame-right, just outside the frame. "
            "Behind her the black Maybach at frame-left and the stone entrance steps at frame-right. She speaks sharply, her voice shaking with alarm and anger. Her head and lips move. The camera holds still.",
            "一个稳定的中近景，楼下的庄园门前：莉莉一个人侧身朝画面右边，下巴抬起，眼睛盯着画面右上方阳台上、画面之外的男人。她身后，黑色迈巴赫在画面左边，石头入口台阶在画面右边。她尖声说话，声音因惊慌和愤怒而发颤。她的头和嘴唇在动。镜头固定不动。", [1])])

# B04 15 秒一个长镜头（对比 A 的 08+09+10 和 C 版）--------------------------------------------------------
PIN_CHEST = ("Medium close two-shot, chest-up, in profile, both people centered in the middle third of the frame. Lily stands at frame-left with her back flat against the black door of the Maybach, her low ponytail held by a small silver hair clip, "
             "her hands pressed flat against the car door behind her, her eyes wide and fixed on Killian's face; Killian stands at frame-right facing her, very close, in the black silk robe, his right forearm braced on the car roof above and beside her head, "
             "his whole right arm in the frame, his left hand at his side, his eyes lowered on her face. The frame holds exactly two people: Lily and Killian.")
PIN_CHEST_ZH = ("侧面的中近景双人镜头，胸部以上，两个人都在画面中间三分之一。莉莉在画面左边，后背平贴在黑色迈巴赫的车门上，低马尾上别着一枚小银发卡，双手平按在身后的车门上，睁大眼睛盯着基利安的脸；"
                "基利安在画面右边面对她，靠得很近，穿黑色真丝睡袍，右前臂撑在她头旁上方的车顶上，整条右臂都在画面里，左手垂在身侧，眼睛垂下看着她的脸。画面里恰好两个人：莉莉和基利安。")
B.T(False, '04｜逼到车门到埋进颈窝（15秒一个镜头）', 15, ['LilyCoat', 'KillianRobe'], ('villa_front', 'lily_coat', 'killian_robe'), ['villa_front'],
    PIN_CHEST, END + LAY_LK, "（和 C 版 01 号的开场图相同）" + PIN_CHEST_ZH + Z_END + Z_LK,
    "基利安把莉莉逼在车门上说话；然后抽走她的发卡，长发散落；再低头埋进她的颈窝，吸气，睁眼。", "0—15秒侧面中近景，两人居中，镜头固定。",
    ('KillianRobe', "Read it again. You pledged everything.", 1.5),
    f"A steady medium close side-profile two-shot opens from the adopted first frame in {V}: {LC} with her back against the car door, her eyes fixed on {KR}'s face; {KR} close in front of her, his right forearm braced on the car roof. "
    f"He speaks low and slowly, his eyes on her face. Then his right hand comes down from the car roof to the silver clip behind her ear and draws the clip out between two fingers, and her long hair falls loose around her shoulders; her eyes stay on his. "
    "Then he lowers his face into the curve of her neck, his eyes closed, and draws one long slow breath, and his eyes open, dark and intent. She stays pressed against the door. The camera holds still.",
    "一个稳定的侧面中近景双人镜头，从已采用的开场图继续，场景是庄园门前：莉莉背靠车门，眼睛盯着基利安的脸；基利安紧贴在她面前，右前臂撑在车顶上。他低声缓慢地说话，眼睛看着她的脸。然后他的右手从车顶放下来，伸到她耳后的银发卡处，用两根手指把发卡抽出来，她的长发散落在肩上；她的目光一直停在他眼睛上。"
    "然后他把脸低下，埋进她的颈窝，闭着眼，慢慢吸了一口长气，再睁开眼，眼神深沉而危险。她一直贴在车门上。镜头固定不动。",
    voiced("Cold wind, a tiny click of the clip and the soft rustle of hair falling.", "冷风声，发卡轻轻的咔哒声和头发散落的沙沙声。"))
b_seed_fix = B.b.tasks[-1]; b_seed_fix['seed'] = 3308
B_SUMMARY = '（对比测试稿，不进成片）同一段剧情用长片段、一个任务两句台词、片内切镜、现成开场图重新拍一遍：庄园全景；迈巴赫驶入、莉莉站定；管家称她女主人、她纠正；基利安在阳台上让她住进他的卧室、她抗议；他把她逼到车门上，抽走发卡，埋进她的颈窝。'
B.b.finish('第4集B｜对比测试：长片段与现成开场图', B_SUMMARY, OUT_B)

# ======================================================================================================
# C 版：续接（continue）对比：同一个连续动作拆成 3 个 6 秒任务，第 2、3 个用续接（需要带续接节点的工作流）
# ======================================================================================================
C = Rec(OUT_A + '.json', 3360)
C.T(False, '01｜你抵押的全部（续接起点）', 6, ['LilyCoat', 'KillianRobe'], ('villa_front', 'lily_coat', 'killian_robe'), ['villa_front'],
    PIN_CHEST, END + LAY_LK, "（和 B 版 04 号的开场图相同）" + PIN_CHEST_ZH + Z_END + Z_LK,
    "基利安把莉莉逼在车门上，低头看着她，开口。", "0—6秒侧面中近景，两人居中，镜头固定。",
    ('KillianRobe', "Read it again. You pledged everything.", 1.0),
    f"A steady medium close side-profile two-shot opens from the adopted first frame in {V}: {LC} with her back against the car door, her eyes fixed on {KR}'s face; {KR} close in front of her, his right forearm braced on the car roof. "
    "He speaks low and slowly, his eyes on her face. She stays pressed against the door. The camera holds still.",
    "一个稳定的侧面中近景双人镜头，从已采用的开场图继续，场景是庄园门前：莉莉背靠车门，眼睛盯着基利安的脸；基利安紧贴在她面前，右前臂撑在车顶上。他低声缓慢地说话，眼睛看着她的脸。她一直贴在车门上。镜头固定不动。",
    voiced("Cold wind and a faint creak of the car body.", "冷风声和车身轻微的吱呀声。"))
C.b.tasks[-1]['seed'] = 3308
C.T(True, '02｜抽走发卡（续接）', 6, ['LilyCoat', 'KillianRobe'], ('villa_front', 'lily_coat', 'killian_robe'), ['villa_front'],
    PIN_CHEST, END + LAY_LK, "（开场图和 01 号相同，因为 01 号结束时就是这个姿势）" + PIN_CHEST_ZH + Z_END + Z_LK,
    "基利安的右手从车顶放下来，把莉莉发间的发卡抽走，她的长发散落下来。", "0—6秒侧面中近景，两人居中，镜头固定（和上一段相同）。", None,
    f"A steady medium close side-profile two-shot continues from the previous shot in {V}: {LC} with her back against the car door, her eyes fixed on {KR}'s face; {KR} close in front of her. "
    "His right hand comes down from the car roof to the silver clip behind her ear and draws the clip out between two fingers, and her long hair falls loose around her shoulders. Her eyes stay on his. The camera holds still.",
    "一个稳定的侧面中近景双人镜头，接着上一段继续，场景是庄园门前：莉莉背靠车门，眼睛盯着基利安的脸；基利安紧贴在她面前。他的右手从车顶放下来，伸到她耳后的银发卡处，用两根手指把发卡抽出来，她的长发散落在肩上。她的目光一直停在他眼睛上。镜头固定不动。",
    silent("A tiny click of the clip and the soft rustle of hair falling.", "发卡轻轻的咔哒声和头发散落的沙沙声。"), cont=True)
C.b.tasks[-1]['seed'] = 3309
C.T(True, '03｜颈窝（续接）', 6, ['LilyCoat', 'KillianRobe'], ('villa_front', 'lily_coat', 'killian_robe'), ['villa_front'],
    "Medium close two-shot, chest-up, in profile, both people centered in the middle third of the frame. Lily stands at frame-left with her back against the black door of the Maybach, her long loose chestnut hair around her shoulders, "
    "her hands pressed flat against the car door behind her, her eyes wide and fixed on Killian's face; Killian stands at frame-right facing her, very close, his right hand lowered to his side holding the silver hair clip, his eyes on her face. "
    "The frame holds exactly two people: Lily and Killian.",
    END + LAY_LK,
    "（开场图是 02 号结束时的状态）侧面的中近景双人镜头，胸部以上，两个人都在画面中间三分之一。莉莉在画面左边，后背贴着黑色迈巴赫的车门，栗棕色的长发松散地披在肩上，双手平按在身后的车门上，睁大眼睛盯着基利安的脸；基利安在画面右边面对她，靠得很近，右手垂到身侧，手里拿着那枚银发卡，眼睛看着她的脸。画面里恰好两个人：莉莉和基利安。" + Z_END + Z_LK,
    "基利安低头埋进莉莉的颈窝，深深吸了一口气，再睁开眼，眼神变得极其危险。（成片里在这里切断）", "0—6秒侧面中近景，两人居中，镜头固定（和上一段相同）。", None,
    f"A steady medium close side-profile two-shot continues from the previous shot in {V}: {KR} lowers his face into the curve of {LC}'s neck, his eyes closed, her loose hair around her shoulders. "
    "He draws one long slow breath, then his eyes open, dark and intent, his face still against her neck. She stays pressed against the door. The camera holds still.",
    "一个稳定的侧面中近景双人镜头，接着上一段继续，场景是庄园门前：基利安把脸低下，埋进莉莉的颈窝，闭着眼，她的长发散在肩上。他慢慢吸了一口长气，然后睁开眼，眼神深沉而危险，脸仍贴在她的颈边。她一直贴在车门上。镜头固定不动。",
    silent("Faint rustle of hair and cloth, then quiet.", "头发和衣料轻轻的沙沙声，然后安静。"), cont=True)
C.b.tasks[-1]['seed'] = 3310
C_SUMMARY = '（对比测试稿，不进成片）基利安把莉莉逼在车门上说“你抵押的是全部”，然后抽走她的发卡，低头埋进她的颈窝。这一连串动作拆成 3 个任务，用“续接”连起来。'
C.b.finish('第4集C｜对比测试：续接', C_SUMMARY, OUT_C)

# ======================================================================================================
# 说明
# ======================================================================================================
def table(rec, with_chain=True):
    segs = rec.b.tasks
    rows = ["| 号 | 名字 | 秒 | 在场人数 | 连接方式 | 英语台词 | 种子 |", "|---|---|---|---|---|---|---|"]
    for i, s in enumerate(segs):
        if s['dialogue']:
            dl = '；'.join(f"{x['speaker']}：{x['text']}（{x['start_seconds']}秒开口计划）" for x in s['dialogue'])
        else:
            dl = '（无台词）'
        if s['continuity'] == 'continue':
            link = '续接'
        elif s.get('opening_frame_key'):
            link = '现成开场图'
        elif s['depends_on_previous']:
            link = '承接前段'
        else:
            link = '硬切'
        rows.append(f"| {i+1:02d} | {s['title'].split('｜')[1]} | {s['duration_seconds']} | {len(s['characters'])} | {link} | {dl} | {s['seed']} |")
    return '\n'.join(rows)


def prompts(rec):
    out = []
    for i, s in enumerate(rec.b.tasks):
        out.append(f"### {i+1:02d}｜{s['title'].split('｜')[1]}（{s['duration_seconds']} 秒）")
        out.append(f"- **开场图：** {rec.zh[i]}")
        for k, sh in enumerate(s['shots']):
            tag = f"视频（镜头{k+1}：{sh['start_seconds']}—{sh['end_seconds']}秒）" if len(s['shots']) > 1 else '视频'
            out.append(f"- **{tag}：** {sh['visual_zh']}")
        out.append(f"- **声音：** {s['sound_zh']}")
        for x in s['dialogue']:
            out.append(f"- **台词（单独传给插件）：** {x['speaker']}：“{x['text']}”（计划 {x['start_seconds']}—{x['end_seconds']} 秒）")
        out.append("")
    return '\n'.join(out)


STYLE_NOTE = ("每个任务的视频提示词前面还会加这句固定的风格话：**“真人实拍，电影感，写实，皮肤有自然质感，浅景深，温暖奢华的光线，超宽 8:3 宽银幕画面。”** "
              "开场图提示词前面也有一段固定的开头：**“一张来自写实真人浪漫惊悚片的完整首帧，超宽 8:3 宽银幕构图。皮肤自然，能看到毛孔，布料和材质真实。固定的场景参考图决定地点，人物肖像只决定被点名的人。”** 下面不再重复。")

md = []
md.append("# 第 4 集（英语台词、追加批次）：正式版 + 两份对比测试（2026-10-09）\n")
md.append(f"""这一集有三个文件，**只有 A 是正式的，B、C 是实验，不进成片**。

| 文件 | 用途 | 任务 | 秒 | 要不要跑 |
|---|---|---|---|---|
| `{OUT_A}_全选复制粘贴.txt` | **A 正式版**：5–6 秒短片段，承接前段只在“同一批人、同一地点”时打开 | {len(A.b.tasks)} | {sum(t['duration_seconds'] for t in A.b.tasks)} | 要，接在第 3 集之后 |
| `{OUT_B}_全选复制粘贴.txt` | **B 对比**：长片段、一个任务两句台词、片内切镜、现成开场图 | {len(B.b.tasks)} | {sum(t['duration_seconds'] for t in B.b.tasks)} | 想测再跑，放在 A 之后；也可以放进总文档最后 |
| `{OUT_C}_全选复制粘贴.txt` | **C 对比**：续接（continue），同一个连续动作拆 3 段 | {len(C.b.tasks)} | {sum(t['duration_seconds'] for t in C.b.tasks)} | **只有视频工作流带“续接节点”才能导入**；导入报“所选工作流没有关联续接输入”就不用管它 |

三个文件的素材和人物逐字相同（追加规则 F11），所以 B、C 必须在 A 之后追加，每一份要等上一份全部跑完才能追加（插件源码里有这个检查）。B、C 在插件里会各占一集的位置，看完视频可以删掉。
""")
md.append("## 一、这次查清的插件事实（来自源码 v0.8.3.6，写稿部分与 v0.8.3.10 相同）\n")
md.append("""- **`opening_frame_key` 不是续接开关**：它的意思是“这个任务不生成开场图，直接拿一张现成的图当第一帧”（图必须是稿子里声明过的图片素材），并且**不能同时用承接前段**。续接开关是 **`continuity: "continue"`**（同时必须 `depends_on_previous: true`；每集第一个任务必须是 `cut`）。
- **续接要工作流支持**：所选视频工作流里必须接好“续接节点”（上一段视频、续接开关、重叠秒数），否则导入时就报错。
- **`use_previous_episode_state`**（稿子里每个任务都有，我一直写 false）：只给每集第 1 个任务用，意思是把上一集最后采用的画面当位置参考。第 3 集结尾是试衣间、第 4 集开头是庄园，地点不同，所以这一集用不上。
- **追加时同名素材应该沿用旧图（读源码得出，没实测）**：追加窗口会把同名的素材绑定到第一批已经生成好的图，不会重新画。如果成立，“第 2 集房间和第 1 集对不上”就不是房间素材图被重画，而是**每个片段的开场图每次都是重新生成的**；要压住这个，只能靠固定布局句子、承接前段，或者用现成开场图。验证很简单：看第 2、3 集里的人物脸和房间素材是不是和第 1 集同一张。（我之前记的“写成 generate 会重新生成”可能只在整份稿子单独新建时成立，这条等你验证后再决定要不要改。）
""")
md.append("## 二、A 正式版（10 个任务）\n")
md.append(table(A))
md.append("""
**这一版和旧版第 4 集的区别：** 不再写 “Nobody else / No hands”，人数改写成 “The frame holds exactly N people”；去掉 “slightly / only / perfectly” 这类程度词；每只手的位置写清楚（尤其 08–10 号：基利安的右前臂撑车顶、抽发卡的是他的右手、莉莉的双手按在车门上）；固定布局句子按场景分开写（庄园门前一套，阳台一套）；承接前段只在 02（前一个没有人）、09、10（同一对人、同一个地方、连续动作）打开。

**台词改动：** “女主人”不写 mistress（在美国人耳朵里是“情妇”），改成 “the lady of the house”；“主卧”改成 “bedroom”；莉莉原来的 “我只是……” 太长，只留前半句。其余照旧。

**台词时间：** 每句 7 个单词以内，每句后面留 1 秒以上。照旧：声音常常到片尾才结束，验收时听结尾。
""")
md.append("### A 版：给 H3 的提示词（中文全译，一个字不漏）\n")
md.append(STYLE_NOTE + "\n")
md.append(prompts(A))
md.append("## 三、B 对比测试（5 个任务）：做完能得到什么\n")
md.append(table(B))
md.append(f"""
| 对比 | 看什么 | 做完能得到 |
|---|---|---|
| B00 | 用素材图当第一帧（`opening_frame_key`）：比例对不对（要 8:3）、画面是不是和素材图一模一样、风吹松树的动作像不像 | 这个办法能不能用。能用的话，以后每集第 1 个任务可以用一张**你挑好的图**当第一帧，跨集场景就能对上 |
| B01 对比 A 的 01+02 | 10 秒里一次切镜：切镜之后车、台阶、阳台、铁门还在不在原来的位置；切镜时间（计划 4.5 秒）；莉莉像不像人物图 | “接缝在片内”和“接缝在片间”哪个更稳（规律 7、假设 H12） |
| B02 对比 A 的 03+04 | 一个任务两个人各说一句：两句都念了没有、顺序对不对、口型是不是对的人、有没有乱码 | 一个任务能不能放两句台词（能的话任务数可以少一半） |
| B03 对比 A 的 05+06 | 阳台→楼下回头的切镜 + 两句台词：第一句有没有在切镜前念完（计划 5.5 秒）、莉莉脸对不对 | 对话场面能不能用“片内切镜”代替两个任务 |
| B04 对比 A 的 08+09+10 和 C | 15 秒一个镜头完成“逼到车门→抽发卡→埋颈窝”：三个动作的顺序做不做得出来、人物有没有变形 | 长镜头连续动作和“承接前段”（A）、“续接”（C）哪个最连贯 |

**风险（我预判，没试过）：** B04 一连串动作可能只做出前一两个；B02/B03 两句台词的第二句可能被挤到片尾或念成含糊的声音；15 秒的片段更容易在后半段人物变形；B01、B03 的开场图里因为同时带了两个人的肖像，可能多出另一个人，请先看开场图（B03 的开场图应该只有基利安）。
""")
md.append("### B 版：给 H3 的提示词（中文全译）\n")
md.append(prompts(B))
md.append("## 四、C 对比测试（3 个任务）：做完能得到什么\n")
md.append(table(C))
md.append("""
**做法：** 和 B04 同一段动作，拆成 3 个 6 秒任务。02、03 号用续接：上一段的最后约 1 秒（22 帧）会被原样放到新片段开头，所以三个任务的镜头位置和构图写成一样（都是侧面中近景），只写动作的继续。

**做完能得到：** 连续动作用“续接”拆开，接缝是不是真的看不出来；和 A（承接前段、每段构图不同）、B04（15 秒一个镜头）比，哪个最连贯。这是续接的第 2 次实测（第 1 次是 277 帧的 O5，出了花屏），本稿每段只有 6 秒，帧数远小于那次。

**如果导入报“所选工作流没有关联续接输入”，这份就不能用，不用管它，对 A、B 没有影响。**
""")
md.append("### C 版：给 H3 的提示词（中文全译）\n")
md.append(prompts(C))
open(os.path.join(FOLDER, '第04集/第04集_说明.md'), 'w', encoding='utf-8').write('\n'.join(md))
print('说明已写')
