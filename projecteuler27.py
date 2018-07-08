import pandas as pd
import numpy as np
import datetime
timee = datetime.datetime.now()
# Project Euler 27
#
# Euler discovered the remarkable quadratic formula:
#
# n2+n+41
# It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41 is clearly divisible by 41.
#
# The incredible formula n2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.
#
# Considering quadratics of the form:
#
# n2+an+b, where |a|<1000 and |b|≤1000
#
# where |n| is the modulus/absolute value of n
# e.g. |11|=11 and |−4|=4
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.

def is_prime(n):
    if n % 2 == 0 or n%3 == 0:
        return False
    i = 5
    while (i*i <= n):
        if n % i == 0 or n% (i+2) == 0:
            return False
        i = i + 6
    return True

def func():
    for x in range(-999, 1000):
        for y in range(-1000, 1002):
            d = -1
            r = 0
            for z in range(100):
                num = z**2+z*x+y
                if num > 0:
                    if is_prime(num):
                        d +=1
                if d == z:
                    r +=1
                if r == z:
                    if r > 39:
                        print(r, z, x, y, datetime.datetime.now() - timee)

func()
