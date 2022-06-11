#!/usr/bin/env python3

from luma.core.render import canvas

import os
from dialog_oled import *
from mount import *
from common import *

from config import *

dialog_time("USB Gadget", "Gitmanik 2022", 2.5)

with canvas(OLED) as draw:
    dada = os.listdir("data/")
    ctr = 0
    print(dada)
    for da in dada:
        draw.text((0, 9*ctr), text=da, fill="white", font=FONT_SMALL)
        ctr +=1

mount_iso("data/dsl-4.11.rc1.iso") # TODO: Remove

input()