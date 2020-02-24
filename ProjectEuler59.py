import datetime
import cProfile
import io
import pstats
from numpy import binary_repr
import numpy as np
import binascii
import itertools
from pprint import pprint
# Project Euler Problem 59
# Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.
#
# A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.
#
# For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.
#
# Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.
#
# Your task has been made easy, as the encryption key consists of three lower case characters. Using p059_cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.

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
def main():
    def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
        n = int(bits, 2)
        return int2bytes(n).decode(encoding, errors)

    def int2bytes(i):
        hex_string = '%x' % i
        n = len(hex_string)
        return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

    with open('p059_cipher.txt', 'rb') as f:
        data = f.read().decode('utf-8')
        combos = [x for x in itertools.permutations(range(97, 123), 3)]
        # combos = [(103, 111, 100)]
        first = data.split(',')[::3]
        second = data.split(',')[1::3]
        third = data.split(',')[2::3]
        for each in combos:
            full = {'first': [], 'second': [], "third": []}
            for x in range(len(first)):
                output = {'first':[], 'second':[], "third":[]}
                for t in range(len(binary_repr(int(first[x]), 8))):
                    try:
                        xor_first = binary_repr(each[0], 8)[t] != binary_repr(int(first[x]), 8)[t]
                        xor_second = binary_repr(each[1], 8)[t] != binary_repr(int(second[x]), 8)[t]
                        xor_third = binary_repr(each[2], 8)[t] != binary_repr(int(third[x]), 8)[t]
                        output['first'].append(str(int(xor_first)))
                        output['second'].append(str(int(xor_second)))
                        output['third'].append(str(int(xor_third)))
                        r = ''.join(output['first'])
                        q = ''.join(output['second'])
                        s = ''.join(output['third'])
                    except Exception as e:
                        xor_first = binary_repr(each[0], 8)[t] != binary_repr(int(first[x]), 8)[t]
                        output['first'].append(str(int(xor_first)))
                        r = ''.join(output['first'])

                full['first'].append(text_from_bits(r))
                full['second'].append(text_from_bits(q))
                full['third'].append(text_from_bits(s))

            full["first"] = full["first"][:len(first)]
            full["second"] = full["second"][:len(second)]
            full["third"] = full["third"][:len(third)]

            nuts = []
            for wow in range(len(first)):
                try:
                    nuts.append(full['first'][wow])
                except:
                    pass
                try:
                    nuts.append(full['second'][wow])
                except:
                    pass
                try:
                    nuts.append(full['third'][wow])
                except:
                    pass
            final = ''.join(nuts)
            print(each)
            if '. ' in final:
                if 'the' in final:
                    if 'are' in final:
                        if ' I ' in final:
                            print(final)
                            print(sum([ord(x) for x in final]))
                            break

main()
