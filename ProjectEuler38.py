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
print(timee)

aa = range(1,10)
b = list(itertools.permutations(aa))
b = [list(x) for x in b]
r = [[str(x) for x in b[t]] for t in range(len(b))]
r = [int(''.join(x)) for x in r]
print(r)
z = []
for x in range(2,10):
    z.append([i for i in range(1,x)])

for x in range(1,np.round(int(987654321/2))):
    for y in z:
        print(x,y)


print(datetime.datetime.now()-timee)
