import numpy as np
def is_prime(n):
    if n % 2 == 0 or n%3 == 0:
        return False
    i = 5
    while (i*i <= n):
        if n % i == 0 or n% (i+2) == 0:
            return False
        i = i + 6
    return True
c = [2,3]+[a for a in range(1,700002,2) if is_prime(a)]
c = sorted(c)
d = (a for a in range(1,100002,2) if a not in c)
r = (2*a**2 for a in range(1,100))
print(list(c))
print(list(d))
print(list(r))
#
# for x in c:
#     for y in r:
#         if x+y not in d:
#             print(x+y)
g = [x+y for x in c for y in r if x+y not in d if x+y not in c if x+y%2 != 0]
print(sorted(set(g)))