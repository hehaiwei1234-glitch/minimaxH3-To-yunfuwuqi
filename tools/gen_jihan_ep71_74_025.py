#!/usr/bin/env python3
"""《极寒末日：我的隐秘安全屋》剧本第 71–74 集，追加稿 025（2026-10-15 夜，hh 挂机，要 20 集；本批是最后一批，终）。
故事见 `剧本/第55-74集_结局版大纲.md`。以 024（第 67–70 集）的 JSON 为底，必须等 024 在插件里全部跑完再追加；追加窗口不要勾每集／总／任务秒数。
写法分配：
  第 71 集 开门之前：B（快）——潜望镜里看到冰裂、融水成河，换衣服、整理背包、把日志放进背包（过渡、整理，节奏快）。
  第 72 集 走出去：A（慢）——第一次打开暗门走出去，融雪成泥，风和光。
  第 73 集 冰面：A——站在冰湖上，把番茄种子埋在雪边，回头看那座山。
  第 74 集 陌生人的声音：A——腰间的收音机响了，“有人吗……这里是曙光营地”，她说“我在”，“我们找了你很久，苏医生。”（第二季钩子，终）
偏离原大纲：极光在冰面上只拍天空和冰面的光，不拍“落在冰上的光带”这种细节形态；“清点装备”并进背包任务；陌生人的声音只用画外音，不画人；
  营地只拍远处山脊上一排小小的灯，不拍人；苏清月不“怀孕”，不“看到星空”，也不拍林峰的幻影。
H3 方面的风险（交稿时单列，不算我的错）：
  · 71-01／71-03／71-05 画外音（伊甸）和画面里的人混排；71-04 她把日志放进背包的手部动作；
  · 72-01 外门开启（只拍结果：门已开、光照在脸上）；72-02／72-03 林地泥泞、融水流成小溪；72-05 极光下的冰面（大场景、光）；
  · 73-02 蹲在雪边埋种子（手部＋小纸袋）；73-06 回头看山（人物转头）；73-07 腰间收音机小灯和杂音；
  · 74-03／74-05 对着收音机说话（说话人对象不在画面里）、陌生人只有声音（可能被画成多出一个人）；74-06 最后一镜吊臂升起的大远景。
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _jihan_base6 as B6
import _jihan_base7 as B7
from _jihan_base7 import *
import _jihan_base8 as B8
from _jihan_base8 import *
import _h3draft as _H
_H.configure(smooth=True, fixed_seed=37407)
OUT = '合并稿/025_第71-74集_开门之前走出去冰面陌生人的声音_制作稿_追加'
S = Session('合并稿/024_第67-70集_最后一道闸门说好会回来一个人的伊甸余温_制作稿_追加.json', OUT, 94000)
B6.S = S
B7.S = S

# ---------------------------------------------------------------------------------------------- 衣着／声音
SU_HOME = "in an oversized charcoal henley that is clearly a man's, the sleeves rolled many times at her wrists, black thermal leggings and thick grey socks, her long black hair tied back loosely"
SU_OUT = "in a dark olive waterproof insulated parka zipped to the chin with the hood down, black thermal trousers and waterproof boots, a black knit hat over her tied-back black hair, a worn dark-green canvas backpack on both shoulders with a small black headset clipped to one strap, a small olive handheld radio clipped to her belt"
SU_OUT_BARE = "in a dark olive waterproof insulated parka zipped to the chin with the hood down, black thermal trousers and waterproof boots, a black knit hat over her tied-back black hair, a small olive handheld radio clipped to her belt"
look('stranger_radio', 'Stranger', "a small olive handheld field radio with a short antenna", 'none', 'its')
B7.VOICE_ONLY.add('stranger_radio')
B7.ZN['stranger_radio'] = '陌生人'
B7.VD['stranger_radio'] = ("a careful, tired young man's voice heard through crackling radio static, from the small olive handheld radio", '隔着沙沙杂音从那台橄榄绿手持小收音机里传出的、小心而疲惫的年轻男声')
STR_EN = "A careful, tired young man's voice heard through crackling radio static, speaking clear Mandarin Chinese, hopeful and a little out of breath." + VT_EN
STR_ZH = '隔着收音机沙沙杂音传来的、小心而疲惫的年轻男声，普通话清楚，带着希望，有一点喘。' + VT_ZH
SU_LD = {'stranger_radio': ('into the small olive handheld radio held up to her mouth', '对着举到嘴边的橄榄绿手持小收音机')}

# ---------------------------------------------------------------------------------------------- 场景
PERI_SCREEN = Scene('periscope_room', PERI.end,
                    " Fixed stage layout: a close view of the round view screen filling the middle of the frame, showing a grey dawn snowfield with dark streams of meltwater running through the snow, a wide river of brown water crossing it and the surface of a far frozen lake split by a long black crack; nobody in the scene.")
AIR_OUT = Scene('airlock', " Hard white strip lights fall on the white-tiled airlock.",
                " Fixed stage layout: a long steel bench with a folded white polar suit on it runs along the left wall; the bare white-tiled floor lies in the middle of the frame; a heavy round steel hatch door with a big wheel stands in the right wall at frame-right.")
AIR_BAG = Scene('airlock', AIR_OUT.end,
                " Fixed stage layout: a long steel bench along the left wall with a dark-green canvas backpack standing open on it and a small pile of folded clothes, tins and a water bottle beside it; the bare white-tiled floor lies in the middle of the frame; a heavy round steel hatch door with a big wheel stands in the right wall at frame-right.")
AIR_HATCH = Scene('airlock', AIR_OUT.end,
                  " Fixed stage layout: a close view of the big steel wheel of the round hatch door filling the middle of the frame, the white-tiled wall around it; nobody in the scene.")
LIVING_QUIET = Scene('bunker_living', LIVING.end,
                     " Fixed stage layout: a close view of the small round wooden dining table in the middle of the frame with two white teacups upside down on a cloth, a folded charcoal blanket on the sofa behind; nobody in the scene.")
HATCH_OPEN = Scene('thaw_forest', " A soft pre-dawn blue light falls on a dripping forest, the wind warm and wet.",
                   " Fixed stage layout: a hollow dead tree trunk with its camouflaged hatch standing open on a dark passage is at frame-left; the middle of the frame is a slope of brown wet mud and patchy old snow with thin streams of meltwater running through it; dripping pines stand in the background.")
THAW_WALK = Scene('thaw_forest', HATCH_OPEN.end,
                  " Fixed stage layout: a narrow trail of brown mud and patchy old snow winds down the middle of the frame between dripping pines, thin streams of meltwater running along both sides of it; far at the back of the frame the trees open onto a pale glowing sky.")
EDGE = Scene('thaw_forest', " A deep blue dusk with a green aurora rising over a frozen lake, the air cold and still.",
             " Fixed stage layout: the last dripping pines stand at frame-left and frame-right framing the middle of the frame; beyond them a wide frozen lake glitters under a broad green aurora that fills the sky; patches of old snow line the shore.")
ICE = Scene('ice_lake', " A broad green and violet aurora hangs over a vast frozen lake, its ice glittering faintly and the air cold and still.",
            " Fixed stage layout: a vast flat frozen lake fills the middle of the frame, the ice dark and glassy with pale cracks and patches of old snow; the snowy shore with a dark line of pines runs along the back; a dark mountain with a faint hump stands far at frame-right; a broad aurora fills the sky.")
SHORE = Scene('ice_lake', ICE.end,
              " Fixed stage layout: a snowy shore of dark wet soil and old snow fills the middle of the frame at the edge of the frozen lake; the flat glassy ice lies behind it at the back of the frame; a broad aurora fills the sky above.")
SHORE_SEED = Scene('ice_lake', ICE.end,
                   " Fixed stage layout: a close view of a small patch of dark wet soil at the edge of the old snow in the middle of the frame, a few tiny pale seeds pressed into it; the soft grey ice glows behind; nobody in the scene.")
MOUNTAIN = Scene('ice_lake', ICE.end,
                 " Fixed stage layout: a wide view across the frozen lake toward the dark mountain filling the back of the frame under a broad aurora, a faint small dark spot at its foot among the pines; nobody in the scene.")
BELT_RADIO = Scene('ice_lake', ICE.end,
                   " Fixed stage layout: a close view of a small olive handheld radio clipped to the dark olive parka at the belt filling the middle of the frame, a tiny amber light on it blinking; the soft glow of the ice behind; nobody's face in the scene.")
RIDGE_LIGHTS = Scene('ice_lake', ICE.end,
                     " Fixed stage layout: a wide view of the dark far shore of the frozen lake at the back of the frame, along a ridge a short line of tiny warm yellow lights glowing in the dark; the aurora above; nobody in the scene.")
TOMATO_CLOSE = Scene('eden', EDEN.end,
                     " Fixed stage layout: a close view of a tomato vine in the middle of the frame with rows of small green tomatoes hanging among leaves, clear water sliding along the channel below; pink-violet grow-lamp light glows behind and the hydroponic channels blur; nobody in the scene.")
EDEN_FARM = Scene('eden', EDEN.end,
                  " Fixed stage layout: long tiers of white hydroponic channels full of lettuce and tomato plants fill the middle of the frame under rows of hanging pink-violet grow lamps; a small wooden lectern at frame-left holds a closed black notebook; a tall tomato vine heavy with red fruit stands at frame-right beside a metal watering can; the steel staircase stands behind.")
CORR_HOME = Scene('bunker_hall', " Soft warm wall lights line a long quiet concrete corridor.",
                  " Fixed stage layout: a long clean grey concrete corridor recedes down the middle of the frame with warm wall lights along both sides, a heavy round steel hatch door closed at the far end of it; a row of closed steel doors stands along the left wall.")
MELT_CLOSE = Scene('thaw_forest', HATCH_OPEN.end,
                   " Fixed stage layout: a close view of a thin stream of clear meltwater running over brown mud and a patch of old grey snow in the middle of the frame, a few small pebbles and a pine needle drifting with it; the soft blue light glints on the water; nobody in the scene.")
ICE_WALK = Scene('ice_lake', ICE.end,
                 " Fixed stage layout: the snowy shore is at the bottom of the frame and the vast flat dark glassy ice of the frozen lake stretches away across the middle of the frame under the broad aurora, a faint line of pale cracks running across it; a dark mountain stands far at frame-right.")
ICE_BOOT = Scene('ice_lake', ICE.end,
                 " Fixed stage layout: a close view of the dark glassy ice in the middle of the frame with a pale crack running across it, a grey frozen bubble trapped deep inside, and one worn waterproof boot standing on it at the edge of the frame; the green aurora light glows on the ice.")
STRAP_CLOSE = Scene('ice_lake', ICE.end,
                    " Fixed stage layout: a close view of the shoulder strap of a worn dark-green canvas backpack in the middle of the frame with a small black headset clipped to it, a corner of a black notebook showing at the pocket edge, the soft glow of the ice behind; nobody's face in the scene.")
AE = lambda en, zh: (en, zh)

new_scene_defs = True

# ================================================================================================ 第 71 集（B）
mode('B')
b71 = S.episode('剧本第71集｜开门之前', '苏清月透过潜望镜看见冰面开裂、融水成河，伊甸说地表温度三度、通道已无危险；她换上外套，把日志、口粮和水装进背包，把林峰的耳麦扣在背包带上，对伊甸说出去看看；她关上厨房的灯，在气闸舱里手按在外门的手轮上。', 71)
new_scene(b71, 'thaw_forest', '正在融化的山林（滴水的松树，棕色的湿泥和残雪，融水细细地流成小溪，天空发蓝）',
          'A thawing mountain forest with dripping pines, brown wet mud and patches of old snow, thin streams of meltwater running through it and a soft blue sky.',
          '一片正在融化的山林：滴着水的松树，棕色的湿泥和残雪，融水细细地流成小溪，天空泛着柔和的蓝色。',
          'the mud trail, the streams and the dripping pines')
new_scene(b71, 'ice_lake', '极光下的冰湖（宽阔的冰湖，深色玻璃般的冰面带着浅色裂纹，岸边有残雪和松树，远处有一座深色的山，天空有绿色和紫色的极光）',
          'A vast frozen lake under a broad green and violet aurora, dark glassy ice with pale cracks, patches of old snow along the shore with a dark line of pines, and a dark mountain far in the distance.',
          '极光下一片辽阔的冰湖：深色玻璃般的冰面带着浅色的裂纹，岸边是残雪和一排深色的松树，远处是一座深色的山，天空中有绿色和紫色的宽阔极光。',
          'the frozen lake, the shore and the aurora')
b71.character('Stranger', 'radio_set', STR_EN, STR_ZH)

DL('71-01', '01｜潜望镜室：苏清月把眼睛贴在潜望镜上，伊甸说地表三度，冰面开裂，融水成河，她说我知道了', PERI,
   [P('su_cozy', 'left', "standing at the thick black periscope column in profile facing frame-left, her eye pressed to the padded rubber eyepiece and both hands on the grips, her head tipped toward the column", 'obj:the padded rubber eyepiece', "her lips parting, her eyes wide and bright, her brows lifted", outfit=SU_HOME)],
   'Medium shot, the woman from the head to the waist, in the middle third of the frame, at the periscope.',
   [('eden_voice', "地表三度。冰面开裂。", 'su_cozy', 'soft clear', '轻柔清楚'),
    ('eden_voice', "融水已经成河。", 'su_cozy', 'soft clear', '轻柔清楚'),
    ('su_cozy', "我知道了。", 'eden_voice', 'low steady', '低沉平稳')],
   V('A faint electronic hum, the squeak of the eyepiece and a quiet breath.', '轻轻的电子嗡声、目镜轻轻的吱声和一声安静的呼吸。'),
   AE("Cool blue-white light from the view screen washes her cheekbone and the glint of the eyepiece while a faint amber lamp warms the back of her hair.",
      "视频屏幕冷冷的蓝白光漫过她的颧骨和目镜上的一点反光，一盏淡淡的琥珀色灯暖着她脑后的头发。"),
   post_en='after the last line she lifts her head from the eyepiece and turns toward the round screen on the wall',
   post_zh='最后一句之后，她把头从目镜上抬起来，转向墙上的圆形屏幕',
   cam=push1('her face at the eyepiece', '她贴着目镜的脸'), bg='On the wall at frame-right a round view screen glows blue-white.', tail=1.5)

INS('71-02', '02｜屏幕特写：灰蒙蒙的黎明里，雪地上暗色的融水细流汇成一条宽宽的棕色河，远处冰湖的冰面裂开一道长长的黑缝', 6, PERI_SCREEN,
    'Close shot of the round screen, the thawing land in the middle third of the frame, nobody in the scene.',
    "On the round screen a grey dawn snowfield is streaked with dark threads of meltwater that join into a wide brown river sliding across it; far away the surface of the frozen lake splits along a long black crack. The picture trembles very slightly.",
    "圆形屏幕里，灰蒙蒙的黎明里，雪地上一道道暗色的融水细流汇成一条宽宽的棕色河，缓缓从画面上淌过；远处冰湖的冰面沿着一道长长的黑缝裂开。画面微微颤着。",
    Q('The faint electronic hum of the screen and a distant low creak of ice.', '屏幕轻轻的电子嗡声和远处冰面低低的吱嘎声。'),
    'The frame holds the round screen, and nobody in the scene.',
    push('the round screen', '圆形屏幕'),
    AE("Cold blue-white screen light flickers across the dark concrete wall around it and the brown water on the screen glints with a thin pale shine.",
       "屏幕冷冷的蓝白光在周围深色的混凝土墙上闪着，屏幕里棕色的河水泛着一层薄薄的浅色亮光。"))

DL('71-03', '03｜地下二层农场：苏清月站在农场里，把日志合上放在小讲台上又拿起来，对伊甸说农场交给你，伊甸说浇水补光授粉，她说每一棵都要活着', EDEN_FARM,
   [P('su_cozy', 'left', "standing at the small wooden lectern in profile facing frame-right, one hand resting on the closed black notebook and the other on the metal watering can, her head lifted toward the rows of plants", 'obj:the rows of plants', "her lips pressed together, her eyes soft and steady, her brows level", outfit=SU_HOME)],
   'Medium shot, the woman from the head to the waist, in the middle third of the frame, at the lectern.',
   [('su_cozy', "农场，交给你了。", 'eden_voice', 'low steady', '低沉平稳'),
    ('eden_voice', "浇水、补光、授粉。", 'su_cozy', 'soft clear', '轻柔清楚'),
    ('su_cozy', "每一棵，都要活着。", 'eden_voice', 'low firm', '低沉坚定'),
    ('eden_voice', "明白，苏女士。", 'su_cozy', 'soft warm', '轻柔温暖')],
   V('The soft trickle of water in the channels, the faint hum of grow lamps and a quiet breath.', '水槽里轻轻的流水声、生长灯轻轻的嗡鸣和一声安静的呼吸。'),
   AE("Pink-violet grow-lamp light haloes her tied-back hair and glows on the leaves behind her while a thin mist drifts through the beams.",
      "粉紫色的生长灯光在她扎起的头发上描出光晕，照得她身后的叶子发亮，薄薄的雾气从光柱里飘过。"),
   post_en='after the last line she lifts the notebook from the lectern and tucks it under her arm',
   post_zh='最后一句之后，她把日志从小讲台上拿起来，夹在胳膊下面',
   cam=push1('her face and the plants behind her', '她的脸和她身后的植物'), tail=1.5)

INS('71-04', '04｜番茄藤特写：粉紫色灯光下，一排小小的青番茄挂在藤上，水槽里的水轻轻流着', 7, TOMATO_CLOSE,
    'Close shot of the tomato vine, the green tomatoes in the middle third of the frame, nobody in the scene.',
    "Rows of small green tomatoes hang on the vine under pink-violet lamps while clear water slides slowly along the channel below. A single leaf trembles. Nothing else moves.",
    "粉紫色的灯光下，一排排小小的青番茄挂在藤上，下面的水槽里清澈的水缓缓地流着。一片叶子轻轻颤了一下。别的什么都不动。",
    Q('The faint trickle of water in the channels and the soft hum of the grow lamps.', '水槽里细细的流水声和生长灯轻轻的嗡鸣。'),
    'The frame holds the tomato vine, and nobody in the scene.',
    push('the small green tomatoes', '那些小小的青番茄'),
    AE("Pink-violet grow-lamp light glows through the translucent skin of the small tomatoes and thin mist drifts through the beams while the green leaves blur softly behind.",
       "粉紫色的生长灯光透过小番茄半透明的表皮发亮，薄薄的雾气从光柱里飘过，后面的绿叶柔柔地虚着。"))

TAA('71-05', '05｜走廊：苏清月沿着安静的灰色走廊走向气闸舱，走过的墙灯一盏一盏暗下去，她的脚步没有停', 8, CORR_HOME,
    [P('su_cozy', 'center', "walking down the long grey concrete corridor in profile facing frame-right, her arms loose at her sides and her head up, the warm wall lights going dark one after another behind her", 'obj:the closed round hatch door at the far end of the corridor', "her lips pressed together, her eyes steady and wet, her brows level", outfit=SU_HOME)],
    'Wide shot, the woman in profile in the middle third of the frame, small in the corridor.',
    "<su_cozy> walks steadily away down the long grey corridor toward the closed round hatch door at its far end, her head up and her boots echoing, the warm wall lights behind her going dark one after another until she walks in a pool of dim light, a small black headset hanging in her hand.",
    "苏清月稳稳地沿着长长的灰色走廊朝尽头那扇关着的圆形舱门走去，头抬着，靴子的脚步声回响着，她身后暖色的墙灯一盏一盏暗下去，直到她走在一圈昏暗的光里。",
    Q('Echoing footsteps on concrete and the soft click of wall lights switching off one by one.', '混凝土上回响的脚步声和墙灯一盏一盏熄灭轻轻的咔哒声。'),
    AE("Soft warm light pools around her and drifts across the pack on her shoulders while the corridor behind falls into velvet dark.",
       "柔和的暖光在她周围聚成一圈，漫过她，身后的走廊沉进天鹅绒一样的黑暗里。"),
    holds='The frame holds the corridor, and one person: Su.',
    cam=track('her', '她'))

DL('71-06', '06｜气闸舱：苏清月在长钢凳旁把深橄榄色的防水外套拉到下巴，伊甸说背包已备好，她说够了', AIR_BAG,
   [P('su_arctic', 'left', "standing beside the long steel bench in profile facing frame-right, both hands pulling the zip of a dark olive parka up to her chin, her head lifted toward the open backpack on the bench", 'obj:the open backpack on the bench', "her lips pressed together, her eyes clear and steady, her brows level", outfit=SU_OUT_BARE)],
   'Medium shot, the woman from the head to the knees, in the middle third of the frame, beside the bench.',
   [('eden_voice', "背包已备好。三天口粮。", 'su_arctic', 'soft careful', '轻柔小心'),
    ('su_arctic', "够了。", 'eden_voice', 'low steady', '低沉平稳'),
    ('eden_voice', "外面不再是冬天了。", 'su_arctic', 'soft gentle', '轻柔温和'),
    ('su_arctic', "我去看看。", 'eden_voice', 'low quiet', '低沉安静')],
   V('The crisp slide of a zip, the soft rustle of waterproof fabric and the clink of a tin in the bag.', '拉链清脆的滑动声、防水布料轻轻的沙沙声和背包里罐头轻轻的碰撞声。'),
   AE("Hard white strip light bounces off the white tiles and lays a clean pale edge along the olive shoulder of her parka while a long soft shadow of her stretches across the floor.",
      "硬朗的白色灯管光从白瓷砖上弹回来，在她橄榄色外套的肩头勾出一道干净的浅色边，她长长的软影子横在地面上。"),
   post_en='after the last line she lifts the dark-green backpack from the bench and slings it onto both shoulders',
   post_zh='最后一句之后，她把深绿色的背包从钢凳上提起来，背到两个肩膀上',
   cam=push1('her face and the zip', '她的脸和拉链'), tail=1.5)

TAA('71-07', '07｜气闸舱：苏清月把黑色的日志放进背包最里面的格子，拉上拉链，再把林峰的黑色耳麦扣在背包带上', 8, AIR_BAG,
    [P('su_arctic', 'center', "standing at the long steel bench in profile facing frame-left, her right hand sliding the worn black notebook into the inner pocket of the backpack and her left hand holding a small black headset by its cord", 'obj:the black notebook in her hand', "her lips pressed together, her eyes soft and wet, her brows drawn gently together", outfit=SU_OUT_BARE)],
    'Medium shot, the woman from the head to the waist, in the middle third of the frame, at the bench.',
    "<su_arctic> slides the worn black notebook into the inner pocket of the open backpack and zips the pocket shut, then clips the small black headset onto the shoulder strap and rests her fingertips on it for a moment; her chin dips, then lifts.",
    "苏清月把磨旧了的黑色日志放进敞开的背包最里面的口袋里拉上拉链，然后把那只小小的黑色耳麦扣在肩带上，指尖在上面停了一会儿；她的下巴低下去，又抬起来。",
    Q('The soft scrape of a zip and a small click of a clasp.', '拉链轻轻的刮擦声和扣子小小的一声咔哒。'),
    AE("Soft white strip light skims the worn black cover of the notebook and the small black headset gleams a tiny bright dot where her fingertip rests.",
       "柔和的白色灯管光掠过日志磨旧的黑色封面，她指尖停着的地方，那只小耳麦泛着一个小小的亮点。"),
    holds='The frame holds the bench and the woman, and one person: Su.',
    cam=push1('her hands and the headset', '她的双手和耳麦'))

INS('71-08', '08｜客厅：桌上两只白瓷茶杯倒扣在布上，沙发上叠着一条炭灰色的毯子，灯一盏一盏暗下去，剩下炉灶上一点暗红', 6, LIVING_QUIET,
    'Close shot of the dining table and the folded blanket, the two upturned cups in the middle third of the frame, nobody in the scene.',
    "Two white teacups lie upside down on a cloth on the small round table and a charcoal blanket is folded neatly on the sofa behind; the warm lamps go out one after another until only a dull ember-red glow from the stove is left. Nothing else moves.",
    "小圆桌的布上倒扣着两只白瓷茶杯，后面沙发上整整齐齐叠着一条炭灰色的毯子；暖色的灯一盏一盏熄灭，最后只剩炉灶上一点暗暗的炭红。别的什么都不动。",
    Q('A soft click of switches one after another and the faint tick of the cooling stove.', '开关一个接一个轻轻的咔哒声和冷却中的炉灶轻轻的嗒嗒声。'),
    'The frame holds the table and the blanket, and nobody in the scene.',
    slide('toward frame-left', '左', 'the folded blanket fills the middle third of the frame', '叠好的毯子占满画面中间三分之一'),
    AE("Warm amber lamp light dies slowly away and leaves a dull ember glow rimming the edge of the cups while a thin pale dust floats once in the last glow.",
       "暖琥珀色的灯光慢慢暗下去，只在杯子的边缘留下一圈暗暗的炭火光，细细的灰尘在最后一点光里飘了一下。"))

DL('71-09', '09｜气闸舱：苏清月站在圆形外门前把手放在手轮上，伊甸问确认开启，她说等一下', AIR_OUT,
   [P('su_arctic', 'left', "standing in front of the heavy round steel hatch door at frame-right in profile facing frame-right, her right hand resting flat on the big wheel and the backpack on her shoulders, her head lifted toward the hatch door", 'obj:the round steel hatch door', "her lips pressed together, her eyes steady and wet, her brows lifted slightly", outfit=SU_OUT)],
   'Medium shot, the woman from the head to the knees, in the middle third of the frame, at the hatch door.',
   [('eden_voice', "是否确认开启外门？", 'su_arctic', 'soft gentle', '轻柔温和'),
    ('su_arctic', "等一下。", 'eden_voice', 'low quiet', '低沉安静'),
    ('su_arctic', "我想，再看他一眼。", 'eden_voice', 'low breaking', '低沉发颤'),
    ('eden_voice', "好的，苏女士。", 'su_arctic', 'soft warm', '轻柔温暖')],
   V('A low hum of the shelter and a small shaky breath.', '避难所低低的嗡声和一声小小的发颤的呼吸。'),
   AE("Hard white strip light lays a clean pale edge along her cheek and the steel wheel and a thin soft shadow of her hand falls across the dull metal.",
      "硬朗的白色灯管光在她的脸颊和钢制手轮上勾出一道干净的浅边，她的手投下一层薄薄的软影子落在暗淡的金属上。"),
   post_en='after the last line she turns her head and looks back toward the dark corridor behind her',
   post_zh='最后一句之后，她扭过头，回头看向身后黑暗的走廊',
   cam=slide('toward frame-right', '右', 'her hand on the wheel and her profile fill the middle third of the frame', '她放在手轮上的手和她的侧脸占满画面中间三分之一'), tail=1.5)

# ================================================================================================ 第 72 集（A）
mode('A')
b72 = S.episode('剧本第72集｜走出去', '苏清月第一次打开暗门，对伊甸说我会回来的；她从枯树干里走出去，外面的雪化成了泥，松树滴着水，融水细细地流；她踩着泥路走到林子边，抬头看见天空上宽阔的极光；她轻轻地说原来外面这么亮，你看到了吗。', 72)

DL('72-01', '01｜气闸舱：苏清月转动手轮，外门打开，一束淡淡的蓝光落在她的脸上，伊甸说外界四度，她说谢谢你伊甸，我会回来的', AIR_HATCH,
   [P('su_arctic', 'left', "standing at the open round hatch door in profile facing frame-right, both hands on the big steel wheel, the hatch door swung open at frame-right letting in a bar of pale blue light, her head lifted toward the light", 'obj:the open round hatch door', "her lips parting, her eyes wide and wet, her brows lifted", outfit=SU_OUT)],
   'Medium shot, the woman from the head to the waist, in the middle third of the frame, at the open hatch.',
   [('eden_voice', "外门已开启。外界四度。", 'su_arctic', 'soft clear', '轻柔清楚'),
    ('su_arctic', "谢谢你，伊甸。", 'eden_voice', 'low warm', '低沉温暖'),
    ('eden_voice', "祝您平安，苏女士。", 'su_arctic', 'soft warm', '轻柔温暖'),
    ('su_arctic', "我会回来的。", 'eden_voice', 'low steady', '低沉平稳')],
   V('The deep soft thump of a heavy door settling open, the whisper of cold wet wind and a quiet breath.', '厚重的门沉沉地停在打开位置的一声闷响、冷而湿的风轻轻的呼啸和一声安静的呼吸。'),
   AE("A bar of soft pale blue dawn light spills through the open hatch and edges her wet cheek and the olive shoulder of her parka while loose strands of her hair stir in the wet wind.",
      "一道柔和的淡蓝色黎明光从打开的门里泻进来，勾亮了她湿润的脸颊和橄榄色外套的肩，她松开的几缕头发在湿湿的风里轻轻飘动。"),
   post_en='after the last line she steps through the open hatch door and out of the frame, the bar of pale light falling empty across the floor',
   post_zh='最后一句之后，她迈过敞开的外门走出画面，一道淡淡的光空空地落在地面上',
   cam=push1('her face and the bar of light', '她的脸和那道光'), tail=2.0)

TAA('72-02', '02｜枯树里的暗门：苏清月从空心的枯树干里弯腰钻出来，站直，抬头深深吸了一口气，湿泥和融雪在她的脚边', 8, HATCH_OPEN,
    [P('su_arctic', 'center', "standing upright in profile facing frame-right on the muddy slope next to the hollow dead tree trunk, her head tipped back and her chest rising in a deep breath, one hand holding the strap of her backpack", 'obj:the pale sky above the trees', "her lips parting, her eyes wide and bright, her brows lifted", outfit=SU_OUT)],
    'Medium shot, the woman from the head to the knees, in the middle third of the frame, outside the tree.',
    "<su_arctic> straightens up after ducking out of the hollow trunk, tips her head back toward the pale sky and takes one slow deep breath of the wet air, her boots sinking a little into the brown mud and her breath fogging faintly in the air.",
    "苏清月从空心的树干里弯腰钻出来，直起身，把头向后仰朝着淡淡的天空，缓缓地深深吸了一口湿润的空气；她的靴子在棕色的泥里微微陷下去，呼出的气在空中淡淡地起了雾。",
    Q('Dripping water from the pines, the soft squelch of mud and a slow deep breath.', '松树上滴水的声音、泥巴轻轻的噗叽声和一声缓缓的深呼吸。'),
    AE("Soft blue pre-dawn light filters through the dripping pines and beads every needle with a tiny bright drop while a warm wet breeze lifts the loose strands at her temples.",
       "柔和的蓝色黎明前的光穿过滴水的松树，把每一根针叶都挂上一颗亮晶晶的小水珠，一阵温暖潮湿的微风掀动她鬓边的碎发。"),
    holds='The frame holds the dead tree and the woman, and one person: Su.',
    cam=lowrise('her face and the sky', '她的脸和天空'))

TAA('72-03', '03｜融雪的山路：苏清月沿着棕色的泥路慢慢往下走，靴子踩进泥里，路边的融水细细地流，滴水的松树在两边', 9, THAW_WALK,
    [P('su_arctic', 'center', "walking away down the muddy trail seen from behind, her backpack on both shoulders and her head turning slowly from side to side to look at the dripping trees, her boots sinking into the mud at each step", 'obj:the dripping pines beside the trail', "her chin lifted, her gaze wandering, her posture unhurried", outfit=SU_OUT)],
    'Wide shot, the woman from behind in the middle third of the frame, small on the trail.',
    "<su_arctic> walks slowly away down the narrow muddy trail with the pale glowing sky ahead, turning her head from one side to the other to look at the dripping pines, thin streams of meltwater running along both sides of the trail and her boots sinking a little with every step.",
    "苏清月沿着窄窄的泥路慢慢往前走，前面是发着淡光的天空，她的头从一边转到另一边，看着滴水的松树，路两边细细的融水流着，靴子每一步都微微陷进泥里。",
    Q('Soft footsteps squelching in mud, the trickle of meltwater and the patter of drops from the trees.', '脚步踩在泥里轻轻的噗叽声、融水细细的流淌声和树上落下来的水滴声。'),
    AE("Soft pearly light glows at the end of the trail and the wet pines drip bright drops through it while a low thin mist drifts across the mud around her boots.",
       "小路尽头泛着柔和的珍珠色光，湿漉漉的松树滴下来亮亮的水珠穿过它，一层低低的薄雾飘过她靴子边的泥地。"),
    holds='The frame holds the trail, and one person: Su, from behind.',
    cam=follow('her', '她', 'the pale glowing sky at the end of the trail fills the middle of the frame', '小路尽头那片发光的天空占满画面中间'))

TAA('72-04', '04｜林子边缘：苏清月停在最后几棵松树中间，抬头看见天空，她的嘴慢慢张开，眼睛里映着绿色的光', 8, EDGE,
    [P('su_arctic', 'center', "standing still between the last two pines in profile facing frame-right with her head tipped back, her lips parting slowly and her eyes wide, the backpack on both shoulders", 'obj:the broad aurora filling the sky', "her lips parting, her eyes wide and shining with tears, her brows lifted", outfit=SU_OUT)],
    'Medium shot, the woman from the head to the waist, in the middle third of the frame, at the edge of the forest.',
    "<su_arctic> stops between the last two pines and tips her head back, her lips parting slowly and her eyes widening as green light from a broad aurora spreads across her face; her hand rises halfway to her mouth and stops.",
    "苏清月停在最后两棵松树中间，把头向后仰，嘴唇慢慢张开，眼睛越睁越大，一片宽阔的极光的绿色光慢慢铺在她脸上；她的手抬到一半、停在了嘴边。",
    Q('A hush of still cold air, a tiny shaky breath and a drop falling from a branch.', '冷而静的空气里的一片寂静、一声小小的发颤的呼吸和树枝上落下的一滴水。'),
    AE("Soft green aurora light slides slowly across her face and wet eyes and the glints of tears catch it like tiny lamps while the dark pines frame her on both sides.",
       "柔和的绿色极光光线慢慢滑过她的脸和湿润的眼睛，眼里的泪光接住它像一盏盏小灯，两边深色的松树把她框在中间。"),
    holds='The frame holds the two pines and the woman, and one person: Su.',
    cam=push1('her face lit by the green light', '她被绿光照亮的脸'))

INS('72-05', '05｜融水特写：棕色的泥地上，一条清澈的细细融水流过残雪，带着小石子和一根松针慢慢往下淌', 7, MELT_CLOSE,
    'Close shot of the meltwater stream, the stream in the middle third of the frame, nobody in the scene.',
    "A thin stream of clear meltwater runs over brown mud and a patch of old grey snow, carrying a few small pebbles and a pine needle slowly downhill. Nothing else moves.",
    "一条清澈的细细融水流过棕色的泥地和一小块灰色的残雪，带着几颗小石子和一根松针慢慢往下淌。别的什么都不动。",
    Q('The soft trickle of meltwater and the patter of single drops from the pines.', '融水细细的流淌声和松树上单个水滴落下的声音。'),
    'The frame holds the meltwater stream, and nobody in the scene.',
    push('the stream of meltwater', '那条融水细流'),
    AE("Soft blue light glints along the clear water and tiny bright beads run down the pine needle while the brown mud glistens wet.",
       "柔和的蓝光在清澈的水面上闪烁，小小的亮珠顺着那根松针滚下去，棕色的泥地湿漉漉地发亮。"))

TAA('72-06', '06｜融雪的山路：苏清月在小溪边蹲下来，摘下一只手套，把手指伸进融水里，又慢慢收回来看着指尖的水珠', 8, THAW_WALK,
    [P('su_arctic', 'center', "crouching beside the thin stream in profile facing frame-right, her bare right hand held out with its fingertips in the clear running water and her gloved left hand on her knee, her head bowed toward the water", 'obj:the clear running water', "her lips parting, her eyes soft and wide, her brows lifted", outfit=SU_OUT)],
    'Medium shot, the woman from the head to the knees, in the middle third of the frame, crouching beside the stream.',
    "<su_arctic> crouches beside the thin stream, pulls off her right glove and lets her fingertips sink into the clear running meltwater, then lifts her hand slowly and watches the bright drops run off her fingertips.",
    "苏清月在细细的溪水边蹲下来，摘下右手的手套，让指尖浸进清澈流动的融水里，然后慢慢抬起手，看着亮亮的水珠从指尖滑落。",
    Q('The soft trickle of meltwater, a tiny sharp breath at its coldness and drops falling.', '融水细细的流淌声、因为冰凉而小小的一声吸气和水滴落下的声音。'),
    AE("Soft blue light glints along the water and runs bright on her wet fingertips while a thin warm mist drifts through the dripping pines behind her.",
       "柔和的蓝光在水面上闪烁，在她湿漉漉的指尖上亮晶晶地淌着，她身后滴水的松树间飘着一层薄薄的暖雾。"),
    holds='The frame holds the stream, and one person: Su.',
    cam=push1('her fingertips and the water', '她的指尖和溪水'))

INS('72-07', '07｜冰湖全景：一片辽阔的冰湖在宽阔的绿色和紫色极光下面微微发亮，岸边有残雪和一排深色的松树，远处一座深色的山', 8, ICE,
    'Wide shot of the whole frozen lake, the glassy ice in the middle third of the frame, nobody in the scene.',
    "A broad green and violet aurora slowly ripples across the sky above a vast frozen lake whose dark glassy ice glitters faintly with pale cracks; patches of old snow line the shore and a dark mountain stands far away. A thin mist drifts across the ice.",
    "宽阔的绿色和紫色的极光在天空中缓缓地像波浪一样荡开，下面是一片辽阔的冰湖，深色玻璃般的冰面带着浅色的裂纹微微发亮；岸边是残雪，远处立着一座深色的山。一层薄雾在冰面上飘过。",
    Q('A long low sigh of wind across the ice and a faint far creak of the ice settling.', '风掠过冰面长长低低的叹息声和远处冰面沉降时轻轻的吱嘎声。'),
    'The frame holds the frozen lake and the sky, and nobody in the scene.',
    rise('the broad aurora over the whole lake', '整片湖上宽阔的极光'),
    AE("Green and violet curtains of aurora ripple slowly over the sky and lay long soft bands of cold colour across the glassy ice while thin silver mist drifts low over its surface.",
       "绿色和紫色的极光幕布在天空中缓缓地荡开，在玻璃般的冰面上铺出长长的柔和的冷色光带，薄薄的银色雾气低低地飘在冰面上。"))

DL('72-08', '08｜林子边缘：苏清月站在松树间望着极光，轻声说原来外面这么亮，说你看到了吗，她的手摸了摸背包带上的耳麦', EDGE,
   [P('su_arctic', 'center', "standing between the last two pines in profile facing frame-right with her head tipped back toward the aurora, her right hand lifted to touch the small black headset clipped to her backpack strap", 'obj:the broad aurora filling the sky', "her lips curving in a small trembling sweet smile, her eyes shining with tears, her brows lifted", outfit=SU_OUT)],
   'Medium shot, the woman from the head to the waist, in the middle third of the frame, at the forest edge.',
   [('su_arctic', "原来，外面这么亮。", 'su_arctic', 'low wondering', '低沉带着惊叹'),
    ('su_arctic', "你看到了吗？", 'su_arctic', 'low breaking', '低沉发颤')],
   V('The hush of still cold air, a tiny shaky breath and a faint drop from the branches.', '冷而静的空气的寂静、一声小小的发颤的呼吸和树枝上轻轻的一滴水声。'),
   AE("Soft green aurora light slides across her tear-bright eyes and the small black headset gleams a tiny green dot under her fingertip while her breath fogs in a thin white thread.",
      "柔和的绿色极光光线滑过她含泪发亮的眼睛，她指尖下那只小小的黑色耳麦泛着一个小小的绿色亮点，她呼出的气化成一缕细细的白雾。"),
   post_en='after the last line she lowers her hand from the headset and takes one slow step forward out from between the pines',
   post_zh='最后一句之后，她的手从耳麦上放下来，慢慢向前迈了一步，走出两棵松树之间',
   cam=pull('her face', '她的脸', 'the two pines, the lake and the broad aurora', '两棵松树、冰湖和宽阔的极光'), tail=2.5)

# ================================================================================================ 第 73 集（A）
b73 = S.episode('剧本第73集｜冰面', '苏清月走上冰湖的岸边，在残雪边蹲下来，用戴手套的手挖一个小坑，把番茄种子从小纸袋里倒进去盖上土，轻声说这是你的番茄，春天会长出来，说我会回来浇水；她站起来回头看那座山；腰间的收音机亮起了小灯，响起沙沙的杂音。', 73)

TAA('73-01', '01｜冰湖岸边：苏清月沿着岸边的残雪走到冰湖的边上，停在冰面和残雪的交界处，低头看着脚下深色的冰', 8, SHORE,
    [P('su_arctic', 'center', "standing at the edge where the old snow meets the dark glassy ice in profile facing frame-right, her head bowed toward the ice at her feet and her backpack on both shoulders", 'obj:the dark glassy ice at her feet', "her lips pressed together, her eyes steady and wet, her brows drawn gently together", outfit=SU_OUT)],
    'Medium shot, the woman from the head to the knees, in the middle third of the frame, on the shore.',
    "<su_arctic> walks slowly along the shore to the place where the old snow meets the glassy ice and stops, looking down at the dark ice at her feet; her boot nudges the edge of the ice and she watches a pale crack drift under the surface.",
    "苏清月沿着岸边慢慢走到残雪和玻璃般的冰面相接的地方停下，低头看着脚下深色的冰；她的靴尖碰了碰冰的边缘，看着冰面下一道浅色的裂纹慢慢漂过去。",
    Q('The crunch of soft old snow, a long low sigh of wind and a faint far creak of ice.', '松软的残雪被踩过的脆响、风长长低低的叹息和远处冰面轻轻的吱嘎声。'),
    AE("A broad green aurora lays cold colour along the glassy ice and rims her cheek and the shoulder of her parka while thin mist drifts low across the ice behind her.",
       "一片宽阔的绿色极光在玻璃般的冰面上铺开冷冷的颜色，勾亮了她的脸颊和外套的肩头，她身后薄薄的雾气低低地飘过冰面。"),
    holds='The frame holds the shore and the ice, and one person: Su.',
    cam=track('her', '她'))

TAA('73-02', '02｜岸边残雪：苏清月蹲下来，把一个小纸袋里细细的种子倒在手心，用戴手套的手在湿土里按出一个小坑', 10, SHORE,
    [P('su_arctic', 'center', "crouching on the shore in profile facing frame-right, a small brown paper packet in her left hand tipped over her gloved right palm and her gloved fingers pressing a small hollow into the dark wet soil at the edge of the old snow", 'obj:the small hollow in the wet soil', "her lips pressed together, her eyes soft and steady, her brows drawn gently together", outfit=SU_OUT)],
    'Medium shot, the woman from the head to the knees, in the middle third of the frame, crouching on the shore.',
    "<su_arctic> crouches at the edge of the old snow, tips a few tiny pale seeds from a small brown paper packet into her gloved palm and presses a small hollow into the dark wet soil with her fingers, then lays the seeds into the hollow one by one with great care.",
    "苏清月在残雪的边上蹲下来，把小纸袋里的几粒细细的浅色种子倒进戴着手套的手心，用手指在黑色的湿土里按出一个小坑，然后很小心地把种子一粒一粒放进小坑里。",
    Q('The soft scrape of a gloved hand in wet soil, the tiny rustle of paper and a slow breath.', '戴手套的手在湿土里轻轻刮擦的声音、纸袋小小的沙沙声和一声缓缓的呼吸。'),
    AE("Cool green aurora light slides along the brown paper and the tiny seeds in her palm glint like grains of pale gold while a thin mist drifts past the edge of the snow.",
       "清凉的绿色极光光线滑过褐色的纸袋，她手心里细小的种子闪着像浅金色的细粒一样的光，一缕薄雾从残雪的边缘飘过。"),
    holds='The frame holds the soil and the snow, and one person: Su.',
    cam=push1('her hands and the small hollow in the soil', '她的双手和土里的小坑'))

DL('73-03', '03｜岸边残雪：苏清月用手轻轻盖上土，轻声说这是你的番茄，说春天会长出来，说我会回来浇水', SHORE,
   [P('su_arctic', 'center', "crouching on the shore in profile facing frame-right, her gloved hands patting soft dark soil over the small hollow at the edge of the old snow, her head bowed toward the soil", 'obj:the small patch of soil under her hands', "her lips curving in a small trembling sweet smile, her eyes shining with tears, her brows drawn gently together", outfit=SU_OUT)],
   'Medium shot, the woman from the head to the knees, in the middle third of the frame, crouching on the shore.',
   [('su_arctic', "这是你的番茄。", 'su_arctic', 'low tender', '低沉温柔'),
    ('su_arctic', "春天，会长出来。", 'su_arctic', 'low soft', '低沉轻柔'),
    ('su_arctic', "我会回来，浇水。", 'su_arctic', 'low breaking', '低沉发颤')],
   V('The soft pat of soil under gloved hands, a faint creak of ice and a quiet breath.', '戴手套的手把土轻轻拍实的声音、冰面轻轻的吱嘎声和一声安静的呼吸。'),
   AE("Soft green aurora light glows along her bowed cheek and the dark soil under her hands and tiny wet crystals of old snow sparkle at its edge while a thin mist drifts low across the ice behind.",
      "柔和的绿色极光光线沿着她低着的脸颊和手下深色的土轻轻发亮，残雪的边上细小的湿冰晶闪着光，一层薄雾低低地从她身后的冰面上飘过。"),
   post_en='after the last line she lays her gloved palm flat on the patch of soil for a moment and then lifts it',
   post_zh='最后一句之后，她把戴手套的手心平平地放在那一小片土上停了一会儿，然后拿开',
   cam=push1('her face bowed over the soil', '她低头望着土的脸'), tail=2.5)

INS('73-04', '04｜种子特写：深色的湿土上有一小块新翻过的地方，一滴融水从残雪的边上滴下来，落在那块土上，慢慢渗进去', 6, SHORE_SEED,
    'Close shot of the small patch of soil, the patch in the middle third of the frame, nobody in the scene.',
    "A small freshly patted patch of dark wet soil sits at the edge of the old snow; a single bright drop of meltwater swells at the edge of the snow, falls onto the patch and slowly soaks in. Nothing else moves.",
    "残雪的边上有一小块刚拍实的深色湿土；一滴明亮的融水在残雪的边缘慢慢鼓起来，滴落在那块土上，慢慢渗进去。别的什么都不动。",
    Q('The faint quiet tick of a single drop and the soft hush of cold air.', '一滴水轻轻的嗒的一声和冷空气柔和的寂静。'),
    'The frame holds the patch of soil, and nobody in the scene.',
    push('the patch of soil', '那一小块土'),
    AE("Cool green aurora light slides over the dark wet soil and the single drop glints like a tiny lamp as it falls while the grey ice glows soft and out of focus behind.",
       "清凉的绿色极光光线滑过深色的湿土，那一滴水落下时像一盏小灯一样闪了一下，后面灰色的冰柔柔地发着光、虚虚的。"))

TAA('73-05', '05｜冰湖岸边：苏清月慢慢站起来，转过身，抬起头望着很远的地方，肩上的背包带上耳麦轻轻晃了一下', 8, SHORE,
    [P('su_arctic', 'center', "standing up and turning on the shore to face frame-left, her head lifted toward the far dark mountain, her hands hanging at her sides and the small black headset swinging on her backpack strap", 'obj:the far dark mountain', "her lips parting, her eyes wide and steady, her brows lifted", outfit=SU_OUT)],
    'Medium shot, the woman from the head to the knees, in the middle third of the frame, on the shore.',
    "<su_arctic> rises slowly from her crouch and turns her whole body toward the far dark mountain, lifting her head to look at it, the small black headset swinging once on her backpack strap and her breath fogging in a thin white thread.",
    "苏清月从蹲着的姿势慢慢站起来，整个身子转向远处深色的山，抬起头望着它，背包带上的小黑耳麦晃了一下，她呼出的气化成一缕细细的白雾。",
    Q('The crunch of snow under boots, a slow breath and a long low sigh of wind.', '靴子踩过雪的脆响、一声缓缓的呼吸和风长长低低的叹息。'),
    AE("Green and violet aurora light slides across her face and the olive shoulder of her parka and her fogging breath glows like a thin silver thread while cold mist drifts behind her.",
       "绿色和紫色的极光光线滑过她的脸和橄榄色外套的肩头，她呼出的雾气像一缕细细的银线一样发亮，身后冷冷的雾气飘动着。"),
    holds='The frame holds the shore and the woman, and one person: Su.',
    cam=slide('toward frame-left', '左', 'her profile and the far mountain fill the middle third of the frame', '她的侧脸和远处的山占满画面中间三分之一'))

TAA('73-06', '06｜冰湖：苏清月一步一步走到冰面上，在深色的冰上走了几步，停下来，张开双臂又慢慢放下，抬头望着极光', 8, ICE_WALK,
    [P('su_arctic', 'center', "standing on the dark glassy ice a few steps from the shore seen from behind and slightly from the side, her arms lifted a little from her sides and her head tipped back toward the broad aurora, the backpack on both shoulders", 'obj:the broad aurora filling the sky', "her chin lifted, her gaze wide, her posture open", outfit=SU_OUT)],
    'Wide shot, the woman small in the middle third of the frame, standing on the ice.',
    "<su_arctic> steps out from the shore onto the dark glassy ice and walks a few slow steps, then stops, lifts her arms a little from her sides and tips her head back toward the broad aurora, her fogging breath rising in the cold.",
    "苏清月从岸边走到深色的冰面上，缓缓走了几步停下来，两臂微微从身侧抬起，把头向后仰着望着宽阔的极光，呼出的雾气在冷空气里升起。",
    Q('Soft footsteps on ice, a faint far creak of the lake and a slow breath.', '冰面上轻轻的脚步声、湖面远处轻轻的吱嘎声和一声缓缓的呼吸。'),
    AE("Slow curtains of green and violet aurora pour over the glassy ice and lay her long soft shadow across it while thin silver mist drifts at her boots.",
       "缓缓的绿色和紫色极光幕布倾在玻璃般的冰面上，把她长长的软影子铺在冰上，薄薄的银色雾气在她靴边飘动。"),
    holds='The frame holds the ice and the woman, and one person: Su.',
    cam=arc('her', '她', 'the dark mountain stands behind her at frame-right', '深色的山站在她身后画面右边'))

INS('73-07', '07｜冰面特写：玻璃般的深色冰面上一道浅色裂纹横过，冰里冻着一个灰色的小气泡，一只靴子踩在画面边缘', 6, ICE_BOOT,
    'Close shot of the ice, the crack in the middle third of the frame, nobody in the scene.',
    "A pale crack runs across the dark glassy ice with a grey frozen bubble trapped deep inside it, and one worn waterproof boot stands still at the edge of the frame. A tiny shiver of light moves along the crack. Nothing else moves.",
    "玻璃般的深色冰面上一道浅色的裂纹横过去，冰的深处冻着一个灰色的小气泡，画面边缘站着一只磨旧了的防水靴，一动不动。一缕很小的光沿着裂纹颤了一下。别的什么都不动。",
    Q('A faint deep creak from under the ice and the hush of the still night.', '冰层下面轻轻的一声深沉的吱嘎和静夜的寂静。'),
    'The frame holds the ice and the crack, and nobody in the scene.',
    push('the crack in the ice', '冰上的那道裂纹'),
    AE("Green aurora light slides along the pale crack and glints deep inside the glassy ice around the frozen bubble while a thin mist drifts across the surface.",
       "绿色的极光光线沿着浅色的裂纹滑过去，在玻璃般的冰里、冻着的小气泡周围闪着，一层薄雾飘过冰面。"))

INS('73-08', '08｜远山：隔着辽阔的冰湖，那座深色的山静静地立在极光下面，山脚的松树里有一个小小的深色的点', 8, MOUNTAIN,
    'Wide shot of the far mountain across the lake, the mountain in the middle third of the frame, nobody in the scene.',
    "Across the vast frozen lake a dark mountain stands silent under a broad green and violet aurora, and at its foot among the pines a faint small dark spot is just visible. A thin mist drifts low across the ice. Nothing else moves.",
    "隔着辽阔的冰湖，一座深色的山静静地立在宽阔的绿色和紫色极光下面，山脚的松树里隐约有一个小小的深色的点。一层薄雾低低地飘过冰面。别的什么都不动。",
    Q('A long low sigh of wind across the ice and a faint far creak.', '风掠过冰面长长低低的叹息声和远处一声轻轻的吱嘎。'),
    'The frame holds the mountain and the lake, and nobody in the scene.',
    push('the far dark mountain', '远处深色的山'),
    AE("A broad aurora pours slow green and violet light over the dark mountain and lays a long cool shine along the glassy ice while thin silver mist drifts low across it.",
       "宽阔的极光把缓缓的绿色和紫色光倾在深色的山上，在玻璃般的冰面上铺出一道长长的清凉的光，薄薄的银色雾气低低地飘过冰面。"))

DL('73-09', '09｜冰湖岸边：苏清月望着远山，轻声说林峰，你的山还在，说我看见了，她的手按在胸口', SHORE,
   [P('su_arctic', 'center', "standing on the shore in profile facing frame-left, her right hand pressed flat against the front of her parka over her chest and her head lifted toward the far dark mountain", 'obj:the far dark mountain', "her lips curving in a small trembling sweet smile, her eyes shining with tears, her brows lifted", outfit=SU_OUT)],
   'Medium shot, the woman from the head to the waist, in the middle third of the frame, on the shore.',
   [('su_arctic', "你的山，还在。", 'su_arctic', 'low tender', '低沉温柔'),
    ('su_arctic', "我看见了。", 'su_arctic', 'low breaking', '低沉发颤')],
   V('A long low sigh of wind, a tiny shaky breath and a faint creak of ice.', '风长长低低的叹息、一声小小的发颤的呼吸和冰面轻轻的一声吱嘎。'),
   AE("Soft green aurora light glows on her tear-bright eyes and the olive wool of her glove where it rests against her chest while her fogging breath drifts away in the cold.",
      "柔和的绿色极光光线映在她含泪发亮的眼睛上，也映在她按在胸口的橄榄色手套上，她呼出的雾气在冷空气里飘开。"),
   post_en='after the last line she closes her eyes for a moment and takes one slow breath',
   post_zh='最后一句之后，她闭上眼睛停了一会儿，缓缓地吸了一口气',
   cam=push1('her face', '她的脸'), tail=2.5)

# ================================================================================================ 第 74 集（A，终）
b74 = S.episode('剧本第74集｜陌生人的声音', '苏清月腰间的收音机忽然沙沙响，一个陌生的年轻男声说有人吗，这里是曙光营地；她拿起收音机，用手指按住按钮，说我在；陌生人说终于联系上了，我们找了你很久，苏医生；远处山脊上亮着一排小小的灯。', 74)

TAA('74-01', '01｜冰湖岸边：苏清月腰间的收音机忽然亮起小灯、沙沙响起来，她一动不动地站住，低头看向腰间', 8, SHORE,
    [P('su_arctic', 'center', "standing very still on the shore in profile facing frame-right, her head turning down toward the small olive handheld radio at her belt whose tiny amber light has begun to blink, her hands frozen at her sides", 'obj:the small olive radio at her belt', "her lips parting, her eyes wide, her brows lifted", outfit=SU_OUT_BARE)],
    'Medium shot, the woman from the head to the knees, in the middle third of the frame, on the shore.',
    "A sudden burst of static comes from the small olive radio at her belt and its tiny amber light begins to blink; <su_arctic> freezes mid-breath, her head turning slowly down toward the radio and her fogging breath stopping for a moment.",
    "她腰间那台橄榄绿的小收音机忽然响起一阵沙沙声，小小的琥珀色灯开始闪烁；苏清月屏住了呼吸，头慢慢地低下去看向收音机，呼出的雾气停了一下。",
    Q('A sudden crackle of radio static, a tiny sharp intake of breath and the hush of the cold night.', '收音机里突然响起的沙沙声、一声小小的倒吸气和寒夜的寂静。'),
    AE("A tiny amber light blinks at her belt and picks out the edge of her glove while cold green aurora light stays soft on her widened eyes and her fogging breath hangs in the still air.",
       "她腰间一点小小的琥珀色光一闪一闪，映亮了手套的边缘，清凉的绿色极光光线柔柔地落在她睁大的眼睛上，她呼出的雾气悬在静止的空气里。"),
    holds='The frame holds the shore and the woman, and one person: Su.',
    cam=push1('her face and the blinking light', '她的脸和闪着的小灯'))

INS('74-02', '02｜腰间收音机特写：一台橄榄绿的小收音机别在外套的腰带上，小小的琥珀色灯一闪一闪，沙沙的杂音时大时小', 6, BELT_RADIO,
    'Close shot of the small radio, the radio in the middle third of the frame, nobody in the scene.',
    "A small olive handheld radio clipped to a dark olive parka at the belt sits in the middle of the frame, its tiny amber light blinking and its short antenna trembling slightly with each rise and fall of the static. Nothing else moves.",
    "一台橄榄绿的小收音机别在深橄榄色外套的腰带上，在画面中间，小小的琥珀色灯一闪一闪，短短的天线随着杂音的起伏微微颤着。别的什么都不动。",
    Q('A rising and falling hiss of radio static and a faint far creak of ice.', '收音机里时大时小的沙沙杂音和远处冰面轻轻的一声吱嘎。'),
    'The frame holds the small radio, and nobody in the scene.',
    push('the small radio', '那台小收音机'),
    AE("The tiny amber light pulses against the dark olive fabric and a cool green wash of aurora light slides slowly over the antenna while the glassy ice glows soft and blurred behind.",
       "小小的琥珀色灯在深橄榄色的布料上一明一灭，清凉的绿色极光光线慢慢滑过天线，后面玻璃般的冰面柔柔地发着光、虚虚的。"))

DL('74-03', '03｜冰湖岸边：苏清月把收音机从腰带上取下来举在胸前，收音机里一个陌生的年轻男声说有人吗，说这里是曙光营地', SHORE,
   [P('su_arctic', 'center', "standing on the shore in profile facing frame-right, the small olive handheld radio lifted in both gloved hands in front of her chest and her head bowed toward it, her fingers still off the button", 'obj:the small olive radio in her hands', "her lips parting, her eyes wide and wet, her brows drawn together", outfit=SU_OUT_BARE)],
   'Medium shot, the woman from the head to the waist, in the middle third of the frame, on the shore.',
   [('stranger_radio', "有人吗？这里是曙光营地。", 'su_arctic', 'careful hopeful', '小心带着希望'),
    ('stranger_radio', "有人吗？请回答。", 'su_arctic', 'careful hopeful', '小心带着希望')],
   V('Crackling radio static rising and falling and a tiny shaky breath.', '收音机里时大时小的沙沙杂音和一声小小的发颤的呼吸。'),
   AE("The tiny amber light of the radio pulses against her gloves and a cool green wash of aurora light lies on her wet cheek while thin silver mist drifts behind her over the ice.",
      "收音机小小的琥珀色灯在她的手套上一明一灭，清凉的绿色极光光线落在她湿润的脸颊上，薄薄的银色雾气在她身后的冰面上飘动。"),
   post_en='after the last line her right thumb moves slowly toward the button on the side of the radio and stops just above it',
   post_zh='最后一句之后，她的右手拇指慢慢移向收音机侧面的按钮，停在它的上方',
   cam=push1('her face and the radio', '她的脸和收音机'), tail=2.5, dur=12)

INS('74-04', '04｜远处山脊：冰湖的对岸，一道深色的山脊上有一小排温暖的黄色小灯，在极光下面静静地亮着', 7, RIDGE_LIGHTS,
    'Wide shot of the far shore, the short line of lights in the middle third of the frame, nobody in the scene.',
    "Across the dark frozen lake a short line of tiny warm yellow lights glows steadily along a far ridge under the broad aurora. Nothing moves.",
    "隔着深色的冰湖，远处的山脊上有一小排温暖的黄色小灯，在宽阔的极光下面稳稳地亮着。什么都不动。",
    Q('A long low sigh of wind and the faint hiss of radio static far in the background.', '风长长低低的叹息声和远远的背景里收音机轻轻的沙沙声。'),
    'The frame holds the far ridge and its lights, and nobody in the scene.',
    push('the line of tiny lights', '那一小排小灯'),
    AE("The tiny warm yellow lights glow steadily like a string of embers against the dark ridge while green and violet aurora light pours slowly over them and cold mist drifts across the lake in front.",
       "那一小排温暖的黄色小灯像一串炭火一样稳稳地亮在深色的山脊上，绿色和紫色的极光光线缓缓倾在它们上面，冷冷的雾气飘过前面的湖面。"))

INS('74-05', '05｜背包带特写：磨旧的深绿色背包带上夹着那只小黑耳麦，口袋边露出日志的一个黑色封角，一阵风吹过，耳麦轻轻晃了一下', 6, STRAP_CLOSE,
    'Close shot of the backpack strap, the headset in the middle third of the frame, nobody in the scene.',
    "A small black headset is clipped to the worn dark-green strap of a backpack and a corner of a black notebook shows at the pocket edge; a breath of wind comes and the headset swings once and settles. Nothing else moves.",
    "磨旧了的深绿色背包带上夹着一只小小的黑色耳麦，口袋边露出一个黑色日志的封角；一阵风吹过来，耳麦轻轻晃了一下，又停住。别的什么都不动。",
    Q('A soft breath of wind, the faint hiss of radio static and the tiny tick of the headset clasp.', '一阵轻轻的风、收音机轻轻的沙沙声和耳麦扣子小小的一声嗒。'),
    'The frame holds the strap and the headset, and nobody in the scene.',
    push('the small black headset', '那只小黑耳麦'),
    AE("Soft green aurora light slides over the black plastic of the headset and glints a tiny dot on its clasp while the glow of the ice blurs behind.",
       "柔和的绿色极光光线滑过耳麦的黑色塑料外壳，在它的扣子上闪出一个小亮点，后面冰面的光柔柔地虚着。"))

TAA('74-06', '06｜冰湖岸边：苏清月看着对岸的灯，慢慢吸了一口气，把收音机举到嘴边，大拇指按在按钮上', 8, SHORE,
    [P('su_arctic', 'center', "standing on the shore in profile facing frame-right, the small olive radio lifted close to her mouth in her right glove with her thumb on its button, her head lifted toward the far lights", 'obj:the far ridge across the lake', "her lips pressed together, her eyes steady and wet, her brows drawn gently together", outfit=SU_OUT_BARE)],
    'Medium shot, the woman from the head to the waist, in the middle third of the frame, on the shore.',
    "<su_arctic> looks across the lake toward the far ridge, draws one slow breath that fogs in the cold air, then raises the small olive radio close to her mouth and settles her thumb on the button, her chin lifting.",
    "苏清月看向湖对岸的山脊，缓缓吸了一口气，呼出的雾在冷空气里散开，然后把橄榄绿的小收音机举到嘴边，拇指稳稳按在按钮上，下巴抬了起来。",
    Q('A slow breath, the rise and fall of faint radio static and the hush of the cold night.', '一声缓缓的呼吸、收音机里轻轻时大时小的沙沙声和寒夜的寂静。'),
    AE("Green and violet aurora light slides across her face and the olive shoulder of her parka and her fogging breath glows like a thin silver thread while the tiny amber light of the radio pulses at her lips.",
       "绿色和紫色的极光光线滑过她的脸和橄榄色外套的肩头，她呼出的雾气像一缕细细的银线一样发亮，嘴边收音机小小的琥珀色灯一明一灭。"),
    holds='The frame holds the shore and the woman, and one person: Su.',
    cam=push1('her face and the radio at her lips', '她的脸和嘴边的收音机'))

DL('74-07', '07｜冰湖岸边：苏清月对着收音机说我在，陌生人说终于联系上了，说我们找了你很久，苏医生', SHORE,
   [P('su_arctic', 'center', "standing on the shore in profile facing frame-right, the small olive radio held up close to her mouth in her right glove and her head lifted toward the far lights", 'obj:the far ridge across the lake', "her lips parting, her eyes shining with tears, her brows lifted", outfit=SU_OUT_BARE)],
   'Medium shot, the woman from the head to the waist, in the middle third of the frame, on the shore.',
   [('su_arctic', "我在。", 'stranger_radio', 'low steady', '低沉平稳'),
    ('stranger_radio', "终于联系上了。", 'su_arctic', 'careful relieved', '小心而如释重负'),
    ('stranger_radio', "我们找了你很久，苏医生。", 'su_arctic', 'careful warm', '小心而温暖')],
   V('Crackling radio static, a tiny shaky breath and a long low sigh of wind.', '收音机里的沙沙杂音、一声小小的发颤的呼吸和风长长低低的叹息。'),
   AE("Green and violet aurora light slides across her tear-bright eyes and the olive radio and her fogging breath hangs like a silver thread while the tiny amber light pulses against her glove.",
      "绿色和紫色的极光光线滑过她含泪发亮的眼睛和橄榄绿的收音机，她呼出的雾气像一缕银线一样悬着，小小的琥珀色灯在她的手套上一明一灭。"),
   post_en='after the last line she slowly lowers the radio from her mouth and holds it against her chest, her eyes still on the far lights',
   post_zh='最后一句之后，她慢慢把收音机从嘴边放下来，按在胸前，眼睛仍望着远处的灯',
   cam=push1('her face', '她的脸'), tail=2.5, ld=SU_LD, dur=12)

TAA('74-08', '08｜冰湖全景：极光下辽阔的冰湖岸边，苏清月是一个很小的深色身影，把收音机按在胸前，对岸山脊上一排小小的灯静静亮着，镜头缓缓升起', 10, ICE,
    [P('su_arctic', 'center', "standing very small and motionless on the snowy shore in profile facing frame-right, the small olive radio held against her chest in both gloved hands and her head lifted toward the far ridge", 'obj:the far ridge across the lake', "her lips parting, her eyes bright, her brows lifted", outfit=SU_OUT_BARE)],
    'Wide shot of the whole lake, the small figure in the middle third of the frame at the bottom, the aurora filling the sky above.',
    "A broad green and violet aurora fills the sky over the vast frozen lake; <su_arctic> stands small and motionless on the snowy shore holding the radio against her chest, and far across the ice a short line of tiny warm lights shows along a ridge; the picture rises slowly above her and holds.",
    "宽阔的绿色和紫色的极光铺满了辽阔冰湖的天空；苏清月小小的、一动不动地站在雪岸上，把收音机按在胸前，远远的冰面对岸，山脊上有一小排温暖的小灯亮着；画面从她身后缓缓升高，然后停住。",
    Q('A long low sigh of wind across the ice, the faint hiss of radio static and the deep hush of the night.', '风掠过冰面长长低低的叹息声、收音机轻轻的沙沙声和夜晚深深的寂静。'),
    AE("Slow curtains of green and violet aurora pour cold colour over the glassy ice and along the far ridge the tiny warm lights glow like a string of embers while thin silver mist drifts across the lake.",
       "缓缓的绿色和紫色极光幕布把冷冷的颜色倾在玻璃般的冰面上，远处山脊上那一小排温暖的小灯像一串炭火一样亮着，薄薄的银色雾气飘过湖面。"),
    holds='The frame holds the whole lake and the sky, and one small figure: Su.',
    cam=rise('the whole sky of aurora over the lake with her small figure far below', '整片冰湖上方布满极光的天空和远远下面她那小小的身影'))

doc = S.finish()
report()
