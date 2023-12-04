sum = 0
with open("input.txt") as f:
    cards = [line.strip() for line in f.readlines()]


def cleanup(str_list):
    return list(
        map(lambda x: int(x.strip()), filter(lambda x: x != "", str_list.split(" ")))
    )


card_count = len(cards)
card_map = {}
for i in range(card_count):
    card_map[i + 1] = 1  # 1 indexed

for card in cards:
    card_split = card.split(":")
    card_id = int(card_split[0].replace("Card", "").strip())
    values_split = card_split[1].split("|")
    winnings = cleanup(values_split[0])
    havings = cleanup(values_split[1])
    print(f"Card {card_id}: {winnings} | {havings}")

    matching_count = 0
    for number in havings:
        if number in winnings:
            matching_count += 1
            offset = card_id + matching_count
            if offset <= card_count:
                card_map[offset] += 1 * card_map[card_id]
    sum += card_map[card_id]

print(sum)
