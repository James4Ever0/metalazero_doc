import inspect
import os

def doc(target):
    return inspect.getdoc(target)

d = doc(os)
# filter the form of the shit.
info = d.split()
import random
import traceback

def recursive_fault_handling(err):
    try:
        info_err = err.split()
        targets = random.sample(err,5)
        t = ".".join(targets)
        print("remedy command:",t)
        e = eval(t)
        print("remedy result:",e)
    except:
        err = traceback.format_exc()
        recursive_fault_handling(err)

def base_error_handling():
    try:
        targets = random.sample(info,5)
        t = ".".join(targets)
        print("executing program:",t)
        e = eval(t)
        print("eval result:",e)
    except:
        print("eval error")
        # infinite err handling?
        # HOW DO YOU MAKE IT RIGHT?
        err = traceback.format_exc()
        recursive_fault_handling(err)

def safe_exec(func):
    try:
        func()
    except:
        pass

def my_eval(command):
    try:
        print("executing command:",command)
        e = eval(command)
        print("eval result:",e)
    except:
        err = traceback.format_exc()
        recursive_fault_handling(err)

def safe_eval(command):
    safe_exec(my_eval(command))

def get_targets(x,target=str):
    t= []
    for y in x:
        if type(y) == target:
            t.append(y)
        else:
            t0 = get_targets(y)
            t+=t0
    return t
def mix_targets(x,y):
    t = []
    for x0 in get_targets(x):
        for y0 in get_targets(y):
            t.append(x0+y0)
            t.append(y0+x0)
    return t

def eval_single(target):
    try:
        print("executing target:",target)
        r = eval(target)
        print("result:",r)
    except:
        err = traceback.format_exc()
        print("error:",err)
if __name__ == "__main__":
    safe_exec(base_error_handling)
    program_base = ["inspect.{}".format(x) for x in dir(inspect)]
    flatten = lambda x: [y for z in x for y in z]
    targets = ["()",*dir(inspect),".",flatten([dir(eval(x)) for x in program_base])]
#    pb2 = [[x+y for x in program_base] for y in targets]
    pb2 = mix_targets(program_base, targets)
    for target in pb2:
#        safe_eval(target)
        eval_single(target)
