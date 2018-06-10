import numpy as np
import pandas as pd

# Project Euler Problem 42
# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.
#
# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?

def func(a):
    a = a.lower()
    if a == 'a':
        return 1
    elif a == 'b':
        return 2
    elif a == 'c':
        return 3
    elif a == 'd':
        return 4
    elif a == 'e':
        return 5
    elif a == 'f':
        return 6
    elif a == 'g':
        return 7
    elif a == 'h':
        return 8
    elif a == 'i':
        return 9
    elif a == 'j':
        return 10
    elif a == 'k':
        return 11
    elif a == 'l':
        return 12
    elif a == 'm':
        return 13
    elif a == 'n':
        return 14
    elif a == 'o':
        return 15
    elif a == 'p':
        return 16
    elif a == 'q':
        return 17
    elif a == 'r':
        return 18
    elif a == 's':
        return 19
    elif a == 't':
        return 20
    elif a == 'u':
        return 21
    elif a == 'v':
        return 22
    elif a == 'w':
        return 23
    elif a == 'x':
        return 24
    elif a == 'y':
        return 25
    elif a == 'z':
        return 26
bb = pd.read_csv('words.txt', names = None)
q = [0.5*n*(n+1) for n in range(1, 2000)]
p = [sum([func(x) for x in str(x)]) for x in bb]
d = [x for x in p if x in q]
print(len(d))