import numpy as np
import datetime
import cProfile
import io
import pstats

# Project Euler Problem 58
# Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.
#
# 37 36 35 34 33 32 31
# 38 17 16 15 14 13 30
# 39 18  5  4  3 12 29
# 40 19  6  1  2 11 28
# 41 20  7  8  9 10 27
# 42 21 22 23 24 25 26
# 43 44 45 46 47 48 49
#
# It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.
#
# If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?

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
    primes = set(primes2(1_000_000_000))
    p = [x for x in range(2,100_001) if x%2 != 0]
    squares = [x**2 for x in p]
    wow = {}
    primes_in_square = []
    total = []
    for i, x in enumerate(squares):
        wow[i+2] = [x-(p[i]-1), x-(p[i]-1)*2, x-(p[i]-1)*3]
        for each in wow[i+2]:
            if each in primes:
                primes_in_square.append(each)
        total.append(4)
        a = len(primes_in_square) / (sum(total) + 1)
        if a < 0.1:
            print(i, x, np.sqrt(x), a)
            break

run()