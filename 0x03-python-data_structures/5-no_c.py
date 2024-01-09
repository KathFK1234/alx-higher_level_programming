#!/usr/bin/python3
def no_c(my_string):
    for x in my_string:
        if (x == "c" or x == "C"):
            new_string = ''.join(char for char in my_string if char != x)
            print(new_string)
