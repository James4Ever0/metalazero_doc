truth=open("base.py","r").read().split("\n")
truth=list(filter(lambda x: len(x)> 2, truth))

class mylist(list):
    def __sub__(self, other):
        return [x for x in self if x not in other]
truth=mylist(truth)
import random
import traceback
while True:
    try:
        r=random.choice(truth)
        r0=r.split()
        r0=random.choice(r0)
        r1=r.replace(r0,"___")
        print("question:",r1)
        hints=truth - mylist([r])
        random.shuffle(hints)
        hints=hints[:3]
        for x in range(3):
            ans=input("answer:\n")
            if ans == r0:
                print("correct!")
                break
            else:
                print("incorrect!")
                print("the correct answer is:", r0)
                print("your answer is:", ans)
                print("hint:",hints.pop())
        print("correct form:",r)
        print("continue?")
        input()
    except:
        traceback.print_exc()
        print("exception printed above!")
        pass
