#!/bin/bash
# the shit must be running on the background.
# this is to kill those running processes.
ps aux | cat | grep node | grep chrome_receive | awk '{print $2}' | xargs kill -s SIGKILL
cd eventService && node chrome_receive.js &
cd replService && node chrome_console.js &
# are you sure that you will not upload those sensitive data?

# launch the virtualService.
ps aux | cat | grep python3 | grep ptyproc.py | awk '{print $2}' | xargs kill -s SIGKILL
cd virtualService/shellService && python3 ptyproc.py -p 8778
cd ../../ # make sure it is launching and blocking?
