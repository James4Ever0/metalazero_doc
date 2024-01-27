#!/bin/bash
ifconfig | grep -Eo "broadcast.+" | grep -Eo "[0-9]+.[0-9]+.[0-9]+.[0-9]+" | xargs -iabc python3 broadcast_client.py -i abc
