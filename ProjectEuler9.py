import numpy as np
import pandas as pd

# Project Euler Problem 9
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

xn = range(1,999)
xx = [x**2 for x in xn]

for x in xx:
    for y in xx:
        z = x+y
        if z in xx:
            if np.sqrt(x) + np.sqrt(y) + np.sqrt(z) == 1000:
                print('ANSWER: ',np.sqrt(x)*np.sqrt(y)*np.sqrt(z),' = ' ,np.sqrt(x),np.sqrt(y),np.sqrt(z))
