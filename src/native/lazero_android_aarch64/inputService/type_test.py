from subprocess import Popen, PIPE

cmd="su"
p=Popen([cmd],stdin=PIPE,stdout=PIPE,stderr=PIPE)
# print(dir(p.stdin))
# use communicate
#for _ in range(3):
out,err= p.communicate(input='input text "123"'.encode("utf-8"))
print(out,err)
