#!/usr/bin/python3
def element_at(my_list, idx):
    if (idx >= len(my_list) or idx < 0):
        x = None
        return (x)
    else:
        return (my_list[idx])
