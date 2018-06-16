import numpy as np
import datetime
# Project Euler Problem 33

# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
timee = datetime.datetime.now()
print(timee)
d = []
for x in range(10, 100):
    for y in range(10, 100):
        if str(x)[0] == str(y)[0]:
            try:
                if int(str(x)[1])/int(str(y)[1]) == x/y:
                    d.append(['{}/{}'.format(x,y),x/y ])
            except:
                pass
        if str(x)[0] == str(y)[1]:
            try:
                if int(str(x)[1])/int(str(y)[0]) == x/y:
                    d.append(['{}/{}'.format(x, y), x / y])
            except:
                pass
        if str(x)[1] == str(y)[0]:
            try:
                if int(str(x)[0])/int(str(y)[1]) == x/y:
                    d.append(['{}/{}'.format(x, y), x / y])
            except:
                pass
        if str(x)[1] == str(y)[1] and str(x)[1] != '0':
            try:
                if int(str(x)[0])/int(str(y)[0]) == x/y:
                    d.append(['{}/{}'.format(x, y), x / y])
            except:
                pass
r = 1.0
for x in d:
    if x[1] < 1.0:
        r = r*x[1]
print(1/r)
print(datetime.datetime.now()-timee)
