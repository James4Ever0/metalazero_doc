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
sudo rm -f multiserv/$1/ramdisk/*
sudo find -P multiserv/$1/ramdisk/ | xargs sudo unlink
sudo rm -rf multiserv/$1/ramdisk/*
