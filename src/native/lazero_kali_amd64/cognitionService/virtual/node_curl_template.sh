#!/bin/bash
python3 pure_fuzz.py -d 3 | xargs -iabc bash -c "rm node_curl_telnet_abc.js"
#python3 pure_fuzz.py -d 3 | xargs -iabc bash -c "sed \"s/TEMPLATE/abc/g\" node_curl_telnet.template > node_curl_telnet_abc.js"
