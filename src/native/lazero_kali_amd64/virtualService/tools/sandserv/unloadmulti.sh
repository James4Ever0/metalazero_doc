#!/bin/bash
sudo umount -f multiserv
psk=$(sudo ls -1 multiserv/ | wc -c)
# if failed, then do not continue! unless you are an idiot.
# or not.
# just think! also for symlink on windows. caution when doing chroot/symlink.
if [ $psk -eq 0 ]
then
	sudo rm -rf multiserv
fi
