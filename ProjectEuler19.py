import pandas as pd
import numpy as np
#Project Euler 19
#jan 1 1900 was a monday
#how many sundays are there from jan 1 1901 to 2000 that fall on first of the month

#leap years are every 4 years except those that are centuries divisible by 400.
def check(x):
    if x % 4 == 0:
        return True
    return False

leapyear = [x for x in range(1901,2001) if check(x)]
year = range(1,366)
dd = sum([365 for x in range(1901,2001) if x not in leapyear])+len(leapyear)*366
r = [6]
q = 6
while q < dd:
    q = q+7
    r.append(q)
def firsts():
    c = []
    for x in range(1901, 2001):

        if x in leapyear:
            days = [31,29, 31, 30, 31, 30, 31, 31, 30, 31, 30 , 31]
        else:
            days = [31,28, 31, 30, 31, 30, 31, 31, 30, 31, 30 , 31]

        c.extend(days)
    return [sum(c[:x])+1 for x in range(len(c))]
print(len([x for x in firsts() if x in r]))