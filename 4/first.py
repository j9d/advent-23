from typing import List

total = 0
cards: List[str] = []

with open("input.txt", "r") as f:
    for line in f:
        cards.append(line.strip())
for card in cards:
    score = 0
    header, games = [part.strip() for part in card.split(":")]
    winning_str, game_str = [nums.strip() for nums in games.split("|")]
    winning = [int(item) for item in winning_str.split()]
    game = [int(item) for item in game_str.split()]
    for number in game:
        if number in winning:
            if score == 0:
                score += 1
            else:
                score *= 2
    total += score

print(total)
