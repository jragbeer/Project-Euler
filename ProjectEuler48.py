import numpy as np
# Project Euler Problem 48
#
# The series, 11 + 22 + 33 + ... + 1010 = 10405071317.
#
# Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.

b = (x**x for x in range(1,1001))
print(str(sum(b))[-10:])
