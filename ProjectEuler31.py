import cProfile
import io
import itertools
import pstats

# Project Euler Problem 31
#
# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
#
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:
#
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?
#
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
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
def stuff():
    a = [100,50, 20,10,5,2,1]
    b = {i:range(0,int(200/i)) for i in a}
    print(*list(b.values()))
    r = itertools.product(*list(b.values()))
    final = [x for x in r if sum([x[0] * 100, x[1] * 50, x[2] * 20, x[3] * 10, x[4] * 5, x[5] * 2, x[6]]) == 200]
    print(len(final)+8)
stuff()