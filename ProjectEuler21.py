import numpy as np
import pandas as pd

# Project Euler Problem 21

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.
def func(x):
    try:
        if q[x-1]==x:
            return 0
        if q[q[x-1]-1] == x:
            return q[x-1]
        else:
            return 0
    except:
        return 0

r = []
z = np.arange(1,10001).tolist()
for x in range(1,10001):
    p = []
    for y in z[:x-1]:
        if x%y == 0:
            p.append(y)
    r.append(p)
q = [sum(x) for x in r]
ooo = [func(x) for x in q]
print(sum(set(ooo)))

