#!/bin/bash
s3=$(which bash)
command="sudo proot"
#command="$PWD/bin/libjudger.so --exe_path=$3 --args='proot -0'" 
#command+=" -i $s2:$s2 "   
command+=" -0 "   
command+=" -r root -b /dev/null:/dev/null "

command+=" -b /sys/fs/selinux/null:/sys/fs/selinux/null "  
command+=" -b /dev/tty:/dev/tty " 
#command+=" $PWD/bin/libjudger.so --exe_path=$s3 --seccomp_rule_name=\"nokill\""    
#command+=" /bin/sh"     
command+=" $s3 -c ./incage.sh"     
$command
