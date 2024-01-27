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
bash -c "./multikill.sh $1"
bash -c "./multiunloadroot.sh $1"
bash -c "./multiunloadram.sh $1"
