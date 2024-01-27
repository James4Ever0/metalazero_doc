#!/bin/bash
export PROOT_NO_SECCOMP=0
command="bin/x86_64/proot"
command+=" -0 "
#command+=" -r root --cwd=$PWD --pwd=$PWD"
command+=" -r root -b /dev/null:/dev/null "
#command+=" bin/x86_64/libjudger.so --max_cpu_time=100 --exe_path=$(which bash)"
#command+=" bin/x86_64/libjudger.so --max_cpu_time=100 --exe_path=$(which bash) --seccomp_rule_name=nokill"
#command+=" -b /sys/fs/selinux/null:/sys/fs/selinux/null "
#command+=" -b /dev/tty:/dev/tty "
#command+=" -b /dev/stdin:/dev/stdin "
#command+=" -b /dev/stdout:/dev/stdout "
#command+=" -b /dev/stderr:/dev/stderr "
$command
