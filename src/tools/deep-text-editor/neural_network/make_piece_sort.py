truth=open("base.py","r").read().split("\n")
truth=list(filter(lambda x: len(x)> 2, truth))
import random
import copy
import traceback

while True:
    try:
        t1=random.choice(truth)
        t0=t1.split()
        base=[x for x in range(len(t0))]
        b1=copy.deepcopy(base)
        random.shuffle(base)
        base0=[t0[x] for x in base]
        r1=["{}: {}".format(i,x) for i,x in enumerate(base0)]
        print("question:")
        print("\n".join(r1))
        ans=input("answer:\n")
        ans = [int(x) for x in ans.split(" ")][:len(t0)]
        ans = [base0[x] for x in ans]
        b0=[None]*len(b1)
        for z in b1:
            x,y = base[z],b1[z]
            b0[x] = y
        #r0 = " ".join([str(x) for x in b0])
        if ans == t0:
            print("correct!")
        else:
            print("incorrect!")
            cr=sum([int(ans[x] == t0[x]) for x in range(len(t0))])/len(t0)
            print("correct rate:", cr)
            print("the correct answer is:", t0)
            print("your answer is:", ans)
        print("correct form:", t1)
        print("continue?")
        input()
        #print("correct form:","\n".join(truth))
    except:
        traceback.print_exc()
        print("exception printed above!")
        pass
