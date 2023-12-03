import re
from typing import List

total = 0
non_symbols = "0123456789."
engine: List[str] = []
numbers: List[List[tuple]] = []

def look_around(row: int, col: int) -> int:
    found_numbers = []
    for searchrow in range(row - 1, row + 2):
        # Handle border rows
        if searchrow < 0 or searchrow >= len(engine):
            continue
        for searchcol in range(col - 1, col + 2):
            if searchcol < 0 or searchcol >= len(line):
                continue
            # For each square surrounding the gear:
            # - If it's part of a number, mark the number as found (add it to the list).
            # - Ignore if the number is already in the list.
            # This will break if a gear happens to be surrounded by two identical numbers.
            # Luckily, my puzzle input is merciful.
            for num in numbers[searchrow]:
                if num[0] not in found_numbers and searchcol >= num[1] and searchcol <= num[2]:
                    found_numbers.append(num[0])
    if len(found_numbers) == 2:
        return found_numbers[0] * found_numbers[1]
    return 0

with open("input.txt") as f:
    # Load the engine into memory
    for line in f:
        # REMEMBER TO TRIM YOUR STRINGS!
        engine.append(line.strip())
for row, line in enumerate(engine):
    # Build a list of matches (numbers) and where they are
    numbers.append([])
    for match in re.finditer(r"\w+", line):
        span = match.span()
        numbers[row].append((int(match[0]), span[0], span[1] - 1))
for row, line in enumerate(engine):
    # Find each gear (*).
    # Look around it to find any numbers.
    # If there are two, multiply and add to the total.
    for col, char in enumerate(line):
        if char == "*":
            total += look_around(row, col)

print(total)
