# this is real time clock prediction.
import time
import random

rng=lambda:random.randint(2,5)
p=rng()
while True:
    print("clock ticking.")
    p-=1
    if p<=0:
        print("SURPRISE!")
        p=rng()
    time.sleep(1)
