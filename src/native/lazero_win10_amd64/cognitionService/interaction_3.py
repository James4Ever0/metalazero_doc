import shellConnect as Sc

# to represent how you type these words? type it exactly according to what you've done in the past?
# we want it to learn anything from this process.
import time as T
clist=["hello world{}".format(x) for x in range(5)]
cnt=0
import random as R
SR=R.SystemRandom()

def rsel(string):
    try:
        return SR.choice(string.split())
    except:
        return ""
nx,override="",False

while True:
    Sc.restart()
    if not override:
        cmd=clist[cnt]
        Sc.inputs(cmd)
    else:
        Sc.inputs(nx)
    T.sleep(1)
    content = Sc.display()
    print(content)
    nx=rsel(content)
    if nx!="":
        override=True
    cnt+=1
    cnt%=len(clist)
