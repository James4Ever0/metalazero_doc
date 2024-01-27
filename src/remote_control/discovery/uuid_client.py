if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--ip",type=str,required=True)
    args = parser.parse_args()
    host = args.ip
    import requests
    try:
        req = requests.get("http://{}:8010".format(host),timeout=1)
        text = req.text
        print({"ip":host,"text":text})
    except:
        pass
