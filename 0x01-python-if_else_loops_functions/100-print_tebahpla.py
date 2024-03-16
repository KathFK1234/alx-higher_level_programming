#!/usr/bin/python3
letters = []
for value in range(122, 96, -1):
    if value % 2 == 0:
        letter = chr(value)
    else:
        letter = chr(value).upper()
    letters = "".join(letter)
    print("{}".format(letters), end="")
