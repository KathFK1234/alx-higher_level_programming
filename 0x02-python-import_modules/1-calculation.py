#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, calc.add))
    print("{} - {} = {}".format(a, b, calc.sub))
    print("{} * {} = {}".format(a, b, calc.mul))
    print("{} / {} = {}".format(a, b, calc.div))
