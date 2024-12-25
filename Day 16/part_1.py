import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star_with_turn_penalty(start, goal, grid):
    def get_neighbors(node):
        neighbors = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x2, y2 = node[0] + dx, node[1] + dy
            if 0 <= x2 < len(grid) and 0 <= y2 < len(grid[0]) and grid[x2][y2] == 0:
                neighbors.append((x2, y2))
        return neighbors

    open_set = []
    heapq.heappush(open_set, (0, start, None))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_set:
        _, current, previous = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return (path[::-1], g_score)

        for neighbor in get_neighbors(current):
            tentative_g_score = g_score[current] + 1
            if previous and (current[0] - previous[0], current[1] - previous[1]) != (neighbor[0] - current[0], neighbor[1] - current[1]):
                tentative_g_score += 1000  # Penalty for turns

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor, current))

    return None

with open("Day 16/input.txt", "r") as file:
    grid = file.read().split("\n")

# Example usage:
start = None
goal = None

for row in grid:
    for col in row:
        if col == "S":
            start = (grid.index(row), row.index(col))
        elif col == "E":
            goal = (grid.index(row), row.index(col))

grid = [[1 if cell == "#" else 0 for cell in row] for row in grid]

solve = a_star_with_turn_penalty(start, goal, grid)

path, g_score = solve

print(g_score[goal])  # Output: 10






