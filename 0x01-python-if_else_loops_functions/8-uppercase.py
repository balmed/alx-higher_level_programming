#!/usr/bin/python3
def to_uper(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return (ord(c) - 32)
    else:
        return ord(c)

def uppercase(str):
    newstr = ""
    for c in str:
        newstr += "%c" % to_uper(c)
        print("{:s}".format(newstr))
