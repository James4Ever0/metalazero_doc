#!/bin/bash
bin/libjudger.so --exe_path=$(which bash) --seccomp_rule_name=freeze
#bin/libjudger.so --exe_path=$PWD/runas.sh --seccomp_rule_name=nokill
