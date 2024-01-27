#!/bin/bash
c0=$(echo $1 |wc -c )
#echo $c0
if [ $c0 -le 1 ]
then
        echo "chroot no argument."
        exit 1
else
        :
fi
d1=$1
s3=$(which bash)
command="sudo proot"
#command="$PWD/bin/libjudger.so --exe_path=$3 --args='proot -0'" 
#command+=" -i $s2:$s2 "   
command+=" -0 "   
command+=" -r multiserv/$d1/root -b /dev/null:/dev/null "

command+=" -b /sys/fs/selinux/null:/sys/fs/selinux/null "  
command+=" -b /dev/tty:/dev/tty " 
#command+=" $PWD/bin/libjudger.so --exe_path=$s3 --seccomp_rule_name=\"nokill\""    
#command+=" /bin/sh"     
command+=" $s3 -c ./incage.sh"     
$command
