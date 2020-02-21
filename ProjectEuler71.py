import numpy as np
import cProfile
import io
import datetime
import itertools
import pstats
from tqdm import tqdm
from pprint import pprint
import math

# Project Euler Problem 71
# Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.
#
# If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:
#
# 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
#
# It can be seen that 2/5 is the fraction immediately to the left of 3/7.
#
# By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size, find the numerator of the fraction immediately to the left of 3/7.

def profile(fnc):
    """A decorator that uses cProfile to profile a function"""

    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        retval = fnc(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retval

    return inner

@profile
def run():
    max_fraction = 3/7
    min_fraction = float(np.around(3/7, 5))
    d = 1000000
    output = {}
    for x in tqdm(range(1, d+1)):
        for y in range(int(min_fraction*x), int(3*x/7)+1):
            if x%2 == 0:
                if y%2 == 0:
                    continue
            if math.gcd(x, y) == 1:
                c = y/x
                e = f"{y}/{x}"
                if min_fraction < c < max_fraction:
                    output[c] = e
    p = max([x for x in output.keys()])
    print(p, output[p])
run()