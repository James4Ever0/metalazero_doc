import shellConnect as Sc

# to represent how you type these words? type it exactly according to what you've done in the past?
# we want it to learn anything from this process.
import time as T
clist=["hello world{}".format(x) for x in range(5)]
cnt=0
while True:
    Sc.restart()
    cmd=clist[cnt]
    Sc.inputs(cmd)
    T.sleep(1)
    content = Sc.display()
    print(content)
    cnt+=1
    cnt%=len(clist)
