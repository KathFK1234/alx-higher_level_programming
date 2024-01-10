#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    if (idx >= len(my_list) or idx < 0):
        return (new_list)
    else:
        my_list[idx] = element
        print(my_list)
        print(x)
