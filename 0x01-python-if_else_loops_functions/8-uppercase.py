#!/usr/bin/python3
def uppercase(str):
    for character in str:
        x = ord(character)

        if (x >= 97 and x <= 122):
            x -= 32
            print("{}\n".format(chr(x)), end="")
