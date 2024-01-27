#!/bin/bash
# cd $(dirname $0)
## unset LD_PRELOAD in case termux-exec is installed
#./loadram.sh
./tloadroot_x64.sh
sudo chmod  777 root
#sudo chmod -R 777 root
#unset LD_PRELOAD
#set LD_PRELOAD=/lib/libtermux-exec.so
#set LD_LIBRARY=/lib
#bin/x86_64/libjudger.so  --exe_path="./command_x64.sh"
#bin/x86_64/libjudger.so  --seccomp_rule_name="nokill" --exe_path="./command_x64.sh"
#command="sudo proot"
#command+=" -0 "
#command+=" -r root -b /dev/null:/dev/null "
##command+=" -b /sys/fs/selinux/null:/sys/fs/selinux/null "
#command+=" -b /dev/tty:/dev/tty "
#$command
./command_x64.sh
# no need to use selinux/null.
