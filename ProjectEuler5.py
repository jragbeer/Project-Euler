import numpy as np
import pandas as pd

# Project Euler Problem 5
#
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

p  = 1*2*3*4*5*7*11*13*17*19*9*16+1
def check(num):
    count = 0
    for y in range(1,21):


        if num % y == 0:
            count = count + 1
            #print(num,y,count)

        if count == 20:
            print('WOOOW:    ',num)
xx = range(1, p)
for x in xx[::-1]:
    check(x)
