import numpy as np
import pandas as pd

# Project Euler Problem 3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

def is_prime(n):
    if n % 2 == 0 or n%3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True

num = 600851475143
pp = [i for i in np.arange(np.ceil(np.sqrt(num)))]
b = [x for x in pp if num%x == 0]
for y in b:
    if is_prime(y):
        print(y)
