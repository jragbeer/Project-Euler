import numpy as np
import pandas as pd
import datetime
import math
# Project Euler Problem 8
# Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.
#
# If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:
#
# 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
#
# It can be seen that 2/5 is the fraction immediately to the left of 3/7.
#
# By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size, find the numerator of the fraction immediately to the left of 3/7.

timee = datetime.datetime.now()
def hcf(p,u):
    ppp = math.ceil(p/2)+1
    uuu = math.ceil(u / 2) + 1
    z = [i for i in range(1,ppp) if p/i == int(p/i)]
    o = [i for i in range(1,uuu) if u/i == int(u/i)]
    qqq = [zz for zz in z if zz in o]
    if len(qqq) > 1:
        return False
    else:
        return True
def run():
    nn = 3/7
    ww = 1000001
    qq = {y/x:f"{y}/{x}" for x in range(1,ww) for y in range(1,x) if y/x <= nn if hcf(x,y)}
    a = (sorted(list(qq.keys())))
    print(qq[a[-2]])

run()
print(datetime.datetime.now()-timee)