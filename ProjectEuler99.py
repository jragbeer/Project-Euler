import numpy as np
import pandas as pd
from pprint import pprint
# Project Euler Problem 99
# Comparing two numbers written in index form like 211 and 37 is not difficult, as any calculator would confirm that 211 = 2048 < 37 = 2187.
#
# However, confirming that 632382518061 > 519432525806 would be much more difficult, as both numbers contain over three million digits.
#
# Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.
#
# NOTE: The first two lines in the file represent the numbers in the example given above.


def run():
    def nums(tup):
        return tup[0]**tup[1]

    with open('base_exp.txt', 'rb') as f:
        pairs = [tuple((int(str(x.decode())[:-1].split(',')[0]), int(str(x.decode())[:-1].split(',')[1]))) for x in f.readlines()]
        z = {}
        for x in range(len(pairs)):
            print(x)
            z[nums(pairs[x],)] = x+1
        print(z[max(list(z.keys()))], max(list(z.keys())))
run()