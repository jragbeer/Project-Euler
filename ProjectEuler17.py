import numpy as np
# Project Euler Problem 16
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?

# one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen, twenty
#   1   2   3       4       5   6       7   8       9   10      11      12      13      14          15      16          17          18      19      20
def twodigit(n):
    n = str(n)
    #twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety
    nums = {'0':0,'2':6, '3':6, '4':5, '5':5, '6':5, '7':7, '8':6, '9':6}
    return nums[n]

def threedigit(n):
    n = str(n)
    nums = {'0': 0, '1': 3, '2': 3, '3': 5, '4': 4, '5': 4, '6': 3, '7': 5, '8': 5, '9': 4}
    return nums[n]+10

def check(n):
    nums = {'0':0,'1':3, '2':3, '3':5,'4':4,'5':4,'6':3,'7':5,'8':5,'9':4,'10':3}
    nums10 = {'11':6,'12':6,'13':8,'14':8,'15':7,'16':7,'17':9,'18':8,'19':8,'20':6}
    n = int(n)
    if n < 11:
        n = str(n)
        return nums[n]
    elif n < 21:
        n = str(n)
        return nums10[n]

def spell(n):
    if n < 21:
        return check(n)
    n=str(n)
    if len(n) == 3:
        f = threedigit(n[0])
        if int(n[1:3]) < 21:
            if str(n)[1:3] == '00':
                return f - 3
            if str(n)[1] == '0':
                return f + check(n[2])

            return f + check(str(n)[1:3])

        s = twodigit(n[1])
        t = check(n[2])
        return f+s+t
    elif len(n)==2:
        s = twodigit(n[0])
        t = check(n[1])
        return s+t
    elif len(n) == 1:
        return check(n)
    elif len(n) == 4:
        return 11
print(sum([spell(i) for i in range(1,1001)]))


