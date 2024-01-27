truth0=open("base.py","r").read().split("\n")
truth0=list(filter(lambda x: len(x)> 2, truth0))
import copy
truth=copy.deepcopy(truth0)
truth=[x.split() for x in truth]
truth=list(set([x for y in truth for x in y]))
def findall(content,target,span=5):
    cnt=copy.deepcopy(content)
    cur=0
    r=[]
    while cur != -1:
        cur=cnt.find(target)
        if cur != -1:
            x,y=cur-span,cur+len(target)+span
            if x<0:
                x=0
            result=cnt[x:y]
            r.append(result)
            cnt=cnt[y:]
    return r
import random
import traceback
window=5
import tty
import sys
tty.setcbreak(sys.stdin)
while True:
    rtoken=random.choice(truth)
    rtarget=[findall(x,rtoken) for x in truth0]
    rtarget=[x for y in rtarget for x in y]
    random.shuffle(rtarget)
    for r in rtarget:
        print("searching token:", rtoken)
        fst=r[:5]
        nxt=r[5:]
        r1=fst
        try:
            for r0 in nxt:
                print("question:",r1)
                print("answer:")
                ans=sys.stdin.read(1)
                if ans == r0:
                    print("correct!")
                else:
                    print("incorrect!")
                    print("the correct answer is:", r0)
                    print("your answer is:", ans)
                r1+=r0
            print("correct form:",r)
            print("continue?")
            input()
        except:
            traceback.print_exc()
            print("exception printed above!")
            pass
