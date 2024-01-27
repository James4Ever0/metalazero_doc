#!/bin/bash
env COLUMNS=500 LINES=500 top -n 1 -q 2>&1 | grep bash | grep reloadscript | grep -Eo '^.?.?.?[0-9]+'  | xargs kill
bash -c ./tunloadroot.sh
bash -c ./unloadram.sh
