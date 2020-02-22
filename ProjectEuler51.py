import numpy as np
from tqdm import tqdm
import cProfile
import io
import pstats
import gc
import itertools
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
    def primes2(n):
        correction = (n % 6 > 1)
        n = {0: n, 1: n - 1, 2: n + 4, 3: n + 3, 4: n + 2, 5: n + 1}[n % 6]
        sieve = [True] * (n // 3)
        sieve[0] = False
        for i in range(int(n ** 0.5) // 3 + 1):
            if sieve[i]:
                k = 3 * i + 1 | 1
                sieve[((k * k) // 3)::2 * k] = [False] * ((n // 6 - (k * k) // 6 - 1) // k + 1)
                sieve[(k * k + 4 * k - 2 * k * (i & 1)) // 3::2 * k] = [False] * (
                        (n // 6 - (k * k + 4 * k - 2 * k * (i & 1)) // 6 - 1) // k + 1)
        return [2, 3] + [3 * i + 1 | 1 for i in range(1, n // 3 - correction) if sieve[i]]
    def find_possible_combos(b):
        c = range(len(b))
        all_combos = []
        for i in c[1:]:
            all_combos.append(list(itertools.combinations(c, i)))
        flat_list = [item for sublist in all_combos for item in sublist if len(item) < len(b)]
        return flat_list


    num = 1_000_000
    a = primes2(num)
    for each in a[5:]:
        q = str(each)
        cool = find_possible_combos(q)
        total = []
        for r in range(10):
            each_num = []
            for k in cool:
                other = []
                for i in range(len(q)):
                    # print(k, i)
                    if i in k:
                        other.append(f"{r}")
                    else:
                        other.append(q[i])
                other = ''.join(other)
                each_num.append(int(other))

            for k in each_num:
                if k in a:
                    total.append(k)
        print()

    # if len(each_num) > 5:
    #     print(each_num)


run()