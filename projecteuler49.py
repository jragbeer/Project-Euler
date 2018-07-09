import pandas as pd
import numpy as np
import datetime
import itertools
timee = datetime.datetime.now()
# Project Euler 49
#
# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
#
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
#
# What 12-digit number do you form by concatenating the three terms in this sequence?
def is_prime(n):
    if n % 2 == 0 or n%3 == 0:
        return False
    i = 5
    while (i*i <= n):
        if n % i == 0 or n% (i+2) == 0:
            return False
        i = i + 6
    return True

a = [x for x in range(1000, 10000) if is_prime(x)]
def func(x):
    x = str(x)
    b = itertools.permutations(x)
    d = [int(''.join(i for i in x)) for x in b if is_prime(int(''.join(i for i in x) )) if len(str(int(''.join(i for i in x))) ) == 4]
    return d

rrr = []
c = [func(x) for x in a if len(func(x))>=1]
z = [sorted(d) for d in c]
for pp in range(len(z)):
    for x in range(len(z[pp])):
        for y in range(len(z[pp])):
            if (z[pp][x]-z[pp][y]) + z[pp][x] in z[pp]:
                if z[pp][x] != (z[pp][x]-z[pp][y]) + z[pp][x]:
                    rrr.append(z[pp][y])
                    rrr.append(z[pp][x])
print(''.join(str(i) for i in list(set(rrr))[3:]))