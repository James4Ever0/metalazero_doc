truth=open("base.py","r").read().split("\n")
truth=list(filter(lambda x: len(x)> 2, truth))
import random
import traceback
window=5
import tty
import sys
tty.setcbreak(sys.stdin)
while True:
    try:
        r=random.choice(truth)
        fst=r[:5]
        nxt=r[5:]
        r1=fst
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
