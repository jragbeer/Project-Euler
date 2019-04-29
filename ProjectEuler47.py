import pandas as pd
import numpy as np
import datetime
import cProfile
import io
import pstats
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
def is_prime(n):
    if n % 2 == 0 or n%3 == 0:
        return False
    i = 5
    while (i*i <= n):
        if n % i == 0 or n% (i+2) == 0:
            return False
        i = i + 6
    return True
@profile
def main():
    bignum = 500000

    a = [2, 3, 4] + [x for x in range(2, int(bignum / 8)) if is_prime(x)]

    print(a)
    new_list = dict()
    gotcha = []
    for x in a:
        for y in a:
            if x * y < bignum / 4 + 1:
                if x != y:
                    for z in a:
                        if x * y * z < bignum / 2 + 1:
                            if y != z:
                                if z != x:
                                    for q in a:
                                        if q not in [x, y, z]:
                                            www = x * y * z * q
                                            if www < bignum:
                                                for i in range(bignum):
                                                    if www == i:
                                                        new_list[i] = {1: x, 2: y, 3: z, 'num': i}
                                                        try:
                                                            if new_list[i - 3]['num'] - new_list[i - 4]['num'] == 1:
                                                                if new_list[i - 2]['num'] - new_list[i - 3]['num'] == 1:
                                                                    if new_list[i - 1]['num'] - new_list[i - 2]['num'] == 1:
                                                                        if new_list[i]['num'] - new_list[i - 1]['num'] == 1:
                                                                            k = sorted([i, i - 1, i - 2, i - 3, i - 4])
                                                                            # print(k)
                                                                            if k not in gotcha:
                                                                                gotcha.append(k)
                                                                                thing = []
                                                                                for t in k:
                                                                                    thing.append(list(new_list[t].values()))
                                                                                ok = [o for ttt in thing for o in ttt]
                                                                                # print(ok)
                                                                                if len(ok) == len(list(set(ok))):
                                                                                    print(np.min(k))
                                                        except:
                                                            pass

    print(datetime.datetime.now() - timee)

main()