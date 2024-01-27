#!/bin/bash
c0=$(echo $1 |wc -c )
#echo $c0
if [ $c0 -le 1 ]
then
        echo "no argument."
        exit 1
else
        :
fi
bash -c "./multiunloadroot.sh $1"
sudo mkdir -p multiserv/$1/root
# there's autodetect.
#better use bindfs as standard.
sudo bin/unionfs -o allow_root,cow,uid=0,gid=0 multiserv/$1/ramdisk/=RW:/=RO multiserv/$1/root/
sudo chmod 777 multiserv/$1/root
