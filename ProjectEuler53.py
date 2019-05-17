# Project Euler 53

# There are exactly ten ways of selecting three from five, 12345:
#
# 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
#
# In combinatorics, we use the notation, 5C3=10.
#
# In general, nCr=n!r!(n−r)!, where r≤n, n!=n×(n−1)×...×3×2×1, and 0!=1.
#
# It is not until n=23, that a value exceeds one-million: 23C10=1144066.
#
# How many, not necessarily distinct, values of nCr for 1≤n≤100, are greater than one-million?
#
def factorial(x):
    c = 1
    for i in range(1,x+1):
        c*=i
    return c

def comb(q, r):
    r_fact = factorial(r)
    n_fact = factorial(q)
    both = factorial(q-r)
    try:
        return n_fact/(both*r_fact)
    except:
        return n_fact
count = 0
for y in range(101):
    for i in range(y-1):
        result = comb(y, i)
        if result > 1000000:
            count +=1

print(count)