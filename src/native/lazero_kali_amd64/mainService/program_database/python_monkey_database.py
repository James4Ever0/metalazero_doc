#import apsw
import sqlite3
#import pysqlite3
# we need to verify its correctness.
# like coq in python?
c = sqlite3.connect("python_monkey.db")
#c = apsw.Connection("python.db")
#print(dir(sqlite))
#print(dir(c))
#help(c)
#cursor = c.cursor()
#help(cursor)
import traceback
def try_execute(statement,data=None):
    try:
        if data == None:
            c.execute(statement)
        else:
            assert type(data) == tuple
            c.execute(statement, data)
        c.commit()
        return True
    except:
        traceback.print_exc()
    return False
statement = "create table source_code ( Id int primary key, Program varchar(255) unique, Comment varchar(255))"
try_execute(statement)
statement = "insert into source_code (Id, Program, Comment) values (1, \"import numpy\",\"import statement\")"
try_execute(statement)

statement = "insert into source_code (Id, Program, Comment) values (2, ?, ?)"
data = ('lambda x: x.replace("abc","")','replace statement')
try_execute(statement, data)

statement = "select distinct Id, Program, Comment from source_code order by -Id "
cursor = c.execute(statement)
# how do you escape anything?
ind=0
for a in cursor:
    ind,_,_ = a
    break
ind+=1

a = "lambda {} : {}"
import random

operator = [x for x in "+-*/%"]
letters = [x for x in "xyzabcdef"]
import time
rest = lambda: time.sleep(0.5)
def monkey():
    comment = "monkey program"
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
    return target, comment
print("will start recording if is valid statement.")
print("i will categorize these functions.")
while True:
    program, comment = monkey()
    statement = "insert into source_code (Id, Program, Comment) values (?, ?, ?)"
    try:
        eval(program)
        print("eval succeed.")
        data = (ind, program, comment)
        result = try_execute(statement, data)
        if result:
            ind+=1
            print("insert succeed.")
        else:
            print("failed to insert program.")
    except:
        print("invalid program.")
