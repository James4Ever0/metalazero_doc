import pyperclip
import argparse
import sys
# macos pbcopy pbpaste
# linux xclip xsel
# kw: copy paste
def copy(content):
    pyperclip.copy(content)

def paste():
    return pyperclip.paste()

def read():
    return sys.stdin.read()

parser = argparse.ArgumentParser()
parser.add_argument("action",type=str,choices=["copy","paste"],required=True)
args = parser.parse_args()

action = args.action
if action == "copy":
    content = read()
    copy(content)
else:
    print(paste(),end="")
