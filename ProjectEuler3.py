import numpy as np
import pandas as pd
import datetime
# #Project Euler Problem 3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
timee = datetime.datetime.now()
print(timee)
#y = 13195
y = 600851475143

facty = [x for x in range(1,y) if y%x == 0]

new = []
for x in facty:
    for z in facty:
        if x%z != 0 and x > z:
            new.append((x,z))

p = {str(facty[x]): len(facty[:x])-1 for x in range(len(facty))}

first = [x[0] for x in new]
second = [x[1] for x in new]

df = pd.DataFrame(data = {'a':first, 'b':second})
dat = pd.DataFrame(df.groupby('a').count())

maxx = [x for x in dat.index if p[str(x)] == dat['b'][x]]
print(max(maxx))
print(datetime.datetime.now() - timee)
