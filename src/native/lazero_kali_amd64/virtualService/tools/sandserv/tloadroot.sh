#!/bin/bash
bash -c ./tunloadroot.sh
bash -c ./loadram.sh
mkdir root
# there's autodetect.
# better use bindfs as standard.
s0=$(id -u)
sudo bin/unionfs -o allow_root,cow,uid=$s0,gid=$s0 ramdisk/=RW:/=RO root/
sudo chmod 777 root
