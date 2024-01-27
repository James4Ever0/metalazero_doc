#!/bin/bash
#sudo ls -1 multiserv | xargs -I % bash -c "./multikill.sh %"
sudo ls -1 multiserv | xargs -I % bash -c "./multiterm.sh %"
./unloadmulti.sh
sudo rm -rf multiserv
# you need to unload the thing.
