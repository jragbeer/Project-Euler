import cProfile
import io
import pstats
# Project Euler Problem 75

# It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle triangle in exactly one way, but there are many more examples.
#
# 12 cm: (3,4,5)
# 24 cm: (6,8,10)
# 30 cm: (5,12,13)
# 36 cm: (9,12,15)
# 40 cm: (8,15,17)
# 48 cm: (12,16,20)
#
# In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle, and other lengths allow more than one solution to be found; for example, using 120 cm it is possible to form exactly three different integer sided right angle triangles.
#
# 120 cm: (30,40,50), (20,48,52), (24,45,51)
#
# Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly one integer sided right angle triangle be formed?
#
import numpy as np
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
    def stuff(a,b,c):
        if a**2+b**2 == c**2:
            return True
        return False

    q = []
    for p in range(12,1501,2):
        w = int(p/2)
        for x in range(2,w):
            for y in range(2,x):
                for z in range(5,w,5):
                    t = x+y+z
                    if t == p:
                        # q.append(t)
                        if stuff(x, y, z):
                            print(t, [x,y,z])
                            q.append(t)
    tt = set(q)
    print(q)
    pp = [x for x in tt if q.count(x) == 1]
    print(pp)
main()
