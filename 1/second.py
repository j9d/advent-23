total = 0
nums = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

def find_num(input: str, reverse: bool):
    if reverse:
        results = {term: input.rfind(term) for term in nums.keys()}
        return nums[max(results, key=results.get)]
    results = {term: input.find(term) for term in nums.keys() if input.find(term) >= 0}
    return nums[min(results, key=results.get)] * 10

with open("input.txt", "r") as f:
    for line in f:
        total += find_num(line, False)
        total += find_num(line, True)

print(total)
