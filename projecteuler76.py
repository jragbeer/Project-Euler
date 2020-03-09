import gc
import cProfile
import io
import itertools
import pstats
import time

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

def add_first_two_numbers(b):
    return [b[0] + b[1]] + b[2:]
def all_pairs(a):
    w = [sorted((x, a-x)) for x in range(a,1,-1)]
    return w[1:]

def final(input_list):
    for each in input_list:
        print(1, each)
        try:
            input_list.append(add_first_two_numbers(each))
        except IndexError:
            pass
    print('-'*8)
    input_list = [sorted(x) for x in input_list if len(x) > 1]
    input_list.sort()
    input_list = list(k for k,_ in itertools.groupby(input_list))
    return input_list

@profile
def start():
    ti = time.time()
    num = 10
    stuff = [x for x in all_pairs(num)] + [[1 for x in range(num)]]
    stuff = final(stuff,)
    print(time.time()-ti)
    interesting = [len(stuff)+1, len(stuff)]
    print(len(stuff))
    r = 0
    while interesting[-2] != interesting[-1]:
        r+=1
        print(r)
        stuff = final(stuff)
        print(len(stuff))
        interesting.append(len(stuff))
        gc.collect()
    print()
    print(len(list(stuff)))
    print(time.time()-ti)

start()