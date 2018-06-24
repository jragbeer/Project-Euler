import numpy as np
import datetime

# Project Euler Problem 41

# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
#
# What is the largest n-digit pandigital prime that exists?
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
def zeros(n):
    n = str(n)

    for x in n:
        if x == '0':
            return False
    return True
def check(n):
    n = str(n)
    for x in n:
        if int(x) in range(len(n)+1, 10):
            return False
    return True

p = (x for x in np.arange(2143,87654322, dtype = 'uint64'))
r = (x for x in p if len(set(str(x))) == len(str(x)))
q = (x for x in r if is_prime(x))
t = (x for x in q if zeros(x))
w = [x for x in t if check(x)]
print(w[-1])
print(datetime.datetime.now()-timee)