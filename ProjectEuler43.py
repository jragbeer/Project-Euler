import numpy as np
import pandas as pd
from decimal import *
# Project Euler Problem 43

# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.
#
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
#
# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.

p = (x for x in iter(range(1023456789, 9876543211)) if len(str(x)) == len(set(str(x))))

def first(n):
    n = int(str(n)[1:4])
    if n % 2 == 0:
        return True

def second(n):
    n = int(str(n)[2:5])
    if n % 3 == 0:
        return True

def third(n):
    n = int(str(n)[3:6])
    if n % 5 == 0:
        return True

def fourth(n):
    n = int(str(n)[4:7])
    if n % 7 == 0:
        return True

def fifth(n):
    n = int(str(n)[5:8])
    if n % 11 == 0:
        return True

def sixth(n):
    n = int(str(n)[6:9])
    if n % 13 == 0:
        return True

def seventh(n):
    n = int(str(n)[7:10])
    if n % 17 == 0:
        return True

r = (x for x in p if first(x) if second(x) if third(x) if fourth(x) if fifth(x) if sixth(x) if seventh(x))

print(sum(r))