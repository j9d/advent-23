from typing import Dict, List

sequence = [
    "soil",
    "fertilizer",
    "water",
    "light",
    "temperature",
    "humidity",
    "location",
]
seeds: List[int] = []
closest = 999_999_999_999
maps: Dict[str, List[Dict[str, int]]] = {
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
    # Process seed numbers into destinations
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
            # Import seeds from the first line
            seeds = [int(s) for s in line.split()[1:]]
            continue
        data = line.split()
        # Ignore empty lines
        if not data:
            continue
        if data[1] == "map:":
            # Change mode
            mode = data[0].split("-")[2]
            continue
        # Import maps from the current mode
        maps[mode].append(create_map(int(data[1]), int(data[0]), int(data[2])))

for seed in seeds:
    result = process_seed(seed)
    if result < closest:
        closest = result

print(closest)
