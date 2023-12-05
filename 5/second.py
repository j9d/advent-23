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
maps = {
    "soil": [],
    "fertilizer": [],
    "water": [],
    "light": [],
    "temperature": [],
    "humidity": [],
    "location": [],
}

def valid_seed(seed: int) -> bool:
    for s in seeds:
        if seed >= s[0] and seed < s[0] + s[1]:
            return True
    return False

def chunk_list(arr: List[int]) -> List[List[int]]:
    # Chunk a list to group adjacent pairs.
    # e.g. [1, 2, 3, 4, 5, 6] becomes [[1, 2], [3, 4], [5, 6]]
    return [arr[i:i+2] for i in range(0, len(arr), 2)]

def create_map(source: int, dest: int, range: int) -> Dict[str, int]:
    return {
        "source": source,
        "dest": dest,
        "range": range,
    }

def process_reverse(seed: int) -> int:
    # Process destination numbers back into seeds
    for mode in sequence[::-1]:
        for map in maps[mode]:
            diff = map["source"] - map["dest"]
            if seed >= map["dest"] and seed < map["dest"] + map["range"]:
                seed += diff
                break
    return seed

with open("input.txt", "r") as f:
    mode = "soil"
    for idx, line in enumerate(f):
        if idx == 0:
            # Import seeds from the first line
            seeds = chunk_list([int(s) for s in line.split()[1:]])
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

# Start from the lowest destination number (probably 0).
# Process destination numbers in reverse to find a seed.
# If a seed is valid, print it and done.
destinations = [map["dest"] for map in maps["location"]]
start = min(destinations)
stop = max(destinations)
for seed in range(start, stop):
    res = process_reverse(seed)
    if valid_seed(res):
        print(seed)
        break
