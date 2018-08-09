import numpy as np
import pandas as pd
import datetime
#Project Euler Problem 92
# A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.
#
# For example,
#
# 44 → 32 → 13 → 10 → 1 → 1
# 85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89
#
# Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.
#
# How many starting numbers below ten million will arrive at 89?
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
