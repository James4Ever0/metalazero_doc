from pynvim import attach
ad, pt="localhost", 9897
args=["nvim", "--embed", "--headless"]
#args=["env", "nvim", "--embed", "--headless"]
ed=attach("child",argv=args)
#ed=attach("stdio",argv=args)
#ed=attach('tcp', address=ad, port=pt)
cmd="echo 'hello world'"
ed.command(cmd)
print(dir(ed))
print([x for x in ed.windows])
print([x for x in ed.buffers])
print(ed.version)
print(ed.command_output(cmd))
