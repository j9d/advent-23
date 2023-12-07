from enum import IntEnum
from typing import Dict
from functools import cmp_to_key

class HandType(IntEnum):
    FIVE_OF_A_KIND = 6
    FOUR_OF_A_KIND = 5
    FULL_HOUSE = 4
    THREE_OF_A_KIND = 3
    TWO_PAIR = 2
    ONE_PAIR = 1
    HIGH_CARD = 0

ordering = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
hands: Dict[str, int] = {}
total = 0

def get_hand_type(hand: str) -> HandType:
    cards: Dict[str, int] = {}
    for card in hand:
        if not cards.get(card):
            cards[card] = 0
        cards[card] += 1
    counts = list(cards.values())
    highest = max(counts)
    if highest == 5:
        return HandType.FIVE_OF_A_KIND
    if highest == 4:
        return HandType.FOUR_OF_A_KIND
    if highest == 3:
        return HandType.FULL_HOUSE if 2 in counts else HandType.THREE_OF_A_KIND
    if highest == 2:
        return HandType.TWO_PAIR if counts.count(2) == 2 else HandType.ONE_PAIR
    return HandType.HIGH_CARD

def cmp(a: str, b: str) -> int:
    type_a = get_hand_type(a)
    type_b = get_hand_type(b)
    if type_a != type_b:
        return 1 if type_a > type_b else -1
    for card_a, card_b in zip(a, b):
        if card_a != card_b:
            return 1 if ordering.index(card_a[0]) > ordering.index(card_b[0]) else -1

with open("input.txt", "r") as f:
    for line in f:
        hand = line.split()
        hands[hand[0]] = int(hand[1])
hands_sorted = list(hands.keys())
hands_sorted.sort(key=cmp_to_key(cmp))
for idx, hand in enumerate(hands_sorted):
    total += (idx + 1) * hands[hand]

print(total)
