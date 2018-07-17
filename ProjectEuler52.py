import numpy as np

#Project Euler Problem 52
#
# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
#
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
#
for x in range(1,100000000):
    b = [x * b for b in range(1,7)]
    for y in range(len(b)):
        if set(str(b[0])) == set(str(b[y])):
            if set(str(b[1])) == set(str(b[y])):
                try:
                    if set(str(b[2])) == set(str(b[y])):
                        try:
                            if set(str(b[3])) == set(str(b[y])):
                                q = int(''.join(set(str(b[0]))))
                                d = int(''.join(set(str(b[1]))))
                                t = int(''.join(set(str(b[2]))))
                                v = int(''.join(set(str(b[3]))))
                                # print(set(str(b[0])),set(str(b[y])))
                                print(b)
                                if len(b) == 6:
                                    break
                        except:
                            pass
                except:
                    pass


