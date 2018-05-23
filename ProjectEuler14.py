import pandas as pd
import numpy as np
import datetime

timee = datetime.datetime.now()

kk = np.array([i for i in np.arange(1,1000001,2)])

def evenfunc(n):
    return n/2
def oddfunc(n):
    return 3*n + 1
def func(n):
    cnt = 1

    if n % 2 == 0:
        p = evenfunc(n)
        cnt = cnt+1
    else:
        p = oddfunc(n)
        cnt = cnt + 1

    while p > 1:
        if p%2 == 0:
            p = evenfunc(p)
            cnt = cnt + 1
        else:
            p = oddfunc(p)
            cnt = cnt + 1

    return cnt

rr = [func(x) for x in kk]
print(datetime.datetime.now()-timee)
print('\n{}'.format(kk[np.argmax(rr)]))