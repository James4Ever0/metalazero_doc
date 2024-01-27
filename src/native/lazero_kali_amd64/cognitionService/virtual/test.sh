#!/bin/bash
# you are not echoing them.
echo hello > hello
cat hello >(tee -a stdout.log)
#cat hello 1>(tee -a stdout.log) 2>(tee -a stderr.log)
