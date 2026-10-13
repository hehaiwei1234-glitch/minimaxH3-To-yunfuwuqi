"""《极寒末日》第 13 集起共用的定义：第 9–12 集（006）新增的外貌／场景／声音，从 gen_jihan_ep9_12_006.py 原样复制。007 先 `from _jihan_base3 import *`。006 生成脚本一字不动。"""
from _jihan_base2 import *

look('lin_white', 'LinWhite', "in a clean white dress shirt with the sleeves rolled to his forearms and dark trousers, his black hair neatly combed", 'steady dark-brown', 'his', eth=CN30)
look('su_cozy', 'SuCozy', "in an oversized soft cream knit sweater and black thermal leggings, thick grey socks, her long black hair loose over her shoulders", 'soft dark-brown', 'her', eth=CN_F28)
look('su_surgeon', 'SuSurgeon', "in a fitted black long-sleeve thermal top and dark trousers, white surgical gloves, thin gold-rimmed glasses on her nose, her long black hair pinned in a tight bun", 'focused dark-brown', 'her', eth=CN_F28)

# ---------------------------------------------------------------------------------------------- 新场景
SOFA = Scene('bunker_sofa', " Warm amber light from soft recessed lamps fills the cozy underground living area.",
             " Fixed stage layout: a deep brown leather sofa with a thick grey cashmere blanket stands in the middle of the frame facing the room, with a low wooden coffee table in front of it; the open kitchen with the black-and-gold stove is at frame-left; a wall of small security monitors is at center-right behind the sofa; the heavy round steel hatch door is in the right wall at far frame-right.")
MED = Scene('med_room', " Hard white light from a round surgical lamp falls on the small windowless medical room.",
            " Fixed stage layout: a steel operating table covered with a sterile blue drape stands in the middle of the frame under a round surgical lamp; a steel instrument tray with an open silver metal case stands at frame-left; a plain steel chair stands at frame-right; the white-tiled walls fill the background.")
EDENDOOR = Scene('eden_door', " Cool concrete-corridor light with a thin glow of pink-violet leaking through the gap around the door.",
                 " Fixed stage layout: the bare concrete corridor fills the frame; a heavy steel door with a keypad stands at frame-right with a thin line of pink-violet light glowing around its edges.")
PUMP = Scene('pump_room', " Hard white work-lamp light falls on the damp compact concrete pump room.",
             " Fixed stage layout: a huge clear acrylic water tank stands at frame-right; thick transparent pipes run along the left wall to a steel pump station; a control panel with one big green start button stands in the middle of the frame; the floor is damp with a drain.")
BATH = Scene('bathroom', " Warm soft light and thick white steam fill the tiled bathroom.",
             " Fixed stage layout: a frosted-glass shower door with a rainfall shower head behind it stands at frame-center-left; a wooden bench with folded white towels and a folded grey cotton shirt stands at frame-right; the wall is white tile.")
EDEN = Scene('eden', " Rows of pink-violet full-spectrum grow lamps bathe the vast underground farm level in a dreamy glow.",
             " Fixed stage layout: long tiers of white hydroponic channels full of young lettuce and tomato seedlings fill the middle of the frame under rows of hanging pink-violet grow lamps; a warm incubator box with a glass window and a red heat lamp stands at frame-right; a steel staircase rises at frame-left; the concrete walls fill the background.")
COLD = Scene('cold_store', " Frosty cold white light falls on the walk-in cold store.",
             " Fixed stage layout: steel shelving stacked with white boxes of frozen meat, seafood and vegetables fills the left and middle of the frame; a shelf at eye level holds brightly packaged hotpot base boxes in the middle; a heavy insulated door stands at frame-right.")
CHUTE = Scene('snow_stump', " A silent frozen forest under a black sky with a faint green aurora; the white light of the snow glows.",
              " Fixed stage layout: a snow-capped boulder is at frame-left; a dead tree stump with a small round dark glass lens in its side stands at center-left; in the snow in front of the stump a long smooth dark chute slopes down into the ground; snow-laden pines stand in the background.")


SOUND_MED = voiced('The faint hum of the surgical lamp, the soft clink of steel instruments and slow breathing.', '手术灯轻微的嗡鸣、钢器械轻轻的碰撞声和缓慢的呼吸声。')
SOUND_BUNKER = voiced('The faint hum of the air system and the low murmur of a generator far away.', '空气系统轻微的嗡鸣和远处发电机低低的运转声。')
