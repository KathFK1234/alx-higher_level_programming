#!/usr/bin/python3
def uppercase(str):
    for character in str:
        x = ord(character)

        if (x >= 97 and x <= 122):
            x -= 32
            print("{}".format(chr(x)), end="")
    print("\n")
