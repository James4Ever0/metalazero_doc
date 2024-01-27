#!/bin/bash
bash -c ./tunloadroot.sh
mkdir root
# there's autodetect.
#better use bindfs as standard.
sudo bin/unionfs -o allow_root,cow,uid=0,gid=0 ramdisk/=RW:/=RO root/
sudo chmod 777 root
