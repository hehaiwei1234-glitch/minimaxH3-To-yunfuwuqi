"""《极寒末日》补拍包共用的定义（2026-10-14）：运镜词汇表（hh 10-14 09:51 “运镜太死板，要大电影感”）、新外貌、声音。
运镜仍写成“动作＋终点”（H22：13 个里 12 个做出来）；这里的拉远、升降、跟拍、低机位都是第一次用，风险写在交稿说明里。"""
from _jihan_base3 import *


def pull(what_en, what_zh, to_en, to_zh):
    return (f'The camera starts close on {what_en} and pulls back slowly until {to_en} fills the frame.',
            f'镜头从{what_zh}的特写开始慢慢拉远，直到{to_zh}占满画面。')


def rise(to_en, to_zh):
    return (f'The camera rises slowly on a crane until {to_en} fills the frame.', f'镜头像吊臂一样缓缓升高，直到{to_zh}占满画面。')


def descend(to_en, to_zh):
    return (f'The camera descends slowly on a crane from high above until it hangs at street level and {to_en} fills the frame.',
            f'镜头像吊臂一样从高处缓缓降下来，停在街面的高度，{to_zh}占满画面。')


def follow(who_en, who_zh, to_en, to_zh):
    return (f'The camera follows behind {who_en} at walking pace until {to_en}.', f'镜头在{who_zh}身后以步行的速度跟着，直到{to_zh}。')


def slide(dir_en, dir_zh, end_en, end_zh):
    return (f'The camera slides slowly {dir_en} until {end_en}.', f'镜头缓缓向{dir_zh}平移，直到{end_zh}。')


look('bbq_vendor', 'Vendor', "in a sweat-stained white tank top and a greasy apron with a towel over one shoulder", 'small bright', 'his', eth='a stocky Chinese man in his forties')
look('office_guy', 'Clerk', "in a white dress shirt with rolled sleeves and a loosened tie", 'relaxed dark', 'his', eth='a Chinese office worker in his thirties')
look('raider_lean', 'Lean', "in a torn camouflage jacket with a dirty scarf pulled up over his mouth and nose, a steel crowbar in one hand", 'jittery bloodshot', 'his', eth='a wiry Chinese man in his twenties')

VENDOR_EN = 'A loud adult male street-vendor voice, hearty and raspy, speaking clear Mandarin Chinese.' + VT_EN
VENDOR_ZH = '洪亮的成年男声，摊贩的嗓子，爽朗带沙，普通话清楚。' + VT_ZH
CLERK_EN = 'A relaxed adult male voice, a little tipsy and cheerful, speaking clear Mandarin Chinese.' + VT_EN
CLERK_ZH = '放松的成年男声，微醺而愉快，普通话清楚。' + VT_ZH
LEAN_EN = 'A shrill young adult male voice, jittery and mean, speaking clear Mandarin Chinese.' + VT_EN
LEAN_ZH = '尖利的年轻男声，神经质又阴狠，普通话清楚。' + VT_ZH

SOUND_CROWD = voiced('The bright din of a busy boulevard at noon: traffic, chatter, cicadas and the sizzle of a grill.', '中午热闹大街的嘈杂：车流、人声、知了和烤架的滋滋声。')
SOUND_WIND = breathy('A rising low howl of wind and a deep creak of ice spreading.', '渐渐变大的低沉风声和冰层蔓延时深沉的嘎吱声。')
SOUND_FROZEN = breathy('A thin long howl of wind through frozen streets and the faint tick of ice settling.', '风穿过冰封街道长长的呼啸和冰层沉降时细细的嘀嗒声。')
