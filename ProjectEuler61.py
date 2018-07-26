import numpy as np
import datetime
import itertools

# Project Euler Problem 61
# Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers are all figurate (polygonal) numbers and are generated by the following formulae:
#
# Triangle	 	P3,n=n(n+1)/2	 	1, 3, 6, 10, 15, ...
# Square	 	P4,n=n2	 	1, 4, 9, 16, 25, ...
# Pentagonal	 	P5,n=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
# Hexagonal	 	P6,n=n(2n−1)	 	1, 6, 15, 28, 45, ...
# Heptagonal	 	P7,n=n(5n−3)/2	 	1, 7, 18, 34, 55, ...
# Octagonal	 	P8,n=n(3n−2)	 	1, 8, 21, 40, 65, ...
# The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three interesting properties.
#
# The set is cyclic, in that the last two digits of each number is the first two digits of the next number (including the last number with the first).
# Each polygonal type: triangle (P3,127=8128), square (P4,91=8281), and pentagonal (P5,44=2882), is represented by a different number in the set.
# This is the only set of 4-digit numbers with this property.
# Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and octagonal, is represented by a different number in the set.
def tri(n):
    return int((n*(n+1))/2)
def square(n):
    return n**2
def pent(n):
    return int((n*(3*n-1))/2)
def hex(n):
    return n*(2*n-1)
def hept(n):
    return int(n*(5*n-3)/2)
def oct(n):
    return n*(3*n-2)

tris = [tri(x) for x in range(1000) if tri(x)>999 and tri(x)<10001]
squares = [square(x) for x in range(1000) if square(x)>999 and square(x)<10001]
pents = [pent(x) for x in range(1000) if pent(x)>999 and pent(x)<10001]
hexs = [hex(x) for x in range(1000) if hex(x)>999 and hex(x)<10001]
hepts = [hept(x) for x in range(1000) if hept(x)>999 and hept(x)<10001]
octs = [oct(x) for x in range(1000) if oct(x)>999 and oct(x)<10001]
a = '8256 5625 2512 1281 8128 2882'

a = a.split()
print(a)
a = sum([int(x) for x in a ])
print(a)
# b = list(itertools.permutations([tris, squares, pents, hexs, hepts, octs]))
# print(b)
# print(b[0])
# print(tris)
# for pp in b:
#     for x in pp[0]:
#         for y in pp[1]:
#             for z in pp[2]:
#                 for t in pp[3]:
#                     for u in pp[4]:
#                         for i in pp[5]:
#                             if str(x)[2:] == str(y)[:2]:
#                                 if str(y)[2:] == str(z)[:2]:
#                                     if str(z)[2:] == str(t)[:2]:
#                                         if str(t)[2:] == str(u)[:2]:
#                                             if str(u)[2:] == str(i)[:2]:
#                                                 if str(i)[2:] == str(x)[:2]:
#                                                     print(x,y,z,t,u,i)



