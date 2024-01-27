import random
# filter out those needless to execute.
rng=lambda:random.randint(2,5)
targets=["type","move","select","click"]
rtg=lambda:random.choice(targets)
import time
tgs=[]
while True:
    tgs.append((rng(),rtg()))
    tgs=[(x[0]-1,x[1]) for x in tgs]
    tgs=list(sorted(tgs))
    tm=[x for x in tgs if x[0] == 0]
    tl=[x for x in tgs if x not in tm]
    print("executing:",tm)
    print("pending:",tl)
    time.sleep(1)
    tgs=tl
