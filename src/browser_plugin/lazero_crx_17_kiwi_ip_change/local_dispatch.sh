#!/bin/bash
#rm ../lazero_crx_releases/chrome-.zip
getNumber=$(ls ../lazero_crx_releases -1 | grep chrome | grep -o "[0-9]*" | sort | tail --lines 1 | awk '{print 1+$0;exit}')
zip -r ../lazero_crx_releases/chrome-$getNumber.zip *
