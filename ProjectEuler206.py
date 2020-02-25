import numpy as np
from tqdm import tqdm

# Project Euler Problem 46
# Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
# where each “_” is a single digit.
#
a = 1929394959697989990
b = 1020304050607080900
ceil = np.ceil(np.sqrt(a))
floor = np.floor(np.sqrt(b))

for x in tqdm(range(int(ceil)+1, int(floor), -1)):
    nice = x**2
    if nice == int(nice):
        if str(nice)[-1] == '0':
            if str(nice)[-3] == '9':
                if str(nice)[-5] == '8':
                    if str(nice)[-7] == '7':
                        if str(nice)[-9] == '6':
                            if str(nice)[-11] == '5':
                                if str(nice)[-13] == '4':
                                    if str(nice)[-15] == '3':
                                        if str(nice)[-17] == '2':
                                            print(x, x**2)
                                            break
