import numpy as np
import datetime
import itertools
# Project Euler Problem 38
# Take the number 192 and multiply it by each of 1, 2, and 3:
#
# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
#
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
#
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
timee = datetime.datetime.now()
def func(x, y):
    d = [str(x*a) for a in y]
    return ''.join(d)
def zeros(x):
    x = str(x)
    for y in x:
        if y == '0':
            return False
    return True
aa = range(1,10)
b = list(itertools.permutations(aa))
b = [list(x) for x in b]
r = [[str(x) for x in b[t]] for t in range(len(b))]
r = [int(''.join(x)) for x in r]
z = [[i for i in range(1,x)] for x in range(2,9)]
q = [int(func(x,y)) for x in range(1,9999) for y in z[1:]]
print(sorted([d for d in q if len(str(d))==9 if len(set(str(d))) == len(str(d)) if zeros(d)])[-1])
print(datetime.datetime.now()-timee)