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
d1=$1
sudo touch judger.log
sudo chmod 777 judger.log
s0=$(sudo mount 2>&1 | grep $PWD/multiserv/$1/ramdisk | grep myramdisk |  wc -c)
s1=$(sudo mount 2>&1 | grep $PWD/multiserv/$1/root | grep unionfs |  wc -c)
if [ $s0 -eq 0 ]
then
#	echo ram
	bash -c "./multiram.sh $d1"
fi
if [ $s1 -eq 0 ]
then
#	echo root
	bash -c "./multiroot.sh $d1"
fi
s7=$(which tmux)
s6=$(sudo which init)
s5=$(sudo which kill)
s9=$(sudo which su)
s10=$(sudo which sudo)
s4=$(which kill)
s8=/system/bin/kill
s11=/sbin/su
#echo $s7 | python3 efilter.py ramdisk
# it is able to kill itself.
# sorry. no one can stop that from happening.
# and that is part of the game.
echo $s6 | python3 efilter.py multiserv/$1/ramdisk | xargs sudo mkdir -p
echo $s5 | python3 efilter.py multiserv/$1/ramdisk | xargs sudo mkdir -p
echo $s4 | python3 efilter.py multiserv/$1/ramdisk | xargs sudo mkdir -p
echo $s7 | python3 efilter.py multiserv/$1/ramdisk | xargs sudo mkdir -p
echo $s8 | python3 efilter.py multiserv/$1/ramdisk | xargs sudo mkdir -p
echo $s9 | python3 efilter.py multiserv/$1/ramdisk | xargs sudo mkdir -p
echo $s10 | python3 efilter.py multiserv/$1/ramdisk | xargs sudo mkdir -p
echo $s11 | python3 efilter.py multiserv/$1/ramdisk | xargs sudo mkdir -p
sudo touch multiserv/$1/ramdisk$s6
sudo touch multiserv/$1/ramdisk$s5
sudo touch multiserv/$1/ramdisk$s9
sudo touch multiserv/$1/ramdisk$s11
sudo touch multiserv/$1/ramdisk$s10
sudo touch multiserv/$1/ramdisk$s4
sudo touch multiserv/$1/ramdisk$s8
sudo touch multiserv/$1/ramdisk$s7
sudo chmod 777 multiserv/$1/root
sudo chmod 777 multiserv/$1/ramdisk
#s2=$(id nobody -u)
#unset LD_PRELOAD
#set LD_PRELOAD=/lib/libtermux-exec.so
#set LD_LIBRARY=/lib
bash -c "./multichroot.sh $d1"
#command="bash -c './multichroot.sh $d1'"
#command="sudo $PWD/bin/libjudger.so --exe_path=$PWD/chroot.sh"
#command+=" -i $s2:$s2 "
#command+=" --seccomp_rule_name=\"nokill\""
#$command
