#import apsw
import sqlite3
#import pysqlite3
# we need to verify its correctness.
# like coq in python?
c = sqlite3.connect("python.db")
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
print("will start recording if is valid statement.")
print("i will categorize these functions.")
while True:
    program = input("please give the code:\n")
    comment = input("code comment:\n")
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
