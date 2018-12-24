import datetime
import cProfile
import io
import pstats

def profile(fnc):
    """A decorator that uses cProfile to profile a function"""

    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        retval = fnc(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retval

    return inner
# Project Euler Problem 62
# The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.
#
# Find the smallest cube for which exactly five permutations of its digits are cube.
# timee = datetime.datetime.now()
#
#
# p = [str(x**3) for x in range(10001,50001)]
# print(timee)
#
# # for x in p:
# #     # d = []
# #     # for y in list(itertools.permutations(x)):
# #     #     if ''.join(y) in p:
# #     #         d.append(''.join(y))
# #     # d =
# #     d = list(set([''.join(y) for y in list(itertools.permutations(x)) if ''.join(y) in p]))
# #     if len(d) == 5:
# #         break
#
# # z = [list({''.join(y) for y in list(itertools.permutations(x)) if ''.join(y) in p}) for x in p]
#
# # def main():
# #     for x in p:
# #         b = set(''.join(y) for y in itertools.permutations(x))
# #         if len(b)==5:
# #             print(b)
# @profile
# def main():
#     k = ''.join
#     w = itertools.permutations
#     b = [(k(y) for y in w(x)) for x in p]
#     for x in b:
#         if len(list(x)) == 5:
#             print(x)
# main()

@profile
def main():
    timee = datetime.datetime.now()
    S = {}
    for i in range(1, 10001):
        h = tuple(sorted(list(str(i * i * i))))
        if h in S:
            S[h]= S[h] + [i * i * i]
            if len(S[h]) == 5:
                print(S[h])
                break
        else:
            S[h] = [i * i * i]
    timee2 = datetime.datetime.now()
    print(timee2-timee)
main()