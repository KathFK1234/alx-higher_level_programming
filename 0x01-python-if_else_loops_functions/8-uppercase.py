#!/usr/bin/python3
def uppercase(str):
    output = ("")
    for character in str:
        x = ord(character)

        if (x >= 97 and x <= 122):
            x -= 32
            output += "{}".format(chr(x))
        else:
            output += "{}".format(character)
    output += "\n"
    print(output)
