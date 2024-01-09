#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    for x in tuple_a[0:1]:
        for y in tuple_b[0:1]:
            c = int(tuple_a[0] + tuple_b[0])
            d = int(tuple_a[1] + tuple_b[1])
            tuple_new = (c,d)
            return (tuple_new)
