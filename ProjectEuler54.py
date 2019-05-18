from collections import Counter
def func(a,b):
    a_nums = [x[0] for x in a]
    b_nums = [x[0] for x in b]
    a_symbol = [x[1] for x in a]
    b_symbol = [x[1] for x in b]
    result_b = check_twos(b_nums)
    result_a = check_twos(a_nums)
    print('HAND 1')
    print(result_a)
    print('HAND 2')
    print(result_b)


mapping = {'J':11, 'T':10, 'Q':12, 'K':13, 'A':14}
mapping_p2 = {str(i): i for i in range(2,10)}

mapping.update(mapping_p2)
print(mapping)
def check_twos(a):

    new_sorted_nums = sorted([mapping[zz] for zz in a], reverse = True)
    print(new_sorted_nums)



    t = Counter(a).most_common(5)
    z = [x[1] for x in t]
    if z[0] == 4:
        return 7
    elif z[0] == 3:
        if z[1] == 2:
            return 6 # full house
        else:
            return 3 # three of a kind
    elif z[0] == 2:
        if z[1] == 2:
            return 2  # two pairs
        else:
            return 1  # one pair
    else:
        return 0  # high card

with open('p054_poker.txt', 'r') as f:
    wow = f.readlines()
    for yy in range(len(wow)):
        hands = wow[yy].strip().split()
        hand1 = hands[:5]
        hand2 = hands[5:]
        print(hand1)
        print(hand2)
        func(hand1, hand2)