#!/bin/sh

set -u
set -e

# Add a console on tty1
if [ -e ${TARGET_DIR}/etc/inittab ]; then
    grep -qE '^tty1::' ${TARGET_DIR}/etc/inittab || \
	sed -i '/GENERIC_SERIAL/a\
tty1::respawn:/sbin/getty -L  tty1 0 vt100 # HDMI console' ${TARGET_DIR}/etc/inittab
fi
rm -rf ${TARGET_DIR}/opt/app
git clone https://github.com/Gitmanik/DriveGadget.git ${TARGET_DIR}/opt/app
mv ${TARGET_DIR}/opt/app/S99app ${TARGET_DIR}/etc/init.d
chmod +x ${TARGET_DIR}/opt/app/run.sh
chmod +x ${TARGET_DIR}/etc/init.d/S99app
