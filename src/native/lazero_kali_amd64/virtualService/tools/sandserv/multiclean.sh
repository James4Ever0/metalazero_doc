#!/bin/bash
#sudo ls -1 multiserv | xargs -I % bash -c "./multikill.sh %"
sudo ls -1 multiserv | xargs -I % bash -c "./mclean.sh %"
#./unloadmulti.sh
#sudo rm -rf multiserv
# you need to unload the thing.
