import numpy as np
import datetime
import itertools

# Project Euler Problem 62
# The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.
#
# Find the smallest cube for which exactly five permutations of its digits are cube.

p = [str(x**3) for x in range(1,10001)]

# for x in p:
#     # d = []
#     # for y in list(itertools.permutations(x)):
#     #     if ''.join(y) in p:
#     #         d.append(''.join(y))
#     # d =
#     d = list(set([''.join(y) for y in list(itertools.permutations(x)) if ''.join(y) in p]))
#     if len(d) == 5:
#         break

z = (list({''.join(y) for y in list(itertools.permutations(x)) if ''.join(y) in p}) for x in p if len(list({''.join(y) for y in list(itertools.permutations(x)) if ''.join(y) in p})) == 5)
print(next(z))