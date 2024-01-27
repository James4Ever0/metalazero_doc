#!/bin/bash
./unloadmulti.sh
sudo mkdir multiserv
sudo chmod 777 multiserv
sudo mount -t tmpfs -o size=10m myramdisk multiserv
