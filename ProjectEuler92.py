import numpy as np
import pandas as pd
import datetime
#Project Euler Problem 1

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.
def run():
    zzz = datetime.datetime.now()
    def func1(n):
        c = 0
        z = 0
        p = n
        while True:
            p = func2(p)
            if p == 1:
                z += 1
                break
            if p == 89:
                c += 1
                break
        return z, c
    def func2(n):
        n = str(n)
        d = sum([int(x)**2 for x in n])
        return d
    w = [x for x in range(2, 10000001)]
    ay, by = zip(*[func1(x) for x in w])
    print(sum(by), '89')
    print(datetime.datetime.now()-zzz)
run()
