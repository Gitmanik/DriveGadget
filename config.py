from luma.core.interface.serial import i2c
from luma.oled.device import sh1106 

from common import *

MNT_POINT = "/mnt/gadget"

FONT_BIG = make_font("UbuntuMono-R.ttf", 20)
FONT_NORMAL = make_font("UbuntuMono-R.ttf", 15)
FONT_SMALL = make_font("UbuntuMono-R.ttf", 12)

OLED = sh1106(i2c(port=1, address=0x3c))
MNT_POINT = "/mnt/gadget"