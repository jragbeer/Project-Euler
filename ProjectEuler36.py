import numpy as np
import datetime
# Project Euler Problem 36
#
# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
#
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not include leading zeros.)

timee = datetime.datetime.now()
print(timee)
def make_binary(n):
    b = str()
    for x in range(0,21)[::-1]:
        if n / 2**x >=1:
            n = n%2**x
            b = b + str(1)
        else:
            b = b+str(0)
    return b

xx = np.arange(1000000).tolist()
pp = [x for x in xx if str(x) == str(x)[::-1]]
qq = [x for x in pp if str(int(make_binary(x)))==str(int(make_binary(x)))[::-1]]
print(sum(qq))

print(datetime.datetime.now()-timee)
