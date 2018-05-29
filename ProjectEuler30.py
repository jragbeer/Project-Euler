import numpy as np
import pandas as pd
from decimal import *
# Project Euler Problem 30
#
# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#
# 1634 = 14 + 64 + 34 + 44
# 8208 = 84 + 24 + 04 + 84
# 9474 = 94 + 44 + 74 + 44
# As 1 = 14 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.


xx = [str(x) for x in range(1,1000000)]
def check(p):
    b = []
    for x in p:
        b.append(int(x)**5)
    if sum(b) == int(p):
        return int(p)
    else:
        return 0
d = []
for x in xx:
    d.append(check(x))
print(sum(d)-1)


