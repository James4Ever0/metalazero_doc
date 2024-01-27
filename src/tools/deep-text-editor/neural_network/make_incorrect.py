truth=open("base.py","r").read().split("\n")
truth=list(filter(lambda x: len(x)> 2, truth))
import random
import traceback
while True:
    try:
        r=random.choice(truth)
        r0=r.split()
        r2=random.choice(r0)
        r0=random.choice(r0)
        r1=r.replace(r0,"___")
        print("question:",r1)
        ans=input("answer:\n")
        if ans == r2:
            print("correct!")
        else:
            print("incorrect!")
            print("the correct answer is:", r2)
            print("your answer is:", ans)
        print("correct form:",r)
        print("continue?")
        input()
    except:
        traceback.print_exc()
        print("exception printed above!")
        pass
