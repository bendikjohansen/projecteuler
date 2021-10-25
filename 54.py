from collections import Counter

file = open('54.txt', 'r')
plays = [[rows.strip().split(' ')[:5], rows.strip().split(' ')[5:]] for rows in file.readlines()]

def values_per_suit(hand):
    return [
        [to_numerical(card[0]) for card in hand if card[1] == 'H'],
        [to_numerical(card[0]) for card in hand if card[1] == 'D'],
        [to_numerical(card[0]) for card in hand if card[1] == 'S'],
        [to_numerical(card[0]) for card in hand if card[1] == 'C']
    ]


def to_numerical(value):
    if value == 'A': return 14
    if value == 'K': return 13
    if value == 'Q': return 12
    if value == 'J': return 11
    if value == 'T': return 10
    return int(value)


def has_royal_flush(values):
    print(values)
    return any([set(suit) == set(range(10,15)) for suit in values])


def has_straight_flush(values):
    for suit in values:
        if [v - min(suit) for v in suit] == [0,1,2,3,4]:
            return True
    return False


def has_four_of_a_kind(values):
    counted_values = Counter([value for suit in values for value in suit])
    value, count = counted_values.most_common()[0]
    print(value, count)
    return count == 4, value


def has_full_house(values):
    counted_values = Counter([value for suit in values for value in suit])
    return counted_values.most_common()[0][1] >= 2 and any([len(suit) >= 3 for suit in values])


def has_flush(values):
    return any([len(suit) == 5 for suit in values])


def has_straight(values):
    flat_values = [value for suit in values for value in suit]
    print
    return [v - min(flat_values) for v in flat_values] == [0,1,2,3,4]

def evaluate_hand(hand):
    values = values_per_suit(hand)

    properties = []
    if has_royal_flush(values):
        properties.append('royal flush')
    if has_straight_flush(values):
        properties.append('straight flush')
    four_of_a_kind, value = has_four_of_a_kind(values)
    if four_of_a_kind:
        properties.append(('four of a kind', value))
    if has_full_house(values):
        properties.append('full house')
    if has_flush(values):
        properties.append('flush')
    if has_straight(values):
        properties.append('straight')
    
    return properties


print(evaluate_hand(['TS', 'TH', 'TC', 'TD', 'AS']))