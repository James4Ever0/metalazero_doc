import json
import os
content = json.loads(open("programs.json","r").read())
for k in content.keys():
    for v in content[k]:
        name = "{}_{}_evaluator.py".format(k,v)
        os.system("touch {}".format(name))
