from typing import Dict

sequence = [
    "soil",
    "fertilizer",
    "water",
    "light",
    "temperature",
    "humidity",
    "location",
]
seeds = []
destinations = {}
maps = {
    "soil": [],
    "fertilizer": [],
    "water": [],
    "light": [],
    "temperature": [],
    "humidity": [],
    "location": [],
}

def create_map(source: int, dest: int, range: int) -> Dict[str, int]:
    return {
        "source": source,
        "dest": dest,
        "range": range,
    }

def process_seed(seed: int) -> int:
    for mode in sequence:
        for map in maps[mode]:
            diff = map["dest"] - map["source"]
            if seed >= map["source"] and seed <= map["source"] + map["range"]:
                seed += diff
                break
    return seed

with open("input.txt", "r") as f:
    mode = "soil"
    for idx, line in enumerate(f):
        if idx == 0:
            seeds = [int(s) for s in line.split()[1:]]
            destinations = {s: -1 for s in seeds}
            continue
        data = line.split()
        if not data:
            continue
        if data[1] == "map:":
            # Change mode
            mode = data[0].split("-")[2]
            continue
        maps[mode].append(create_map(int(data[1]), int(data[0]), int(data[2])))
for seed in seeds:
    destinations[seed] = process_seed(seed)

print(min(destinations.values()))
