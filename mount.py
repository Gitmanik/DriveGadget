from dialog_oled import *
import os

def mount_com(name):
    if name.endswith(".iso"):
        mount_iso(name)
    else:
        dialog_ok("Error", f"Cannot mount {name[:4]} yet.")
        return

def mount_iso(name):
    active = os.path.ismount(MNT_POINT)
    if active:
        print("needs umount")
        c = os.system("umount " + MNT_POINT)
        print(c)
    code = os.system(f"mount -o loop,ro {name} {MNT_POINT}")
    print(code)