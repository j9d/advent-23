with open("input.txt", "r") as f:
    lines = f.readlines()
    time = int("".join(lines[0].split()[1:]))
    record = int("".join(lines[1].split()[1:]))

win_scenarios = time
for holding_time in range(0, int(time / 2)):
    distance = holding_time * (time - holding_time)
    if distance > record:
        break
    win_scenarios -= 1
for holding_time in reversed(range(int(time / 2), time)):
    distance = holding_time * (time - holding_time)
    if distance > record:
        break
    win_scenarios -= 1

print(win_scenarios)
