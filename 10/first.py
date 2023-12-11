from typing import List, Tuple

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
DIRECTIONS = [UP, RIGHT, DOWN, LEFT]

def to_tuple(direction: int) -> Tuple[int, int]:
    if direction == UP:
        return (-1, 0)
    if direction == RIGHT:
        return (0, 1)
    if direction == DOWN:
        return (1, 0)
    if direction == LEFT:
        return (0, -1)

def visit(direction_of_travel: int, row: int, col: int) -> Tuple[int, int]:
    try:
        char = maze[row][col]
    except IndexError:
        return False
    return char in valid_destinations[direction_of_travel]

valid_destinations = [
    ["|", "7", "F"],
    ["-", "J", "7"],
    ["|", "J", "L"],
    ["-", "L", "F"],
]
actions = {
    "|": [UP, DOWN],
    "-": [LEFT, RIGHT],
    "F": [RIGHT, DOWN],
    "7": [LEFT, DOWN],
    "L": [UP, RIGHT],
    "J": [UP, LEFT],
    "S": [UP, DOWN, LEFT, RIGHT]
}

maze: List[List[str]] = []
to_visit: List[Tuple[int, int]] = []
recorded = set()
with open("input.txt", "r") as f:
    for idx, line in enumerate(f):
        row = []
        for i in range(len(line.strip())):
            row.append(line[i])
            if line[i] == "S":
                start = (idx, i)
        maze.append(row)

to_visit.append(start)
recorded.add(start)
# Flood fill (ish)
while to_visit:
    curr = to_visit.pop()
    char = maze[curr[0]][curr[1]]
    for direction in actions[char]:
        travel = to_tuple(direction)
        new = (curr[0] + travel[0], curr[1] + travel[1])
        valid = visit(direction, *new)
        if valid and new not in recorded:
            to_visit.append(new)
            recorded.add(new)

# We've recorded all the unique nodes in the main path.
# One big circle. The furthest node is just halfway along it.
print(len(recorded) // 2)
