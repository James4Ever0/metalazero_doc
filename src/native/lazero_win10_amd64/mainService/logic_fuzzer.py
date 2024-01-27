# this is to create custom function via shits.
# basic binary shits.
# who can tell?
import random

# we want some basic logic expressions. not just shits.
# we want our fucking program.

def generate_expression(length,complexity=5,brackets=3,join=True):
    kw =["and", "or","not"]
    assert length > 1 and type(length) == int
    output = []
    kw0 = ["k{}".format(x) for x in range(length)]
    br = ["(",")"]
    output.append(random.choice(kw0))
    for x in range(complexity-1):
        a,b = random.choice(kw0), random.choice(kw)
        if b == "not":
            output.append(br[0])
        output.append(b)
        output.append(a)        
        if b == "not":
            output.append(br[1])
#    random.shuffle(kw0)
#    i=0
    # we want brackets.
    # but how to add these shits?
#    for x in kw0:
#        output.insert(0+i,x)
    for x in range(brackets):
        inds = []
        for a,b in enumerate(output):
            if b not in kw:
                inds.append(a)
        t0 = random.sample(inds,2)
        a,b = t0
        if a>b:
            a,b = b,a
        adjustment = 4
        output.insert(a,br[0])
        output.insert(b+adjustment,br[1])
    return " ".join(output) if join else output
if __name__ == "__main__":
    length = 5
    output = generate_expression(length)
    # how do we find the optimization function?
    # how do we change the fucking logic?
    print("target logic:",output)
