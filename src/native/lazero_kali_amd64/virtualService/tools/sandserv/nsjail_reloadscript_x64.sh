#!/bin/bash
sudo touch judger.log
sudo chmod 777 judger.log
s0=$(sudo mount 2>&1 | grep $PWD/ramdisk | grep myramdisk |  wc -c)
s1=$(sudo mount 2>&1 | grep $PWD/root | grep unionfs |  wc -c)
if [ $s0 -eq 0 ]
then
	bash -c ./loadram.sh
fi
if [ $s1 -eq 0 ]
then
	bash -c ./treloadroot_x64.sh
fi
s7=$(which tmux)
s6=$(sudo which init)
#s5=$(sudo which kill)
#s9=$(sudo which su)
s10=$(sudo which sudo)
s4=$(which kill)
#s8=/system/bin/kill
#s11=/sbin/su
#echo $s7 | python3 efilter.py ramdisk
# it is able to kill itself.
# sorry. no one can stop that from happening.
# and that is part of the game.
echo $s6 | python3 efilter.py ramdisk | xargs sudo mkdir -p
#echo $s5 | python3 efilter.py ramdisk | xargs sudo mkdir -p
echo $s4 | python3 efilter.py ramdisk | xargs sudo mkdir -p
echo $s7 | python3 efilter.py ramdisk | xargs sudo mkdir -p
#echo $s8 | python3 efilter.py ramdisk | xargs sudo mkdir -p
#echo $s9 | python3 efilter.py ramdisk | xargs sudo mkdir -p
echo $s10 | python3 efilter.py ramdisk | xargs sudo mkdir -p
#echo $s11 | python3 efilter.py ramdisk | xargs sudo mkdir -p
sudo touch ramdisk$s6
#sudo touch ramdisk$s5
#sudo touch ramdisk$s9
#sudo touch ramdisk$s11
sudo touch ramdisk$s10
sudo touch ramdisk$s4
#sudo touch ramdisk$s8
sudo touch ramdisk$s7
sudo chmod 777 root
sudo chmod 777 ramdisk
./pivot.sh
#./command_x64.sh
#command="bash -c ./chroot.sh"
#command="sudo $PWD/bin/libjudger.so --exe_path=$PWD/chroot.sh"
#command+=" -i $s2:$s2 "
#command+=" --seccomp_rule_name=\"nokill\""
#$command
