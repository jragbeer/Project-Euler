import cProfile
import io
import pstats

#Project Euler Problem 63
#
# The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.
#
# How many n-digit positive integers exist which are also an nth power?
# print(len([x for x in range(1,10000000001) for y in range(1,100001) if y**len(str(x))==x]))

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
    c= 0
    for x in range(1,10001):
        for y in range(1,10):
            a = str(y**x)
            if len(a) == x:
                c+=1
    print(c, 'integers are nth-powers')
main()