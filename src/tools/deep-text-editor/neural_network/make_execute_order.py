truth=open("base.py","r").read().split("\n")
truth=list(filter(lambda x: len(x)> 2, truth))
import random
import copy
import traceback

base=[x for x in range(len(truth))]
b1=copy.deepcopy(base)
while True:
    try:
        for i in range(len(truth)):
            r0=False
            while r0 is not True or (ans is not r0):
                random.shuffle(base)
                target=random.choice(base)
                print("{} question:".format(i),truth[target])
                ans=input("answer:\n")
                ans= ans == "yes"
                r0= target == i
                if ans == r0 :
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
