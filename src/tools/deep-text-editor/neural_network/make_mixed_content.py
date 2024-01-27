# the format must change, or shall we?
# how do we evaluate shits according to mixed content? GAN?
# usually mixed content can be read as matrix, but that is not always the case.
# so we would assume something else.
# linear - processing - matrix[slide] - processing - evaluate
import random
# if these things cannot be plugged right in then what?
# you need duplication, and the duplication always change.
taskgen=lambda:random.randint(1,100)
def problem():
    myarr=[taskgen() for _ in range(taskgen())]
    return myarr, len(myarr)
    # to predict the shit out of your imagination.
    # i mean neural network is just a lucrative way of describing the efficiency of collaboration.
import traceback
import copy
while True:
    try:
        t,v=problem()
        stack=[]
        buff=[]
        for x in t:
            buff.append(x)
            print("stack:",stack)
            print("buff:",buff)
            ans=input("cut?:\n")
            if ans == "yes":
                stack.append(copy.deepcopy(buff))
                buff=[]
            else:
                pass
        stack.append(copy.deepcopy(buff))
        print("final stack:",stack)
    except:
        traceback.print_exc()
        print("exception printed above.")
