import numpy as np
import datetime

# Project Euler Problem 7
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?
timee = datetime.datetime.now()
def is_prime(n):
    if n % 2 == 0 or n%3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i+=6
    return True
a = 2
xn = [x for x in range(1,1200000) if is_prime(x)]
print(xn[9999])
print(datetime.datetime.now()-timee)