import cProfile
import io
import pstats

# Project Euler Problem 686
# 27=128 is the first power of two whose leading digits are "12".
# The next power of two whose leading digits are "12" is 280.
#
# Define p(L,n) to be the nth-smallest value of j such that the base 10 representation of 2j begins with the digits of L.
# So p(12,1)=7 and p(12,2)=80.
#
# You are also given that p(123,45)=12710.
#
# Find p(123,678910).
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
import math
@profile
def run():
    def find_mantissa(a):
        b = a*(math.log(2, 10))
        c = b%1
        return str(10**c)

    def do(already_done):
        for x in [196, 289, 485]:
            ask = already_done + x
            w = find_mantissa(ask)[:4]
            if w  == "1.23":
                return ask
        return ask
    already_done = 90
    for y in range(2, 678911):
        already_done = do(already_done)
        if y == 45:
            print(y, already_done)

    print(already_done)

run()
