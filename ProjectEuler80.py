import numpy as np
import pandas as pd
import math
import decimal
# Project Euler Problem 80

# It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.
#
# The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.
#
# For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.
decimal.getcontext().prec = 120
print(sum([sum([int(x) for x in str(decimal.Decimal(y).sqrt()).replace('.','')[:100]]) for y in [x for x in range(100) if math.sqrt(x) != int(math.sqrt(x))]]))