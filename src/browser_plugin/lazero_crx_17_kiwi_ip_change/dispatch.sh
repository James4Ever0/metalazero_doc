#!/bin/bash
vd=$(ls ~/storage/shared/chrome/ -1 | wc -l | awk '{print $0}')
zip -r ~/storage/shared/chrome/chrome-$vd.zip *
