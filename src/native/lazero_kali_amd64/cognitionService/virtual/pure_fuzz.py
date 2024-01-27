#import sys
import argparse
parser=argparse.ArgumentParser()
parser.add_argument('-d','--depth',type=int,help='depth of possible flags combination',default=2)
parser.add_argument("-p","--prefix",action="store_true")
args=parser.parse_args()

depth=args.depth
pre=args.prefix
candidates=[chr(x+ord('a'))for x in range(26)]
candidates=candidates+[x.upper() for x in candidates]

import itertools
prefix="" if not pre else "-"
flags=[prefix+"".join(x) for x in itertools.combinations(candidates,depth)]

#print(pargs)
for x in flags:
    print(x)
