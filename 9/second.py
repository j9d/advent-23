from typing import List

sequences: List[List[str]] = []
with open("input.txt", "r") as f:
    for line in f:
        sequences.append([int(i) for i in line.split()][::-1])

def predict_sequence(sequence: List[int]) -> int:
    differences: List[int] = []
    for i in range(len(sequence) - 1):
        differences.append(sequence[i+1] - sequence[i])
    if all(x == differences[0] for x in differences):
        return differences[0]
    return differences[-1] + predict_sequence(differences)

total = 0
for sequence in sequences:
    next = predict_sequence(sequence)
    total += sequence[-1] + next

print(total)
