#!/data/data/com.termux/files/usr/bin/bash
# cd $(dirname $0)
## unset LD_PRELOAD in case termux-exec is installed
#./loadram.sh
./tloadroot.sh
sudo chmod 777 root
#unset LD_PRELOAD
#set LD_PRELOAD=/lib/libtermux-exec.so
#set LD_LIBRARY=/lib
command="sudo proot"
command+=" -0 "
command+=" -r root -b /dev/null:/dev/null "
command+=" -b /sys/fs/selinux/null:/sys/fs/selinux/null "
command+=" -b /dev/tty:/dev/tty "
$command
# no need to use selinux/null.
