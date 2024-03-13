#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        if i == j:
            continue
        if (str(i) + str(j))[0] == (str(j) + str(i))[0]:
            continue
        else:
            print("{}".format(str(i) + str(j)), end=", " if str(i) + str(j) != "89" else "")
