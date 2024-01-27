import random
import copy
mem=10
window=3
memory=[]
# we want to know how deep it goes like.
# this shall be recursive memory.
# we develop this from scratch.

rng=lambda: random.randint(1,5)
base=[rng() for _ in range(window)]
while True:
    print("world:", base)
    ans=input("seen?\n")
    r0=base in memory
    ans= ans=="yes"
    if ans == r0:
        print("correct!")
    else:
        print("incorrect!")
        print("seen:",r0)
    memory.insert(0,copy.deepcopy(base))
    if len(memory)>mem:
        memory.pop()
    base.insert(0,rng())
    base.pop()
