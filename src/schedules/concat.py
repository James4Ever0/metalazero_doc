import base64
def decode(data):
    if type(data) == str:
        data = data.encode("utf-8")
    return base64.b64decode(data).decode("utf-8")

def encode(data):
    if type(data) == str:
        data = data.encode("utf-8")
    return base64.b64encode(data).decode("utf-8")
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-d","--decode",action="store_true")
    args = parser.parse_args()

    data=input()
    if args.decode:
        print(decode(data),end="")
    else:
        print(encode(data),end="")
