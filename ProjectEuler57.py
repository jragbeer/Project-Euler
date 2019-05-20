#Project Euler Problem 57
#
# It is possible to show that the square root of two can be expressed as an infinite continued fraction.
#
# √ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...
#
# By expanding this for the first four iterations, we get:
#
# 1 + 1/2 = 3/2 = 1.5
# 1 + 1/(2 + 1/2) = 7/5 = 1.4
# 1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
# 1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...
#
# The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.
#
# In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?

# a = '1+1/2'
# def thing(b):
#     q = b.rfind('2')
#     return b[:q]+'{}'.format('(2+1/2)')+')'*b[:q].count('(')
# p = 0
# for x in range(100):
#     a = thing(a)
    # c = eval(a)
    # print(a, c)
    # if c[0] > c[1]:
    #     p += 1
# print(p)
top = [1,3]
bottom = [1,2]
x = 1
num = 0
while x < 1000:
    next_top = top[x]*2 + top[x-1]
    next_bottom = bottom[x]*2 + bottom[x-1]
    top.append(next_top)
    bottom.append(next_bottom)
    if len(str(next_top)) > len(str(next_bottom)):
        num += 1
    x += 1
print(num)



