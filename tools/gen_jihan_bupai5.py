#!/usr/bin/env python3
"""《极寒末日：我的隐秘安全屋》补拍包 5（2026-10-16，hh 14:24）：大雪里的冰封人群，1 个任务 12 秒，无台词。
接在补拍3 的情侣冰雕（C-01 相拥→C-02 已成冰雕→C-03 冰封天桥全景）之后放进成片：
  F-01 大雪纷飞的广场：前景是那对相拥的冰雕（陈屿、许然，同补拍3 的外貌和冰壳），身后广场上有几十个同样被冰封的人
       （奔跑的、蹲着的、伸着手的、成对抱在一起的），大片雪花斜着落，肩头头顶堆着雪；
       运镜：从低机位贴着雪面开始，缓缓向前滑过相拥的情侣，同时像吊臂一样升高，直到整个广场和几十个冰雕人占满画面（一个连续运动，动作＋终点）。
以补拍4 的 JSON 为底（026 → 补拍3 → 补拍4 → 补拍5），必须等补拍4 在插件里全部跑完再追加；追加窗口不要勾每集／总／任务秒数。
另有单独版（tools/make_standalone.py），新建一部剧直接贴。
H3 方面的风险（交稿时单列、不算我的错）：
  · 几十个冰雕人容易画成一团糊的白、或者有的人脸变形；冰壳可能只画成一层白粉；
  · 冰雕可能被画“活”（转头、动手）；大片雪花可能只是静止的纹理而不是在落；
  · 低机位前滑加升高是复合运镜（动作＋终点），可能只做成其中一个；
  · 前景情侣的拥抱可能走样；约一成开场图不按文字画。
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _jihan_base6 as B6
import _jihan_base7 as B7
from _jihan_base7 import *
import _jihan_base8 as B8
from _jihan_base8 import *
import _h3draft as _H
_H.configure(smooth=True, fixed_seed=37407, cap=12)
OUT = '补拍/追加版_接在主剧后面_带全剧素材/补拍5_大雪里的冰封人群_制作稿_追加'
if os.environ.get('H3_REV'):      # 修订模式：补拍5 要接在“修订版补拍3”（里面有陈屿、许然的素材）后面，不是接在 026 后面
    os.environ['H3_REV'] = '补拍/追加版_接在主剧后面_带全剧素材/修订版/补拍3_地球固定镜头与情侣冰雕_制作稿_修订_追加.json'
S = Session('补拍/追加版_接在主剧后面_带全剧素材/补拍4_末日景色十八个_制作稿_追加.json', OUT, 98000)
B6.S = S
B7.S = S

CNM = 'a Chinese man in his late twenties'
CNF = 'a Chinese woman in her late twenties'
CY_LIVE = "in a charcoal wool overcoat over a grey crewneck sweater and dark trousers, his short neat black hair tousled by the wind"
XR_LIVE = "in a long camel wool coat over a cream knit sweater, her long black hair loose and lifted by the wind"
CY_ICE = "in a charcoal wool overcoat completely sealed in clear glittering ice and thick white frost, long icicles hanging from the sleeves and the hem, his black hair stiff with white rime"
XR_ICE = "in a long camel wool coat completely sealed in clear glittering ice and thick white frost, icicles hanging from the hem, her long black hair stiff with white rime and frozen mid-air"
look('chenyu', 'Chenyu', CY_LIVE, 'steady dark-brown', 'his', eth=CNM)
look('xuran', 'Xuran', XR_LIVE, 'soft dark-brown', 'her', eth=CNF)
B7.ZN.update({'chenyu': '陈屿', 'xuran': '许然'})
AE = lambda en, zh: (en, zh)

mode('A')
_H.CFG['sfx_loud'] = True

PLAZA = Scene('snow_plaza', " Heavy snow falls in big slow flakes through cold blue-grey air and a low pale sun glows behind the cloud.",
              " Fixed stage layout: a wide city plaza at the crossing of two boulevards lies buried under deep smooth snow, glass towers hung with long icicles rising on both sides and at the back of the frame, snow-buried cars standing silent up to their windows, a dead traffic light on a pole at frame-right, and across the whole plaza dozens of people sealed in clear ice stand perfectly still in the falling snow.")

bF = S.episode('补拍5｜大雪里的冰封人群（接在补拍3 的情侣冰雕之后）',
               '大雪纷飞的广场上，那对相拥的情侣已是冰雕，镜头贴着雪面向前滑过他们同时缓缓升高，露出整个广场上几十个保持着各种姿势的冰封的人。', 12)
new_scene(bF, 'snow_plaza', '大雪里的城市广场（两条大街交叉的宽广场被深深的雪埋住，两边和身后是挂满长冰柱的玻璃大楼，车埋在雪里只露出窗户，右边一根红绿灯杆灭着，广场上几十个被透明冰封住的人一动不动站在大雪里）',
          'A wide city plaza at the crossing of two boulevards buried under deep smooth snow, glass towers hung with long icicles on both sides and behind, cars buried to their windows in snow, a dead traffic light on a pole at the right, and dozens of people sealed in clear ice standing perfectly still across the plaza in heavy falling snow.',
          '两条大街交叉的城市宽广场被深深的雪埋住，两边和身后是挂满长冰柱的玻璃大楼，车埋在雪里只露出窗户，右边一根红绿灯杆灭着，广场上几十个被透明冰封住的人一动不动站在大雪里。',
          'the deep snow, the icicle-hung towers, the buried cars and the frozen people across the plaza')

AES_F01 = AE("A low pale sun breaks through a gap in the heavy snow cloud and a cold gold shaft lights up the falling flakes like glitter, while long blue shadows of the ice figures stretch across the deep snow.",
             "一轮低低的苍白太阳从厚厚的雪云缝隙里透出来，一道冷冷的金色光柱把落下的雪花照得像碎金，冰封的人在深雪上拉出长长的蓝色影子。")

TAA('F-01', '01｜大雪广场：大片雪花斜着落，前景是那对相拥的冰雕，镜头贴着雪面向前滑过他们同时缓缓升高，露出整个广场上几十个保持着各种姿势的冰封的人', 12, PLAZA,
    [P('chenyu', 'center-right', "standing in the foreground in profile facing frame-left, both arms wrapped around Xuran's back with both hands holding her shoulder blades, his chin resting lightly against her forehead", 'closed', "his face calm under a layer of white frost, tiny ice crystals clinging to his lashes and brows", outfit=CY_ICE, shut='gently closed'),
     P('xuran', 'center-left', "standing in the foreground in profile facing frame-right pressed against his chest, both hands gripping the back of his overcoat, her face tilted up toward his", 'closed', "her face calm and peaceful under a layer of white frost, one tiny frozen tear on her cheek", outfit=XR_ICE, shut='gently closed')],
    'Medium-wide low-angle shot just above the snow, the two embracing figures from the head to the knees in the middle third of the frame in the foreground, and behind them the whole plaza.',
    "<chenyu> and <xuran> stand sealed in clear ice in their embrace in the foreground, snow piled thick on their shoulders and hair, perfectly still. Behind them across the plaza dozens of other people stand sealed in clear glittering ice in the poses they froze in: some caught mid-run with an arm stretched forward, some crouched, some reaching toward each other, pairs and small groups huddled together, every one of them perfectly still with snow piled on their heads and shoulders. Heavy snow falls in big slow flakes that slant on the wind, and fine powder snow streams low along the ground. Nothing moves except the falling snow and the drifting powder. The camera glides forward low over the snow past the embracing figures while rising slowly on a crane until the whole plaza with the two small embracing figures and the dozens of frozen people fills the frame.",
    "陈屿和许然在前景保持着拥抱，被封在晶莹发亮的冰里，肩上和头发上堆着厚厚的雪，一动不动。他们身后，整个广场上还有几十个人被封在透明发亮的冰里，保持着冻住那一刻的姿势：有的跑到一半手臂向前伸着，有的蹲着，有的朝对方伸着手，还有成对的、成小群抱在一起的，每个人都一动不动，头上肩上堆着雪。大片的雪花顺着风斜斜地慢慢落下，细细的雪粉贴着地面流过。除了落雪和飘动的雪粉，什么都不动。镜头贴着雪面低低地向前滑过相拥的两个人，同时像吊臂一样缓缓升高，直到整个广场、两个小小的相拥的身影和几十个冰封的人占满画面。",
    Q('The long low howl of a snowstorm wind sweeping across the empty plaza, the hiss of snow driven over ice, the soft rustle of heavy flakes and, far off, one slow crack of ice from a tower.', '暴风雪长长低低的呼啸掠过空荡荡的广场、雪粒被风吹过冰面的嘶嘶声、大片雪花轻轻的沙沙声，远处一座大楼传来一声缓慢的冰裂声。'),
    AES_F01,
    holds='The frame holds the two embracing frozen figures in the foreground, dozens of other frozen people standing sharp and clear across the plaza, the buried cars and the icicle-hung towers.',
    groups=[('the frozen crowd', 'back', 'obj:the falling snow')], room={'Chenyu', 'Xuran', 'the frozen crowd'},
    bg='Behind them dozens of frozen people stand across the snowy plaza, all sharp and clear, none blurred, in poses of running, crouching, reaching and holding each other, with the icicle-hung towers at the back.',
    cam=('The camera glides forward low over the snow past the embracing figures while rising slowly on a crane until the whole plaza and the dozens of frozen people fill the frame.', '镜头贴着雪面低低地向前滑过相拥的两个人，同时像吊臂一样缓缓升高，直到整个广场和几十个冰封的人占满画面。'))

doc = S.finish()
report()
