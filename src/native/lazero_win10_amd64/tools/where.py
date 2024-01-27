# import subprocess
from subprocess import Popen, PIPE

def where(target):
    p = Popen(["where",target],stderr=PIPE,stdout=PIPE)
    p = p.communicate()[0].decode("utf-8") # bytes.
    p0 = p.split("\n")
    p0 = [x.replace("\n", "").replace("\r","") for x in p0]
    p0 = list(filter(lambda x:len(x)>0,p0))
    return p0