#!/bin/bash
# the shit must be running on the background.
# can we run this under bash?
# cannot find the cli args.
ps aux | cat | grep node | grep chrome_receive | awk '{print $2}' | xargs kill -s SIGKILL
cd eventService && node chrome_receive.js &
cd replService && node chrome_console.js
cd ../
# ps -W <- show both processes.