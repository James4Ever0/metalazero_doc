#import sys
targets=[]
# this is program database.
while True:
#    line=sys.stdin.readline()
    line = input()
    if line not in targets:
        targets.append(line)
        print("found uniq target:\n",line)
