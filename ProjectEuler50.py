import numpy as np

# Project Euler Problem 50

# The prime 41, can be written as the sum of six consecutive primes:
#
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
#
# Which prime, below one-million, can be written as the sum of the most consecutive primes?

def is_prime(n):
    if n % 2 == 0 or n%3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i+=6
    return True
p = [2,3]+[x for x in range(2,1000000) if is_prime(x)]
d = [y for x in range(len(p[:550])-1) for y in range(20,550) if sum(p[x:x+y]) in p]
r = np.argmax(d)
print(d[r])

for x in range(1,1001):
    if sum(p[x:x+d[r]]) in p:
        print(sum(p[x:x+d[r]]))
