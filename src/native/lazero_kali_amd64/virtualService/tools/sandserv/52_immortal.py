#!/usr/bin/env python

#
# Seccomp Library test program
#
# Copyright (c) 2019 Cisco Systems, Inc. <pmoore2@cisco.com>
# Author: Paul Moore <paul@paul-moore.com>
#

#
# This library is free software; you can redistribute it and/or modify it
# under the terms of version 2.1 of the GNU Lesser General Public License as
# published by the Free Software Foundation.
#
# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License
# for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this library; if not, see <http://www.gnu.org/licenses>.
#

import argparse
import sys
import os

import util

from seccomp import *
import errno
# check for official libseccomp tests for usage!


def test():
#    set_api(3)
    util.install_trap()
    f = SyscallFilter(ALLOW)
#    f.remove_arch(Arch())
#    f.add_arch(Arch("x86_64"))
#    f.add_arch(Arch("x86"))
    #f.add_rule_exactly(ERRNO(13),"kill")
    f.add_rule_exactly(ERRNO(errno.EACCES),"kill")
    # add more shits.
    f.load()

test()
print("about to launch restricted bash.")
os.system("./reloadscript_x64.sh")
print("exit restricted bash.")
# kate: syntax python;
# kate: indent-mode python; space-indent on; indent-width 4; mixedindent off;
