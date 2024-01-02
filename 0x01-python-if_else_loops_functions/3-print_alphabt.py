#!/usr/bin/python3
for i in range(97, 123):
    if (i != 101 and i != 113):
        a = chr(i)
        b = str(a)
        print("{}".format(b), end="")
