#!/bin/bash
#sed "s/{/{\n/g" background.js
#sed "s/\;/\;\n/g" background.js
sed -i -f format.sed background.js
