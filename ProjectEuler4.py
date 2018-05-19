import numpy as np
import pandas as pd

x = y = range(100,1000)
z = [str(p*q) for p in x for q in y]
n = [int(x) for x in z if x == x[::-1]]
print(max(n))