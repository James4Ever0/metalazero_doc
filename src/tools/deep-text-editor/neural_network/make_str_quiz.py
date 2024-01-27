truth=open("base.py","r").read().split("\n")
truth=list(filter(lambda x: len(x)> 2, truth))
import random
import traceback
def exc_exec(program):
    try:
        return str(eval(program))
    except:
        return traceback.format_exc()
        #return "Exception."
while True:
    try:
        r=random.choice(truth)
        r0=dir(r)
        r0=random.choice(r0)
        r1="r.{}()".format(r0)
        r0=exc_exec(r1)
        print("command:",r1)
        r1=r0.split()
        r1=random.choice(r1)
        r0=r0.replace(r1,"___")
        print("result:",r0)
        ans=input("answer:\n")
        if ans == r1:
            print("correct!")
        else:
            print("incorrect!")
            print("the correct answer is:", r1)
            print("your answer is:", ans)
        #print("correct form:",r)
        print("continue?")
        input()
    except:
        traceback.print_exc()
        print("exception printed above!")
        pass
