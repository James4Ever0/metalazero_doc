#!/bin/bash
echo "[$(date)] speaking: $@"
espeak -a 200 -p 100 "$@"
sleep 2
