import os
#import sys
import argparse
parser=argparse.ArgumentParser()
parser.add_argument('-p','--program',type=str,help='program name to launch',required=True)
parser.add_argument('-d','--depth',type=int,help='depth of possible flags combination',default=2)
parser.add_argument('args',metavar='N',type=str,nargs='+',help='subargs passing to program')
args=parser.parse_args()

program=args.program
depth=args.depth
pargs=args.args
candidates=[chr(x+ord('a'))for x in range(26)]
candidates=candidates+[x.upper() for x in candidates]

import itertools
flags=["-"+"".join(x) for x in itertools.combinations(candidates,depth)]

#print(pargs)
for x in flags:
    cmd=" ".join([program,x,*pargs])
    print(cmd)
