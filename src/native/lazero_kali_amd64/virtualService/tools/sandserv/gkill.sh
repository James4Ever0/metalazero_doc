#!/bin/bash
sudo env COLUMNS=500 LINES=500 top -n 1 -q 2>&1 | grep proot | grep root | grep -Eo '^.?.?.?[0-9]+' | xargs sudo kill -s 9
env COLUMNS=500 LINES=500 top -n 1 -q 2>&1 | grep bash | grep chroot.sh | grep -Eo '^.?.?.?[0-9]+'  | xargs kill -s 9 
env COLUMNS=500 LINES=500 top -n 1 -q 2>&1 | grep bash | grep reloadscript.sh | grep -Eo '^.?.?.?[0-9]+'  | xargs kill -s 9 
