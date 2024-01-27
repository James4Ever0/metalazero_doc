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
sudo env COLUMNS=500 LINES=500 top -n 1 -q 2>&1 | grep proot | grep multiserv/$1/root | grep -Eo '^.?.?.?[0-9]+' | xargs  sudo kill -s 9 
env COLUMNS=500 LINES=500 top -n 1 -q 2>&1 | grep bash | grep multichroot | grep -E "\.sh.?.?.?$1" | grep -Eo '^.?.?.?[0-9]+'  | xargs kill -s 9
env COLUMNS=500 LINES=500 top -n 1 -q 2>&1 | grep bash | grep multireload | grep -E "\.sh.?.?.?$1" | grep -Eo '^.?.?.?[0-9]+'  | xargs kill -s 9 
