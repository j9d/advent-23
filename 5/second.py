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
seeds = []
closest = 999_999_999_999
maps = {
    "soil": [],
    "fertilizer": [],
    "water": [],
    "light": [],
    "temperature": [],
    "humidity": [],
    "location": [],
}

def chunk_list(arr: List[int]) -> List[List[int]]:
    return [arr[i:i+2] for i in range(0, len(arr), 2)]

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
            seed_staging = chunk_list([int(s) for s in line.split()[1:]])
            print(seed_staging)
            for l in seed_staging:
                seeds.extend([i for i in range(l[0], l[0] + l[1])])
            continue
        data = line.split()
        if not data:
            continue
        if data[1] == "map:":
            # Change mode
            mode = data[0].split("-")[2]
            continue
        maps[mode].append(create_map(int(data[1]), int(data[0]), int(data[2])))
print(len(seeds))
for idx, seed in enumerate(seeds):
    if idx % 10_000_000 == 0:
        print(f'done {idx}')
    val = process_seed(seed)
    if val < closest:
        closest = val

print(closest)
