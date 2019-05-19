#Project Euler Problem 54
#
#
# In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:
#
# High Card: Highest value card.
# One Pair: Two cards of the same value.
# Two Pairs: Two different pairs.
# Three of a Kind: Three cards of the same value.
# Straight: All cards are consecutive values.
# Flush: All cards of the same suit.
# Full House: Three of a kind and a pair.
# Four of a Kind: Four cards of the same value.
# Straight Flush: All cards are consecutive values of same suit.
# Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
# The cards are valued in the order:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
#
# If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.
#
# Consider the following five hands dealt to two players:
#
# Hand	 	Player 1	 	Player 2	 	Winner
# 1	 	5H 5C 6S 7S KD
# Pair of Fives
#  	2C 3S 8S 8D TD
# Pair of Eights
#  	Player 2
# 2	 	5D 8C 9S JS AC
# Highest card Ace
#  	2C 5C 7D 8S QH
# Highest card Queen
#  	Player 1
# 3	 	2D 9C AS AH AC
# Three Aces
#  	3D 6D 7D TD QD
# Flush with Diamonds
#  	Player 2
# 4	 	4D 6S 9H QH QC
# Pair of Queens
# Highest card Nine
#  	3D 6D 7H QD QS
# Pair of Queens
# Highest card Seven
#  	Player 1
# 5	 	2H 2D 4C 4D 4S
# Full House
# With Three Fours
#  	3C 3D 3S 9S 9D
# Full House
# with Three Threes
#  	Player 1
# The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.
#
# How many hands does Player 1 win?

from collections import Counter

def compare(a,b):
    a_nums = [x[0] for x in a]
    b_nums = [x[0] for x in b]
    a_suit = [x[1] for x in a]
    b_suit = [x[1] for x in b]

    b_number_result, b_cards_ordered = check_numbers(b_nums)
    a_number_result, a_cards_ordered = check_numbers(a_nums)

    b_suit_result, b_most_common_suit = check_suit(b_suit)
    a_suit_result, a_most_common_suit = check_suit(a_suit)

    b_final = b_number_result
    if b_final == 5:
        if b_number_result == 4:
            if b_cards_ordered == sorted(range(10,15),reverse=True):
                b_final = 9
            else:
                b_final = 8
        else:
            b_final = b_number_result


    a_final = a_number_result
    if a_final == 5:
        if a_number_result == 4:
            if a_cards_ordered == sorted(range(10,15)):
                a_final = 9
            else:
                a_final = 8
        else:
            a_final = a_number_result

    if a_final == b_final:
        if a_final == 0:
            for i in range(5):
                if b_cards_ordered[0] > a_cards_ordered[0]:
                    return 2, b_final
                elif b_cards_ordered[0] < a_cards_ordered[0]:
                    return 1, a_final
        elif a_final == 1:
            a_cards_pairs = Counter(a_cards_ordered)
            b_cards_pairs = Counter(b_cards_ordered)

            if a_cards_pairs.most_common(1)[0] > b_cards_pairs.most_common(1)[0]:
                return 1, a_final
            elif a_cards_pairs.most_common(1)[0] < b_cards_pairs.most_common(1)[0]:
                return 2, b_final
            else:
                for i in range(5):
                    if b_cards_ordered[0] > a_cards_ordered[0]:
                        return 2, b_final
                    elif b_cards_ordered[0] < a_cards_ordered[0]:
                        return 1, a_final

    winner = max(a_final, b_final)
    if winner == a_final:
        return 1, a_final
    elif winner == b_final:
        return 2, b_final

            # else:
            #     pass

def check_numbers(hand):

    new_sorted_nums = sorted([card_rank_mapping[card] for card in hand], reverse = True)
    t = Counter(hand).most_common(5)
    z = [x[1] for x in t]

    if new_sorted_nums == [14, 5, 4, 3, 2]:
        return 4, new_sorted_nums

    if z[0] == 4:
        # four of a kind
        return 7, new_sorted_nums
    elif z[0] == 3:
        if z[1] == 2:
            # full house
            return 6, new_sorted_nums
        else:
            # three of a kind
            return 3, new_sorted_nums
    elif z[0] == 2:
        if z[1] == 2:
            # two pairs
            return 2, new_sorted_nums
        else:
            # one pair
            return 1, new_sorted_nums
    else:

        if new_sorted_nums[0] - new_sorted_nums[1] == 1:
            if new_sorted_nums[1] - new_sorted_nums[2] == 1:
                if new_sorted_nums[2] - new_sorted_nums[3] == 1:
                    if new_sorted_nums[3] - new_sorted_nums[4] == 1:
                        return 4, new_sorted_nums
        # high card
        return 0, new_sorted_nums

def check_suit(hand):

    t = Counter(hand).most_common(5)
    z = [x[1] for x in t]
    if len(z)==1:
        return 5, t[0][0]
    else:
        return 0, t[0][0]


# 0 -- High Card: Highest value card.
# 1 -- One Pair: Two cards of the same value.
# 2 -- Two Pairs: Two different pairs.
# 3 -- Three of a Kind: Three cards of the same value.
# 4 -- Straight: All cards are consecutive values.
# 5 -- Flush: All cards of the same suit.
# 6 -- Full House: Three of a kind and a pair.
# 7 -- Four of a Kind: Four cards of the same value.
# 8 -- Straight Flush: All cards are consecutive values of same suit.
# 9 -- Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

card_rank_mapping = {'J':11, 'T':10, 'Q':12, 'K':13, 'A':14}
card_rank_mapping_p2 = {str(i): i for i in range(2,10)}

card_rank_mapping.update(card_rank_mapping_p2)

card_suit_mapping = {'C': 1, 'D':2, 'H':3, 'S':4}


with open('p054_poker.txt', 'r') as f:
    wow = f.readlines()
    player_one_wins = 0
    for yy in range(len(wow)):
        hands = wow[yy].strip().split()
        hand1 = hands[:5]
        hand2 = hands[5:]
        this_hand_winner, this_hand_rank = compare(hand1, hand2)
        if this_hand_winner == 1:
            player_one_wins += 1
    print(player_one_wins)