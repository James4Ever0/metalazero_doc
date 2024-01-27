import datetime
from concat import encode, decode
def get_now():
    return datetime.datetime.now()

def compare_time(a,b,decode=True,inverse=False):
    if decode:
        a, b = decode(a), decode(b)
    a, b = datetime.datetime.fromisoformat(a), datetime.datetime.fromisoformat(b)
    target = a > b
    if inverse:
        target = not target
    return target

def sort_time(_list, decode=True, encode=True, inverse=False):
    if decode:
        _list = [decode(x) for x in _list]
    _list = [datetime.datetime.fromisoformat(x) for x in _list]
    _list = list(sorted(_list))
    _list = [x.isoformat() for x in _list]
    if encode:
        _list = [encode(x) for x in _list]
    if inverse:
        _list = list(reversed(_list))
    return _list

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-a",type=str)
    parser.add_argument("-b",type=str)
    parser.add_argument("-d","--decode",action="store_true")
    parser.add_argument("-n","--now",action="store_true")
    parser.add_argument("-i","--inverse",action="store_true")
    parser.add_argument("-e","--encode",action="store_true")
    args = parser.parse_args()
    a, b = args.a, args.b
    if args.now:
        target=get_now().isoformat()
        if args.encode:
            target=encode(target)
        print(target)
    elif args.a is not None and args.b is not None:
        target = compare_time(a, b, args.decode, args.inverse)
        target = int(target)
        exit(target)
    else:
        print("the argument format is somehow wrong.")
# you can compare in this way.
# you can also specify to decode or not.
