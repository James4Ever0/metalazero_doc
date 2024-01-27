# usually regular expression just contains everything, so we use every shit to develop the regular expression.
import random
import re

def test_regular(expression):
    try:
        re.compile(expression)
        return True
    except:
        return False

def generate_expression(length=7,generator=lambda: chr(random.randint(0,200))):
    target=""
    for _ in range(length):
        target += generator()
    return target

if __name__ == "__main__":
    # undecidable, we never know what the heck will be going on.
    # cause you don't see it happens.
    for _ in range(200):
        g = generate_expression()
        print("expression:",g,"isValid:",test_regular(g))
# can we build some shit out of our discovery?
