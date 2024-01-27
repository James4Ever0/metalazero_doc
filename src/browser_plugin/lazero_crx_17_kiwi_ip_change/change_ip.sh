target_ip=$1
ls -1 | grep js | xargs -iabc sed -i "s/localhost:4999/$target_ip:4999/g" abc
