# the format must change, or shall we?
# how do we evaluate shits according to mixed content? GAN?
# usually mixed content can be read as matrix, but that is not always the case.
# so we would assume something else.
import numpy as np
# linear - processing - matrix[slide] - processing - evaluate
import random
# if these things cannot be plugged right in then what?
# you need duplication, and the duplication always change.
taskgen=lambda:random.randint(1,100)
calcgen=lambda:(taskgen(), taskgen())
def problem():
    a,b=calcgen()
    # to predict the shit out of your imagination.
    s=random.choice(["-","+","*","/"])
    t="{} {} {}".format(a,s,b)
    v=eval(t)
    return t,v
import traceback
while True:
    try:
        t,v=problem()
        print("problem:",t)
        ans=input("answer:\n")
        if abs(float(ans) - v)<0.01:
            print("correct.")
        else:
            print("incorrect!")
            print("answer is:",v)
            print("your answer is:",ans)
    except:
        traceback.print_exc()
        print("exception printed above.")
