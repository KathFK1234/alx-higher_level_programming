#!/usr/bin/python3
def islower(c):
    for i in range(97, 123):
        a = chr(i)
        b = str(a)

        if (c == b):
            return (True)
        else:
            return (False)
