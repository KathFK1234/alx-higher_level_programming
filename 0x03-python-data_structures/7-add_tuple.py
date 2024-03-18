#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    for x in tuple_a[0:1]:
        for y in tuple_b[0:1]:
            c = int(tuple_a[0] + tuple_b[0])
            d = int(tuple_a[1] + tuple_b[1])
            if len(tuple_a) < 2:
                d = int(0 + tuple_b[1])
            elif len(tuple_b) < 2:
                d = int(tuple_a[1] + 0)
            elif len(tuple_a) < 2 and len(tuple_b) < 2:
                d = (0 + 0)
            tuple_new = (c,d)
            return (tuple_new)
