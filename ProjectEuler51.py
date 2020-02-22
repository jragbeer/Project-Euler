import numpy as np
from tqdm import tqdm
import cProfile
import io
import pstats
import gc
import itertools
import sys
import time
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
    def find_possible_combos(array):
        c = range(len(array))
        all_combos = []
        for i in c[1:]:
            all_combos.append(list(itertools.combinations(c, i)))
        flat_list = [item for sublist in all_combos for item in sublist if len(item) < len(array)]
        return flat_list

    num = 1_000_000
    primes = primes2(num)
    primes_set = set(primes)
    for each in primes[5:]:
        q = str(each)
        combos = find_possible_combos(q)
        for k in combos:
            each_num = []
            for digit in range(10):
                each_num.append(int(''.join([f"{digit}" if i in k else q[i] for i in range(len(q))])))
            total = [p for p in each_num if p in primes_set]
            if len(total) == 8:
                ting = [len(str(que)) for que in total]
                if np.mean(ting) == ting[0]:
                    print(total[0])
                    break
        else:
            continue
        break

run()