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

    def factors(n):
        return set(x for tup in ([i, n // i]
                                 for i in range(1, int(n ** 0.5) + 1) if n % i == 0) for x in tup)

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

    def func(r):
        facts = factors(r)
        wow = []
        for x in facts:
            if x + r / x in primes:
                wow.append(1)
            else:
                return False
        if len(wow) == len(facts):
            return True
        return False

    num = 100_000_001
    primes = set(primes2(num))
    p = [i for i in range(2, num, 2) if func(i)]
    print(p)
    print(sum(p)+1)

run()