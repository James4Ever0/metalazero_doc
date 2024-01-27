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
        print("question:",r1)
        r0=exc_exec(r1)
        ans=input("answer:\n")
        if ans == r0:
            print("correct!")
        else:
            print("incorrect!")
            print("the correct answer is:", r0)
            print("your answer is:", ans)
        #print("correct form:",r)
        print("continue?")
        input()
    except:
        traceback.print_exc()
        print("exception printed above!")
        pass
