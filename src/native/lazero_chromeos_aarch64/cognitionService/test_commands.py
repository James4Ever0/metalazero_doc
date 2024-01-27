import subprocess
program = subprocess.Popen(["bash","get_commands.sh"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)

#print(dir(program))
stdout, stderr = program.communicate()
#print(stdout, stderr)
#nothing from stderr.
array = stdout.decode("utf-8")
array = array.split("\n")
#print("length of commands:",len(array))
import itertools
import os
for comp in itertools.combinations(array,r=2):
    cmd = " ".join(comp)
    os.system(cmd)
