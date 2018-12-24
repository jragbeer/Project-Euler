import datetime
import cProfile
import io
import pstats
# Project Euler Problem 60
# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.
#
# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

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
    timee = datetime.datetime.now()

    def checkall(x, y, z):
        zx = int(str(z) + str(x))
        zy = int(str(z) + str(y))
        xz = int(str(x) + str(z))
        yz = int(str(y) + str(z))
        xy = int(str(x) + str(y))
        yx = int(str(y) + str(x))
        q = [zx, zy, xz, yz, xy, yx]
        for i in q:
            if i not in newprimes:
                return False
        return True

    def check(u):
        c = int('7' + u)
        if c in newprimes:
            a = int('3' + u)
            if a in newprimes:
                b = int(u + '3')
                if b in newprimes:
                    d = int(u + '7')
                    if d in newprimes:
                        return True

    def primes(n):
        sieve = [True for x in range(n)]
        prime_lst = []
        for i in range(2, n):
            if sieve[i]:
                prime_lst.append(i)
                for j in range(i * 2, n, i):
                    sieve[j] = False
        return prime_lst
    primelist = primes(100001)
    newprimes = set(primes(10000000001))
    for x in primelist[4:]:
        if check(str(x)):
            for y in primelist[4:]:
                if x == y:
                    continue
                if check(str(y)):
                    for z in primelist[4:]:
                        if x==z or z==y:
                            continue
                        if check(str(z)):
                            if checkall(x,y,z):
                                print(x,y,z)

    timee2 = datetime.datetime.now()
    print(timee2-timee)

main()