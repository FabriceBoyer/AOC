sum = 0
with open("input.txt") as f:
    games = [line.strip() for line in f.readlines()]

for game in games:
    game_split = game.split(":")
    game_id = int(game_split[0].replace("Game", ""))
    draws = game_split[1].split(";")
    possible = True
    for draw in draws:
        counts_and_colors = draw.split(",")
        for count_and_color in counts_and_colors:
            count_and_color_split = count_and_color.strip().split(" ")
            count = int(count_and_color_split[0])
            color = count_and_color_split[1]
            if color == "red" and count > 12:
                possible = False
                break
            if color == "green" and count > 13:
                possible = False
                break
            if color == "blue" and count > 14:
                possible = False
                break
    if possible:
        sum += game_id

print(sum)
