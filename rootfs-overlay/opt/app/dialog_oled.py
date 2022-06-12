from interact import *
from common import *
from config import *
from luma.core.render import canvas
import time

def dialog_ok(title, text):
    with canvas(OLED) as draw:  
        draw_middle(draw, FONT_BIG, title, 25)
        draw_middle(draw, FONT_NORMAL, text, 40)

        draw_middle(draw, FONT_NORMAL, "[ok]", 60)
        
        wait_ok()

def dialog_time(title, text, t):
    with canvas(OLED) as draw:  
        draw_middle(draw, FONT_BIG, title, 25)
        draw_middle(draw, FONT_NORMAL, text, 40)

    time.sleep(t)

