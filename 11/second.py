from typing import List

grid: List[List[str]] = []
galaxies: List[List[int]] = []
total = 0
with open("input.txt", "r") as f:
    for line in f:
        grid.append([i for i in line.strip()])

# Populate galaxies
for i, row in enumerate(grid):
    for j, col in enumerate(row):
        if col == "#":
            galaxies.append([i, j])

# Expand vertically
for row in range(len(grid) - 1, -1, -1):
    if all([x == "." for x in grid[row]]):
        for g in range(len(galaxies)):
            if galaxies[g][0] > row:
                galaxies[g][0] += 999_999

# Expand horizontally
for col in range(len(grid[0]) - 1, -1, -1):
    column = []
    for row in range(len(grid)):
        column.append(grid[row][col])
    if all([x == "." for x in column]):
        for g in range(len(galaxies)):
            if galaxies[g][1] > col:
                galaxies[g][1] += 999_999

# Calculate distances
for target in range(len(galaxies)):
    for to_compare in range(target + 1, len(galaxies)):
        total += abs(galaxies[target][0] - galaxies[to_compare][0])
        total += abs(galaxies[target][1] - galaxies[to_compare][1])

print(total)
