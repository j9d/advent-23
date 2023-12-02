total = 0
nums = "123456789"
with open("input.txt", "r") as f:
    for line in f:
        for char in line:
            if char in nums:
                total += int(char) * 10
                break
        for char in line[::-1]:
            if char in nums:
                total += int(char)
                break

print(total)
