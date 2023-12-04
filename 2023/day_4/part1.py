sum = 0
with open("input.txt") as f:
    cards = [line.strip() for line in f.readlines()]


def cleanup(str_list):
    return list(
        map(lambda x: int(x.strip()), filter(lambda x: x != "", str_list.split(" ")))
    )


for card in cards:
    card_split = card.split(":")
    card_id = int(card_split[0].replace("Card", "").strip())
    values_split = card_split[1].split("|")
    winnings = cleanup(values_split[0])
    havings = cleanup(values_split[1])
    print(f"Card {card_id}: {winnings} | {havings}")

    points = 0
    for number in havings:
        if number in winnings:
            if points == 0:
                points = 1
            else:
                points *= 2
    sum += points

print(sum)
