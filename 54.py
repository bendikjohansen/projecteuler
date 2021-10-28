from collections import Counter

file = open('54.txt', 'r')
plays = [[row.strip().split(' ')[:5], row.strip().split(' ')[5:]] for row in file.readlines()]
def values_per_suit(hand): return [[to_numerical(card[0]) for card in hand if card[1] == suit] for suit in 'CHSD']

def to_numerical(value):
    if value == 'A': return 14
    if value == 'K': return 13
    if value == 'Q': return 12
    if value == 'J': return 11
    if value == 'T': return 10
    return int(value)

def royal_flush(values): return any([set(suit) == set(range(10,15)) for suit in values]), 1

def straight_flush(values):
    return any([[v - min(suit) for v in sorted(suit)] == [0,1,2,3,4] for suit in values]), 1

def four_of_a_kind(values):
    most_common = Counter([value for suit in values for value in suit]).most_common()[0]
    return most_common[1] == 4, most_common[0]

def full_house(values):
    most_common = Counter([value for suit in values for value in suit]).most_common()
    return most_common[0][1] == 3 and most_common[1][1] == 2, most_common[0][0]

def flush(values):
    return any([len(suit) == 5 for suit in values]), 1

def straight(values):
    flat_values = sorted([value for suit in values for value in suit])
    return [v - min(flat_values) for v in flat_values] == [0,1,2,3,4], 1

def three_of_a_kind(values):
    counted_values = Counter([value for suit in values for value in suit])
    value, count = counted_values.most_common()[0]
    return count == 3, value

def two_pairs(values):
    most_common = Counter([value for suit in values for value in suit]).most_common()
    return len(most_common) >= 2 and most_common[0][1] == 2 and most_common[1][1] == 2, max(most_common[0][0], most_common[1][0])

def one_pair(values):
    most_common = Counter([value for suit in values for value in suit]).most_common()[0]
    return most_common[1] == 2, most_common[0]

def evaluate_highest_cards(hand):
    values = values_per_suit(hand)
    return sum([v * 15**i for i, v in enumerate(list(sorted([value for suit in values for value in suit])))])

def evaluate_hand(hand):
    values = values_per_suit(hand)
    checks = [royal_flush, straight_flush, four_of_a_kind, full_house, flush, straight, three_of_a_kind, two_pairs, one_pair]
    for index, check in enumerate(checks):
        valid, score = check(values)
        if valid:
            return 15**(len(checks)-index) * score
    return 0

def evaluate_play(first_hand, second_hand):
    first_eval, second_eval = evaluate_hand(first_hand), evaluate_hand(second_hand)

    if first_eval > second_eval:
        return 1
    if second_eval > first_eval:
        return 0

    first_highest, second_highest = evaluate_highest_cards(first_hand), evaluate_highest_cards(second_hand)
    if first_highest > second_highest:
        return 1
    if second_highest > first_highest:
        return 0

print(sum([evaluate_play(*play) for play in plays]))
