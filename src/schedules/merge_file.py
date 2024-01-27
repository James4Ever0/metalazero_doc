import json
def parse_file(target):
    with open(target,"r") as f:
        target = json.loads(target)
    return target

if __name__ == "__main__":
    import os
    from get_time import sort_time
    # how to sort this datetime shit?
    # i mean they are apparently time sorted.
    if os.path.exists(".latest"):
        print("latest repo have been fetched. will begin to merge task files.")
