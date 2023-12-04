from typing import Dict, List

cards: List[str] = []
processed_cards: Dict[int, List[int | List[int]]] = {}

def count_matches(winning: List[int], current_game: List[int]) -> int:
    return len([num for num in current_game if num in winning])

with open("input.txt", "r") as f:
    for line in f:
        cards.append(line.strip())
for card in cards:
    # Process cards into the following structure:
    # {
    #   game_id: [
    #       copies,
    #       [winning numbers],
    #       [current numbers],
    #   ],
    # }
    header, games = [part.strip() for part in card.split(":")]
    game_id = int(header[5:8].strip())
    winning_str, game_str = [nums.strip() for nums in games.split("|")]
    winning = [int(item) for item in winning_str.split()]
    game = [int(item) for item in game_str.split()]
    processed_cards[game_id] = [1, winning, game]
for game_id in sorted(processed_cards.keys()):
    # `matches` == how many games in the future should be incremented.
    # `copies` == copies of the current card/game.
    # Increment future games' copies by `copies`, up to `matches` future games.
    copies, winning, current_game = processed_cards[game_id]
    matches = count_matches(winning, current_game)
    # I'm glad that `range()` behaves like this but it looks so ugly
    for future_game_id in range(game_id + 1, game_id + 1 + matches):
        processed_cards[future_game_id][0] += copies

print(sum([processed_cards[game_id][0] for game_id in processed_cards.keys()]))
