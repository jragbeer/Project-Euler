import pandas as pd
import numpy as np
import datetime
import cProfile
import io
import pstats
import itertools
timee = datetime.datetime.now()
# The first two consecutive numbers to have two distinct prime factors are:
#
# 14 = 2 × 7
# 15 = 3 × 5
#
# The first three consecutive numbers to have three distinct prime factors are:
#
# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.
#
# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

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
def func():
    def is_prime(n):
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while (i * i <= n):
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i = i + 6
        return True
    def factors(n):
        # find factors, and check if they're in the list of primes
        t = [x for x in sorted(list(set(itertools.chain.from_iterable((i, n // i)
                                                     for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))) if x in a]
        # if 2 and 4 are in list, only use 4 as the prime
        if 2 and 4 in t:
            t.remove(2)
        return t
    bignum = 150000
    a = [2, 3, 4] + [x for x in range(2, int(bignum / 4)) if is_prime(x)]
    right = [z for z in range(bignum) if len(factors(z)) >= 4]
    for x in range(len(right)):
        if right[x]+1 == right[x+1]:
            if right[x] + 2 == right[x + 2]:
                if right[x] + 3 == right[x + 3]:
                    print(right[x])
                    break
func()
