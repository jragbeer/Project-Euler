import numpy as np
import pandas as pd

# Project Euler Problem 37
# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

def is_prime(n):
    if n == 3:
        return True
    if n % 2 == 0 or n%3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i+=6
    return True


def rtrunc(n):
    n = str(n)
    if int(n[-1]) == 1:
        return False
    if int(n[-1]) == 0 or int(n[-1])% 2 == 0:
        return False
    p = len(n)
    while p > 1:
        n = n[-p+1:]
        if not is_prime(int(n)):
            return False
        p = len(n)
    return True

def ltrunc(n):
    n = str(n)
    if int(n[0]) == 1:
        return False
    if int(n[0]) == 0 or int(n[0])% 2 == 0:
        return False
    p = len(n)
    while p > 1:
        n = n[:p-1]
        if not is_prime(int(n)):
            return False
        p = len(n)
    return True

def func(n):
    if not is_prime(n):
        return False
    if rtrunc(n):
        if ltrunc(n):
            return True
d = [i for i in range(10, 1000000)]
pp = [x for x in d if func(x)]
print(sum(pp)+23)
