#!/usr/bin/python3
def no_c(my_string):
    for x in my_string:
        if (x == "c"):
            new_str = ''.join(char for char in my_string if char != x and char != x.upper)
            print(new_str)
