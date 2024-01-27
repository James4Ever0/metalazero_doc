import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d","--dir",type=str,required=True,help="absolute directory to change all files under it into executables.")
args = parser.parse_args()

import os.path as P
import os

_dir = args.dir
assert P.isabs(_dir)
assert P.isdir(_dir)

# execute the shell script?
import tempfile

cmd = ["#!/bin/bash","cd {}".format(_dir),"find | xargs -iabc chmod +x abc"]
cmd = "\n".join(cmd)

from uuid_fname import ufname

with tempfile.TemporaryDirectory() as tmpdir:
    assert P.isabs(tmpdir)
    fname = ufname("sh")
    script_path = P.join(tmpdir,fname)
    with open(script_path,"w+",encoding="utf-8") as f:
        f.write(cmd)
    os.system("chmod +x {}".format(script_path))
    os.system(script_path)
