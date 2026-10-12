#!/usr/bin/env python3
"""剧本第 27–32 集（晚宴大厅一卷：次日清晨→联合晚宴→猎杀→Luna 觉醒→白狼王登场），合并稿编号 008（2026-10-12）。

写法版本：长镜头（8–10 秒）＋站位表自动生成（tools/_scene.py）＋“一个任务只放一件慢的持续的事”。
hh 10-12 11:57 看完第 25、26 集后，我自己的归纳（见 CLAUDE.md）：成功的是“只有一件慢的、持续的事”（说话、亲吻、被推近），
失败的全是“一个任务里塞 3–4 个快动作／机械动作”（打飞、推开、锁门、窗帘）。所以这批：
  · 一个任务一件事；快动作（泼酒反弹、吊灯坠落、扑刺、冲击波）各自单独成 5–6 秒任务，开场图从起手姿势画起，任务里不再塞别的；
  · 前后因果在任务边界切开（拳头收紧放到下一个任务开头，对应 31-05 的 trigger → 32-01 的 effect）；
  · 每个任务的“看着谁／在场的人／状态”由站位表程序检查；
  · 偏离剧本的地方写在下面，hh 可否决。

故事填实（剧本第 27–32 集是大纲，补的地方）：
  第 27 集 ① 第 26 集黑屏之后的“第二天早晨”：会议桌、散落的文件和碎布，他侧躺撑着头，莉莉睡在他胸口，盖着他的外套，锁骨上多了一个发光的银色印记（推近到印记）。
         ② 她醒来想坐起来、腰酸得发软，捶他骂“昨晚你简直疯了”，他笑着亲她的指节：“怪你自己太好吃”（亲密但不露骨）。
         ③ 他把她打横抱起走出会议室，镜头跟着他们离开，只剩空桌（交代“他们离开了”，也给窃听器让出画面）。
         ④ 空桌下一个硬币大的黑色窃听器闪着红光（无人镜头，观众先看到阴谋的工具）。
         ⑤ 地下室里赛琳娜坐轮椅（两腿打着石膏＝第 25 集被他打到墙上的后果），摘下耳机，对她父亲说“今晚我要她死”，大长老答“在宴会上，当着所有人”。
         （剧本里赛琳娜独自一人，我加了她父亲在场，让“今晚我要她死”有对象，也为下一集大长老当众羞辱莉莉埋伏笔。）
  第 28 集 ① 全场死寂：他挽着盛装的莉莉沿红地毯走来，宾客们转头看着（横向跟拍）。
         ② 大长老端着酒杯拦住：“你把这个人类玩具带来了？”“你让所有的狼丢脸！”
         ③ 赛琳娜手腕一翻，红酒泼向莉莉的裙子——他抬手、酒停在半空、弹回去，泼了赛琳娜一脸（剧本是泼了大长老和赛琳娜两个人，
           我只让赛琳娜挨泼：画面里同时有大长老会变成 4 个有名字的人）。
         ④ 他用手帕擦她根本没沾上酒的指尖，抬眼问大长老：“你刚才说谁是玩具？”（先动作后台词，台词在后半任务）。
  第 29 集 ① 大长老捏碎酒杯、瞳孔变黄：“你要为她跟整个元老院开战？我们家控制欧洲 40%！”（原台词压成两句）。
         ② 他回一句“欧洲的 40%？可爱。”打个响指，阿贾克斯递上平板，他把屏幕举到老人面前：“十分钟前我已经让你们破产了。”（镜头推近到平板和老人的脸）。
         ③ 老人看着屏幕心脏病发作，捂着胸口跪下倒地，赛琳娜（浑身红酒）尖叫。
         ④ 其余元老一个个低头，老人被两个保镖拖走，赛琳娜被推着轮椅跟走（宽景，镜头慢慢拉远到整个大厅都低着头）。
         ⑤ 莉莉闻到腐肉似的血腥味，抬头看见通风口渗出黑雾：“有东西从通风口进来了！”（剧本是“有危险”，补上能被看见的东西）。
  第 30 集 ① 水晶吊灯坠落砸在大厅中央（宾客尖叫后退，两人在左边楼梯脚下）。
         ② 烟尘里，变异的保罗站在碎水晶中间（头顶是被撕开的通风口＝他从哪儿来），握着银匕首，对莉莉说“你夺走了一切，所以你去死”。
           （剧本写他“浑身脓包”，改成“灰色的、被毒液侵蚀的、有黑色血管的脸”，不画脓包。）
         ③ 保罗举刀扑向莉莉，基利安把她拉到身后，银刃插进他的左胸（单独一个 5 秒任务，只放这一件事）。
         ④ 他单膝跪下，黑血染透白衬衫，保罗仍握着刀柄，莉莉尖叫他的名字（保罗留在画面里，下一集他才拔刀）。
  第 31 集 ① 保罗拔出匕首，举过他的头顶，基利安吐出黑血（银毒压住他的自愈），“再见，Alpha”。
         ② 莉莉站起来，眼睛爆发银光、头发飘起（保罗的刀僵在半空，惊恐地看着她）。（推近到银色的眼睛）
         ③ 刀落下的瞬间她抬手，银色冲击波把保罗轰飞到大厅另一头的墙上（广角，把整条路径放进画面）。
         ④ 保罗嵌在裂开的墙里，宾客全部趴在地上，莉莉一步步走过去。
         ⑤ 她对他说“没人能动我的男人还活着”，抬起手、手指弯成抓握（拳头收紧留给下一集）。
  第 32 集 ① 她的拳头一收紧，保罗的惨叫戛然而止，银光熄灭，他软软滑落（不拍“化成肉泥”）；基利安在左边慢慢站起来。
         ② 莉莉脱力往后倒，他接住她——伤口已经愈合：“这点毒杀不了我，小妻子。”“我只是想看你为我发火的样子。”
         ③ 他抱着她转身，面对满厅趴着的宾客，金眼与银眼（镜头拉远到全厅）。
         ④ 冰雪狂风吹过敞开的高窗，白色西装、银色长发的卢修斯踩着冰霜走进来：“把 Luna 交出来，不然你们死。”
偏离剧本：不拍“吊灯砸在人群里”（砸在空地上，宾客只是惊叫后退）；保罗不画脓包；“化成肉泥”改成“软软滑落”；
  所有“一瞬间”的集体动作（宾客趴下）直接给结果状态；不拍“几万狼人”（后面集再说）。
左右方向（晚宴大厅，全场固定）：红地毯从画面左到右，楼梯和入口在画面左，长宴会桌在画面右；
  大长老／赛琳娜一律在基利安的左边，莉莉一律在基利安的右边；保罗从画面左边来（所以他和莉莉之间隔着基利安，刀刺进基利安面向左的这一侧＝左胸）；
  保罗被轰飞、嵌进的墙在画面最左；基利安跪在画面右；卢修斯从后墙偏左的高窗进来；窗在后墙。
"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _scene import *

BASE = '合并稿/006_第25-26集_致命催化剂到办公桌上的臣服_制作稿_追加.json'
OUT = '合并稿/008_第27-32集_次日清晨到白狼王登场_制作稿_追加'
S = Session(BASE, OUT, 12000)

# ---------------------------------------------------------------------------------------------- 外貌（人物素材键 → 开场图里的描写）
look('killian', 'Killian', "in the tailored black three-piece suit, white shirt and dark tie", 'cold dark-gray', 'his')
look('killian_shirt', 'KillianShirt', "in only a white dress shirt open at the collar with the sleeves rolled up, a dark tie hanging loose", 'cold dark-gray', 'his')
look('killian_gold', 'KillianGold', "in the tailored black three-piece suit, white shirt and dark tie, long black claws at his fingertips", 'burning gold', 'his')
look('killian_wounded', 'KillianWounded', "in the black suit with the jacket hanging open over a white shirt torn at the left chest and soaked with spreading black blood", 'cold dark-gray', 'his')
look('lily_morning', 'LilyMorning', "in an oversized white men's shirt torn at one shoulder with a black suit jacket draped over her shoulders, her chestnut hair tangled and loose", 'hazel-green', 'her')
look('lily_gown', 'LilyGown', "in the floor-length silver star-sequined evening gown with a plunging back, the large pink diamond necklace at her throat, her chestnut hair pinned in an elegant low updo", 'hazel-green', 'her')
look('lily_gown_silver', 'LilyGownSilver', "in the floor-length silver star-sequined evening gown with the large pink diamond necklace at her throat, her long chestnut hair loose and lifting", 'luminous silver-white', 'her')
look('selena_chair', 'SelenaChair', "seated in a sleek black wheelchair with both legs in thick white plaster casts on the footrests, with sleek copper-red hair in a high ponytail, in the fitted deep-burgundy dress with the silver wolf-head brooch", 'amber', 'her')
look('elder', 'Elder', "in the black three-piece suit with the silver wolf-head lapel pin and a dark grey tie, his white hair swept back", 'cold pale', 'his')
look('elder_wolf', 'ElderWolf', "in the black three-piece suit with the silver wolf-head lapel pin and a dark grey tie, his white hair swept back, fangs showing", 'burning yellow', 'his')
look('ajax', 'Ajax', "in a sharp charcoal suit with a clear coiled earpiece, his short dark hair neatly combed", 'steady dark-brown', 'his')
look('paul_mutant', 'PaulMutant', "gaunt and hunched in a torn dirty shirt, his grey scarred skin crossed by dark spreading veins, a slim silver dagger gripped in his right fist", 'milky grey', 'his')
look('lucius', 'Lucius', "with long straight silver hair, in a pure white tailored suit with a white fur-trimmed collar and frost on his shoulders", 'icy-blue', 'his')

# ---------------------------------------------------------------------------------------------- 场景（固定布局句每个任务都带）
LAY_CR = " Fixed stage layout: the long polished dark-wood table runs across the room from frame-left to frame-right; the tall carved high-backed chair at the head of the table is at frame-left; the row of leather chairs lines the far side of the table; the tall dark double doors with brass handles are at frame-right; tall windows with dark drapes are at the back."
CR_MORNING = Scene('council_room', " Warm gold morning sunlight slants through the gaps in the heavy drapes across the polished table, the paneled room softly blurred behind.", LAY_CR)
LAY_GH = " Fixed stage layout: the polished cream marble floor with a wide dark-red carpet runs across the hall from frame-left to frame-right; the wide marble staircase rises at frame-left beside the tall double entrance doors; the long banquet table with white linen and champagne towers stands along frame-right; the huge crystal chandeliers hang above the middle of the hall; gold-trimmed columns and tall arched windows with gold drapes line the back wall."
GH = Scene('gala_hall', " Warm golden chandelier light, the grand hall softly blurred behind.", LAY_GH)
LAY_BS = " Fixed stage layout: the steel table with the laptop, the bank of small monitors and the black speaker box is at frame-left; the single bare bulb hangs in the middle of the room; the heavy steel door is at frame-right."
BS = Scene('basement_room', " A single bare bulb throws harsh shadows, the damp concrete room softly blurred behind.", LAY_BS)

# ---------------------------------------------------------------------------------------------- 第 27 集
b27 = S.episode('剧本第27集｜王座上的印记', '次日清晨，会议桌上，他侧躺撑着头，指尖抚过她锁骨上发光的银色印记；她醒来捶他骂他疯子，他笑着亲她的手；他抱着她走出会议室。空桌下一个窃听器闪着红光。地下室里，坐轮椅的赛琳娜对她父亲说：今晚我要她死。', 27)
V = S.src['characters']
def voice(name): return V[name]['voice_description']['en'], V[name]['voice_description']['zh']
# --- 新素材（加在第一个 Batch 上，最终文档会合并）
b27.person('lily_morning', '莉莉（晨起，披着他的黑西装外套，锁骨上有银色印记）',
           'Lily, the same adult woman in her mid-twenties as in the reference, with long wavy chestnut-brown hair tangled and loose, large hazel-green eyes, fair skin with a soft flush, wearing an oversized white men\'s cotton dress shirt torn at one shoulder with a black suit jacket draped over her shoulders, and a small silver wolf-shaped mark glowing softly on her left collarbone. The portrait fixes her identity and clothes, not staging.',
           '莉莉，和参考图里同一位二十五岁左右的成年女人，栗色长卷发凌乱松散，榛绿色的大眼睛，皮肤白皙带着淡淡的红晕；穿一件肩头撕破的肥大白色男式棉衬衫，肩上披着一件黑色男式西装外套，左边锁骨上有一个小小的、发着柔光的银色狼形印记。肖像固定她的长相和衣着，不固定姿势。',
           "A photorealistic half-body portrait of the same woman as in the reference image, long wavy chestnut-brown hair tangled and loose, large hazel-green eyes, fair skin with a soft flush, wearing an oversized white men's cotton dress shirt torn at one shoulder with a black suit jacket draped over her shoulders, a small silver wolf-shaped mark glowing softly on her left collarbone. She faces the camera with a drowsy, soft expression. Soft even studio light, plain neutral gray background, natural skin texture with visible pores.", ref='lily')
b27.person('lily_gown', '莉莉（银色星光晚礼服，粉钻项链）',
           'Lily, the same adult woman in her mid-twenties as in the reference, large hazel-green eyes, wearing a floor-length silver star-sequined evening gown with thin straps and a plunging back, a large pink diamond pendant necklace at her throat, her chestnut hair pinned in an elegant low updo. The portrait fixes her identity and clothes, not staging.',
           '莉莉，和参考图里同一位二十五岁左右的成年女人，榛绿色的大眼睛，穿一件及地的银色星光亮片晚礼服，细肩带、后背露得很低，脖子上戴着一颗很大的粉钻吊坠项链，栗色头发盘成优雅的低发髻。肖像固定她的长相和衣着，不固定姿势。',
           "A photorealistic half-body portrait of the same woman as in the reference image, large hazel-green eyes, wearing a floor-length silver star-sequined evening gown with thin straps and a plunging back, a large pink diamond pendant necklace at her throat, her chestnut hair pinned in an elegant low updo. She faces the camera with a composed, regal expression. Soft even studio light, plain neutral gray background, natural skin texture with visible pores.", ref='lily')
b27.person('lily_gown_silver', '莉莉（银色晚礼服，银白色的眼睛，头发飘起）',
           'Lily, the same adult woman in her mid-twenties as in the reference, wearing the floor-length silver star-sequined evening gown with the large pink diamond pendant necklace, her long chestnut hair loose and lifting as if in a wind; her eyes glow a luminous silver-white. The portrait fixes her identity, clothes and eye color, not staging.',
           '莉莉，和参考图里同一位二十五岁左右的成年女人，穿及地的银色星光亮片晚礼服，戴着大粉钻吊坠项链，栗色长发松开、像被风吹着飘起来；眼睛发出明亮的银白色光。肖像固定她的长相、衣着和眼睛颜色，不固定姿势。',
           "A photorealistic half-body portrait of the same woman as in the reference image, wearing a floor-length silver star-sequined evening gown with a large pink diamond pendant necklace, her long chestnut hair loose and lifting as if in a wind, her eyes glowing a luminous silver-white. She faces the camera with a fierce, calm expression. Soft even studio light, plain neutral gray background, natural skin texture with visible pores.", ref='lily')
b27.person('selena_chair', '赛琳娜（坐轮椅，双腿打着石膏）',
           'Selena, the same elegant adult woman in her late twenties as in the reference, with sleek copper-red hair in a high ponytail and sharp amber eyes, seated in a sleek black wheelchair with both legs in thick white plaster casts resting on the footrests, wearing the fitted deep-burgundy high-neck dress with the small silver wolf-head brooch. The portrait fixes her identity, clothes and wheelchair, not staging.',
           '赛琳娜，和参考图里同一位二十八岁左右、优雅的成年女人，铜红色高马尾，琥珀色的锐利眼睛，坐在一张光滑的黑色轮椅上，两条腿打着厚厚的白色石膏、放在脚踏板上，穿着合身的深酒红色高领连衣裙，领口别着小小的银色狼头胸针。肖像固定她的长相、衣着和轮椅，不固定姿势。',
           'A photorealistic full-body portrait of the same woman as in the reference image, sleek copper-red hair in a high ponytail, sharp amber eyes, seated in a sleek black wheelchair with both legs in thick white plaster casts resting on the footrests, wearing a fitted deep-burgundy high-neck dress with a small silver wolf-head brooch at the collar. She faces the camera with a bitter, haughty expression. Soft even studio light, plain neutral gray background, natural skin texture with visible pores.', ref='selena')
b27.person('elder_wolf', '大长老（暴怒，眼睛变成黄色）',
           'Elder, the same old man in his sixties as in the reference, with swept-back white hair, a deeply lined face and a thin cruel mouth, wearing the black three-piece suit with the silver wolf-head lapel pin and dark grey tie; his eyes glow a burning yellow with narrow wolf pupils and his canine teeth are bared in rage. The portrait fixes his identity, clothes and features, not staging.',
           '大长老，和参考图里同一位六十多岁的老年男人，白发向后梳，脸上皱纹很深，嘴唇薄而冷酷，穿黑色三件套西装、翻领上别着银色狼头胸针、深灰色领带；眼睛发出燃烧般的黄色、瞳孔收成狼一样的细线，犬齿因暴怒而龇出来。肖像固定他的长相、衣着和特征，不固定姿势。',
           'A photorealistic half-body portrait of the same old man as in the reference image, swept-back white hair, deeply lined face, wearing a black three-piece suit with a silver wolf-head lapel pin and a dark grey tie, his eyes glowing a burning yellow with narrow wolf pupils, his canine teeth bared. He faces the camera with a furious, snarling expression. Soft even studio light, plain neutral gray background, natural skin texture with visible pores.', ref='elder')
b27.person('ajax', '阿贾克斯（基利安的特助）',
           'Ajax, a tall, broad-shouldered adult man in his late thirties with short neatly combed dark hair, steady dark-brown eyes and a square jaw, wearing a sharp charcoal suit, a white shirt, a black tie and a clear coiled earpiece. The portrait fixes his identity and clothes, not staging.',
           '阿贾克斯，三十八岁左右、身材高大、肩膀宽阔的成年男人，黑色短发梳得整整齐齐，深褐色的眼睛沉稳，下巴方正，穿一套剪裁利落的炭灰色西装、白衬衫、黑领带，戴着一只透明的卷线耳机。肖像固定他的长相和衣着，不固定姿势。',
           'A photorealistic half-body portrait of a tall, broad-shouldered adult man in his late thirties with short neatly combed dark hair, steady dark-brown eyes and a square jaw, wearing a sharp charcoal suit, a white shirt, a black tie and a clear coiled earpiece. He faces the camera with a calm, disciplined expression. Soft even studio light, plain neutral gray background, natural skin texture with visible pores.')
b27.person('killian_wounded', '基利安（西装敞开，左胸撕破沾着黑血）',
           'Killian, the same very tall, broad-shouldered adult man in his early thirties as in the reference, with short swept-back black hair, a sharp jawline and light stubble, wearing a black suit with the jacket hanging open over a white shirt torn at the left chest and soaked with spreading black blood, a platinum luxury wristwatch on his left wrist. The portrait fixes his identity and clothes, not staging.',
           '基利安，和参考图是同一个三十出头、身材极高、肩膀宽阔的成年男性，黑色短发向后梳，下颌线锋利，有浅胡茬，穿着敞开外套的黑色西装，里面的白衬衫左胸被撕破、浸满了不断扩大的黑色血迹，左手腕戴铂金名表。肖像固定他的长相和衣着，不固定姿势。',
           'A photorealistic half-body portrait of the same man as in the reference image, short swept-back black hair, sharp jawline, light stubble, cold dark-gray eyes, wearing a black suit with the jacket hanging open over a white shirt torn at the left chest and soaked with spreading black blood, a platinum luxury wristwatch on his left wrist. He faces the camera with a pained, clenched expression. Soft even studio light, plain neutral gray background, natural skin texture with visible pores.', ref='killian')
b27.person('paul_mutant', '保罗（被毒液侵蚀，灰白的皮肤和黑色血管）',
           'Paul, the same man in his late twenties as in the reference but gaunt and ravaged: sunken cheeks, pale grey scarred skin crossed by dark spreading veins and milky grey eyes, wearing a torn dirty shirt, a slim silver dagger gripped in his right hand. The portrait fixes his identity and features, not staging.',
           '保罗，和参考图是同一个二十八岁左右的男人，但已经形销骨立：脸颊凹陷，灰白色的皮肤上布满伤疤和不断蔓延的黑色血管，眼睛是浑浊的乳灰色；穿着撕破的脏衬衫，右手握着一把细长的银匕首。肖像固定他的长相和特征，不固定姿势。',
           'A photorealistic half-body portrait of the same man as in the reference image but gaunt and ravaged, sunken cheeks, pale grey scarred skin crossed by dark spreading veins, milky grey eyes, wearing a torn dirty shirt, a slim silver dagger gripped in his right hand. He faces the camera with a feral, vacant expression. Soft even studio light, plain neutral gray background, natural skin texture with visible pores.', ref='paul')
b27.person('lucius', '卢修斯（北方白狼王）',
           'Lucius, a strikingly handsome adult man in his early thirties with long straight silver hair, pale flawless skin and icy-blue eyes, wearing a pure white tailored suit with a white fur-trimmed collar, frost glittering on his shoulders. The portrait fixes his identity and clothes, not staging.',
           '卢修斯，三十出头、英俊得夺目的成年男人，银色长直发，皮肤苍白无瑕，眼睛是冰蓝色，穿一套纯白色剪裁合身的西装、领口镶着白色毛边，肩上落着闪光的霜。肖像固定他的长相和衣着，不固定姿势。',
           'A photorealistic half-body portrait of a strikingly handsome adult man in his early thirties with long straight silver hair, pale flawless skin and icy-blue eyes, wearing a pure white tailored suit with a white fur-trimmed collar, frost glittering on his shoulders. He faces the camera with a cold, contemptuous expression. Soft even studio light, plain neutral gray background, natural skin texture with visible pores.')
b27.scene('gala_hall', '联合晚宴大厅（红地毯横向，楼梯在左）',
          'A grand gala ballroom: a polished cream marble floor with a wide dark-red carpet running across the hall from left to right, a wide marble staircase rising at the left beside tall double entrance doors, a long banquet table with white linen and champagne towers along the right, gold-trimmed columns and tall arched windows with gold drapes along the back wall, huge crystal chandeliers hanging above the middle, warm golden light. The reference fixes the layout and decor.',
          '盛大的晚宴大厅：抛光的奶油色大理石地面，一条宽阔的深红色地毯从左到右横过大厅，左边是宽阔的大理石楼梯和高大的双开入口门，右边沿墙是铺着白桌布、摆着香槟塔的长长宴会桌，后墙是镶金边的柱子和带金色窗帘的高大拱窗，大厅中间上方挂着巨大的水晶吊灯，温暖的金色灯光。参考图固定布局与陈设。',
          'A photorealistic ultra-wide 8:3 cinemascope shot of a grand gala ballroom seen straight on: a polished cream marble floor with a wide dark-red carpet running across the hall from left to right, a wide marble staircase rising at the left beside tall double entrance doors, a long banquet table with white linen and champagne towers along the right, gold-trimmed columns and tall arched windows with gold drapes along the back wall, huge crystal chandeliers hanging above the middle, warm golden light, nobody in the hall. The frame holds the staircase, the carpet, the columns, the windows, the chandeliers and the banquet table.')
b27.scene('basement_room', '地下室（监听室）',
          'A small dark concrete basement room: bare grey concrete walls, a steel table at the left holding a laptop, a bank of small monitors and a black speaker box, a single bare bulb hanging from the ceiling, a heavy steel door at the right, damp stains on the walls. The reference fixes the layout and decor.',
          '一间昏暗狭小的混凝土地下室：光秃秃的灰色混凝土墙，左边是一张钢桌，上面放着笔记本电脑、一排小显示器和一个黑色音箱，天花板上吊着一只裸灯泡，右边是一扇厚重的钢门，墙上有潮湿的水渍。参考图固定布局与陈设。',
          'A photorealistic ultra-wide 8:3 cinemascope shot of a small dark concrete basement room: bare grey concrete walls, a steel table at the left holding a laptop, a bank of small monitors and a black speaker box, a single bare bulb hanging from the ceiling, a heavy steel door at the right, damp stains on the walls, nobody in the room. The frame holds the steel table, the monitors, the bulb and the steel door.')
for name, key, base in [('LilyMorning', 'lily_morning', 'LilyShirt'), ('LilyGown', 'lily_gown', 'LilyRed'), ('LilyGownSilver', 'lily_gown_silver', 'LilySilver'),
                        ('SelenaChair', 'selena_chair', 'Selena'), ('KillianWounded', 'killian_wounded', 'Killian')]:
    b27.character(name, key, *voice(base))
b27.character('ElderWolf', 'elder_wolf', 'A mature old male voice, hoarse and roaring with rage, cracking at the top, speaking clear American English. Every word is fully voiced and audible.',
              '年老的男声，因暴怒而沙哑咆哮、在高处破音，说清楚的美式英语。每个字都正常发声、清晰可辨。')
b27.character('Ajax', 'ajax', 'A mature adult male voice, calm, flat and disciplined, speaking clear American English. Every word is fully voiced and audible.',
              '成熟成年男声，冷静、平稳、训练有素，说清楚的美式英语。每个字都正常发声、清晰可辨。')
b27.character('PaulMutant', 'paul_mutant', 'A rough adult male voice, wet, rasping and broken like an animal forcing out words, speaking clear American English, slurred but understandable. Every word is fully voiced and audible.',
              '粗哑的成年男声，湿漉漉、嘶哑、破碎，像野兽硬挤出字句，说清楚的美式英语，含混但听得懂。每个字都正常发声、清晰可辨。')
b27.character('Lucius', 'lucius', 'A cold adult male voice, smooth, silky and unhurried with an icy, contemptuous edge, speaking clear American English. Every word is fully voiced and audible.',
              '冰冷的成年男声，顺滑、柔软、不急不慢，带冰一样的轻蔑，说清楚的美式英语。每个字都正常发声、清晰可辨。')

KS_SHIRT = '白衬衫，没受伤'
LM = '白衬衫披着他的黑外套，锁骨有银印'

S.T('27-01', '01｜清晨，他撑着头看她，指尖抚过她锁骨上发光的银色印记', 10, CR_MORNING,
    [P('killian_shirt', 'left', 'lying on his side on the long polished table, propped up on his left elbow, his right hand resting on Lily\'s collarbone', 'Lily', 'his lips soft and slightly parted, his brows relaxed'),
     P('lily_morning', 'right', 'lying on the table with her head against his chest', 'closed', 'her lips softly parted, her brows smooth', extra='a small silver wolf-shaped mark glowing on her left collarbone')],
    'Close side-on two-shot, both people from the head to the chest, in the middle third of the frame, on the long polished council table in the morning light, torn silk and scattered papers around them.',
    '<killian_shirt> strokes one fingertip slowly along <lily_morning>\'s collarbone, his cold dark-gray eyes on her sleeping face, his lips soft and his brows relaxed; the small silver wolf mark under his fingertip glows a little brighter. <lily_morning> sleeps against his chest, her eyes closed, her lips softly parted and her brows smooth, her breathing slow and even. The camera pushes in until the glowing silver mark fills the frame.',
    '清晨，会议桌上，他侧躺撑着头，右手指尖慢慢抚过她锁骨上发光的银色狼形印记，看着熟睡的她；她靠在他胸口睡着，呼吸平缓。镜头推近，直到发光的银色印记占满画面。',
    breathy('Soft slow breathing, the faint whisper of fabric and a gentle airy shimmer of sound.', '轻柔缓慢的呼吸声、衣料轻微的摩擦声和一点轻轻的、空灵的闪光声。'),
    cam=('The camera pushes in until the glowing silver mark fills the frame.', '镜头推近，直到发光的银色印记占满画面。'),
    room={'Killian', 'Lily'}, new=True, st={'Killian': (KS_SHIRT, KS_SHIRT), 'Lily': (LM, LM)})

# ---------------------------------------------------------------------------------------------- 状态用词（站位表比对字符串，前后必须逐字相同）
from _h3draft import silent
CR_UNDER = Scene('council_room', " Dim warm light under the polished table, the empty paneled room softly blurred in the distance.", '')
GH_UP = Scene('gala_hall', " Warm golden light from below, the grand hall softly visible beyond.", '')
A_T = '炭灰西装，戴耳机'
K_T = '黑色三件套，没受伤'
K_TAB = '黑色三件套，手里拿着平板'
K_STAB = '黑色三件套，左胸插着银匕首'
K_KNEEL = '单膝跪地，左胸浸满黑血'
K_UP = '站起来，左胸浸满黑血'
L_G = '银色礼服，粉钻项链，盘发'
L_AW = '银色礼服，银眼，头发飘起'
E_T = '黑色三件套，手里端着酒杯'
E_DOWN = '倒在地上，昏过去'
E_CRUSH = '酒杯捏碎，黄眼獠牙'
S_DRY = '轮椅，石膏腿，酒红裙，干净'
S_WET = '轮椅，石膏腿，酒红裙，浑身红酒'
P_STAND = '握着银匕首，站着'
P_STAB = '匕首扎在基利安左胸'
P_FREE = '匕首拔出，握在手里'
P_UP = '双手举着匕首'
P_WALL = '嵌在裂开的墙里'
P_SLUMP = '软软滑落在墙根'
ROOM_GH = {'Killian', 'Lily', 'Elder', 'Selena', 'Ajax', 'Guests', 'Elders'}

# ============================================================================================== 第 27 集（续）
S.T('27-02', '02｜她醒来捶他：你昨晚简直疯了；他亲她的指节：怪你太好吃', 10, CR_MORNING,
    [P('killian_shirt', 'left', "lying on his side on the long polished table, propped up on his left elbow, holding Lily's right hand against his lips", 'Lily', 'the corner of his mouth lifted in warm amusement, his brows relaxed'),
     P('lily_morning', 'right', "half sitting up on the table, her left hand pressed flat against his chest, her torn white shirt slipping off one shoulder under the black jacket", 'Killian', 'her cheeks flushed red, her lips pressed tight, her brows drawn together in mock fury')],
    'Close side-on two-shot, both people from the head to the chest, in the middle third of the frame, on the long polished council table in the morning light, scattered papers around them.',
    "<lily_morning> has just woken and tries to push herself up, then wobbles and gives up; she thumps her fist once against <killian_shirt>'s chest and speaks the first line to <killian_shirt>, her cheeks burning red and her brows drawn together. He catches her fist in his hand and presses a kiss to her knuckles, the corner of his mouth lifted in warm amusement, his eyes on her face, and speaks the second line to <lily_morning> in a low, lazy voice. She looks away for a moment, her flush deepening, then back at him, her lips twitching.",
    "她刚醒，想撑起来又腰酸得软了回去；一拳轻轻捶在他胸口，涨红着脸、皱着眉对他说第一句；他一把握住她的拳头，在她指节上亲了一下，嘴角带着笑意看着她，用低低懒懒的声音对她说第二句；她红着脸移开视线，又转回来看他，嘴角忍不住抽动。",
    voiced('Soft rustling of fabric, a muffled thump of a fist against a chest, a low lazy chuckle.', '衣料轻轻的摩擦声、一拳轻捶在胸口的闷响、一声低低懒懒的轻笑。'),
    lines=[('lily_morning', "You were completely insane last night!", 1.0, 'Killian'), ('killian_shirt', "Blame yourself for being delicious.", 5.0, 'Lily')],
    st={'Killian': (KS_SHIRT, KS_SHIRT), 'Lily': (LM, LM)})

S.T('27-03', '03｜他把她打横抱起，走向双开门', 8, CR_MORNING,
    [P('killian_shirt', 'left', "standing at the head of the long polished table carrying Lily across his arms, one arm under her knees and one under her back", 'Lily', 'the corner of his mouth lifted, his brows relaxed'),
     P('lily_morning', 'center', "held across his arms with her arms wrapped around his neck and her bare feet dangling, the black jacket draped over her", 'Killian', 'her cheeks flushed, her lips softly parted, her brows smooth')],
    'Medium side-on shot, both people from the head to the knees, in the middle third of the frame, in the morning-lit council room, scattered papers and torn silk on the long table beside them.',
    "<killian_shirt> carries <lily_morning> across the room at an easy, unhurried walk toward the tall dark double doors at frame-right, his eyes on her face and the corner of his mouth lifted; <lily_morning> rests her head against his shoulder, her arms around his neck, her eyes on his face, her lips softly parted and her brows smooth. Behind them the long table with its scattered papers slides away to the left. By the end they reach the double doors.",
    "他抱着她，不慌不忙地走向画面右边的双开门，眼睛看着她的脸，嘴角带着笑意；她的头靠在他肩上，双臂环着他的脖子，眼睛看着他，嘴唇微张，眉头舒展。身后摊着文件的长桌慢慢向左滑走。最后他们走到双开门边。",
    breathy('Slow footsteps on the carpet, the soft rustle of fabric, quiet slow breathing.', '缓慢的脚步声踩在地毯上、衣料轻轻的摩擦声、安静缓慢的呼吸声。'),
    cam=('The camera tracks sideways to the right, following them toward the double doors.', '镜头横向向右跟拍，跟着他们走向双开门。'),
    exit={'Killian', 'Lily'}, st={'Killian': (KS_SHIRT, KS_SHIRT), 'Lily': (LM, LM)})

S.T('27-04', '04｜空桌下，一个硬币大的黑色窃听器闪着红光', 6, CR_UNDER, [],
    'Extreme close low-angle shot of the underside of the long polished dark-wood council table, the small device in the middle third of the frame, nobody in the frame.',
    "A coin-sized black listening device is taped under the table edge, a tiny red light blinking on it in a slow steady rhythm; a torn scrap of silk hangs from the table edge above it and sways slightly. The camera pushes in slowly until the blinking red light fills the frame.",
    "桌子下面，一个硬币大的黑色窃听器贴在桌沿下，一个小小的红灯有节奏地慢慢闪烁；上面垂着一小片撕碎的真丝，轻轻晃动。镜头慢慢推近，直到闪烁的红灯占满画面。",
    silent('A faint electronic hum and a tiny steady beep.', '轻微的电子嗡鸣声和一下一下很小的哔哔声。'),
    cam=('The camera pushes in slowly until the blinking red light fills the frame.', '镜头慢慢推近，直到闪烁的红灯占满画面。'),
    holds='The frame holds no people, only the underside of the table and the small black device.')

S.T('27-05', '05｜地下室，坐轮椅的赛琳娜摘下耳机：今晚我要她死', 10, BS,
    [P('selena_chair', 'left', "seated in the wheelchair at the steel table with large black headphones pulled down around her neck, one hand resting on the closed laptop", 'Elder', 'her lips curled in a cold hateful sneer, her brows low'),
     P('elder', 'right', "standing beside the wheelchair with his hands clasped behind his back", 'Selena', 'his thin lips pressed flat, his brows level')],
    'Medium two-shot, both people from the head to the knees, in the middle third of the frame, in the damp concrete basement under a single bare bulb.',
    "<selena_chair> pulls the headphones off her neck and sets them on the table, then speaks the first line to <elder> in a low venomous voice, her amber eyes on his face and her lips curled in a sneer. <elder> listens without moving, his eyes on her face, his thin lips pressed flat, and answers her with the second line to <selena_chair> in a cold, even voice, giving one slow nod.",
    "赛琳娜把脖子上的耳机摘下来放在桌上，然后用低低的、带毒的声音对大长老说出第一句，琥珀色的眼睛盯着他，嘴角冷笑；大长老一动不动地听着，眼睛看着她，薄嘴唇抿成一条线，用冷冷平稳的声音对她回答第二句，慢慢点了一下头。",
    voiced('A faint electronic hiss from the speaker box, a bare bulb humming, the soft click of headphones set on steel.', '音箱里轻微的电子嘶嘶声、裸灯泡的嗡嗡声、耳机放在钢桌上的轻轻一声。'),
    lines=[('selena_chair', "Tonight, I want her dead.", 1.0, 'Elder'), ('elder', "At the banquet, before everyone.", 5.0, 'Selena')],
    room={'Selena', 'Elder'}, new=True, st={'Selena': (S_DRY, S_DRY), 'Elder': (E_T, E_T)})

# ============================================================================================== 第 28 集
b28 = S.episode('剧本第28集｜顶级晚宴的交锋', '联合晚宴大厅，全场死寂。他挽着盛装的莉莉沿红地毯走来；大长老拦住他们，骂莉莉是人类玩具；赛琳娜把红酒泼向莉莉的裙子，酒在半空停住，反弹回去泼了她自己一脸；他用手帕擦莉莉根本没沾上酒的指尖，问大长老：你刚才说谁是玩具？', 28)
S.T('28-01', '01｜全场死寂，他挽着盛装的莉莉沿红地毯走来', 8, GH,
    [P('killian', 'left', "walking in profile toward frame-right along the dark-red carpet, his right arm bent to hold Lily's hand on his forearm", 'obj:the far end of the red carpet at frame-right', 'his jaw set, his lips pressed flat'),
     P('lily_gown', 'right', "walking in profile beside him toward frame-right, her left hand resting on his right forearm and the silver gown trailing behind her", 'obj:the far end of the red carpet at frame-right', 'her chin lifted, her lips closed, her brows level', verb='on')],
    'Wide side-on shot, both people from the head to the feet, in the middle third of the frame, on the wide dark-red carpet across the grand gala hall.',
    "<killian> and <lily_gown> walk slowly side by side along the carpet toward frame-right with measured, unhurried steps, the silver gown rippling at her ankles. Along both sides of the carpet the guests in evening gowns and tuxedos stand frozen with their champagne flutes, and their heads turn one by one to follow the couple, their mouths slightly open, a hush spreading through the hall.",
    "他们并肩沿红地毯向画面右边慢慢走，步子不急不缓，银色的裙摆在她脚边起伏。地毯两侧的宾客穿着晚礼服和燕尾服，端着香槟杯僵在原地，一个接一个地转头跟着这对伴侣，嘴巴微张，整个大厅一片死寂。",
    breathy('Slow footsteps on marble, a hush spreading through the hall, glasses clinking faintly.', '缓慢的脚步声踩在大理石上、大厅里一片寂静慢慢扩散、酒杯轻轻碰响。'),
    cam=('The camera tracks sideways to the right, following the couple along the carpet.', '镜头横向向右跟拍，跟着这对伴侣沿着地毯走。'),
    bg="Along both sides of the carpet, well-dressed guests in evening gowns and tuxedos stand frozen with their champagne flutes, clearly visible and in sharp focus, every head turned toward the couple.",
    groups=[('Guests', '后', 'Killian')], room=ROOM_GH, new=True,
    st={'Killian': (K_T, K_T), 'Lily': (L_G, L_G)})

S.T('28-02', '02｜大长老端着酒杯拦住他们：你把这个人类玩具带来了？', 10, GH,
    [P('elder', 'left', "standing close in profile facing frame-right, a champagne glass in his right hand", 'Killian', 'his thin lips curled in disdain, his brows low'),
     P('killian', 'center', "standing in profile facing frame-left, his jaw set", 'Elder', 'his lips pressed flat, his brows level'),
     P('lily_gown', 'right', "standing at his right side in profile facing frame-left, her left hand resting on his right forearm", 'Elder', 'her chin lifted, her lips closed in calm composure, her brows level')],
    'Medium side-on shot, all three people from the head to the knees, in the middle third of the frame, on the dark-red carpet in the grand gala hall.',
    "<elder> steps into their path and speaks the first line to <killian> in a contemptuous drawl, lifting his glass slightly, then speaks the second line to <killian> with his lip curling back from his teeth, his pale eyes on Killian's face. <killian> stands motionless, his eyes on the old man, his jaw set. <lily_gown> keeps her chin up and her eyes on the old man, her hand tightening very slightly on Killian's forearm.",
    "大长老走上来挡住他们的路，用轻蔑拖长的语调对基利安说出第一句，微微举起酒杯，然后嘴唇卷起露出牙齿，眼睛盯着基利安的脸，对他说出第二句。基利安一动不动，眼睛看着老人，下颌绷紧。莉莉昂着头、眼睛看着老人，放在基利安前臂上的手微微收紧了一点。",
    voiced('A glass clinking faintly, the hush of a silent crowd.', '酒杯轻轻碰响的声音、围观人群的一片寂静。'),
    lines=[('elder', "You brought this human toy here?", 1.0, 'Killian'), ('elder', "You shame every wolf here!", 5.0, 'Killian')],
    bg="Behind them, guests in evening wear stand frozen holding champagne flutes, clearly visible and in sharp focus, every head turned toward the three of them.",
    groups=[('Guests', '后', 'Killian')], st={'Elder': (E_T, E_T), 'Killian': (K_T, K_T), 'Lily': (L_G, L_G)})

S.T('28-03', '03｜赛琳娜把红酒泼向莉莉的裙子，酒在半空停住，反弹回去泼了她一脸', 6, GH,
    [P('selena_chair', 'left', "seated in the wheelchair in profile facing frame-right, her right arm thrown forward with the wrist flicked and an empty glass tilted in her hand", 'Lily', 'her lips pulled back in a vicious sneer, her brows low'),
     P('killian', 'center', "standing in profile facing frame-left, his right arm raised with the palm open toward a spray of red wine that hangs frozen in the air in front of his palm", 'Selena', 'his jaw set, his lips pressed flat, his brows level'),
     P('lily_gown', 'right', "standing at his right side, flinching back, one hand lifted to her chest", 'Selena', 'her lips parted, her brows pulled up')],
    'Medium side-on shot, all three people from the head to the knees, in the middle third of the frame, on the dark-red carpet in the grand gala hall.',
    "The red wine hanging in the air in front of <killian>'s open palm surges backward as if thrown back by an invisible wall and splashes full across <selena_chair>'s face and chest; she recoils with a gasp, her eyes squeezed shut, wine streaming down her face and soaking her burgundy dress. <killian> keeps his palm raised and his eyes on her, unmoved. <lily_gown> stands behind his arm with her eyes on Selena, her lips parted.",
    "停在基利安张开的手掌前面的那团红酒像被一堵看不见的墙弹了回去，整个泼在赛琳娜的脸上和胸口；她倒吸一口气往后一缩，眼睛紧闭，酒顺着脸往下流，浸透了酒红色的裙子。基利安手掌一直举着，眼睛看着她，毫无波动。莉莉站在他手臂后面，眼睛看着赛琳娜，嘴唇微张。",
    breathy('A hard rush of air, a heavy wet splash and a woman\'s shocked gasp.', '一阵猛烈的气流声、一声沉重的泼溅声和一个女人受惊的倒吸气声。'),
    bg="Behind them, guests flinch back with their mouths open, clearly visible and in sharp focus.",
    groups=[('Guests', '后', 'Selena')], st={'Selena': (S_DRY, S_WET), 'Killian': (K_T, K_T), 'Lily': (L_G, L_G)})

S.T('28-04', '04｜他用手帕擦她根本没沾上酒的指尖：你刚才说谁是玩具？', 8, GH,
    [P('elder', 'left', "standing rigid in profile facing frame-right, the champagne glass gripped in his right hand until his knuckles whiten", 'Killian', 'his thin lips white, his brows crashing together'),
     P('killian', 'center', "standing in profile facing frame-left, holding Lily's right hand in his left hand and wiping her fingertips with a white handkerchief in his right hand", 'obj:her fingertips', 'his lips pressed flat, his brows level'),
     P('lily_gown', 'right', "standing at his right side in profile facing frame-left, her right hand held in his", 'Killian', 'her cheeks faintly flushed, her lips closed, her brows level')],
    'Medium side-on shot, all three people from the head to the knees, in the middle third of the frame, on the dark-red carpet in the grand gala hall.',
    "<killian> wipes <lily_gown>'s fingertips slowly and carefully with the handkerchief, one finger at a time, as if she had been soiled. Then he lifts his cold dark-gray eyes to <elder>'s face and speaks the line to <elder> in a soft, level voice. <elder> stares back at him, his face going rigid, his hand gripping the glass harder. <lily_gown> watches Killian's face, her lips pressed together.",
    "基利安用手帕慢慢地、仔细地擦莉莉的指尖，一根一根地擦，好像她真的被弄脏了。然后他抬起冷灰色的眼睛，看着大长老的脸，用轻柔平稳的声音对他说出那句话。大长老瞪着他，脸绷得僵硬，握着酒杯的手更用力。莉莉看着基利安的脸，嘴唇抿紧。",
    voiced('Soft fabric brushing over skin, the hush of a silent crowd.', '手帕轻轻擦过皮肤的声音、围观人群的一片寂静。'),
    lines=[('killian', "Who did you call a toy?", 3.0, 'Elder')],
    bg="Behind them, guests stand frozen in evening wear, clearly visible and in sharp focus.",
    groups=[('Guests', '后', 'Killian')], st={'Elder': (E_T, E_T), 'Killian': (K_T, K_T), 'Lily': (L_G, L_G)})

# ============================================================================================== 第 29 集
b29 = S.episode('剧本第29集｜千亿帝国的降维打击', '大长老气得捏碎酒杯、瞳孔变黄，威胁要跟整个元老院开战；基利安让特助递上平板，告诉他十分钟前已经让他家族破产；老人心脏病发倒下，被保镖拖走，赛琳娜被推走，其余元老低头；莉莉闻到腐肉般的血腥味，发现通风口渗出黑雾。', 29)
S.T('29-01', '01｜大长老捏碎酒杯，瞳孔变黄：你要为一个人类开战？', 10, GH,
    [P('elder_wolf', 'left', "standing rigid in profile facing frame-right, his right fist crushing a champagne glass, champagne and glass shards running over his knuckles", 'Killian', 'his canine teeth bared, his brows crashing together'),
     P('killian', 'center', "standing in profile facing frame-left, his hands relaxed at his sides", 'Elder', 'his lips flat, his brows level'),
     P('lily_gown', 'right', "standing at his right side in profile facing frame-left", 'Killian', 'her lips pressed tight, her brows pulled together')],
    'Medium side-on shot, all three people from the head to the knees, in the middle third of the frame, on the dark-red carpet in the grand gala hall.',
    "The glass in <elder_wolf>'s fist shatters; champagne and glass shards rain onto the marble, and his eyes blaze a burning yellow with narrow wolf pupils. He leans toward <killian> and speaks the first line to <killian> in a hoarse roar, then the second line to <killian>, his lip curling back from his fangs, his eyes locked on Killian's face. <killian> does not move, his eyes on the old man, his lips flat. <lily_gown> glances at Killian's face, her lips pressed tight.",
    "大长老拳头里的酒杯炸开，香槟和玻璃碴子洒在大理石地面上，他的眼睛燃起金黄色、瞳孔收成狼一样的细线。他朝基利安探过身，用沙哑的咆哮对他说出第一句，然后嘴唇卷起露出獠牙，眼睛死死盯着基利安的脸，对他说出第二句。基利安一动不动，眼睛看着老人，嘴唇平直。莉莉看了看基利安的脸，嘴唇抿紧。",
    voiced('Glass cracking and shattering, shards pattering onto marble, a furious guttural roar.', '玻璃裂开碎掉的声音、碎片落在大理石上的声音、愤怒的喉音咆哮。'),
    lines=[('elder_wolf', "You'd go to war for her?!", 1.0, 'Killian'), ('elder_wolf', "We own forty percent of Europe!", 5.0, 'Killian')],
    bg="Behind them, guests stand frozen in evening wear, clearly visible and in sharp focus.",
    groups=[('Guests', '后', 'Killian')], st={'Elder': (None, E_CRUSH), 'Killian': (K_T, K_T), 'Lily': (L_G, L_G)})

S.T('29-02', '02｜基利安：欧洲的40%？可爱。特助递上平板', 8, GH,
    [P('elder_wolf', 'left', "standing rigid in profile facing frame-right, his right hand dripping champagne", 'Killian', 'his fangs bared, his brows crashing together'),
     P('killian', 'center', "standing in three-quarter view turned toward frame-left, his right hand reaching for the tablet that Ajax holds out", 'Elder', 'the corner of his mouth lifted in cold amusement, his brows level'),
     P('ajax', 'right', "standing a step behind Killian's right shoulder in three-quarter view facing frame-left, holding a slim tablet out toward Killian with both hands", 'Killian', 'his jaw level, his lips closed')],
    'Medium shot, all three men from the head to the knees, in the middle third of the frame, on the dark-red carpet in the grand gala hall.',
    "<killian> speaks the line to <elder_wolf> in a light, almost playful voice, the corner of his mouth lifted, then takes the tablet from <ajax>'s hands without looking at it, his eyes staying on the old man's face. <ajax> bows his head slightly, his eyes on Killian, and steps back half a pace. <elder_wolf> glares at him, trembling with rage.",
    "基利安用轻松、几乎带点玩笑的语气对大长老说出那句话，嘴角微微上扬，然后看都不看，从阿贾克斯手里接过平板，眼睛一直留在老人的脸上。阿贾克斯微微低头，眼睛看着基利安，往后退了半步。大长老瞪着他，气得发抖。",
    voiced('A soft electronic chime from the tablet, the hush of a silent crowd.', '平板电脑发出的一声轻轻的电子提示音、围观人群的一片寂静。'),
    lines=[('killian', "Forty percent of Europe? Cute.", 1.0, 'Elder')],
    st={'Killian': (K_T, K_TAB)})

S.T('29-03', '03｜他把平板举到老人面前：十分钟前，我已经让你破产了', 8, GH,
    [P('elder_wolf', 'left', "standing rigid in profile facing frame-right, his hand still dripping champagne", 'obj:the tablet', 'his mouth falling open, his brows shooting up'),
     P('killian', 'right', "standing in profile facing frame-left, holding the tablet up in front of the old man's face with the screen turned toward him, a plunging red stock chart on the screen", 'Elder', 'the corner of his mouth lifted in cold amusement, his brows level')],
    'Medium side-on two-shot, both men from the head to the waist, in the middle third of the frame, on the dark-red carpet in the grand gala hall.',
    "<killian> holds the tablet steady in front of <elder_wolf>'s face and speaks the line to <elder_wolf> in the casual tone of a man talking about the weather. The red chart on the screen plunges steeply down; the old man's burning yellow eyes widen on the screen and slowly the yellow glow in them dies. The camera pushes in slowly until the tablet and the old man's stunned face fill the frame.",
    "基利安把平板稳稳地举在大长老面前，像在谈论天气一样随意地对他说出那句话。屏幕上的红色曲线陡直地往下坠；老人燃烧着黄色的眼睛盯着屏幕越睁越大，眼里的黄光慢慢熄灭。镜头慢慢推近，直到平板和老人惊呆的脸占满画面。",
    voiced('A faint electronic hum from the tablet, a rasping intake of breath.', '平板电脑轻微的电子嗡声、一声嘶哑的吸气声。'),
    lines=[('killian', "Ten minutes ago, I bankrupted you.", 3.0, 'Elder')],
    cam=('The camera pushes in slowly until the tablet and the old man\'s stunned face fill the frame.', '镜头慢慢推近，直到平板和老人惊呆的脸占满画面。'),
    st={'Killian': (K_TAB, K_TAB)})

S.T('29-04', '04｜大长老心脏病发，捂着胸口倒在地上，赛琳娜尖叫', 6, GH,
    [P('selena_chair', 'left', "seated in the wheelchair in profile facing frame-right, red wine dripping from her hair and face, both hands gripping the wheel rims", 'Elder', 'her mouth wide open in a scream, her brows pulled up'),
     P('elder_wolf', 'center', "bent forward at the waist, both hands clutching his chest, his knees buckling", 'Killian', 'his face grey and gritted in agony, his teeth clenched, his brows pulled together'),
     P('killian', 'right', "standing in profile facing frame-left, holding the tablet at his side", 'Elder', 'his lips flat, his brows level')],
    'Medium side-on shot, all three people from the head to the knees, in the middle third of the frame, on the dark-red carpet in the grand gala hall.',
    "<elder_wolf> sinks to his knees clutching his chest, then pitches forward and crashes onto the marble and lies still. <selena_chair> screams at the top of her lungs, her eyes on the old man, tears and wine running down her face. <killian> watches the old man fall, his eyes on him, his lips flat, unmoved.",
    "大长老捂着胸口跪倒下去，然后往前一栽，重重倒在大理石地面上，不动了。赛琳娜扯着嗓子尖叫，眼睛盯着老人，眼泪和红酒一起顺着脸往下流。基利安看着老人倒下，眼睛看着他，嘴唇平直，毫无波动。",
    breathy("A woman's piercing scream, a strangled gasp and a heavy body dropping onto marble.", '一个女人刺耳的尖叫、一声被掐住的喘息和一个沉重的身体倒在大理石上的闷响。'),
    st={'Selena': (S_WET, S_WET), 'Elder': (E_CRUSH, E_DOWN), 'Killian': (K_TAB, K_TAB)})

S.T('29-05', '05｜保镖把大长老拖走，赛琳娜被推走，其余元老一个个低下头', 10, GH,
    [P('killian', 'center', "standing in profile facing frame-left with the tablet at his side, one arm around Lily's waist", 'Elder', 'his jaw set, his lips flat'),
     P('lily_gown', 'right', "standing at his right side in profile facing frame-left, pressed close against him", 'Killian', 'her lips closed, her brows level'),
     P('elder_wolf', 'left', "lying limp on his back on the marble with his arms hooked by two bodyguards who drag him toward frame-left, his heels trailing", 'closed', 'his mouth hanging open, his face slack'),
     ],
    'Wide side-on shot of the grand gala hall, all four people from the head to the feet, the group in the middle third of the frame, on the dark-red carpet.',
    "Two bodyguards in black suits drag <elder_wolf> across the marble toward the tall entrance doors at frame-left, his heels trailing, while a third guard pushes the black wheelchair after them, Selena sitting in it drenched in red wine with her legs in white plaster casts, her eyes on her father. <killian> stands with <lily_gown> pressed against his side and watches them go, his eyes on the old man. Along both sides of the hall the grey-haired elders in black suits lower their heads one after another, bowing deeply with their eyes on the floor. The camera pulls back slowly until the whole hall of bowed heads is in the frame.",
    "两个穿黑西装的保镖拖着大长老在大理石地上往画面左边的入口大门走，他的脚后跟在地上拖着，第三个保镖推着坐着赛琳娜的黑色轮椅跟在后面，她浑身红酒、两腿打着石膏，眼睛看着她父亲。基利安搂着贴在他身边的莉莉，眼睛看着老人被拖走。大厅两侧的灰发元老们一个接一个低下头，深深鞠躬，眼睛盯着地面。镜头慢慢拉远，直到满厅低着头的人都在画面里。",
    breathy('Shoes scraping and dragging on marble, wheelchair wheels rolling, an uneasy murmur dying into silence.', '鞋子在大理石上刮擦拖行的声音、轮椅车轮滚动的声音、不安的低语声渐渐消失成寂静。'),
    cam=('The camera pulls back slowly until the whole hall of bowed heads is in the frame.', '镜头慢慢拉远，直到满厅低着头的人都在画面里。'),
    bg="Two bodyguards in black suits drag the old man and a third guard pushes the black wheelchair with the wine-soaked woman in it; along both sides of the hall grey-haired elders in black suits stand bowing, clearly visible and in sharp focus.",
    groups=[('Selena', '左', 'Elder'), ('Guards', '左', 'Elder'), ('Elders', '两侧', 'obj:the floor')], enter={'Guards'}, exit={'Elder', 'Selena', 'Guards'},
    holds='The frame holds Killian and Lily at the center, the old man dragged away at the left, and the bodyguards, the wheelchair and the bowing elders around them.',
    st={'Killian': (K_TAB, K_TAB), 'Lily': (L_G, L_G), 'Elder': (E_DOWN, E_DOWN)})

S.T('29-06', '06｜莉莉闻到腐肉似的血腥味，对他说：有东西从通风口进来了', 8, GH,
    [P('killian', 'left', "standing in profile facing frame-right with the tablet at his side", 'Lily', 'his brows lowering, his lips parting'),
     P('lily_gown', 'right', "standing in profile facing frame-left, her head tilted slightly back", 'Killian', 'her nostrils flaring, her brows drawn together in alarm')],
    'Medium side-on two-shot, both people from the head to the waist, in the middle third of the frame, in the grand gala hall.',
    "<lily_gown> lifts her chin and her nostrils flare as she catches a foul scent, her lips pulling back in disgust; she turns her eyes to <killian> and speaks the line to <killian> in a low urgent voice. <killian>'s head snaps up, his eyes narrowing as he searches the ceiling, his lips parting, then his eyes return to her face.",
    "莉莉抬起下巴，鼻翼翕动，闻到了一股恶臭的气味，嘴唇厌恶地往后缩；她把眼睛转向基利安，用低低的、急促的声音对他说出那句话。基利安猛地抬头，眼睛眯起来在天花板上搜寻，嘴唇张开，然后目光回到她的脸上。",
    voiced('A sharp sniff, a low tense hush in the hall.', '一声急促的嗅气声、大厅里低低紧绷的寂静。'),
    lines=[('lily_gown', "Something is coming through the vents!", 1.0, 'Killian')],
    exit=set(), st={'Killian': (K_TAB, K_TAB), 'Lily': (L_G, L_G)})

S.T('29-07', '07｜通风口里，黑色的雾一团团渗出来', 5, GH_UP, [],
    'Low upward shot of the high gold-trimmed wall of the grand hall, the gold vent in the middle third of the frame, nobody in the frame.',
    "A gold ceiling vent grille high on the wall slowly bulges and buckles; thick black mist seeps through its slats and rolls down the wall in slow heavy coils, swallowing the warm golden light around it.",
    "大厅高墙上方的金色通风口格栅慢慢鼓起、变形；浓浓的黑色雾气从栅条间渗出来，沿着墙壁一团团缓缓往下滚，吞掉周围温暖的金色灯光。",
    breathy('A low rising hiss, a faint wet scraping inside the metal duct and a far-off echoing growl.', '一阵低低上升的嘶嘶声、金属管道里轻微的湿漉漉的刮擦声和远处传来的回响的低吼。'),
    holds='The frame holds no people, only the wall, the gold vent and the black mist.')

# ============================================================================================== 第 30 集
b30 = S.episode('剧本第30集｜死斗场的亡魂', '巨大的水晶吊灯突然坠落砸在大厅中央，宾客尖叫后退；烟尘里，被毒液侵蚀的变异保罗握着银匕首站在碎水晶中间，头顶是被撕开的通风口；他扑向莉莉，基利安挡在她身前，银刃刺进他的左胸，他单膝跪下，黑血染透白衬衫。', 30)
S.T('30-01', '01｜水晶吊灯断链坠落，砸在大厅中央', 6, GH,
    [P('killian', 'right', "standing at the foot of the banquet table in profile facing frame-left, the tablet in one hand and his other arm around Lily's waist", 'obj:the falling chandelier', 'his jaw clenched, his brows lowered'),
     P('lily_gown', 'right', "standing at his right side in profile facing frame-left, pressed against him", 'obj:the falling chandelier', 'her lips parted, her brows pulled up')],
    'Wide shot of the whole grand gala hall, the couple at the right of the frame, in the middle third of the frame.',
    "The huge crystal chandelier, its chain snapped, plunges the last few feet and smashes onto the marble floor in the middle of the hall in an explosion of crystal and metal, a wave of dust rolling outward. The guests scream and scatter backward, shielding their faces. <killian> lets the tablet fall from his hand and pulls <lily_gown> against his chest, his eyes on the wreck, his jaw clenched.",
    "巨大的水晶吊灯断了链子，坠落最后几英尺，砸在大厅中央的大理石地面上，水晶和金属炸成一片，灰尘像波浪一样向外滚开。宾客们尖叫着往后散开，用手挡住脸。基利安手里的平板掉在地上，他把莉莉拉进怀里，眼睛看着那堆残骸，下颌绷紧。",
    breathy('A deafening crash of shattering crystal, a rolling metallic clang and a wave of screams.', '一声震耳欲聋的水晶碎裂巨响、金属滚动的哐啷声和一片尖叫声。'),
    bg="Guests in evening wear fill the hall, clearly visible and in sharp focus, recoiling from the falling chandelier with their mouths open.",
    groups=[('Guests', '后', 'obj:the falling chandelier')], enter=set(),
    st={'Killian': (K_TAB, K_T), 'Lily': (L_G, L_G)})

S.T('30-02', '02｜烟尘里，变异的保罗站在碎水晶中间：你夺走了一切，所以你去死', 10, GH,
    [P('paul_mutant', 'left', "standing hunched among the glittering crystal shards, the silver dagger in his right fist, a torn ceiling vent hanging open on the wall behind him", 'Lily', 'his lips peeled back from his teeth, his brows low'),
     P('killian', 'center', "standing in profile facing frame-left, one arm pulling Lily behind him", 'Paul', 'his jaw clenched, his lips pressed flat'),
     P('lily_gown', 'right', "standing at his right side half behind him, her hand on his arm", 'Paul', 'her lips parted, her brows pulled together')],
    'Wide side-on shot, all three people from the head to the feet, in the middle third of the frame, across the wrecked crystal and dust on the hall floor.',
    "The dust slowly thins and <paul_mutant> drags himself upright among the shards, his milky grey eyes on <lily_gown>, a dark rasping breath rattling in his chest; he raises the silver dagger and speaks the line to <lily_gown> in a wet, broken voice, his lips peeled back from his teeth. <killian> steps half a pace in front of Lily, his eyes on Paul, his jaw clenched.",
    "灰尘慢慢散开，保罗在碎水晶中间拖着身体站起来，乳灰色的眼睛盯着莉莉，胸腔里发出黑色的、嘶哑的喘息；他举起银匕首，用湿漉漉、破碎的声音对莉莉说出那句话，嘴唇龇出牙齿。基利安往前半步挡在莉莉前面，眼睛盯着保罗，下颌绷紧。",
    voiced('Crystal shards crunching under dragging boots, a wet rasping breath and a low animal rumble.', '碎水晶在拖着的靴子下嘎吱作响、湿漉漉的嘶哑喘息和低低的野兽般的呼噜声。'),
    lines=[('paul_mutant', "You took everything, so you die!", 2.0, 'Lily')],
    enter={'Paul'}, bg="Guests cower along the walls of the hall behind them, clearly visible and in sharp focus.", groups=[('Guests', '后', 'Paul')],
    st={'Paul': (P_STAND, P_STAND), 'Killian': (K_T, K_T), 'Lily': (L_G, L_G)})

S.T('30-03', '03｜保罗扑向莉莉，基利安挡在她身前，银刃刺进他的左胸', 5, GH,
    [P('paul_mutant', 'left', "lunging in profile toward frame-right, body low and stretched, his right arm drawn back with the silver dagger pointed at the middle of Killian's chest", 'Lily', 'his lips peeled back from his teeth, his brows low'),
     P('killian', 'center', "standing in profile facing frame-left, feet braced, his left arm already sweeping behind him to hold Lily back, his chest square to the blade", 'Paul', 'his jaw clenched, his lips pressed flat'),
     P('lily_gown', 'right', "pressed behind his back with both hands gripping his jacket", 'Paul', 'her lips parted, her brows pulled up')],
    'Wide side-on shot, all three people from the head to the feet, in the middle third of the frame, on the cleared marble floor of the hall.',
    "<paul_mutant> completes his lunge and drives the silver dagger into <killian>'s left chest. <killian> grunts through clenched teeth and does not step back, his left arm still holding <lily_gown> behind him, his eyes on Paul's face. <lily_gown> stares at the blade, her mouth opening.",
    "保罗把扑刺完成，银匕首扎进基利安的左胸。基利安咬紧牙关闷哼一声，没有后退，左臂依然把莉莉护在身后，眼睛盯着保罗的脸。莉莉盯着刀刃，嘴巴张开。",
    breathy('A wet thud of steel into flesh, a sharp grunt through clenched teeth and a gasp.', '钢刃扎进肉里的一声湿闷的响声、咬紧牙关发出的一声闷哼和一声倒吸气。'),
    st={'Paul': (P_STAND, P_STAB), 'Killian': (K_T, K_STAB), 'Lily': (L_G, L_G)})

S.T('30-04', '04｜基利安单膝跪下，黑血染透白衬衫，莉莉尖叫他的名字', 8, GH,
    [P('paul_mutant', 'left', "standing in profile facing frame-right, both hands gripping the hilt of the dagger buried in Killian's chest", 'Killian', 'his mouth hanging open in a wet rasping grin'),
     P('killian_wounded', 'center', "sagging forward in profile facing frame-left, his left hand pressed to his chest, black blood spreading across the white shirt", 'Paul', 'his teeth bared, his brows pulled together in pain'),
     P('lily_gown', 'right', "reaching both hands toward Killian's shoulder", 'Killian', 'her mouth open in a scream, her brows pulled up')],
    'Wide side-on shot, all three people from the head to the feet, in the middle third of the frame, on the cleared marble floor of the hall.',
    "<killian_wounded> drops slowly to one knee, black blood spreading across his white shirt, and as he sinks <paul_mutant> wrenches the dagger free and holds it dripping at his side. <lily_gown> shouts the line to <killian_wounded>, her hands reaching for his shoulders, her eyes wide on his face.",
    "基利安慢慢单膝跪下去，黑色的血在白衬衫上蔓延开；他往下沉的时候，保罗把匕首猛地拔出来，让它滴着血垂在身侧。莉莉对着基利安喊出那句话（他的名字），双手伸向他的肩膀，眼睛在他脸上瞪得很大。",
    voiced('A cry of anguish, ragged breathing and a heavy knee striking marble.', '一声痛苦的呼喊、粗重的喘息和膝盖重重磕在大理石上的声音。'),
    lines=[('lily_gown', "Killian!", 1.5, 'Killian')],
    st={'Paul': (P_STAB, P_FREE), 'Killian': (K_STAB, K_KNEEL), 'Lily': (L_G, L_G)})

# ============================================================================================== 第 31 集
b31 = S.episode('剧本第31集｜Luna之怒', '保罗拔出匕首举过头顶，基利安吐出黑血，银毒压住了他的自愈；莉莉站起来，眼睛爆发出银光、头发飘起；保罗的刀落下的瞬间她抬手，银色冲击波把他轰飞到大厅另一头的墙上；全场趴在地上；她一步步走向嵌在墙里的保罗，抬起手说：动我的男人，没人能活着。', 31)
S.T('31-01', '01｜保罗把匕首举过头顶：再见，Alpha。基利安吐出黑血', 8, GH,
    [P('paul_mutant', 'left', "standing in profile facing frame-right, both hands raised high over his head gripping the dripping silver dagger", 'Killian', 'his mouth stretched in a wet rasping grin, his brows low'),
     P('killian_wounded', 'center', "kneeling on one knee in profile facing frame-left, his left hand pressed to his chest, black blood on his chin", 'Paul', 'his teeth bared, his brows pulled together in pain'),
     P('lily_gown', 'right', "kneeling beside him with both hands gripping his arm, a faint silver glow spreading from beneath her pink diamond necklace", 'Killian', 'her lips trembling, her brows pulled up')],
    'Wide side-on shot, all three people from the head to the feet, in the middle third of the frame, on the cleared marble floor of the hall.',
    "<paul_mutant> speaks the line to <killian_wounded> in a wet, broken voice, the dagger trembling high above his head. <killian_wounded> coughs and a mouthful of black blood spills from his lips, his body shuddering, his eyes on Paul. <lily_gown> clings to his arm, her eyes on his face, tears gathering; the faint silver glow beneath her necklace grows a little brighter.",
    "保罗用湿漉漉、破碎的声音对基利安说出那句话，高举过头顶的匕首在颤抖。基利安咳嗽起来，一大口黑血从嘴里涌出来，身体发抖，眼睛盯着保罗。莉莉紧紧抓着他的手臂，眼睛看着他的脸，眼泪涌上来；她项链下面那点银色的光亮了一点点。",
    voiced('Wet, ragged coughing and a low rasping laugh.', '湿漉漉、粗重的咳嗽声和一阵低低的嘶哑笑声。'),
    lines=[('paul_mutant', "Goodbye, Alpha.", 1.5, 'Killian')],
    st={'Paul': (P_FREE, P_UP), 'Killian': (K_KNEEL, K_KNEEL), 'Lily': (L_G, L_G)})

S.T('31-02', '02｜莉莉站起来，眼睛爆发银光，头发飘起，保罗的刀僵在半空', 8, GH,
    [P('paul_mutant', 'left', "standing in profile facing frame-right, both hands raised high over his head gripping the dripping silver dagger, his arms trembling", 'Lily', 'his eyes wide with terror, his lips trembling'),
     P('killian_wounded', 'center', "kneeling on one knee in profile facing frame-left with his head hanging, black blood dripping from his chin", 'obj:the marble floor', 'his jaw clenched'),
     P('lily_gown_silver', 'right', "kneeling beside him with her head lowered, her long chestnut hair lifting weightlessly, silver light spilling from her eyes", 'Killian', 'her lips pressed tight, her brows drawn together')],
    'Wide side-on shot, all three people from the head to the feet, in the middle third of the frame, on the cleared marble floor of the hall.',
    "<lily_gown_silver> rises slowly to her feet beside the kneeling <killian_wounded>, her hair lifting higher around her, then lifts her head toward <paul_mutant>; her eyes blaze a blinding silver-white. <paul_mutant>'s raised dagger freezes in the air, his arms shaking, his eyes wide on her. The camera pushes in until her silver eyes fill the frame.",
    "莉莉在跪着的基利安身边慢慢站起来，头发越飘越高，然后抬头看向保罗，眼睛爆发出刺眼的银白色光芒。保罗高举的匕首僵在半空，手臂发抖，眼睛瞪着她。镜头推近，直到她银色的眼睛占满画面。",
    breathy('A deep rising hum, a rush of wind lifting fabric and a thin tremor of strained breath.', '一阵低沉上升的嗡鸣、风吹起衣料的声音和一声紧绷发颤的细细喘息。'),
    cam=('The camera pushes in until her silver eyes fill the frame.', '镜头推近，直到她银色的眼睛占满画面。'),
    st={'Paul': (P_UP, P_UP), 'Killian': (K_KNEEL, K_KNEEL), 'Lily': (None, L_AW)})

S.T('31-03', '03｜刀落下的瞬间她抬手，银色冲击波把保罗轰飞到大厅另一头的墙上', 5, GH,
    [P('paul_mutant', 'left', "caught mid-strike in profile facing frame-right, the silver dagger descending in both hands a few feet from Lily", 'Lily', 'his eyes wide, his teeth bared'),
     P('lily_gown_silver', 'center', "standing in profile facing frame-left, her right arm extended with the palm open toward him and a ring of silver light blooming at her palm, her hair lifting", 'Paul', 'her jaw set, her lips pressed flat'),
     P('killian_wounded', 'right', "kneeling behind her in profile facing frame-left, his left hand pressed to his chest", 'Lily', 'his brows pulled together')],
    'Ultra-wide side-on shot of the whole length of the grand hall, all three people in the middle third of the frame, the far wall at the extreme left of the frame.',
    "A silver shockwave explodes outward from <lily_gown_silver>'s palm and blasts <paul_mutant> backward across the whole length of the hall; he flies through the air toward frame-left and slams into the far wall, which cracks open around him. <lily_gown_silver> stands unmoving with her arm extended, her silver eyes on him. <killian_wounded> watches her from the floor, his eyes on her.",
    "银色的冲击波从莉莉的手掌炸开，把保罗向后轰飞，穿过整个大厅；他向画面左边飞过去，重重砸在最远处的墙上，墙壁在他身后裂开。莉莉伸着手臂一动不动，银色的眼睛盯着他。基利安跪在地上看着她，眼睛没有离开过她。",
    breathy('A deep booming concussion, a rush of wind, a body slamming into stone and plaster cracking.', '一声低沉轰然的冲击声、一阵风声、一个身体撞在石头上的巨响和灰泥开裂的声音。'),
    st={'Paul': (P_UP, P_WALL), 'Killian': (K_KNEEL, K_KNEEL), 'Lily': (L_AW, L_AW)})

S.T('31-04', '04｜保罗嵌在裂开的墙里，宾客全部趴在地上，莉莉一步步走过去', 8, GH,
    [P('lily_gown_silver', 'center', "walking in profile toward frame-left across the open marble floor with measured steps, her hair lifting, a faint silver glow around her", 'Paul', 'her jaw set, her lips pressed flat'),
     P('paul_mutant', 'left', "embedded in the cracked wall at the far left of the frame, sagging half out of the crater, one hand still clutching the dagger", 'Lily', 'his mouth hanging open, his eyes wide with terror')],
    'Ultra-wide side-on shot of the grand hall, the walking woman in the middle third of the frame, the cracked wall at the left of the frame.',
    "<lily_gown_silver> walks slowly toward <paul_mutant> across the open floor, her bare silver light brightening with each step, her eyes locked on him. All around her the guests and elders lie flat on the marble with their foreheads pressed to the floor and their hands over their heads. The camera tracks sideways to the left, following her.",
    "莉莉一步一步慢慢走向保罗，穿过空旷的地面，随着每一步，周身的银光越来越亮，眼睛死死盯着他。她周围，宾客和元老们全都趴在大理石地上，额头贴着地面，双手抱着头。镜头横向向左跟拍，跟着她。",
    breathy('Slow bare footsteps on marble, a low crackle of energy and a hall full of held breath.', '光脚缓慢踩在大理石上的脚步声、低低的能量噼啪声和满厅屏住呼吸的寂静。'),
    cam=('The camera tracks sideways to the left, following her.', '镜头横向向左跟拍，跟着她。'),
    bg="All around her the guests and elders lie flat on the marble floor with their foreheads pressed to the ground, clearly visible and in sharp focus.",
    groups=[('Guests', '后', 'Lily')],
    st={'Paul': (P_WALL, P_WALL), 'Lily': (L_AW, L_AW)})

S.T('31-05', '05｜她站在他面前，抬手，手指弯成抓握：没人动我的男人还能活着', 8, GH,
    [P('paul_mutant', 'left', "embedded in the cracked wall, sagging half out of the crater, the dagger lying at his feet", 'Lily', 'his mouth hanging open, his eyes wide with terror'),
     P('lily_gown_silver', 'right', "standing in profile facing frame-left, her right hand raised with the fingers curled as if gripping the air", 'Paul', 'her jaw set, her lips pressed flat')],
    'Medium side-on two-shot, both people from the head to the waist, in the middle third of the frame, in front of the cracked wall of the hall.',
    "<lily_gown_silver> stops in front of <paul_mutant>, her silver eyes locked on his face, and speaks the line to <paul_mutant> in a voice cold and quiet as a verdict; as she speaks her raised hand curls slowly into a claw, a ring of silver light gathering around her fingers. <paul_mutant> shrinks back against the wall, his eyes wide on her, his lips trembling.",
    "莉莉在保罗面前站住，银色的眼睛死死盯着他的脸，用冷得像判决书一样安静的声音对他说出那句话；她说话时，抬起的手慢慢弯成爪形，一圈银色的光聚在她的指尖周围。保罗缩在墙上，眼睛瞪着她，嘴唇发抖。",
    voiced('A thin rising hum of energy, a rattling breath.', '一阵细细上升的能量嗡鸣、一声颤抖的喘息。'),
    lines=[('lily_gown_silver', "Nobody touches my man and lives.", 1.5, 'Paul')],
    trigger='Nobody touches my man and lives',
    st={'Paul': (P_WALL, P_WALL), 'Lily': (L_AW, L_AW)})

# ============================================================================================== 第 32 集
look('killian_wounded_gold', 'KillianWoundedGold', "in the black suit with the jacket hanging open over a white shirt torn at the left chest and soaked with black blood, the skin under the tear smooth and healed", 'burning gold', 'his')
b32 = S.episode('剧本第32集｜死神的镰刀', '她的拳头一收紧，保罗的惨叫戛然而止，银光熄灭，他软软滑落在墙根；她脱力倒下，被基利安接住——他的伤口已经愈合，他说这点毒杀不了他，他只是想看她为他发火的样子；他抱着她转向满厅趴着的人，金眼与银眼；冰雪狂风吹开高窗，白衣银发的卢修斯走进来：把Luna交出来，不然你们死。', 32)
b27.person('killian_wounded_gold', '基利安（伤口已愈合，金色的眼睛）',
           'Killian, the same very tall, broad-shouldered adult man in his early thirties as in the reference, with short swept-back black hair, a sharp jawline and light stubble, burning gold eyes, wearing a black suit with the jacket hanging open over a white shirt torn at the left chest and soaked with black blood, the skin under the tear smooth and healed, a platinum luxury wristwatch on his left wrist. The portrait fixes his identity, clothes and eye color, not staging.',
           '基利安，和参考图是同一个三十出头、身材极高、肩膀宽阔的成年男性，黑色短发向后梳，下颌线锋利，有浅胡茬，眼睛是燃烧般的金色，穿着敞开外套的黑色西装，里面的白衬衫左胸撕破、浸满黑色血迹，但撕破处下面的皮肤光滑，伤口已经愈合，左手腕戴铂金名表。肖像固定他的长相、衣着和眼睛颜色，不固定姿势。',
           'A photorealistic half-body portrait of the same man as in the reference image, short swept-back black hair, sharp jawline, light stubble, burning gold eyes, wearing a black suit with the jacket hanging open over a white shirt torn at the left chest and soaked with black blood, the skin under the tear smooth and healed, a platinum luxury wristwatch on his left wrist. He faces the camera with a fierce, amused expression. Soft even studio light, plain neutral gray background, natural skin texture with visible pores.', ref='killian')
b27.character('KillianWoundedGold', 'killian_wounded_gold', *voice('Killian'))
K_HEAL = '西装敞开，衬衫左胸撕破沾黑血，伤口已愈合，金眼'

S.T('32-01', '01｜她的拳头一收紧，保罗的惨叫戛然而止，软软滑落', 6, GH,
    [P('paul_mutant', 'left', "pinned in the cracked wall at the far left of the frame, wrapped in a crackling web of silver light, his head thrown back in a scream", 'Lily', 'his mouth stretched wide, his eyes bulging'),
     P('lily_gown_silver', 'center', "standing in profile facing frame-left, her right arm extended with the hand just snapping closed into a fist, her hair lifting", 'Paul', 'her jaw set, her lips pressed flat'),
     P('killian_wounded', 'right', "pushing himself up from one knee in profile facing frame-left, one hand on the marble floor, the white shirt soaked with black blood", 'Lily', 'his jaw clenched, his brows lowered')],
    'Ultra-wide side-on shot, all three people from the head to the feet, in the middle third of the frame, the cracked wall at the left of the frame.',
    "<lily_gown_silver>'s fist clenches tight; the silver light around <paul_mutant> flares white and goes out, his scream cuts off mid-breath, and his body goes limp and slides slowly down the cracked wall to the floor, where he lies still. Behind her <killian_wounded> pushes himself slowly up from his knee, his eyes on her back.",
    "莉莉的拳头一下握紧；包着保罗的银光闪成白色然后熄灭，他的惨叫在半口气中断，身体软下来，顺着裂开的墙慢慢滑到地上，躺着不动了。在她身后，基利安慢慢从单膝跪地撑着站起来，眼睛看着她的背影。",
    breathy('A last choked scream cut dead, a fading crackle of energy and a limp body sliding down stone.', '最后一声被掐断的惨叫、渐渐消失的能量噼啪声和一个软下来的身体顺着石头滑落的声音。'),
    effect='Nobody touches my man and lives',
    st={'Paul': (P_WALL, P_SLUMP), 'Lily': (L_AW, L_AW), 'Killian': (K_KNEEL, K_UP)})

S.T('32-02', '02｜她脱力倒下，他接住她：这点毒杀不了我，我只是想看你为我发火', 10, GH,
    [P('lily_gown_silver', 'left', "falling backward into his arms with her head tipped back against his shoulder, her knees giving way, her hair settling", 'Killian', 'her eyes heavy, her lips parted'),
     P('killian_wounded_gold', 'right', "standing in profile facing frame-left, holding her up under her arms and around her ribs, the white shirt torn and soaked with black blood but the skin under the tear smooth and healed", 'Lily', 'the corner of his mouth lifted in tender mad delight, his brows relaxed')],
    'Medium side-on two-shot, both people from the head to the waist, in the middle third of the frame, in front of the wrecked hall.',
    "<lily_gown_silver> sags into <killian_wounded_gold>'s arms and he takes her full weight, his hands steady around her ribs. He speaks the first line to <lily_gown_silver> in a low, amused murmur, his gold eyes on her face; she turns her head weakly and looks up at him, her silver eyes widening. Then he leans his face close to hers and speaks the second line to <lily_gown_silver>, his gold eyes burning with a dark, adoring light.",
    "莉莉软软地倒进基利安怀里，他稳稳接住她的全部重量，双手牢牢托着她的肋侧。他低低地、带着笑意地对她说出第一句，金色的眼睛看着她的脸；她虚弱地转过头看着他，银色的眼睛越睁越大。然后他把脸凑近她的脸，对她说出第二句，金色的眼睛里燃烧着黑暗又痴迷的光。",
    voiced('Slow ragged breathing, fabric rustling, a low tender laugh.', '缓慢粗重的呼吸声、衣料的摩擦声、一声低低的温柔的笑。'),
    lines=[('killian_wounded_gold', "That poison can't kill me, little wife.", 1.0, 'Lily'), ('killian_wounded_gold', "I wanted to see you furious.", 5.0, 'Lily')],
    st={'Lily': (L_AW, L_AW), 'Killian': (K_UP, K_HEAL)})

S.T('32-03', '03｜他抱着她转向满厅趴着的人，金眼与银眼，镜头拉远', 8, GH,
    [P('killian_wounded_gold', 'center', "standing in profile facing frame-left, holding Lily across his arms against his chest, his chin lifted", 'obj:the guests lying prostrate on the floor', 'his jaw set, his lips pressed flat'),
     P('lily_gown_silver', 'center', "held across his arms with her head resting against his shoulder, her silver light gleaming", 'Killian', 'her lips parted, her brows smooth')],
    'Medium side-on shot, both people from the head to the knees, in the middle third of the frame, in front of the hall.',
    "<killian_wounded_gold> turns slowly with <lily_gown_silver> in his arms to face the whole hall, his gold eyes sweeping over the guests and elders who lie flat on the marble with their foreheads pressed to the floor. <lily_gown_silver>'s silver eyes gleam against his shoulder, her eyes on his face. The camera pulls back slowly until the whole hall of prostrate people is in the frame.",
    "基利安抱着莉莉慢慢转身，面向整个大厅，金色的眼睛扫过趴在大理石地上、额头贴着地面的宾客和元老们。莉莉靠着他的肩膀，银色的眼睛发着光，看着他的脸。镜头慢慢拉远，直到满厅趴着的人都在画面里。",
    breathy('A hall full of held breath, slow footsteps and the faint ringing hum of power fading.', '满厅屏住呼吸的寂静、缓慢的脚步声和渐渐消退的力量发出的微弱嗡鸣。'),
    cam=('The camera pulls back slowly until the whole hall of prostrate people is in the frame.', '镜头慢慢拉远，直到满厅趴着的人都在画面里。'),
    bg="On the floor in front of them, guests and grey-haired elders lie flat on the marble with their foreheads pressed to the ground, clearly visible and in sharp focus.",
    groups=[('Guests', '前', 'obj:the floor')], st={'Lily': (L_AW, L_AW), 'Killian': (K_HEAL, K_HEAL)})

S.T('32-04', '04｜冰雪狂风吹开高窗，白衣银发的卢修斯踩着冰霜走进来：把Luna交出来，不然你们死', 8, GH,
    [P('lucius', 'left', "stepping down from the tall open arched window onto the marble floor, frost spreading across the floor around his feet, snow whirling in the wind behind him", 'Killian', 'one corner of his mouth lifted in cold contempt, his brows level'),
     P('killian_wounded_gold', 'right', "standing in profile facing frame-left, holding Lily across his arms", 'Lucius', 'his jaw clenched, his lips pressed flat'),
     P('lily_gown_silver', 'right', "held across his arms, her head turned toward the intruder", 'Lucius', 'her lips parted, her brows drawn together')],
    'Wide side-on shot, all three people from the head to the feet, in the middle third of the frame, the tall open arched window behind them at the back wall.',
    "<lucius> takes another unhurried step into the hall as the freezing wind howls past him, a sheet of white frost spreading across the marble from beneath his shoes, and speaks the line to <killian_wounded_gold> in a smooth, silky voice, his icy-blue eyes on Killian. <killian_wounded_gold> tightens his arms around <lily_gown_silver>, his gold eyes locked on the intruder.",
    "冰冷的狂风呼啸着从卢修斯身边掠过，他不慌不忙地又往大厅里走了一步，一片白色的冰霜从他鞋底下在大理石上铺开，他用顺滑柔软的声音对基利安说出那句话，冰蓝色的眼睛看着基利安。基利安把抱着莉莉的手臂收紧，金色的眼睛死死盯着闯入者。",
    voiced('A howling icy wind, the hard crackle of frost spreading across marble.', '冰冷风的呼啸声、冰霜在大理石上蔓延时清脆的噼啪声。'),
    lines=[('lucius', "Hand over the Luna, or die.", 3.0, 'Killian')],
    bg="Guests and elders lie prostrate on the marble across the hall, clearly visible and in sharp focus, a few lifting their heads in terror.",
    groups=[('Guests', '前', 'Lucius')], enter={'Lucius'}, st={'Lily': (L_AW, L_AW), 'Killian': (K_HEAL, K_HEAL)})

S.finish()
