#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if (idx >= len(my_list) or idx < 0):
        return (my_list)
    else:
        x = my_list.copy()
        my_list[idx] = element
        return (my_list)
        return (x)
