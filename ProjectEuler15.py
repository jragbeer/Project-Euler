import numpy as np
import pandas as pd

# Project Euler Problem 15
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#
# How many such routes are there through a 20×20 grid?

def fact(n):
    nums = np.arange(1, n+1).tolist()
    b = 1
    for x in nums:
        b =b*x
    return b

ans = fact(40)/(fact(20)*fact(20))
print(ans)

