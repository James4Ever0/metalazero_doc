import requests as R

PORT=8788

def display():
    req = R.get("http://localhost:{}/display".format(PORT))
    return req.text

from base64 import b64encode as Be

def inputs(text,autoreturn=True):
    assert type(text) == str
    ar = "true" if autoreturn else "false"
    btext = Be(text.encode("utf-8")).decode("utf-8")
    req = R.get("http://localhost:{}/input?autoreturn={}&b64type={}".format(PORT,ar,btext))
    # this is still the screen.
    return req.text

def restart():
    req = R.get("http://localhost:{}/restart".format(PORT))
    return req.text
