from typing import Dict, Tuple

iterations = 0
found = False
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
curr = 'AAA'
while not found:
    for step in sequence:
        if curr == 'ZZZ':
            found = True
            break
        if step == 'L':
            curr = nodes[curr][0]
        if step == 'R':
            curr = nodes[curr][1]
        iterations += 1

print(iterations)
