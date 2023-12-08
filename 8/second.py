from typing import Dict, List, Tuple
from math import lcm

sequence = ""
nodes: Dict[str, Tuple[str, str]] = {}
with open("input.txt", "r") as f:
    for idx, line in enumerate(f):
        if idx == 0:
            sequence = line.strip()
            continue
        if line:
            start = line.strip()[:3]
            left = line.strip()[7:10]
            right = line.strip()[12:15]
            nodes[start] = (left, right)

def search() -> List[int]:
    iterations = 0
    paths = [p for p in list(nodes.keys()) if p[2:3] == 'A']
    results = [0 for p in paths]
    while True:
        for step in sequence:
            if all(results):
                return results
            # Record how many steps it took for each path to
            # reach Z the first time.
            for idx in range(len(paths)):
                if paths[idx][2:3] == 'Z' and results[idx] == 0:
                    results[idx] = iterations
            if step == 'L':
                for idx in range(len(paths)):
                    paths[idx] = nodes[paths[idx]][0]
            if step == 'R':
                for idx in range(len(paths)):
                    paths[idx] = nodes[paths[idx]][1]
            iterations += 1

# Each path reaches Z at the same interval.
# Find the least common multiple of all the path lengths.
result = lcm(*search())
print(result)
