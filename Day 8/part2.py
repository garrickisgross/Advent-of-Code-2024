from itertools import combinations

with open("Day 8/input.txt") as file:
    data = file.read().splitlines()

map = {}
data = [list(i) for i in data]    

for row in range(len(data)):
    for col in range(len(data[row])):
        if data[row][col] != ".":
            if data[row][col] not in map:
                map[data[row][col]] = [(row, col)]
            else:
                map[data[row][col]].append((row, col))

def identify_antinodes(p1: tuple, p2: tuple) -> list:
    x1, y1 = p1
    x2, y2 = p2
    antinodes = []
    dx = x2 - x1
    dy = y2 - y1

    while in_bounds((x1, y1)):
        x1 += dx
        y1 += dy
        antinodes.append((x1, y1))

    while in_bounds((x2, y2)):
        x2 -= dx
        y2 -= dy
        antinodes.append((x2, y2))

    return antinodes

def in_bounds(p: tuple) -> bool:
    x, y = p
    return 0 <= x < len(data) and 0 <= y < len(data[0])

antinodes = set()
for _, value in map.items():
    for i, j in combinations(value, r=2):
        for antinode in identify_antinodes(i, j):
            if in_bounds(antinode):
                antinodes.add(antinode)


print(len(antinodes))






