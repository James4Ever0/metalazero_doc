import argparse
names = dir(argparse.ArgumentParser())
print([x for x in names if "parse" in x])
