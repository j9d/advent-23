total = 0

with open("input.txt", "r") as f:
    for line in f:
        colours = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        game_id = int(line[line.find(" ") + 1:line.find(":")])
        game_info = line[line.find(":") + 1:]
        rolls = game_info.split("; ")
        for roll in rolls:
            dice = roll.split(", ")
            for die in dice:
                num, colour = die.strip().split(" ")
                colours[colour] = max(colours[colour], int(num))
        for colour in colours.keys():
            if colours[colour] == 0:
                colours[colour] = 1
        total += colours["red"] * colours["green"] * colours["blue"]

print(total)
