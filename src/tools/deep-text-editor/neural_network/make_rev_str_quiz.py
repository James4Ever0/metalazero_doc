truth=open("base.py","r").read().split("\n")
truth=list(filter(lambda x: len(x)> 2, truth))
import random
import traceback
import copy
from monkey_editing import monkey 
# we can show hints, which identify the hints may only relates to the effect of hinting, and resembles the real world scenario.
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
        print("command:",monkey(r1))
        cmd=copy.deepcopy(r1)
        r1=r0.split()
        r1=random.choice(r1)
        print("result:",r0)
        ans=input("answer:\n")
        if ans == cmd:
            print("correct!")
        else:
            print("incorrect!")
            print("the correct answer is:", cmd)
            print("your answer is:", ans)
        #print("correct form:",r)
        print("continue?")
        input()
    except:
        traceback.print_exc()
        print("exception printed above!")
        pass
