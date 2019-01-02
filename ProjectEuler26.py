from decimal import *
# Project Euler Problem 26

# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
#
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
getcontext().prec = 3000
def main():
    p = [x for x in range(2,1001)]
    z = [[str(Decimal(1.0)/Decimal(x)).split('.')[1],x] for x in p]
    q = []
    for x in z:
        t = len(set(x[0][100:]))
        if t == 10:
            q.append(x[1])
    z2 = [x for x in z if x[1] in q ]
    def stuff(n):
        num = 6
        y = n[5:num+5]
        cc = []
        for x in range(len(n)):
            if y == n[x:num+x]:
                cc.append(x)
        return (cc[1]-cc[0])-1
    r = []
    for x in z2:

        r.append([stuff(x[0]),x[1]])
    print(sorted(r, key = lambda x: x[0], reverse = True))

main()
