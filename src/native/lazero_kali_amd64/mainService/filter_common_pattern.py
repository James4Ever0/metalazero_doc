# we need to check for common patterns.
# what contains the most information, the pure information?
import random
import copy
import sys
import uuid
my_id = str(uuid.uuid4())
dictionary = []
dlength = lambda: random.randint(3,6)
while True:
    i = sys.stdin.readline()
    # hierachical shits?
    i0 = copy.copy(i)
    orig = len(i)
    for x in dictionary:
        i0 = i0.replace(x,"")
    if len(i0) == orig:
        # or always like that?
        # collect some shits.
        try:
            dictlength = dlength()
            a = random.randint(0,orig-dictlength)
            b = a+dictlength
            dictionary.append(i[a:b])
        except:
            pass
    print(i)
    print("{}_original:".format(my_id),i,file=sys.stderr)
    print("{}_filtered:".format(my_id),i0,file=sys.stderr)
    print("{}_dictionary:".format(my_id),dictionary,file=sys.stderr)
    # you shall introduce multidict.
