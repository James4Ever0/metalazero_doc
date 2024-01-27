a = "lambda {} : {}"
comment = "monkey program"
import random

operator = [x for x in "+-*/%"]
letters = [x for x in "xyzabcdef"]
import time
rest = lambda: time.sleep(0.5)
while True:
    tl = random.randint(2,5)
    ts = random.randint(3,6)
    # internal is equally important than external.
    tl0 = [random.choice(operator) for _ in range(tl+ts-1)]
    tl1 = random.sample(letters,tl)
    tl3 = [str(random.random()) for _ in range(ts)]
    tl2 = tl3+tl1
    random.shuffle(tl2)
    seq = [tl2[x]+tl0[x] for x in range(tl+ts-1)]
    seq += [tl2[-1]]
    seq = "".join(seq)
    head = ",".join(tl1)
    target = a.format(head, seq)
    rest()
    print(target,end="\r\n")
    rest()
    print(comment,end="\r\n")
