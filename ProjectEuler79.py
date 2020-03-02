import cProfile
import io
import pstats

# Project Euler Problem 79
# A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.
#
# The text file, keylog.txt, contains fifty successful login attempts.
#
# Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.

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

@profile
def run():

    def func(num, strt):
        a = num[0]
        b = num[1]
        c = num[2]
        try:
            ind_a = strt.index(a)
        except:
            ind_a = -1
        if a in strt:
            if b in strt:
                if c in strt:
                    pass
                else:
                    strt.insert(ind_a, c)
            else:
                strt.insert(ind_a, b)
        else:
            strt.insert(0, a)
        ind_a = strt.index(a)
        ind_b = strt.index(b)
        ind_c = strt.index(c)
        if ind_a < ind_c:
            pass
        else:
            strt.remove(a)
            strt.insert(ind_c, a)

        if ind_a < ind_b:
            pass
        else:
            strt.remove(a)
            strt.insert(ind_b, a)

        if ind_b < ind_c:
            pass
        else:
            strt.remove(b)
            strt.insert(ind_c, b)

        return strt

    with open("p079_keylog.txt", 'rb') as f:
        data = f.readlines()
        data = [x.decode().strip() for x in data]
        start = [item for sublist in [data[0], data[1]] for item in sublist]
        for y in data[2:]:
            start = func(y, start)
        print(''.join(start))
run()