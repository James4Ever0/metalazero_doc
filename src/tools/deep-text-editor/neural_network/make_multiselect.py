truth=open("base.py","r").read().split("\n")
truth=list(filter(lambda x: len(x)> 2, truth))
tokens=[x.split() for x in truth]
tokens=[x for y in tokens for x in y]
tokens=list(set(tokens))
import random
import traceback
while True:
    try:
        r=random.choice(truth)
        r0=r.split()
        r0=random.choice(r0)
        r1=r.replace(r0,"___")
        print("question:",r1)
        dnd=[x for x in tokens if x != r0]
        dnd=random.sample(dnd,3)
        choices=dnd+[r0]
        random.shuffle(choices)
        print("choices:")
        print("\n".join(choices))
        ans=input("answer:\n")
        ans=int(ans)
        ans=choices[ans]
        if ans == r0:
            print("correct!")
        else:
            print("incorrect!")
            print("the correct answer is:", r0)
            print("your answer is:", ans)
        print("correct form:",r)
        print("continue?")
        input()
    except:
        traceback.print_exc()
        print("exception printed above!")
        pass
