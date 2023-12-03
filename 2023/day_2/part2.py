sum = 0
with open("input.txt") as f:
    games = [line.strip() for line in f.readlines()]
    for game in games:
        game_split = game.split(":")
        game_id = int(game_split[0].replace("Game", ""))
        draws = game_split[1].split(";")
        max_red, max_green, max_blue = 0, 0, 0
        for draw in draws:
            counts_and_colors = draw.split(",")
            for count_and_color in counts_and_colors:
                count_and_color_split = count_and_color.strip().split(" ")
                count = int(count_and_color_split[0])
                color = count_and_color_split[1]
                if color == "red":
                    max_red = max(max_red, count)
                if color == "green":
                    max_green = max(max_green, count)
                if color == "blue":
                    max_blue = max(max_blue, count)
        print(f"Game {game_id}: " f"{max_red} red, {max_green} green, {max_blue} blue")
        power = max_red * max_green * max_blue
        sum += power

print(sum)
