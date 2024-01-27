import random
import math
thr=23
import time
base=lambda x:0.2*math.sin(x)

freq=lambda:random.random()
sm=0
for x in range(5000):
    f=base(x)+freq()
    sm+=f
    sm%=(2 * thr)
    print("frequency:",f)
    print("sum:",sm)
    amp=sm-thr
    if amp>0 and amp <2:
        print("stimulation!",1-abs(amp-1))
    time.sleep(0.3)
