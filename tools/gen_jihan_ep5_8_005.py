#!/usr/bin/env python3
"""《极寒末日：我的隐秘安全屋》剧本第 5–8 集，追加稿 005（2026-10-13 夜）。必须接在 004（剧本第 1–4 集）之后追加：
Session 以 004 的 JSON 为底，style／素材／角色逐字复制；追加窗口不要勾“每集／总／任务秒数”。

写法＝004 同一套（hh 看了 004 第 1、2 集“非常非常满意”，要求保持）：一个任务一件慢的事；每人看着谁写进开场图；每句台词对谁说且对象在画面里；
独白＝一个人在画面里“自言自语”、手上有事做、眼睛看着一个具体的东西；3 秒无人插镜；承接前段只在同场景同一批人的相邻任务打开；运镜写“动作＋终点”。
本稿新增的测试（直接在正片里测，不另写测试稿）：
  · 05-04（13 秒）四句短台词＋结尾动作（苏清月转头看向落地窗），测“最后一句挤在片尾”会不会被结尾动作缓解；
  · 05-02（12 秒）三句台词＋林峰之外的人走出画面的结尾动作（周宁起身离开）；
  · 08-03（6 秒）快动作单独占一个任务：苏清月把燃烧瓶砸向门口，开场图画在出手前一刻；
  · 07-04 趴在雪里不动、两个流浪者擦身走过（三个有名字的人，其中一个几乎看不见）；
  · 各种“外面的雪、里面的暖”的对切（第 6 集街景冻结 → 25℃ 煎牛排；第 8 集雪地 → 暖屋装水泵）。
偏离大纲（交稿时已告诉 hh）：
  · 第 5 集“最后一天”是我自己的末日前大纲（v2）：林峰对周宁交代／苏清月扑空看到曲线／她加订物资只囤到三成／林峰按下红色按钮；
  · 第 6 集降临：白雾逼近和冻结街景分成两个无人插镜（不拍人群瞬间冻住）；苏清月在酒窖的助理文助理走出门去找暖气（再没回来，大纲没有这个人，我补的）；
  · 第 7 集（原大纲第 5 集）：不带散弹枪，只带便携喷枪；暴徒不是黑影，是两个有名字的流浪者擦身走过（有台词，不是“只有声音的人”）；
    手背粘在冻管上撕掉一层皮只拍“抽回手、看手背”，不拍伤口特写；回家后加育苗盘冒出第一批绿芽（养成的第一步）；
  · 第 8 集（原大纲第 6、7 集合并）：暴徒砸门只有锤声，不拍门被砸变形；领头暴徒在门口被燃烧瓶逼退（只拍他退出门口，不拍滚下楼梯）；
    酒精瓶燃烧只拍一次；雪原跋涉只拍一个宽景（冰雕尸体放在远处山脊）；坐标处只有一根树桩，树桩侧面的小镜头玻璃在融雪。
H3 方面的风险（交稿时单列，不算我的错）：四句台词可能各自晚开口、挤在片尾；自言自语时嘴动但声音不对；手部动作（拧瓶盖、塞布条、拧螺丝、戴手套）；
  雪地里穿着厚重衣服的脸是否保脸；趴在雪里的白衣人是否被画成“消失”；远处的三个人影；火光爆燃；开场图约一成不按文字画；“同一处”场景图用参照图（没测过）。
"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _jihan_base import *

OUT = '合并稿/005_第5-8集_最后一天降临白雪呼吸求生_制作稿_追加'
S = Session(BASE_004, OUT, 34000)

# ---------------------------------------------------------------------------------------------- 新外貌
look('lin_arctic', 'LinArctic', "in a bulky pure-white polar expedition suit with the hood up, white goggles pushed up on his forehead and a white neck gaiter pulled down under his chin", 'steady dark-brown', 'his', eth=CN30)
look('su_down', 'SuDown', "in a long cream down coat zipped to the chin over her black silk blouse, thin gold-rimmed glasses on her nose, her long black hair tied back, frost on her lashes", 'sharp dark-brown', 'her', eth=CN_F28)
look('su_trek', 'SuTrek', "in layered white and black down jackets with a black scarf wound up to her chin, ski goggles pushed up on her forehead and a heavy hiking backpack on her shoulders, frost on her lashes and cheeks", 'exhausted dark-brown', 'her', eth=CN_F28)
look('gaunt_drifter', 'Gaunt', "in a layered tattered winter coat with a frost-crusted scarf pulled down under his chin", 'sunken bloodshot', 'his', eth='a gaunt Chinese man in his forties')
look('bearded_drifter', 'Bearded', "in a ragged padded jacket and a knitted cap", 'red-rimmed', 'his', eth='a stocky Chinese man in his forties')
look('brute_raider', 'Brute', "in a stained quilted coat with a ragged scarf pulled up over his nose", 'wild bloodshot', 'his', eth='a heavy-set Chinese man in his thirties')

# ---------------------------------------------------------------------------------------------- 新场景（开场图后缀 + 固定布局）
SPROUTS = Scene('bunker_sprouts', " Hard white work lamps and one soft white-purple grow lamp light the huge concrete hall packed with supplies.",
                " Fixed stage layout: a steel workbench stands at frame-center with a shallow tub of clear water and a white tray of foam seeding blocks, each topped with tiny pale-green seedlings, under a hanging white-purple grow lamp; towering stacks of steel crates, pallets of boxes, generators and big water tanks fill the hall behind it and along both sides.")
STUDIO_DAY = Scene('studio_day', " Cold grey dawn light mixes with the glow of the two monitors in the empty studio.",
                   " Fixed stage layout: the long desk with two large monitors showing orange curves falling steeply is at frame-left; the worn brown leather sofa stands at frame-center-right; a glass studio door is at frame-right beyond the sofa; the floor-to-ceiling window across the back wall shows a pale grey dawn over a quiet city.")
CONTROL = Scene('bunker_control', " Cool green indicator glow and pale work-lamp light fill the compact underground control room.",
                " Fixed stage layout: the steel control console with rows of small green status lights and one big red push-button under a clear flip-up cover stands in the middle of the frame; a wall of six small monitors is at frame-left; a large red digital countdown clock hangs high on the back wall at center-right; a heavy steel door stands in the right wall at frame-right.")
STREET = Scene('street_summer', " Blinding white midday sun glares over the glass towers while the sky at the far end of the street is swallowed by white.",
               " Fixed stage layout: a wide boulevard between glass office towers recedes down the middle of the frame; a line of stopped cars fills both lanes; leafy trees line the sidewalks; at the far end of the street a towering wall of white mist fills the sky.")
FROZEN = Scene('street_frozen', " Dim grey-blue light and a thin white mist hang over the silent frozen boulevard.",
               " Fixed stage layout: the same wide boulevard recedes down the middle of the frame; the stopped cars are encased in ice; bare frost-furred trees line the sidewalks; along the sidewalks stand people frozen mid-stride in white ice; the glass towers are furred with frost.")
CELLAR = Scene('wine_cellar', " Dim yellow light from one bulb falls on frost-furred bottles and cases in the bitterly cold stone cellar.",
               " Fixed stage layout: racks of wine bottles line the left wall; stacked cases of canned food and bottled water stand in the middle of the frame; three concrete steps rise to a heavy steel security door at frame-right; a small round thermometer hangs on the wall above the cases.")
AIRLOCK = Scene('airlock', " Hard white strip lights fall on the white-tiled airlock.",
                " Fixed stage layout: a long steel bench with two hanging white polar suits and a shelf of white goggles runs along the left wall; the bare white-tiled floor lies in the middle of the frame; a heavy round steel hatch door stands in the right wall at frame-right.")
HATCH = Scene('snow_hatch', " A silent frozen night forest under a black sky with a faint green aurora; the white light of the snow glows.",
              " Fixed stage layout: a hollow dead tree trunk with its camouflaged hatch standing open on a black passage is at frame-left; waist-deep snow fills the middle of the frame; snow-laden pines fill the background.")
VENT = Scene('snow_vent', " A silent frozen night forest under a black sky with a faint green aurora; the white light of the snow glows.",
             " Fixed stage layout: a thick steel exhaust pipe sticks out of the deep snow at frame-center-right, its mouth sealed in a heavy block of ice; deep snow fills the foreground; snow-laden pines stand behind it.")
TREK = Scene('snow_trek', " A vast frozen snowfield under a black sky with a faint green aurora; the white light of the snow glows.",
             " Fixed stage layout: a vast open snowfield fills the middle of the frame; a few leafless frozen trees stand at frame-right; far at the back a line of white ice-encased human figures frozen mid-run stands along a low ridge.")
STUMP = Scene('snow_stump', " A silent frozen forest under a black sky with a faint green aurora; the white light of the snow glows.",
              " Fixed stage layout: a snow-capped boulder is at frame-left; a dead tree stump stands at center-left with a small round dark glass lens set in its side and a thin patch of snow melting around the glass; an open snowfield fills the middle of the frame; snow-laden pines stand in the background.")

# ---------------------------------------------------------------------------------------------- 第 5 集（先建第一个 Batch，新素材都加在它上面）
b5 = S.episode('剧本第5集｜最后一天', '最后一天的夜里，林峰把一件羽绒服塞给周宁，让他带家人去高处，别问。第二天清晨苏清月找到空荡荡的工作室，周宁只说他去修度假村了，她看着屏幕上陡直下落的曲线，脸色变了；回到家，她让助理再订一批货，得到的回答是全城的货被一个人买光了，她只囤到三成。地下的控制室里，林峰低声说“最后一天了”，掀开保护盖，按下红色按钮。', 5)

new_person(b5, 'lin_arctic', '林峰（纯白极地防寒服，兜帽、白色护目镜推在额头上）', 'man',
           'Lin, the same lean, athletic Chinese man in his early thirties as in the reference, wearing a bulky pure-white polar expedition suit with the hood up, white goggles pushed up on his forehead and a white neck gaiter pulled down under his chin, his cheeks reddened by cold and a faint shadow of stubble.',
           '林峰，和参考图是同一位三十出头、身形精瘦结实的中国男性，穿着蓬松的纯白极地防寒服、戴着兜帽，白色护目镜推在额头上，白色围脖拉到下巴下面，脸颊被冻得发红，下巴上一层淡淡的胡茬。',
           'a bulky pure-white polar expedition suit with the hood up, white goggles pushed up on his forehead, a white neck gaiter pulled down under his chin, cheeks reddened by cold, a faint shadow of stubble',
           'a hard, focused expression', ref='lin_studio', full=True)
new_person(b5, 'su_down', '苏清月（长款奶白色羽绒服，金丝眼镜，睫毛上有霜）', 'woman',
           'Su, the same elegant Chinese woman in her late twenties as in the reference, with her long black hair tied back, thin gold-rimmed glasses on her nose and frost on her lashes, wearing a long cream down coat zipped to the chin over her black silk blouse.',
           '苏清月，和参考图是同一位二十八岁左右、优雅美丽的中国女性，乌黑的长发束在脑后，鼻梁上架着细金丝眼镜，睫毛上结着霜，穿着拉到下巴的长款奶白色羽绒服，里面是黑色真丝衬衫。',
           'long black hair tied back, thin gold-rimmed glasses, frost on her lashes, wearing a long cream down coat zipped to the chin',
           'a pinched, determined expression', ref='su_suit')
new_person(b5, 'su_trek', '苏清月（三层黑白羽绒服，黑围巾，滑雪护目镜推在额头上，背着登山包）', 'woman',
           'Su, the same elegant Chinese woman in her late twenties as in the reference but without glasses, wearing layered white and black down jackets, a black scarf wound up to her chin, ski goggles pushed up on her forehead and a heavy hiking backpack on her shoulders, frost on her lashes and cheeks, her long black hair tucked under a dark knit hat.',
           '苏清月，和参考图是同一位二十八岁左右、优雅美丽的中国女性，但不戴眼镜，穿着三层黑白相间的羽绒服，黑围巾一直绕到下巴，滑雪护目镜推在额头上，肩上背着沉重的登山包，睫毛和脸颊上都是霜，乌黑的长发塞在深色针织帽里。',
           'no glasses, layered white and black down jackets, a black scarf wound up to her chin, ski goggles pushed up on her forehead, frost on her lashes and cheeks, a dark knit hat',
           'an exhausted, determined expression', ref='su_suit', full=True)
new_person(b5, 'gaunt_drifter', '流浪者甲（瘦得脱相，破旧的多层冬衣，拖着一根铁棍）', 'man',
           'A gaunt Chinese man in his forties with hollow cheeks, cracked lips and sunken bloodshot eyes, wearing a layered tattered winter coat with a frost-crusted scarf pulled down under his chin, dragging a bent iron bar.',
           '一个四十多岁、瘦得脱相的中国男性，两颊凹陷，嘴唇开裂，眼窝深陷、布满血丝，穿着多层破旧的冬衣，结着霜的围巾拉到下巴下面，拖着一根弯了的铁棍。',
           'hollow cheeks, cracked lips, sunken bloodshot eyes, wearing a layered tattered winter coat with a frost-crusted scarf pulled down under his chin',
           'an exhausted, hollow expression', eth='Chinese')
new_person(b5, 'bearded_drifter', '流浪者乙（结着冰碴的黑胡子，破旧的棉夹克，针织帽）', 'man',
           'A stocky Chinese man in his forties with a matted black beard crusted with ice, red-rimmed eyes, a ragged padded jacket and a knitted cap, carrying a short iron pipe.',
           '一个四十多岁、敦实的中国男性，黑胡子纠结着结满冰碴，眼眶发红，穿着破旧的棉夹克、戴着针织帽，手里拿着一截短铁管。',
           'a matted black beard crusted with ice, red-rimmed eyes, a ragged padded jacket and a knitted cap',
           'a numb, bitter expression', eth='Chinese')
new_person(b5, 'brute_raider', '暴徒（壮实的中年男人，脏棉袄，破围巾遮着口鼻，拿大锤）', 'man',
           'A heavy-set Chinese man in his thirties with a stubbled broad face and wild bloodshot eyes, wearing a stained quilted coat with a ragged scarf pulled up over his nose, holding a sledgehammer.',
           '一个三十多岁、体格粗壮的中国男性，宽脸上胡子拉碴，眼睛布满血丝、神情凶狠，穿着脏兮兮的棉袄，破围巾拉起来遮住口鼻，手里拿着一把大锤。',
           'a stubbled broad face, wild bloodshot eyes, wearing a stained quilted coat with a ragged scarf pulled up over his nose',
           'a savage, desperate expression', eth='Chinese')

new_scene(b5, 'studio_day', '林峰的工作室（同一间，清晨的冷灰光，窗外城市安静）', 'The same late-night climate-modeling studio as in the reference image, now in cold grey early-morning light: the long desk with two large monitors still glowing with steeply falling orange curves at the left, the worn brown leather sofa at the center-right, a glass studio door at the right beyond the sofa, a floor-to-ceiling window across the back wall showing a pale grey dawn over a quiet city.',
          '和参考图是同一间气候建模工作室，现在是清晨冷灰色的光：左边长桌上两块大屏幕还亮着，橙色曲线陡直下落，中右是那张旧皮沙发，右边沙发后面是一扇玻璃门，后墙是落地窗、窗外是安静的城市灰蒙蒙的黎明。',
          'the desk with the two monitors, the sofa, the glass door and the grey dawn window')
new_scene(b5, 'bunker_control', '地下控制室（红色按钮、监控墙、红色倒计时钟）', 'A compact underground concrete control room: a steel control console in the middle of the room with rows of small green status lights and one big red push-button under a clear flip-up cover, a wall of six small monitors at the left, a large red digital countdown clock hanging high on the back wall at center-right, a heavy steel door in the right wall, cool green indicator glow and pale work-lamp light.',
          '地下紧凑的混凝土控制室：房间中间是一张钢制控制台，上面一排排小小的绿色指示灯和一个罩着透明翻盖的大红色按钮，左边是一整面六块小屏幕的监控墙，中右的后墙高处挂着一个大红色电子倒计时钟，右墙是一扇厚重的钢门，冷冷的绿色指示灯光和苍白的工作灯光。',
          'the console with the red button, the monitor wall, the red clock and the steel door')
new_scene(b5, 'street_summer', '中午的市中心大街（远处一堵白色的雾墙）', 'A wide city boulevard between glass office towers at midday under a blinding white sun: the street receding down the middle, a line of stopped cars filling both lanes, leafy trees along the sidewalks, and at the far end of the street a towering wall of white mist filling the sky.',
          '中午刺眼的白色阳光下，玻璃写字楼之间一条宽阔的市中心大街：街道向画面深处延伸，两条车道上停着一长排车，人行道两边是枝叶茂盛的行道树，街的尽头一堵高耸的白色雾墙遮住了天空。',
          'the boulevard, the stopped cars, the trees and the white wall of mist at the far end')
new_scene(b5, 'street_frozen', '同一条大街（冻成冰蓝色，车被冰裹住，人形冻在路边）', 'The same wide city boulevard as in the reference image, now frozen in dim grey-blue light and a thin white mist: the stopped cars encased in ice, bare frost-furred trees along the sidewalks, people frozen mid-stride in white ice along the sidewalks, the glass towers furred with frost.',
          '和参考图是同一条宽阔的市中心大街，现在冻在昏暗的灰蓝色光里、飘着一层薄薄的白雾：停着的车被冰裹住，人行道边的行道树光秃秃的、结满霜，路边的人保持着迈步的姿势被冻在白色的冰里，玻璃写字楼上也结了一层霜。',
          'the iced cars, the frost-furred trees, the frozen figures and the frosted towers')
new_scene(b5, 'wine_cellar', '苏清月大平层下面的酒窖（石墙，冷，一盏昏黄的灯）', 'A bitterly cold stone-walled private wine cellar beneath a luxury apartment tower: racks of wine bottles along the left wall, stacked cases of canned food and bottled water in the middle, three concrete steps rising to a heavy steel security door at the right, a small round thermometer on the wall above the cases, one dim yellow bulb, frost furring the bottles.',
          '豪华公寓楼下面一间冷得刺骨的石墙私人酒窖：左墙是一排排酒架，中间堆着成箱的罐头和瓶装水，右边三级混凝土台阶通向一扇厚重的钢制防盗门，货箱上方的墙上挂着一个小圆温度计，一盏昏黄的灯泡，酒瓶上结着一层霜。',
          'the wine racks, the stacked cases, the steps and the heavy steel door')
new_scene(b5, 'airlock', '缓冲舱（白瓷砖，钢长凳，挂着白色防寒服，圆形钢舱门）', 'A narrow white-tiled decontamination airlock: a long steel bench with two hanging white polar suits and a shelf of white goggles along the left wall, a bare white-tiled floor in the middle, a heavy round steel hatch door in the right wall, hard white strip lights.',
          '一间狭长的白瓷砖缓冲舱：左墙边是一条钢制长凳、上面挂着两套白色防寒服、旁边一层架子上放着白色护目镜，中间是光洁的白瓷砖地面，右墙是一扇厚重的圆形钢舱门，白色的硬质灯管光。',
          'the bench with the hanging white suits, the tiled floor and the round steel hatch')
new_scene(b5, 'snow_hatch', '雪林里的枯树洞暗门（树洞里有黑洞洞的通道，腰深的雪）', 'A silent frozen pine forest at night buried in waist-deep snow under a black sky with a faint green aurora: at the left a hollow dead tree trunk whose camouflaged hatch stands open on a black passage, snow-laden pines all around, the white snow glowing.',
          '夜里一片寂静的冰封松林，积雪深到腰部，黑色的天空里有一点淡淡的绿色极光：左边是一截中空的枯树干，伪装的暗门敞开着、露出黑洞洞的通道，四周是压满雪的松树，白雪泛着微光。',
          'the open hollow-trunk hatch, the deep snow and the snow-laden pines')
new_scene(b5, 'snow_vent', '雪林里被冰封住的排气管', 'A silent frozen pine forest at night buried in deep snow under a black sky with a faint green aurora: a thick steel exhaust pipe sticking out of the snow at center-right with its mouth sealed in a heavy block of ice, snow-laden pines behind it, the white snow glowing.',
          '夜里一片寂静的冰封松林，积雪很深，黑色的天空里有一点淡淡的绿色极光：中右处一根粗钢排气管从雪里伸出来，管口被一大块厚冰封死，后面是压满雪的松树，白雪泛着微光。',
          'the ice-sealed steel pipe, the deep snow and the snow-laden pines')
new_scene(b5, 'snow_trek', '一望无际的雪原（远处山脊上一排冻成冰的人形）', 'A vast frozen snowfield at night under a black sky with a faint green aurora: open deep snow filling the middle, a few leafless frozen trees at the right, and far at the back a line of white ice-encased human figures frozen mid-run along a low ridge, the white snow glowing.',
          '夜里黑色天空下一望无际的冰封雪原，有一点淡淡的绿色极光：中间是开阔的深雪，右边有几棵光秃秃的冻树，远处低矮的山脊上有一排冻成白冰的人形、保持着奔跑的姿势，白雪泛着微光。',
          'the open snowfield, the frozen trees and the ice-encased figures on the ridge')
new_scene(b5, 'snow_stump', '同一座山坡变成雪地（青苔岩石盖着雪，枯树桩侧面有一小块镜头玻璃）', 'The same forested mountain hillside as in the reference image, now buried in snow at night under a black sky with a faint green aurora: a snow-capped boulder at the left, a dead tree stump at center-left with a small round dark glass lens set in its side and a thin patch of snow melting around the glass, an open snowfield in the middle, snow-laden pines in the background.',
          '和参考图是同一座深山树林山坡，现在夜里被大雪埋住，黑色的天空里有一点淡淡的绿色极光：左边是盖着雪的岩石，中左是那截枯树桩、侧面嵌着一小块圆形的深色玻璃，玻璃周围一小圈雪正在融化，中间是开阔的雪地，后面是压满雪的松树。',
          'the snow-capped boulder, the stump with the small glass lens and the open snowfield')
new_scene(b5, 'bunker_sprouts', '同一张工作台（海绵块里冒出了第一批嫩绿的芽，头顶亮着粉紫色生长灯）', 'The same steel workbench in the vast supply-packed underground hall as in the reference image, now with a white tray of foam seeding blocks each topped with tiny pale-green seedlings in the shallow tub of clear water under a hanging white-purple grow lamp, towering stacks of steel crates, pallets, generators and water tanks behind it and along both sides.',
          '和参考图是同一张钢制工作台、同一个堆满货的巨大地下大厅，现在浅浅的清水盆里的白色托盘上，每块海绵块顶上都冒出了小小的淡绿色嫩芽，头顶吊着一盏粉紫色的生长灯，后面和两侧是高高的钢箱、货箱、发电机和水箱。',
          'the workbench, the tray of sprouting seedlings under the grow lamp and the stacked supplies')
for _a in b5.d['assets']:
    if _a['key'] == 'bunker_sprouts': _a['generate']['reference_keys'] = ['bunker_work']
    if _a['key'] == 'studio_day': _a['generate']['reference_keys'] = ['studio_night']
    if _a['key'] == 'street_frozen': _a['generate']['reference_keys'] = ['street_summer']
    if _a['key'] == 'snow_stump': _a['generate']['reference_keys'] = ['hill_hidden']

# ---------------------------------------------------------------------------------------------- 声音
SU_DOWN_EN, SU_DOWN_ZH = SU_EN, SU_ZH
for nm, key in (('LinArctic', 'lin_arctic'),):
    b5.character(nm, key, LIN_EN, LIN_ZH)
b5.character('SuDown', 'su_down', SU_EN, SU_ZH)
b5.character('SuTrek', 'su_trek', SU_EN, SU_ZH)
b5.character('Gaunt', 'gaunt_drifter', 'A hoarse adult male voice, cracked and exhausted, speaking clear Mandarin Chinese.' + VT_EN, '嘶哑的成年男声，干裂、筋疲力尽，普通话清楚。' + VT_ZH)
b5.character('Bearded', 'bearded_drifter', 'A heavy adult male voice, numb and bitter, speaking clear Mandarin Chinese.' + VT_EN, '低沉的成年男声，麻木、苦涩，普通话清楚。' + VT_ZH)
b5.character('Brute', 'brute_raider', 'A rough adult male voice, savage and hoarse, speaking clear Mandarin Chinese.' + VT_EN, '粗野的成年男声，凶狠、嘶哑，普通话清楚。' + VT_ZH)


def insert_task(tid, title, dur, scene, framing, act_en, zh, snd, holds, cam, bg=''):
    return S.T(tid, title, dur, scene, [], framing, act_en, zh, snd, cam=cam, holds=holds, room=set(), new=True, bg=bg)


def track(who_en, who_zh):
    return (f'The camera tracks sideways slowly alongside {who_en} until {who_en} stands in the middle third of the frame.', f'镜头缓缓横移跟着{who_zh}，直到{who_zh}走到画面中间三分之一。')


SOUND_CTRL = voiced('A low electric hum from the console and the faint hiss of the air system.', '控制台低低的电流嗡鸣和空气系统轻微的嘶嘶声。')
SOUND_CELLAR = voiced('A thin whistle of wind through the cellar door and her shivering breath.', '风从酒窖门缝里钻进来的细细的呼啸和她发抖的呼吸声。')
SOUND_AIRLOCK = voiced('The low hum of the ventilation and the creak of heavy fabric.', '通风系统低低的嗡鸣和厚重衣料的摩擦声。')

# ---------------------------------------------------------------------------------------------- 第 5 集
S.T('05-01', '01｜最后一晚的工作室：林峰把羽绒服塞给周宁，让他带家人去高处，别问', 10, STUDIO,
    [P('lin_studio', 'center', "standing beside the sofa in profile facing frame-right, holding a folded dark down parka out in both hands toward Ning", 'Ning', "his jaw set, his brows level"),
     P('ning_partner', 'right', "sitting on the leather sofa in profile facing frame-left with the puffer coat on his shoulders, looking up", 'Lin', "his lips parted, his brows pulled together")],
    'Medium-wide shot, both men from the head to the knees, in the middle third of the frame, in the late-night studio.',
    "<lin_studio> holds the folded down parka out to <ning_partner> and speaks the first line to <ning_partner> in a low flat voice, his jaw set and his brows level. <ning_partner> looks up at him and speaks the second line to <lin_studio> in a hoarse, uneasy voice, his lips parted and his brows pulled together. <lin_studio> lays the parka on <ning_partner>'s lap and speaks the third line to <ning_partner> in the same flat voice, his eyes steady on <ning_partner>.",
    "林峰把叠好的羽绒服递到周宁面前，用低沉平淡的声音对周宁说出第一句，下颌绷紧、眉毛平直。周宁抬头看着他，用沙哑不安的声音对林峰说出第二句，嘴唇微张、眉头拧在一起。林峰把羽绒服放在周宁腿上，用同样平淡的声音对周宁说出第三句，眼睛稳稳看着周宁。",
    SOUND_STUDIO,
    lines=[('lin_studio', "带家人去高处。", 0.7, 'Ning'), ('ning_partner', "出什么事了？", 3.5, 'Lin'), ('lin_studio', "多买羽绒服，别问。", 5.9, 'Ning')],
    bg='On the long desk at frame-left the two large monitors glow with the steeply falling orange curves, and the city lights glitter in the window behind them.',
    holds='The frame holds Lin and Ning, the sofa, the desk with the monitors and the window behind them.', room={'Lin', 'Ning'}, new=True,
    st={'Lin': ('皱巴巴的白衬衫，手里捧着叠好的羽绒服', '皱巴巴的白衬衫，手空着'), 'Ning': ('外套披在肩上，坐在沙发上', '羽绒服放在腿上，坐在沙发上')})

S.T('05-02', '02｜第二天清晨的工作室：苏清月找林峰，周宁说他去修度假村了，苏清月看到曲线，周宁起身离开', 12, STUDIO_DAY,
    [P('su_suit', 'left', "standing beside the long desk in profile facing frame-right with her handbag on her arm", 'Ning', "her eyes narrowed, her lips pressed in a thin sharp line"),
     P('ning_partner', 'center', "sitting on the sofa in profile facing frame-left with the dark down parka folded on his lap and the puffer coat on his shoulders", 'Su', "his lips pressed tight, his brows pulled together, dark circles under his eyes")],
    'Medium-wide shot, both from the head to the knees, in the middle third of the frame, in the empty studio at dawn.',
    "<su_suit> speaks the first line to <ning_partner> in a sharp, controlled voice, her eyes narrowed and her lips pressed in a thin sharp line. <ning_partner> looks up at her and speaks the second line to <su_suit> in a hoarse, evasive voice, his lips pressed tight and his brows pulled together. <su_suit> turns her head toward the two monitors where the orange curves fall steeply, her face paling, then turns back and speaks the third line to <ning_partner> in a low, shaken voice. <ning_partner> says nothing, stands up with the parka in his arms and walks to the glass studio door at frame-right, leaving through it until the doorway is empty.",
    "苏清月用锐利而克制的声音对周宁说出第一句，眼睛眯起、嘴唇抿成一条细而锐利的线。周宁抬头看着她，用沙哑躲闪的声音对苏清月说出第二句，嘴唇紧抿、眉头拧在一起。苏清月把头转向两块屏幕——橙色的曲线陡直下落，她脸色发白，然后转回来，用低沉发颤的声音对周宁说出第三句。周宁什么也没说，抱着羽绒服站起来，走向画面右边的玻璃门，穿过去离开，直到门口空无一人。",
    SOUND_STUDIO,
    lines=[('su_suit', "林峰人呢？", 0.7, 'Ning'), ('ning_partner', "他去修度假村了。", 3.1, 'Su'), ('su_suit', "这条曲线，是真的？", 5.6, 'Ning')], exit={'Ning'},
    bg='On the long desk beside her the two large monitors glow with the steeply falling orange curves, and the glass studio door stands at frame-right beyond the sofa.',
    holds='The frame holds Su and Ning, the sofa, the desk with the monitors and the glass door.', room={'Su', 'Ning'}, new=True,
    st={'Su': ('黑色真丝衬衫，站在长桌边', '黑色真丝衬衫，站在长桌边'), 'Ning': ('羽绒服叠在腿上，坐在沙发上', None)})

S.T('05-03', '03｜同一间工作室：周宁走后，苏清月一个人看着曲线，低声自言自语', 10, STUDIO_DAY,
    [P('su_suit', 'center', "standing at the long desk in profile facing frame-left, holding a crumpled printed chart of falling curves up in both hands", 'obj:the crumpled printed chart of falling curves in her hands', "her eyes narrowed, her lips pressed in a thin line, her brows low")],
    'Medium shot, the figure from the head to the knees, in the middle third of the frame, in the empty studio at dawn.',
    "<su_suit> stands alone at the desk with her eyes on the crumpled printed chart in her hands, then murmurs one short line to herself in a low voice, talking to nobody, her lips moving softly, then a second short line, her eyes narrowed and her brows low. Nobody else is in the room.",
    "苏清月一个人站在桌边，眼睛盯着手里皱巴巴的打印曲线图，然后低声自言自语了一句很短的话，不是对任何人说的，嘴唇轻轻动着，接着又是一句，眼睛眯起、眉头压低。房间里没有别人。",
    voiced('A faint electronic hum from the monitors and her low murmur.', '显示器轻微的电子嗡鸣和她低低的自语。'),
    vo=[('su_suit', "不是妄想……", 1.8, 'Su'), ('su_suit', "是倒计时。", 4.5, 'Su')], dep=True, cam=push1('Su', '苏清月'),
    bg='Behind her the two large monitors glow with the steeply falling orange curves and the grey dawn lies over the quiet city in the window.',
    holds='The frame holds Su alone at the desk, the glowing monitors and the dawn window.',
    st={'Su': ('黑色真丝衬衫，站在长桌边', '黑色真丝衬衫，站在长桌边')})

S.T('05-04', '04｜大平层：苏清月让助理再订一批货，被告知全城的货被一个人买光了，她只囤到三成', 13, PENT,
    [P('wen_blazer', 'left', "standing in profile facing frame-right with a tablet hugged to her chest", 'Su', "her brows lifted, her lips pressed together"),
     P('su_suit', 'right', "standing beside the glass table in profile facing frame-left with her phone in one hand", 'Wen', "her eyes narrowed, her lips pressed in a thin line")],
    'Medium two-shot, both from the head to the knees, in the middle third of the frame, in the penthouse living room.',
    "<su_suit> speaks the first line to <wen_blazer> in a firm voice, her eyes narrowed and her lips pressed in a thin line. <wen_blazer> shakes her head and speaks the second line to <su_suit> in a low, anxious voice, her brows lifted and her lips pressed together. <su_suit> speaks the third line to <wen_blazer> in a tight voice. <wen_blazer> speaks the fourth line to <su_suit> in a small voice, then <su_suit> slowly lowers her phone and turns her head toward the floor-to-ceiling window, her face pale and her lips pressed in a thin line.",
    "苏清月用坚定的声音对文助理说出第一句，眼睛眯起、嘴唇抿成一条细线。文助理摇了摇头，用低低的、焦虑的声音对苏清月说出第二句，眉毛上提、嘴唇抿紧。苏清月用紧绷的声音对文助理说出第三句。文助理用很小的声音对苏清月说出第四句，然后苏清月慢慢放下手机，把头转向落地窗，脸色苍白、嘴唇抿成一条细线。",
    SOUND_PENT,
    lines=[('su_suit', "再加订一批。", 0.8, 'Wen'), ('wen_blazer', "全城的货，被人买光了。", 3.6, 'Su'), ('su_suit', "我们囤了几成？", 6.8, 'Wen'), ('wen_blazer', "三成。", 9.3, 'Su')],
    bg='Behind them the floor-to-ceiling windows glare with the white-hot city, and the glass table stands between them with a phone and a notepad on it.',
    holds='The frame holds Wen and Su, the glass table and the glaring windows behind them.', room={'Su', 'Wen'}, new=True,
    st={'Su': ('黑色真丝衬衫，站在玻璃桌边', '黑色真丝衬衫，手机放下'), 'Wen': ('藏青西装外套，站在她旁边', '藏青西装外套，站在她旁边')})

S.T('05-05', '05｜地下控制室：林峰低声说最后一天了，掀开保护盖，按下红色按钮', 10, CONTROL,
    [P('lin_work', 'center', "standing at the steel console in profile facing frame-right, his right hand slowly lifting the clear plastic safety cover from the big red button, his left hand resting on the console", 'obj:the big red push-button under the cover on the console in front of him', "his jaw set, his lips set flat, his brows level")],
    'Medium shot, the figure from the head to the knees, in the middle third of the frame, at the console.',
    "<lin_work> stands alone at the console with his eyes on the big red button, lifts the clear cover with his right hand, then murmurs one line to himself in a low voice, talking to nobody, his lips moving softly, then a second short line, his jaw set and his brows level, and presses the red button down slowly with his thumb. Nobody else is in the room.",
    "林峰一个人站在控制台前，眼睛盯着那个大红色按钮，右手掀开透明的保护盖，然后低声自言自语了一句，不是对任何人说的，嘴唇轻轻动着，接着又是一句很短的，下颌绷紧、眉毛平直，然后用拇指慢慢把红色按钮按了下去。房间里没有别人。",
    voiced('A low electric hum from the console, the click of the plastic cover and his low murmur.', '控制台低低的电流嗡鸣、塑料保护盖的一声轻响和他低低的自语。'),
    vo=[('lin_work', "最后一天了。", 1.5, 'Lin'), ('lin_work', "来吧。", 4.8, 'Lin')], cam=push1('Lin and the red button', '林峰和红色按钮'),
    bg='High on the back wall behind him the large red digital clock glows, and the wall of small monitors stands at frame-left.',
    holds='The frame holds Lin alone at the console, the red button, the monitors and the red clock.', room={'Lin'}, new=True,
    st={'Lin': ('深灰亨利衫和工装背心', '深灰亨利衫和工装背心')})

insert_task('05-06', '06｜插镜：控制室的指示灯全亮了，红色电子钟的数字在跳', 5, CONTROL,
    'Wide establishing shot of the empty control room, the console in the middle third of the frame, nobody in the room.',
    "Every row of status lights along the steel console blazes green, the red button glows lit beneath its open cover, the wall of small monitors flickers awake and the large red digital clock high on the back wall glows with its last seconds. Nothing else moves.",
    "控制室里空无一人：钢制控制台上一排排指示灯全部亮成绿色，红色按钮在掀开的保护盖下亮着，左边那一整面小屏幕闪着亮起来，后墙高处的大红色电子钟亮着最后几秒。别的什么都不动。",
    breathy('Three heavy generators roaring to life far below and a rising electric hum.', '远处地下三台沉重的发电机轰鸣着启动，电流的嗡鸣越来越高。'),
    'The frame holds the console with its lit status lights and the red button, the monitor wall, the red clock and the steel door, and nobody in the room.',
    push('the console and the red clock', '控制台和红色电子钟'))

# ---------------------------------------------------------------------------------------------- 第 6 集
b6 = S.episode('剧本第6集｜降临', '中午的大街上，一堵白色的雾墙滚过来；转眼整条街冻成了冰蓝色，路边的人保持着迈步的姿势成了冰雕。地下安全屋里，林峰一边煎牛排一边说：外面零下七十八度，这里二十五度。酒窖里苏清月和助理冻得发抖，助理去楼上找暖气，再没回来。安全屋里警报亮起：排气管被冻住了，林峰放下刀叉，换上白色防寒服，对自己说：十五分钟，就回来。', 6)

insert_task('06-01', '01｜插镜：中午的大街，远处一堵白色的雾墙滚过来，路边的人停下脚步', 5, STREET,
    'Wide establishing shot of the glass-tower boulevard at midday, the street in the middle third of the frame; no named person.',
    "A towering wall of white mist rolls down the boulevard from the far end toward the camera, while the few pedestrians on the sidewalks stand still with their faces turned toward it and the stopped cars sit with their doors open. Nothing else moves.",
    "中午玻璃写字楼之间的大街：街尽头一堵高耸的白色雾墙朝镜头滚过来，人行道上的几个行人一动不动、脸转向它，停着的车都开着门。别的什么都不动。",
    breathy('A rising low roar of wind and a faint distant car alarm.', '越来越响的低沉风声和远处一声若有若无的汽车警报声。'),
    'The frame holds the boulevard with the stopped cars, the few pedestrians standing still and the white wall of mist at the far end.',
    push('the street', '大街'),
    bg='A few pedestrians stand motionless on the sidewalks with their faces turned toward the far end of the street.')

insert_task('06-02', '02｜插镜：同一条大街冻成了冰蓝色，路边的人保持着迈步的姿势被冻在冰里', 5, FROZEN,
    'Wide establishing shot of the same boulevard, the street in the middle third of the frame; no living person.',
    "The same boulevard lies buried in dim grey-blue light: the cars are encased in ice, the bare trees furred with frost, and along both sidewalks people stand frozen mid-stride in white ice with their arms still swinging. A thin white mist drifts over the street. Nothing else moves.",
    "同一条大街，现在埋在昏暗的灰蓝色光里：车被冰裹住，光秃秃的树结满了霜，两边人行道上的人保持着迈步、手臂还在摆动的姿势被冻在白色的冰里。一层薄薄的白雾飘过街面。别的什么都不动。",
    breathy('A dead silence broken only by a low wind and the faint creak of ice.', '一片死寂，只有低低的风声和冰层轻轻的吱嘎声。'),
    'The frame holds the frozen boulevard with the ice-encased cars, the frost-furred trees and the frozen figures along the sidewalks.',
    push('the street', '大街'))

S.T('06-03', '03｜地下安全屋：林峰一边煎牛排，一边低声说外面零下七十八度，这里二十五度', 12, LIVING,
    [P('lin_home', 'left', "standing at the black-and-gold stove in profile facing frame-right, a steel pan with a thick steak sizzling in front of him and a pair of tongs in his right hand", 'obj:the wall of security monitors at frame-right where a white blizzard rages on every screen', "his jaw relaxed, his lips set in a calm flat line, his brows soft")],
    'Medium shot, the figure from the head to the knees, at the left of the middle third of the frame, in the underground living area.',
    "<lin_home> flips the thick steak in the pan with the tongs, the butter sizzling, his eyes on the monitor wall where a white blizzard rages on every screen, then murmurs one line to himself in a low voice, talking to nobody, his lips moving softly, then a second short line, his jaw relaxed and his brows soft. Nobody else is in the room.",
    "林峰用夹子翻动平底锅里的厚牛排，黄油滋滋作响，眼睛看着监控墙——每块屏幕里都是呼啸的白色暴风雪，然后他低声自言自语了一句，不是对任何人说的，嘴唇轻轻动着，接着又是一句很短的，下颌放松、眉毛舒展。房间里没有别人。",
    voiced('Butter and meat sizzling, a low howl of wind from the monitor speakers, the hum of the air system and his low murmur.', '黄油和牛排滋滋作响、监控喇叭里低低的风的呼啸、空气系统的嗡鸣和他低低的自语。'),
    vo=[('lin_home', "外面，零下七十八度。", 2.0, 'Lin'), ('lin_home', "这里，二十五度。", 6.0, 'Lin')], cam=push1('Lin and the pan', '林峰和平底锅'),
    bg='At the center-right of the frame the wall of security monitors shows a white blizzard raging over a buried, silent street on every screen.',
    holds='The frame holds Lin alone at the stove and the monitor wall.', room={'Lin'}, new=True,
    st={'Lin': ('灰色棉质家居服，光脚，站在炉灶前', '灰色棉质家居服，光脚，站在炉灶前')})

S.T('06-04', '04｜酒窖：暖气彻底停了，苏清月让助理把羽绒服都拿来，助理说去楼上看看，走出门去', 12, CELLAR,
    [P('wen_blazer', 'left', "standing beside the stacked cases in profile facing frame-right with her arms wrapped around herself, her breath clouding", 'Su', "her brows pulled together, her lips trembling", outfit="in a navy blazer under a thin down vest"),
     P('su_down', 'center', "sitting on a case of canned food in profile facing frame-left with her gloved hands rubbing together, her breath clouding", 'Wen', "her eyes narrowed, her lips pressed in a thin line")],
    'Medium two-shot, both from the head to the knees, in the middle third of the frame, in the frozen wine cellar.',
    "<wen_blazer> speaks the first line to <su_down> in a trembling voice, her brows pulled together and her lips trembling. <su_down> rubs her gloved hands and speaks the second line to <wen_blazer> in a low firm voice, her eyes narrowed and her lips pressed in a thin line. <wen_blazer> speaks the third line to <su_down> in a small voice, then climbs the three concrete steps to the heavy steel door at frame-right and goes out through it until the steps stand empty. <su_down> watches her go.",
    "文助理用发颤的声音对苏清月说出第一句，眉头拧在一起、嘴唇发抖。苏清月搓着戴手套的手，用低沉坚定的声音对文助理说出第二句，眼睛眯起、嘴唇抿成一条细线。文助理用很小的声音对苏清月说出第三句，然后爬上三级混凝土台阶，走向画面右边的钢门，穿过去离开，直到台阶上空无一人。苏清月目送她。",
    SOUND_CELLAR,
    lines=[('wen_blazer', "暖气彻底停了，苏总。", 0.8, 'Su'), ('su_down', "把所有羽绒服，都拿来。", 3.8, 'Wen'), ('wen_blazer', "我去楼上看看！", 7.0, 'Su')], exit={'Wen'},
    bg='Behind them the frost-furred wine racks line the left wall, and the heavy steel door stands at the top of the three steps at frame-right.',
    holds='The frame holds Wen and Su, the stacked cases, the steps and the steel door.', room={'Su', 'Wen'}, new=True,
    st={'Su': ('长款奶白色羽绒服，坐在货箱上', '长款奶白色羽绒服，坐在货箱上'), 'Wen': ('藏青西装外套外面套着薄羽绒背心，站在货箱旁', None)})

S.T('06-05', '05｜安全屋：警报响了，林峰低声说排气管冻住了，放下刀叉', 11, LIVING,
    [P('lin_home', 'center', "seated at the small round dining table in profile facing frame-right, a knife and fork in his hands over a half-eaten steak", 'obj:the wall of security monitors at frame-right where a red warning lamp blinks above the blizzard screens', "his jaw tight, his lips pressed flat, his brows low")],
    'Medium shot, the figure from the head to the waist, in the middle third of the frame, at the dining table.',
    "<lin_home> cuts a slice of steak, his eyes on the monitor wall where a red warning lamp starts to blink above the blizzard screens, then lowers his knife, murmurs one line to himself in a low voice, talking to nobody, his lips moving softly, then a second short line, his jaw tight and his brows low, and lays the knife and fork down and pushes his chair back. Nobody else is in the room.",
    "林峰切下一片牛排，眼睛看着监控墙——暴风雪的屏幕上方，一盏红色的警示灯开始闪烁，然后他放下刀，低声自言自语了一句，不是对任何人说的，嘴唇轻轻动着，接着又是一句很短的，下颌绷紧、眉头压低，然后把刀叉放下，把椅子往后推开。房间里没有别人。",
    voiced('A steady shrill electronic alarm, the low howl of wind from the monitor speakers and his low murmur.', '持续尖锐的电子警报声、监控喇叭里低低的风的呼啸和他低低的自语。'),
    vo=[('lin_home', "排气管，冻住了。", 2.5, 'Lin'), ('lin_home', "再不清，今晚缺氧。", 5.5, 'Lin')], cam=push1('Lin', '林峰'),
    bg='The wall of security monitors at the center-right shows a white blizzard on every screen with one red warning lamp blinking above it.',
    holds='The frame holds Lin alone at the dining table and the monitor wall.', room={'Lin'}, new=True,
    st={'Lin': ('灰色棉质家居服，光脚，坐在圆桌边', '灰色棉质家居服，光脚，站起来前把刀叉放下')})

S.T('06-06', '06｜缓冲舱：林峰拉上白色防寒服的拉链，低声说十五分钟就回来', 8, AIRLOCK,
    [P('lin_arctic', 'center', "standing in profile facing frame-right, zipping the front of the bulky white polar suit up to his chin with his right hand while the white goggles hang from his left hand", 'obj:the heavy round steel hatch at frame-right', "his jaw set, his lips set in a hard line, his brows level")],
    'Medium shot, the figure from the head to the knees, in the middle third of the frame, in the airlock.',
    "<lin_arctic> zips the bulky white suit up to his chin, his eyes on the heavy round steel hatch, then murmurs one short line to himself in a low voice, talking to nobody, his lips moving softly, his jaw set and his brows level, and slides the white goggles up onto his forehead. Nobody else is in the airlock.",
    "林峰把蓬松的白色防寒服的拉链拉到下巴，眼睛看着那扇厚重的圆形钢舱门，然后低声自言自语了一句很短的话，不是对任何人说的，嘴唇轻轻动着，下颌绷紧、眉毛平直，然后把白色护目镜推到额头上。缓冲舱里没有别人。",
    voiced('The low hum of the ventilation, the rasp of a heavy zipper and his low murmur.', '通风系统低低的嗡鸣、厚重拉链的嘶啦声和他低低的自语。'),
    vo=[('lin_arctic', "十五分钟，就回来。", 1.8, 'Lin')], cam=push1('Lin', '林峰'),
    bg='Behind him the two white polar suits hang from the bench along the left wall.',
    holds='The frame holds Lin alone in the airlock, the bench with the white suits and the round steel hatch.', room={'Lin'}, new=True,
    st={'Lin': ('白色防寒服，白色护目镜', '白色防寒服，白色护目镜推在额头上')})

# ---------------------------------------------------------------------------------------------- 第 7 集
b7 = S.episode('剧本第7集｜白雪中的呼吸', '林峰穿着白色防寒服推开树洞里的暗门，在腰深的雪里走向被冰封死的排气管，用喷枪融冰。两个拖着铁棍的流浪者从远处摇晃着走来，他趴进雪里一动不动，两人几乎擦着他的头走过去。他修好管子，手背粘在冻管上抽回来时撕掉了一层皮。回到缓冲舱，他脱下结满霜的衣服，在二十五度里松了口气；工作台上的育苗盘冒出了第一批绿芽。监控墙上，一盏黄灯闪了起来——信号来自苏清月那栋楼。', 7)

S.T('07-01', '01｜雪林：林峰推开树洞暗门，在腰深的雪里走向被冰封死的排气管', 8, HATCH,
    [P('lin_arctic', 'left', "wading through the waist-deep snow in profile facing frame-right with a compact blowtorch in his right hand, one step out of the open hatch", 'obj:the snow ahead of him toward the pines at frame-right', "his jaw clenched, his lips pressed flat, his brows low")],
    'Wide shot, the figure from the head to the feet, small in the middle third of the frame, in the snowy forest.',
    "<lin_arctic> wades through the waist-deep snow away from the open hatch, lifting each leg slowly out of the drift, his eyes on the pines ahead, his jaw clenched and his brows low, his breath pouring white in the freezing air. Nobody else is in the forest.",
    "林峰离开敞开的暗门，在腰深的雪里往前走，每一步都要慢慢把腿从雪里拔出来，眼睛看着前面的松林，下颌咬紧、眉头压低，呼出的白气在冰冷的空气里翻涌。树林里没有别人。",
    breathy('Heavy breathing, the crunch of snow and a low wind in the pines.', '沉重的呼吸声、踩雪的嘎吱声和松林里低低的风声。'),
    cam=track('Lin', '林峰'),
    bg='Snow-laden pines stand all around and a faint green aurora hangs in the black sky.',
    holds='The frame holds Lin alone in the deep snow with the open hatch in the hollow trunk at frame-left.', room={'Lin'}, new=True,
    st={'Lin': ('白色防寒服，手里拿着便携喷枪', '白色防寒服，手里拿着便携喷枪')})

S.T('07-02', '02｜雪林：林峰跪在被冰封死的排气管前，用喷枪融冰', 9, VENT,
    [P('lin_arctic', 'center', "kneeling in the snow beside the ice-sealed steel pipe in profile facing frame-right, a compact blowtorch with a steady blue flame held in both hands aimed at the ice", 'obj:the blue flame on the ice-sealed mouth of the pipe', "his jaw clenched, his lips pressed flat, his brows low")],
    'Medium shot, the figure from the head to the knees, in the middle third of the frame, in the snowy forest.',
    "<lin_arctic> kneels beside the ice-sealed pipe and holds the blue flame of the blowtorch against the ice, his eyes on the flame, and the ice melts away in slow drops and runs down the steel, his jaw clenched and his brows low. Nobody else is in the forest.",
    "林峰跪在被冰封死的排气管旁，把喷枪的蓝色火焰对着冰面，眼睛盯着火焰，冰一滴一滴慢慢融化、顺着钢管流下来，下颌咬紧、眉头压低。树林里没有别人。",
    breathy('The steady hiss of the torch, dripping meltwater and a low wind in the pines.', '喷枪稳定的嘶嘶声、融化的冰水滴落的声音和松林里低低的风声。'),
    cam=push1('Lin and the pipe', '林峰和管道'),
    bg='Snow-laden pines stand behind him and a faint green aurora hangs in the black sky.',
    holds='The frame holds Lin alone kneeling beside the ice-sealed pipe.', room={'Lin'}, new=True,
    st={'Lin': ('白色防寒服，跪在排气管旁，喷枪对着冰', '白色防寒服，跪在排气管旁，喷枪对着冰')})

S.T('07-03', '03｜同一处：林峰关掉喷枪，看到远处三个人影，慢慢趴进雪里', 6, VENT,
    [P('lin_arctic', 'center', "kneeling in the snow beside the pipe in profile facing frame-right with the blowtorch switched off in his hand, his head turned toward the distant figures", 'obj:the three dark figures dragging themselves through the haze far behind the pipe at frame-right', "his jaw tight, his lips pressed flat, his brows low")],
    'Medium-wide shot, the figure from the head to the knees, in the middle third of the frame, in the snowy forest.',
    "<lin_arctic> switches off the torch, the blue flame dies, and he turns his head toward the three small dark figures dragging themselves through the haze far behind the pipe, then lowers himself slowly flat into the snow until only the white of his suit shows, his jaw tight and his brows low.",
    "林峰关掉喷枪，蓝色的火焰熄灭，他把头转向排气管后面远处雾气里拖着步子走来的三个小小的黑色人影，然后慢慢把身体放平、趴进雪里，直到只剩一团白色的防寒服，下颌绷紧、眉头压低。",
    breathy('The torch hissing out, a held breath and a low wind in the pines.', '喷枪嘶的一声熄灭、一声屏住的呼吸和松林里低低的风声。'),
    dep=True, cam=push1('Lin', '林峰'),
    bg='Far behind the pipe in the haze three small dark ragged figures drag themselves through the snow, carrying iron bars.',
    holds='The frame holds Lin alone at the pipe, with three small figures far in the haze.',
    st={'Lin': ('白色防寒服，跪在排气管旁，喷枪对着冰', '白色防寒服，趴在雪里')})

S.T('07-04', '04｜同一处：林峰趴在雪里一动不动，两个流浪者几乎擦着他的头走过去', 12, VENT,
    [P('lin_arctic', 'right', "lying flat on his stomach in the snow beside the pipe, the white suit almost vanishing into the drift, his head turned down toward the snow", 'closed', "his jaw clenched, his lips pressed together"),
     P('gaunt_drifter', 'left', "trudging through the snow in profile facing frame-left, an iron bar dragging from one hand, about one meter beyond Lin's head", 'Bearded', "his lips cracked and parted, his brows pulled low"),
     P('bearded_drifter', 'center', "trudging beside Gaunt in profile facing frame-left, a short iron pipe hanging from one hand", 'Gaunt', "his lips pressed bitterly flat, his brows low")],
    'Medium-wide shot, all three from the head to the feet, in the middle third of the frame, in the snowy forest.',
    "<gaunt_drifter> trudges past with his eyes on <bearded_drifter> and speaks the first line to <bearded_drifter> in a cracked, exhausted voice, his lips cracked and parted. <bearded_drifter> speaks the second line to <gaunt_drifter> in a heavy, bitter voice, his lips pressed bitterly flat. <gaunt_drifter> speaks the third line to <bearded_drifter> in a flat voice, and both men trudge on out of the frame at frame-left without a glance at the white lump in the snow beside the pipe, until only the lying <lin_arctic> remains. <lin_arctic> does not move at all, his jaw clenched.",
    "流浪者甲眼睛看着流浪者乙，拖着步子走过去，用干裂疲惫的声音对流浪者乙说出第一句，嘴唇干裂微张。流浪者乙用沉重苦涩的声音对流浪者甲说出第二句，嘴唇苦涩地抿平。流浪者甲用平淡的声音对流浪者乙说出第三句，两人继续拖着脚步走出画面左边，看都没看排气管旁雪里那团白色的东西，直到画面里只剩下趴着的林峰。林峰一动不动，下颌咬紧。",
    voiced('Boots dragging through the snow, the scrape of iron on ice and a low wind in the pines.', '靴子拖过雪地的声音、铁棍刮过冰面的声音和松林里低低的风声。'),
    lines=[('gaunt_drifter', "冻死了……", 1.0, 'Bearded'), ('bearded_drifter', "这儿，根本没吃的。", 4.0, 'Gaunt'), ('gaunt_drifter', "回去，也是等死。", 7.2, 'Bearded')],
    enter={'Gaunt', 'Bearded'}, exit={'Gaunt', 'Bearded'},
    bg='The ice-sealed steel pipe stands beside the white lump of the lying man, and snow-laden pines stand behind.',
    holds='The frame holds Lin lying in the snow, Gaunt and Bearded trudging past, the pipe and the snow-laden pines.',
    st={'Lin': ('白色防寒服，趴在雪里', '白色防寒服，趴在雪里'), 'Gaunt': ('拖着铁棍，走进画面', None), 'Bearded': ('拿着铁管，走进画面', None)})

S.T('07-05', '05｜同一处：林峰爬起来修好管口，手背粘在冻管上，抽回手看着自己的手背', 8, VENT,
    [P('lin_arctic', 'center', "kneeling in the snow beside the pipe in profile facing frame-right, his bare left hand just pulled back from the frozen pipe clamp, the back of it raw and reddened, the white glove hanging from his right hand", 'obj:the raw reddened back of his own bare left hand', "his jaw clenched hard, his lips pressed in a grimace, his brows pulled low")],
    'Medium shot, the figure from the head to the knees, in the middle third of the frame, in the snowy forest.',
    "<lin_arctic> kneels beside the pipe and tightens the last clamp with his bare left hand, then pulls the hand away sharply, his jaw clenched hard and his brows pulled low, and looks down at the raw reddened back of his hand, then slowly pulls the white glove back on over it with his right hand. Nobody else is in the forest.",
    "林峰跪在排气管旁，用光着的左手拧紧最后一个卡箍，然后猛地把手抽回来，下颌咬得很紧、眉头压低，低头看着自己手背上那片发红的伤，然后用右手慢慢把白手套重新套回去。树林里没有别人。",
    breathy('A sharp hiss of breath through clenched teeth, the creak of frozen metal and a low wind in the pines.', '咬紧牙关倒吸一口冷气的嘶声、冻硬的金属的吱嘎声和松林里低低的风声。'),
    dep=True, cam=push1('Lin and his hand', '林峰和他的手'),
    bg='The ice-sealed steel pipe now stands free of ice beside him, and snow-laden pines stand behind.',
    holds='The frame holds Lin alone kneeling beside the pipe.',
    st={'Lin': ('白色防寒服，趴在雪里', '白色防寒服，跪在排气管旁，戴上了手套')})

S.T('07-06', '06｜缓冲舱：林峰回到家，扯下结霜的兜帽，低声说到家了', 9, AIRLOCK,
    [P('lin_arctic', 'center', "sitting on the steel bench in profile facing frame-right, pulling the frost-crusted white hood back off his head with his right hand while his left hand rests stiffly on his knee", 'obj:the heavy round steel hatch at frame-right now closed', "his jaw relaxing, his lips parted in a long breath, his brows loosening")],
    'Medium shot, the figure from the head to the knees, in the middle third of the frame, in the airlock.',
    "<lin_arctic> sits on the bench and pulls the frost-crusted hood back off his head, his breath coming out in a long slow sigh, his eyes on the closed round hatch, then murmurs one short line to himself in a low voice, talking to nobody, his lips moving softly, then a second short line, his jaw relaxing and his brows loosening. Nobody else is in the airlock.",
    "林峰坐在钢长凳上，把结满霜的兜帽从头上扯下来，长长地吐出一口气，眼睛看着已经关上的圆形舱门，然后低声自言自语了一句很短的话，不是对任何人说的，嘴唇轻轻动着，接着又是一句，下颌放松、眉毛舒展。缓冲舱里没有别人。",
    voiced('The low hum of the ventilation, the rasp of frozen fabric and his low murmur.', '通风系统低低的嗡鸣、冻硬的衣料摩擦声和他低低的自语。'),
    vo=[('lin_arctic', "到家了。", 2.2, 'Lin'), ('lin_arctic', "真暖和。", 5.0, 'Lin')], cam=push1('Lin', '林峰'),
    bg='Behind him the other white polar suit hangs from the bench along the left wall.',
    holds='The frame holds Lin alone in the airlock, the bench and the closed round hatch.', room={'Lin'}, new=True,
    st={'Lin': ('白色防寒服，坐在长凳上', '白色防寒服，兜帽已经扯下')})

S.T('07-07', '07｜工作台：育苗盘里冒出了第一批绿芽，林峰低声说出苗了', 9, SPROUTS,
    [P('lin_home', 'center', "standing at the steel workbench in profile facing frame-right with a white towel around his neck and his left hand wrapped in a strip of white gauze held against his chest, bending over the white tray of foam blocks", 'obj:the tiny pale-green seedlings on the tray in the water', "his jaw relaxed, the corners of his mouth lifting in a small pleased curve, his brows soft")],
    'Medium shot, the figure from the head to the waist, in the middle third of the frame, at the workbench.',
    "<lin_home> bends over the white tray in the water and gently touches one tiny pale-green seedling with the tip of his right finger, his eyes on the seedlings, the corners of his mouth lifting in a small pleased curve, then murmurs one short line to himself in a soft voice, talking to nobody, his lips moving softly, then a second short line, his jaw relaxed and his brows soft. Nobody else is in the hall.",
    "林峰俯身看着水里的白色托盘，用右手指尖轻轻碰了碰一株小小的淡绿色嫩芽，眼睛看着那些嫩芽，嘴角浮起一点满意的弧度，然后轻声自言自语了一句很短的话，不是对任何人说的，嘴唇轻轻动着，接着又是一句，下颌放松、眉毛舒展。大厅里没有别人。",
    voiced('Water gently lapping in the tub, the low hum of a generator and his soft murmur.', '水盆里水轻轻荡漾的声音、发电机低低的嗡鸣和他轻轻的自语。'),
    vo=[('lin_home', "出苗了。", 2.4, 'Lin'), ('lin_home', "比我想的，快。", 5.2, 'Lin')], cam=push1('Lin and the seedlings', '林峰和嫩芽'),
    bg='Behind him towering stacks of steel crates, pallets of boxes, generators and big water tanks fill the hall under hard white work lamps.',
    holds='The frame holds Lin alone at the workbench, the tray of seedlings and the stacked supplies behind him.', room={'Lin'}, new=True,
    st={'Lin': ('灰色棉质家居服，左手缠着白纱布，毛巾搭在脖子上', '灰色棉质家居服，左手缠着白纱布，毛巾搭在脖子上')})

S.T('07-08', '08｜安全屋：监控墙上亮起一盏黄灯，林峰擦着头发的手停住，低声念出苏清月的名字', 9, LIVING,
    [P('lin_home', 'center', "standing before the monitor wall in profile facing frame-right, rubbing his damp hair with a white towel in his right hand, his left hand wrapped in white gauze at his side", 'obj:the monitor wall where one small amber lamp blinks above the blizzard screens', "his jaw tightening, his lips pressed flat, his brows drawing together")],
    'Medium shot, the figure from the head to the knees, in the middle third of the frame, in the underground living area.',
    "<lin_home> rubs his damp hair with the towel, his eyes on the monitor wall where a small amber lamp starts to blink above the blizzard screens, the towel slows and stops, then he murmurs one line to himself in a low voice, talking to nobody, his lips moving softly, then a second short line, his jaw tightening and his brows drawing together. Nobody else is in the room.",
    "林峰用毛巾擦着湿漉漉的头发，眼睛看着监控墙——暴风雪的屏幕上方一盏小小的黄灯开始闪烁，毛巾慢下来、停住，然后他低声自言自语了一句，不是对任何人说的，嘴唇轻轻动着，接着又是一句很短的，下颌绷紧、眉头拧起。房间里没有别人。",
    voiced('A soft insistent beep from the monitor wall, the low howl of wind from the speakers and his low murmur.', '监控墙上一声轻轻而固执的哔哔声、喇叭里低低的风的呼啸和他低低的自语。'),
    vo=[('lin_home', "苏清月？", 2.4, 'Lin'), ('lin_home', "看来，麻烦上门了。", 4.6, 'Lin')], cam=push1('Lin and the monitor wall', '林峰和监控墙'),
    bg='The wall of security monitors at the center-right shows a white blizzard on every screen with one small amber lamp blinking above it.',
    holds='The frame holds Lin alone before the monitor wall.', room={'Lin'}, new=True,
    st={'Lin': ('灰色棉质家居服，左手缠着白纱布', '灰色棉质家居服，左手缠着白纱布')})

# ---------------------------------------------------------------------------------------------- 第 8 集
b8 = S.episode('剧本第8集｜苏清月的求生', '酒窖里，苏清月的水已经冻成了冰；门外有人用大锤砸门，她撕下布条塞进酒精瓶、点燃，在门被砸开的一刻把燃烧瓶砸向门口，领头的暴徒被火焰逼退。酒窖的保温层破了，她穿上三层羽绒服，带着林峰给的物流单跳窗入雪。雪原上她一步步往前挪，远处山脊上全是冻成冰的人形。另一边，安全屋里林峰正在装水泵，暖黄的灯光里一片安静。苏清月跪在坐标处，只有一片雪地，直到她看见一截枯树桩上有一小块玻璃，雪落在上面正在融化。', 8)

S.T('08-01', '01｜酒窖：苏清月想拧开瓶盖，水已经冻成了冰，她低声说撑不过今晚', 9, CELLAR,
    [P('su_down', 'center', "sitting on a case of canned food in profile facing frame-right with both gloved hands wrestling the cap of a bottle of water frozen solid, her breath clouding", 'obj:the frozen water bottle in her hands', "her lips cracked and pressed together, her brows drawn tight, her jaw trembling")],
    'Medium shot, the figure from the head to the knees, in the middle third of the frame, in the frozen wine cellar.',
    "<su_down> turns at the cap of the bottle with both gloved hands, her eyes on the bottle where the water has frozen into a solid block, her breath clouding, then murmurs one line to herself in a low voice, talking to nobody, her lips moving softly, then a second short line, her lips cracked and her brows drawn tight. Nobody else is in the cellar.",
    "苏清月戴着手套的两只手拧着瓶盖，眼睛看着那瓶已经冻成一整块冰的水，呼出的白气一团一团，然后她低声自言自语了一句，不是对任何人说的，嘴唇轻轻动着，接着又是一句很短的，嘴唇干裂、眉头紧蹙。酒窖里没有别人。",
    voiced('A thin whistle of wind through the cellar door, the creak of frozen plastic and her low murmur.', '风从酒窖门缝里钻进来的细细的呼啸、冻硬的塑料的嘎吱声和她低低的自语。'),
    vo=[('su_down', "水，也冻住了。", 2.0, 'Su'), ('su_down', "撑不过今晚。", 4.8, 'Su')], cam=push1('Su and the bottle', '苏清月和水瓶'),
    bg='Behind her the frost-furred wine racks line the left wall and the heavy steel door stands at the top of the three steps at frame-right.',
    holds='The frame holds Su alone in the cellar, the stacked cases and the steel door.', room={'Su'}, new=True,
    st={'Su': ('长款奶白色羽绒服，在酒窖里', '长款奶白色羽绒服，在酒窖里')})

S.T('08-02', '02｜酒窖：门外传来锤子砸门的闷响，苏清月撕下布条塞进酒精瓶，点着打火机', 10, CELLAR,
    [P('su_down', 'center', "kneeling beside a crate in profile facing frame-right, stuffing a torn strip of cloth into the neck of a clear bottle of medical alcohol", 'obj:the cloth strip and the neck of the alcohol bottle in her hands', "her eyes narrowed, her lips pressed in a thin hard line, her brows low")],
    'Medium shot, the figure from the head to the knees, in the middle third of the frame, in the frozen wine cellar.',
    "<su_down> kneels with the bottle of medical alcohol and pushes the torn strip of cloth deep into its neck, her eyes on the bottle, heavy hammer blows booming against the steel door behind her, then murmurs one short line to herself in a cold low voice, talking to nobody, her lips moving softly, her eyes narrowed and her brows low, and thumbs a lighter so that a small flame catches the cloth. Nobody else is in the cellar.",
    "苏清月跪在地上，把撕下来的布条深深塞进那瓶医用酒精的瓶口，眼睛看着酒瓶，背后的钢门上传来一下一下沉重的锤击声，然后她用冰冷低沉的声音自言自语了一句很短的话，不是对任何人说的，嘴唇轻轻动着，眼睛眯起、眉头压低，然后拇指一拨打火机，一朵小火苗点着了布条。酒窖里没有别人。",
    voiced('Heavy hammer blows booming against the steel door, the glug of liquid and her cold low murmur.', '钢门上沉重的锤击闷响、液体晃动的咕嘟声和她冰冷低沉的自语。'),
    vo=[('su_down', "想进来，自己拿。", 4.2, 'Su')], dep=True, cam=push1('Su and the bottle', '苏清月和酒瓶'),
    bg='Behind her the heavy steel door at the top of the three steps shudders at frame-right, and the frost-furred wine racks line the left wall.',
    holds='The frame holds Su alone kneeling in the cellar, the steps and the steel door.',
    st={'Su': ('长款奶白色羽绒服，在酒窖里', '长款奶白色羽绒服，在酒窖里')})

S.T('08-03', '03｜酒窖：门被砸开，苏清月把燃烧瓶砸向门口，领头的暴徒被火焰逼退', 6, CELLAR,
    [P('su_down', 'left', "standing at the foot of the three steps in profile facing frame-right with her arm cocked back at her shoulder holding the burning bottle, a flame guttering from its neck", 'Brute', "her eyes narrowed, her lips pressed in a hard line, her brows low"),
     P('brute_raider', 'right', "standing in the shattered doorway at the top of the steps in profile facing frame-left, the sledgehammer raised in both hands", 'Su', "his eyes wild, his lips curled under his scarf, his brows lowered")],
    'Medium-wide shot, both from the head to the feet, in the middle third of the frame, in the frozen wine cellar.',
    "<su_down> throws the burning bottle at the doorway in one hard sweep of her arm and it bursts into a ball of orange flame on the top step, her eyes on <brute_raider>. <brute_raider> lets the sledgehammer fall and reels back from the flames with his arm over his face, staggering out through the doorway until the doorway is empty, flames licking the top step and snow blowing in.",
    "苏清月手臂猛地一挥，把燃烧瓶砸向门口，瓶子在最上面一级台阶上爆成一团橙色的火焰，她的眼睛盯着暴徒。暴徒手里的大锤落下，用手臂挡着脸被火焰逼得连连后退，踉跄着退出门口，直到门口空无一人，火苗舔着最上面一级台阶，雪被风卷进来。",
    breathy('A roaring whoosh of flame, shattering glass and the howl of wind blowing in through the open doorway.', '火焰轰然腾起的声音、玻璃碎裂的声音和风从敞开的门口灌进来的呼啸。'),
    enter={'Brute'}, exit={'Brute'},
    bg='The heavy steel door hangs shattered open at the top of the steps with black night and blowing snow behind it.',
    holds='The frame holds Su at the foot of the steps and Brute in the doorway, the stacked cases and the shattered door.',
    st={'Su': (None, None), 'Brute': ('站在被砸开的门口，举着大锤', None)})

S.T('08-04', '04｜酒窖：苏清月知道保温层破了，穿上第三件羽绒服，低声说她陪他疯一次', 11, CELLAR,
    [P('su_trek', 'center', "standing in the middle of the cellar in profile facing frame-left, zipping the third down jacket up to her chin with one hand and holding a crumpled delivery slip with a hand-drawn map in the other, a heavy backpack on her shoulders", 'obj:the crumpled delivery slip with the hand-drawn map in her hand', "her jaw set, her lips pressed in a hard line, her brows low")],
    'Medium shot, the figure from the head to the knees, in the middle third of the frame, in the frozen wine cellar.',
    "<su_trek> zips the third down jacket up to her chin, her eyes on the crumpled delivery slip in her hand, and murmurs one line to herself in a low voice, talking to nobody, her lips moving softly, then a second short line, then a third, her jaw set and her brows low, and pulls the ski goggles down over her eyes. Nobody else is in the cellar.",
    "苏清月把第三件羽绒服的拉链拉到下巴，眼睛看着手里那张皱巴巴的物流单，低声自言自语了一句，不是对任何人说的，嘴唇轻轻动着，接着又是一句，然后又是一句，下颌绷紧、眉头压低，然后把滑雪护目镜拉下来戴在眼睛上。酒窖里没有别人。",
    voiced('The howl of wind through the shattered doorway, the rasp of a heavy zipper and her low murmur.', '风从被砸开的门口灌进来的呼啸、厚重拉链的嘶啦声和她低低的自语。'),
    vo=[('su_trek', "保温层，破了。", 1.6, 'Su'), ('su_trek', "林峰……", 4.2, 'Su'), ('su_trek', "我陪你，疯一次。", 6.3, 'Su')], cam=push1('Su', '苏清月'),
    bg='Behind her the shattered steel door stands open at the top of the three steps with blowing snow beyond it, and frost-furred wine racks line the left wall.',
    holds='The frame holds Su alone in the cellar, the stacked cases and the open doorway.', room={'Su'}, new=True,
    st={'Su': (None, None)})

S.T('08-05', '05｜雪原：苏清月背着登山包在齐腿深的雪里一步一步往前挪', 8, TREK,
    [P('su_trek', 'center', "wading thigh-deep through the snow in profile facing frame-right, one gloved hand holding her scarf over her mouth, the heavy backpack dragging on her shoulders", 'obj:the white ridge ahead at frame-right', "her jaw clenched, her lips pressed together under the scarf, her brows drawn low")],
    'Wide shot, the figure from the head to the feet, small in the middle third of the frame, in the frozen snowfield.',
    "<su_trek> wades through the thigh-deep snow, lifting each leg slowly out of the drift, her eyes on the white ridge ahead, her jaw clenched and her brows drawn low, her breath pouring white. Nobody else is on the snowfield.",
    "苏清月在齐腿深的雪里往前走，每一步都要慢慢把腿从雪里拔出来，眼睛看着前面白色的山脊，下颌咬紧、眉头压低，呼出的白气翻涌。雪原上没有别人。",
    breathy('Heavy breathing, the crunch of snow and a low steady wind.', '沉重的呼吸声、踩雪的嘎吱声和低低而持续的风声。'),
    cam=track('Su', '苏清月'),
    bg='Far behind her along the low ridge a line of white ice-encased human figures stand frozen mid-run, and a faint green aurora hangs in the black sky.',
    holds='The frame holds Su alone wading through the snowfield, the frozen trees and the ice-encased figures on the ridge.', room={'Su'}, new=True,
    st={'Su': ('三层羽绒服，背着登山包，戴着滑雪护目镜', '三层羽绒服，背着登山包，戴着滑雪护目镜')})

S.T('08-06', '06｜安全屋：外面是死亡的雪原，里面林峰在暖黄的灯光下装水泵', 9, WORK,
    [P('lin_home', 'center', "standing at the steel workbench in profile facing frame-right, tightening a bolt on a small water pump with a screwdriver in his right hand, his left hand wrapped in white gauze held against his chest", 'obj:the small water pump on the workbench in front of him', "his jaw relaxed, his lips set in a calm flat line, his brows soft")],
    'Medium shot, the figure from the head to the waist, in the middle third of the frame, at the workbench.',
    "<lin_home> turns the screwdriver slowly with his right hand to tighten a bolt on the small water pump, his eyes on the pump, his jaw relaxed and his brows soft, and gently wipes the pump housing with the towel around his neck, the tray of green seedlings glowing under the lamp beside him. Nobody else is in the hall.",
    "林峰用右手慢慢转动螺丝刀，拧紧小水泵上的一颗螺栓，眼睛看着水泵，下颌放松、眉毛舒展，然后用脖子上的毛巾轻轻擦了擦水泵的外壳，旁边的灯光下是那盘绿色的嫩芽。大厅里没有别人。",
    breathy('The soft clink of a screwdriver on metal, water lapping in the tub and the low hum of a generator.', '螺丝刀碰在金属上的轻轻叮当声、水盆里水轻轻荡漾的声音和发电机低低的嗡鸣。'),
    cam=push1('Lin and the pump', '林峰和水泵'),
    bg='Behind him towering stacks of steel crates, pallets of boxes, generators and big water tanks fill the hall under hard white work lamps.',
    holds='The frame holds Lin alone at the workbench and the stacked supplies behind him.', room={'Lin'}, new=True,
    st={'Lin': ('灰色棉质家居服，左手缠着白纱布', '灰色棉质家居服，左手缠着白纱布')})

S.T('08-07', '07｜坐标处：苏清月跪在雪地里什么都没有，直到发现树桩上有一小块在融雪的玻璃', 12, STUMP,
    [P('su_trek', 'right', "kneeling in the snow in profile facing frame-left with her gloved hands sunk in the snow in front of her, tears frozen on her cheeks", 'obj:the empty snowfield ahead and then the dead stump at center-left', "her lips cracked and trembling, her brows drawn tight")],
    'Medium-wide shot, the figure from the head to the knees at the right, with the snowfield and the stump in the middle third of the frame.',
    "<su_trek> kneels in the snow with her eyes on the empty snowfield, then murmurs one line to herself in a hoarse low voice, talking to nobody, her lips moving softly, her lips cracked and her brows drawn tight; her eyes drift to the dead stump where a thin patch of snow is melting around a small round glass, she murmurs a second short line, then a third, and crawls two paces toward the stump with one gloved hand stretching toward the glass. Nobody else is on the hillside.",
    "苏清月跪在雪里，眼睛看着空荡荡的雪地，然后用沙哑低沉的声音自言自语了一句，不是对任何人说的，嘴唇轻轻动着，嘴唇干裂、眉头紧蹙；她的目光移到那截枯树桩上——侧面一小块圆形的玻璃周围，一圈薄薄的雪正在融化，她又自言自语了一句很短的，接着又是一句，然后朝树桩爬了两步，一只戴手套的手伸向那块玻璃。山坡上没有别人。",
    voiced('A thin steady wind over the snow, her ragged breathing and her hoarse murmur.', '风吹过雪地细细而持续的声音、她粗重的喘息和她嘶哑的自语。'),
    vo=[('su_trek', "什么都没有……", 1.0, 'Su'), ('su_trek', "等等。", 5.0, 'Su'), ('su_trek', "那块玻璃，在融化。", 7.0, 'Su')], cam=push1('Su and the stump', '苏清月和树桩'),
    bg='At center-left the dead stump stands with a small round dark glass lens set in its side and a thin patch of snow melting around it, with the snow-capped boulder at frame-left.',
    holds='The frame holds Su alone on the snowy hillside, the stump with the glass lens and the snow-capped boulder.', room={'Su'}, new=True,
    st={'Su': ('三层羽绒服，背着登山包，护目镜推在额头上', '三层羽绒服，背着登山包，护目镜推在额头上')})

doc = S.finish()
