total = 1
races = []
with open("input.txt", "r") as f:
    lines = f.readlines()
    times = lines[0].split()[1:]
    records = lines[1].split()[1:]
    for i in range(len(times)):
        races.append([int(times[i]), int(records[i])])

for race in races:
    win_scenarios = 0
    for holding_time in range(1, race[0]):
        distance = holding_time * (race[0] - holding_time)
        if distance > race[1]:
            win_scenarios += 1
    total *= (win_scenarios if win_scenarios > 0 else 1)

print(total)
