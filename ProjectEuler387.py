import numpy as np
import cProfile
import io
import pstats


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
    def trunc(a, ind=2):
        fun = sum([int(i) for i in a])
        p = int(a)/ fun
        if ind==1:
            if p not in primes:
                return False
        if p in final:
            return True
        if len(a) == 1:
            return True
        cool = int(a)% fun
        if cool == 0:
            return trunc(a[:-1])
        return False

    def func(a):
        wow = str(a)
        return trunc(wow[:-1],1)

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

    def gen_primes():
        """ Generate an infinite sequence of prime numbers.
        """
        # Maps composites to primes witnessing their compositeness.
        # This is memory efficient, as the sieve is not "run forward"
        # indefinitely, but only as long as required by the current
        # number being tested.
        #
        D = {}

        # The running integer that's checked for primeness
        q = 2

        while True:
            if q not in D:
                # q is a new prime.
                # Yield it and mark its first multiple that isn't
                # already marked in previous iterations
                #
                yield q
                D[q * q] = [q]
            else:
                # q is composite. D[q] is the list of primes that
                # divide it. Since we've reached q, we no longer
                # need it in the map, but we'll mark the next
                # multiples of its witnesses to prepare for larger
                # numbers
                #
                for p in D[q]:
                    D.setdefault(p + q, []).append(p)
                del D[q]

            q += 1

    num = 10**4
    final = set()
    primes = set()
    b = gen_primes()
    [next(b) for i in range(4)]
    for x in b:
        primes.add(x)
        if 10 < x < num:
            if func(x):
                final.add(x)
        else:
            break
    t = sorted(final)
    print(num)
    print(t)
    print(sum(t))

run()
