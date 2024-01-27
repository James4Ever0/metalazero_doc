formula=lambda x: x/(1+2**x)
import time
for x in range(0,1000):
    v=x/50
    if x%50==0:
        v=formula(v)
        print(round(v*50)*"*")
        time.sleep(0.1)
