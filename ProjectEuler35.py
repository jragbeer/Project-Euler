import numpy as np

# Project Euler Problem 35
#
# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
# How many circular primes are there below one million?

def is_prime(n):
    if n % 2 == 0 or n%3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i+=6
    return True

def check(d):
    d = str(d)
    t = (d[x:] + d[:x] for x in range(len(d)))
    b = [y for y in t if is_prime(int(y))]
    if len(b)== len(d):
        return True
    return False

p = [x for x in range(98, 1000001) if check(x)]
print(len(p)+13)



        # for x in range(len(z)):
        #     t.append(d[x:]+d[:x])
