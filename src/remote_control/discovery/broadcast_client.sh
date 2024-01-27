#!/bin/bash
cnt=200
while true
do
	if [ $cnt -gt 0 ]; then
		python3 broadcast_client.py
		cnt=$(( $cnt - 1 ))
		echo sending packet $cnt
	else
		break
	fi
done
