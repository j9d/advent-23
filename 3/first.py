import re
from typing import List

total = 0
non_symbols = "0123456789."
engine: List[str] = []

def process_match(match: re.Match) -> int:
    cols = match.span()
    for searchrow in range(row - 1, row + 2):
        # Handle border rows
        if searchrow < 0 or searchrow >= len(engine):
            continue
        for searchcol in range(cols[0] - 1, cols[1] + 1):
            if searchcol < 0 or searchcol >= len(line):
                continue
            if engine[searchrow][searchcol] not in non_symbols:
                return int(match[0])
    return 0

with open("input.txt") as f:
    # Load the engine into memory
    for line in f:
        # REMEMBER TO TRIM YOUR STRINGS!
        engine.append(line.strip())
for row, line in enumerate(engine):
    # Find the numbers in each line.
    # Look in the surrounding squares for a symbol.
    # If found, add to the total, otherwise ignore.
    for match in re.finditer(r"\w+", line):
        total += process_match(match)

print(total)
