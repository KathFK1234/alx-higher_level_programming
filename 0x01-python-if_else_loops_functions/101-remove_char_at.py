#!/usr/bin/python3
def remove_char_at(str, n):
    if n < len(str) and n > 0:
        item = str.replace(str[n], "")
        return (item)
    else:
        return (str)
