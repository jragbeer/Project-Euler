import numpy as np

#Project Euler Problem 56

# A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.
#
# Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
print(max([sum([int(b) for b in str(x**y)]) for y in range(1,100) for x in range(1,100)]))