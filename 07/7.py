from functools import cmp_to_key


card_vals = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 1,
    'T': 10
}

all_cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J','Q', 'K', 'A']


def score(hand):
    hand = list(hand)
    hand.sort()
    if hand[0] == hand[1] == hand[2] == hand[3] == hand[4]:
        return 7
    if hand[0] == hand[1] == hand[2] == hand[3] or hand[1] == hand[2] == hand[3] == hand[4]:
        return 6
    if (hand[0] == hand[1] and hand[2] == hand[3] == hand[4]) or (hand[0] == hand[1] == hand[2] and hand[3] == hand[4]):
        return 5
    for i in range(len(hand) - 2):
        if hand[i] == hand[i + 1] == hand[i + 2]:
            return 4
    if (hand[0] == hand[1] and hand[2] == hand[3]) or (hand[1] == hand[2] and hand[3] == hand[4]) or (hand[0] == hand[1] and hand[3] == hand[4]):
        return 3
    for i in range(4):
        if hand[i] == hand[i + 1]:
            return 2
    return 1

def compare(tuple1, tuple2):
    hand1 = tuple1[1]
    hand2 = tuple2[1]
    if score(hand1) > score(hand2):
        return 1
    elif score(hand1) < score(hand2):
        return -1
    else:
        for i in range(len(hand1)):
            card1 = card_vals[hand1[i]] if hand1[i] in card_vals else int(hand1[i])
            card2 = card_vals[hand2[i]] if hand2[i] in card_vals else int(hand2[i])
            if card1 > card2:
                return 1
            elif card1 < card2:
                return -1
    return 0


def part1():
    res = 0
    with open('7.in') as f:
        lines = f.read().strip()
    all_hands = lines.split('\n')
    scores = []
    for hand in all_hands:
        scores.append((score(hand.split()[0]), hand.split()[0], int(hand.split()[1])))
    scores.sort(key=cmp_to_key(compare))
    for i in range(len(scores)):
        res += scores[i][2] * (i + 1)
    print(res)

def score2(hand):
    hand = list(hand)
    hand.sort()
    if hand[0] == hand[1] == hand[2] == hand[3] == hand[4]:
        return 7
    if hand[0] == hand[1] == hand[2] == hand[3] or hand[1] == hand[2] == hand[3] == hand[4]:
        return 6
    if (hand[0] == hand[1] and hand[2] == hand[3] == hand[4]) or (hand[0] == hand[1] == hand[2] and hand[3] == hand[4]):
        return 5
    for i in range(len(hand) - 2):
        if hand[i] == hand[i + 1] == hand[i + 2]:
            return 4
    if (hand[0] == hand[1] and hand[2] == hand[3]) or (hand[1] == hand[2] and hand[3] == hand[4]) or (hand[0] == hand[1] and hand[3] == hand[4]):
        return 3
    for i in range(4):
        if hand[i] == hand[i + 1]:
            return 2
    return 1


def compare2(tuple1, tuple2):
    if tuple1[0] < tuple2[0]:
        return -1
    elif tuple1[0] > tuple2[0]:
        return 1
    hand1 = tuple1[1]
    hand2 = tuple2[1]
    for i in range(len(hand1)):
        card1 = card_vals[hand1[i]] if hand1[i] in card_vals else int(hand1[i])
        card2 = card_vals[hand2[i]] if hand2[i] in card_vals else int(hand2[i])
        if card1 > card2:
            return 1
        elif card1 < card2:
            return -1
    return 0


def part2():
    res2 = 0
    with open('7.in') as f:
        lines = f.read().strip()
    all_hands = lines.split('\n')
    scores = []
    for hand_line in all_hands:
        hand, bid = hand_line.split()
        bid = int(bid)
        max_score = 0
        for new_card in all_cards:
            new_hand = hand.replace('J', new_card)
            max_score = max(max_score, score2(new_hand))
        scores.append((max_score, hand, bid))
    scores.sort(key=cmp_to_key(compare2))
    for i in range(len(scores)):
        res2 += scores[i][2] * (i + 1)
    print(res2)


if __name__ == "__main__":
    part1()
    part2()
