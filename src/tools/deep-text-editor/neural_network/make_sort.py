truth=open("base.py","r").read().split("\n")
truth=list(filter(lambda x: len(x)> 2, truth))
import random
import copy
import traceback

base=[x for x in range(len(truth))]
b1=copy.deepcopy(base)
while True:
    try:
        random.shuffle(base)
        r1=["{}: {}".format(i,truth[x]) for i,x in enumerate(base)]
        print("question:")
        print("\n".join(r1))
        ans=input("answer:\n")
        b0=[None]*len(b1)
        for z in b1:
            x,y = base[z],b1[z]
            b0[x] = y
        r0 = " ".join([str(x) for x in b0])
        if ans == r0:
            print("correct!")
        else:
            print("incorrect!")
            print("the correct answer is:", r0)
            print("your answer is:", ans)
        print("continue?")
        input()
        #print("correct form:","\n".join(truth))
    except:
        traceback.print_exc()
        print("exception printed above!")
        pass
