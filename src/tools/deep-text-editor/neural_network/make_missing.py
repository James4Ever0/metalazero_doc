truth=open("base.py","r").read().split("\n")
truth=list(filter(lambda x: len(x)> 2, truth))
import random
import traceback
import copy
while True:
    try:
        r=random.randint(0,len(truth)-1)
        r1=truth[r]
        r2=copy.deepcopy(truth)
        r2.pop(r)
        r2 = ["{}: {}".format(i,x) for i,x in enumerate(r2)]
        print("question:")
        print("\n".join(r2))
        ans0=input("insert at:\n")
        ans1=input("content:\n")
        if int(ans0) == r and ans1 == r1:
            print("correct!")
        else:
            print("incorrect!")
            print("the correct answer is:", r,r1)
            print("your answer is:", ans0,ans1)
        #print("correct form:",r)
        print("continue?")
        input()
    except:
        #import os
        traceback.print_exc()
        print("exception printed above!")
        #os.abort()
        pass
