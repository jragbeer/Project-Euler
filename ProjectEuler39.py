import numpy as np
import datetime
import math

# Project Euler Problem 39
#
# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
#
# {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p ≤ 1000, is the number of solutions maximised?
#soh cah toa
timee = datetime.datetime.now()
print(timee)

qq = {}
for p in np.arange(120,1001,2):
    qq[str(p)] = 0
    new = []
    for x in np.arange(1, np.round((p+1)/2)):
        for y in np.arange(1, np.round((p+1)/2)):
            for z in np.arange(1, np.round((p+1)/2)):
                if x+y+z == p:
                    if x**2 + y**2 == z**2:
                        new.append(sorted([x,y,z]))

    for x in range(len(new)):

        if new[x] not in new[x+1:]:
            print(new[x], p)
            qq[str(p)] = qq[str(p)]+len(new[x])
print(qq)
print(max(qq, key = qq.get))
print(datetime.datetime.now()-timee)
