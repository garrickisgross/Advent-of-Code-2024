from itertools import product, permutations

with open("Day 7/input.txt") as file:
    data = file.read().splitlines()
    file.close()


for i in range(len(data)):
    data[i]  = data[i].split(":")
    for j in range(len(data[i])):
        data[i][j] = data[i][j].split(" ")


mapping = {}

for i in range(len(data)):
    mapping[data[i][0][0]] = [i for i in data[i][1] if i != ""]

def test(combos, nums):
    ans = int(nums[0])
    for i in range(1,len(nums)):
        if combos[i-1] == "+":
            ans += int(nums[i])
        elif combos[i-1] == "|":
            ans = int(f"{ans}{nums[i]}")
        else:
            ans *= int(nums[i])
    return ans
        

total = 0
for key, value in mapping.items():
    for i in product("+*|", repeat=len(value)-1):
        if test(i, value) == int(key):
            total += int(key)
            break

print(total)