from __future__ import annotations
from dataclasses import dataclass
from functools import cmp_to_key

card_values = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
card_values.reverse()  # make it increasing values


@dataclass
class HandBid:
    hand: str
    bid: int
    kind: int
    # strength: int # precomputed value


def getKind(hand: str) -> int:
    card_count_map = {}
    for card in card_values:
        card_count_map[card] = 0

    for card in hand:
        card_count_map[card] += 1

    card_counts_list = list(card_count_map.values())
    card_counts_list.sort(reverse=True)
    max_card_count = card_counts_list[0]
    second_max_card_count = card_counts_list[1]

    # Five of a kind, where all five cards have the same label: AAAAA
    if max_card_count == 5:
        return 6

    # Four of a kind, where four cards have the same label and one card has a different label: AA8AA
    if max_card_count == 4:
        return 5

    # Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
    if max_card_count == 3 and second_max_card_count == 2:
        return 4

    # Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
    if max_card_count == 3 and second_max_card_count == 1:
        return 3

    # Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
    if max_card_count == 2 and second_max_card_count == 2:
        return 2

    # One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
    if max_card_count == 2 and second_max_card_count == 1:
        return 1

    # High card, where all cards' labels are distinct: 23456
    if max_card_count == 1:
        return 0

    raise Exception("Shouldn't happen")


def compareHands(hand1: HandBid, hand2: HandBid) -> int:
    if hand1.kind > hand2.kind:
        return 1
    elif hand1.kind < hand2.kind:
        return -1
    else:
        return compareStrengthIfSameKind(hand1.hand, hand2.hand)


def compareStrengthIfSameKind(hand1: str, hand2: str) -> int:
    for i in range(len(hand1)):
        card1_value = getValueOfCard(hand1[i])
        card2_value = getValueOfCard(hand2[i])
        if card2_value != card1_value:
            return 1 if card1_value > card2_value else -1
        else:
            continue
    raise Exception("Shouldn't happen")


def getValueOfCard(card: str) -> int:
    return card_values.index(card)


with open("input.txt") as f:
    hands_str = [line.strip() for line in f.readlines()]

handbids = []
for hand_str in hands_str:
    hand_split = hand_str.split(" ")
    hand = hand_split[0]
    bid = int(hand_split[1])
    handbids.append(HandBid(hand, bid, getKind(hand)))
    # print(f"{hand} {bid}")

handbids = sorted(handbids, key=cmp_to_key(compareHands))

total_winnings = 0
for rank, handbid in enumerate(handbids):
    print(f"Hand {rank}: {handbid.hand} {handbid.bid} {handbid.kind}")
    total_winnings += (rank + 1) * handbid.bid

print(total_winnings)
