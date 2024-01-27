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
./multiunloadram.sh $1
sudo mkdir -p multiserv/$1/ramdisk
sudo chmod 777 multiserv/$1/ramdisk
sudo mount -t tmpfs -o size=10m myramdisk multiserv/$1/ramdisk
