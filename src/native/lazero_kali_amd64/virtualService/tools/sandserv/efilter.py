import sys
def f(a,b):
    return filter(lambda x:x!=b,a)
e=sys.argv[1:]
a=""
if len(e)==0:
    pass
else:
    a=e[0]
for x in sys.stdin:
    print("/".join([a]+list(f(f(x.split("/"),""),"/"))[:-1]))
