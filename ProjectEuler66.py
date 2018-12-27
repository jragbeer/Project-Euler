import cProfile
import io
import pstats
import numpy as np

#Project Euler Problem 66

# Consider quadratic Diophantine equations of the form:
#
# x2 – Dy2 = 1
#
# For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.
#
# It can be assumed that there are no solutions in positive integers when D is square.
#
# By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:
#
# 32 – 2×22 = 1
# 22 – 3×12 = 1
# 92 – 5×42 = 1
# 52 – 6×22 = 1
# 82 – 7×32 = 1
#
# Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.
#
# Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.

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
def main():
    D = [x for x in range(3,1001,2) if x**(0.5) != int(x**0.5)]
    print(D)
    qq = []
    for d in D:
        for y in range(1,100000001):
            a = np.sqrt(d * (y ** 2) + 1)
            if a == int(a):
                qq.append(a)
                break
        # print(d)
    print(max(qq))


main()
