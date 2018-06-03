import numpy as np
import datetime
# Project Euler Problem 34

# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

timee = datetime.datetime.now()
print(timee)
def fact(n):
    nums = np.arange(1, n+1).tolist()
    b = 1
    for x in nums:
        b =b*x
    return b

pp = np.arange(fact(9)).tolist()
rr = []
for x in pp:
    x = str(x)
    cc=[]
    for y in range(len(x)):
        if y == 0 or y ==9:
            pass

        cc.append(fact(int(x[y])))
    rr.append(sum(cc))

for x in range(len(rr)):
    if x == rr[x]:
        print(x, rr[x])

print(datetime.datetime.now()-timee)
