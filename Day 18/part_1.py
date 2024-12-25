import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_search(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] == 0:
                tentative_g_score = g_score[current] + 1

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None

with open("Day 18/input.txt", "r") as file:
    data = file.read().splitlines()

data =[(int(x), int(y)) for x, y in [line.split(",") for line in data]]
width = 70
height = 70
length = 1024

grid = [[0 for _ in range(width + 1)] for _ in range(height + 1)]

data = data[:length + 1]

for x, y in data:
    grid[y][x] = 1

path = a_star_search(grid, (0, 0), (width, height))

for row in grid:
    for col in row:
        if col == 0:
            print(".", end="")
        elif col == 1:
            print("#", end="")
        else:
            print("O", end="")
    print()

print()

for x, y in path:
    grid[x][y] = 2

for row in grid:
    for col in row:
        if col == 0:
            print(".", end="")
        elif col == 1:
            print("#", end="")
        else:
            print("O", end="")
    print()

print()

print(f"Shortest path: {len(path) - 1}")