import numpy as np
import pandas as pd

xx = range(1, 5587021441)

def check(num):
    count = 0
    for y in range(1,21):


        if num % y == 0:
            count = count + 1
            #print(num,y,count)

        if count == 20:
            print('WOOOW:    ',num)



for x in xx[::-1]:
    check(x)
