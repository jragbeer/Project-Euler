import datetime
# Project Euler Problem 112
# Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.
#
# Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.
#
# We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.
#
# Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.
#
# Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.
#
# Find the least number for which the proportion of bouncy numbers is exactly 99%.

now = datetime.datetime.now()
possible = [x for x in range(2000001) if x * 0.99 == int(x*0.99)]

def inc(e):
    array = list(str(e))
    fun = []
    for i, each in enumerate(array):
        try:
            r = array[i + 1]
            if each <= r:
                fun.append(each)
        except IndexError:
                pass
    if len(fun) == len(array) - 1:
        return True
    return False
def dec(e):
    array = list(str(e))
    fun = []
    for i, each in enumerate(array):
        try:
            if each >= array[i + 1]:
                fun.append(each)
        except IndexError:
            pass
    if len(fun) == len(array) -1:
        return True
    return False
def inner(input_num):
    bouncy_numbers = []
    for i in range(10, input_num + 1):
        t = inc(i)
        # print(f"{i}, inc:{t}, dec:{q}")
        if not t:
            q = dec(i)
            if not q:
                bouncy_numbers.append(i)
    return len(bouncy_numbers), len(bouncy_numbers)/input_num
def outer(array, div):
    data = []
    for p in (x for x in range(array[-2], array[-1], div) if x in possible):
        a,b = inner(p)
        data.append(p)
        if b < 0.99:
            break
    return data

array = outer(outer(outer([2000000,1], -100000), -10000), -1000)
for p in (x for x in range(array[-2], array[-1], -1) if x in possible):
    a, b = inner(p)
    if b == 0.99:
        print(p,a,b)
        break
print(datetime.datetime.now()-now)
