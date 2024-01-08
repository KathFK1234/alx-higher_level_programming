#!/usr/bin/python3
def no_c(my_string):
    for x in my_string:
        if (x == "c" or x == "C"):
            new_str = my_string.replace(x, "")
            print(new_str)
