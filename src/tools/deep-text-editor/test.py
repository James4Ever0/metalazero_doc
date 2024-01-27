# we will check how you are doing the job.
from editor import editor
import copy

cnt="abcdef"*20
cnt0=copy.copy(cnt)
e=editor(cnt)
assert e.view() == "abcdefabcdefabcdefabcdefabcdef"
e.insert("ghi")
print("current state:",e.content,e.position)
e.replace("def")
print("current state:",e.content,e.position)
external="https://www.baidu.com"
e.copy(external)
print("current state:",e.content,e.position)
e.paste()
print("current state:",e.content,e.position)
e.undo()
print("current state:",e.content,e.position)
e.undo()
print("current state:",e.content,e.position)
e.delete(500)
print("current state:",e.content,e.position)

init, ops= "abcdef"*20, e.dump_operation()
print("init_config:")
print(init,ops)
e0=editor(content=init,operation=ops)
print("result:",e0.view())
print(e0.position)
# isn't that emacs? why you keep reinventing the wheel?
# i guess i just can't help thinking about it. i need to know all i should know.
print(e0.operation)
# shall we apply some reversible logic here?
# to change the representation, to mutate the thing and let the AI to recover.
# you shall make the nars into a test, also pytorch, keras, tensorflow, everything. cause it is so hard to master these shits.
# you can log all your operations.
