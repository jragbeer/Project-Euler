import numpy as np
import pandas as pd

# Project Euler Problem 7
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?
#
a = 2
xn = range(1,120000000)

for x in range(len(xn)):
    count = 0
    for z in range(2,len(xn[:x])):
        if xn[x]%xn[z] != 0:
            count = count + 1

        if count == xn[x]-3:
            a = a + 1

        if a == 10001:
            print(a, xn[x])

