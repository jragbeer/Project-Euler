import numpy as np
import pandas as pd

# Project Euler Problem 4
#
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

x = y = range(100,1000)
z = [str(p*q) for p in x for q in y]
n = [int(x) for x in z if x == x[::-1]]
print(max(n))