with open("Day 6/input.txt") as file:
    data = file.read().splitlines()
    file.close()


# Part 1 - Count the number of positions the guard visits in the map.
# Data is in a 2 dimensional grid, with each point being a coordinate.
# The guard follows the below rules for movement:
#     - If nothing is blocking the guard, it moves in the direction it is facing.
#     - If there is a wall blocking the guard, it turns right.
#     - the guard can start in any position and is represented by the characters [^, v, <, >]
# empty space is represented by a '.'
# walls are represented by '#'

class Puzzle:
    pos: tuple[int, int]
    path = []
    current_direction: int
    directions: list[str] = ["^", ">", "v", "<"]
    can_move = True
    grid: list[list[str]]
    count = 0
    space = "."
    wall = "#"
    visited = set()
    start_direction: int

    def __init__(self, pos, current_direction, grid):
        self.pos = pos
        self.initial_pos = pos
        self.current_direction = current_direction
        self.start_direction = current_direction
        self.grid = grid
        self.copy = self.grid.copy()
        self.initial = self.grid.copy()

    def solve(self) -> int | str:
        iteration_limit = 10000
        iteration_count = 0
        while self.can_move:
            self.visit()
            self.move()
            iteration_count += 1
            if iteration_count > iteration_limit:
                return "Loop"
        return len(self.visited)
    
    def reset(self) -> None:
        self.grid = self.initial.copy()
        self.copy = self.grid.copy()
        self.pos = self.initial_pos
        self.current_direction = self.start_direction
        self.path = []
        self.visited = set()
        self.can_move = True

    def solve_2(self) -> int:
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                self.reset()
                switch = list(self.grid[row])
                switch[col] = self.wall
                self.grid[row] = "".join(switch)
                if self.solve() == "Loop":
                    self.count += 1
        return self.count


    def move(self) -> None:
        x, y = self.pos
        self.path.append(self.pos)
        if self.current_direction == 0:
            if x > 0 and self.grid[x -1][y] != self.wall:
                self.pos = (x - 1, y)
            elif x > 0 and self.grid[x - 1][y] == self.wall:
                self.turn()
            else:
                self.can_move = False

        elif self.current_direction == 1:
            if y < len(self.grid[x]) - 1 and self.grid[x][y + 1] != self.wall:
                self.pos = (x, y + 1)
            elif y < len(self.grid[x]) - 1 and self.grid[x][y + 1] == self.wall:
                self.turn()
            else:
                self.can_move = False

        elif self.current_direction == 2:
            if x < len(self.grid) - 1 and self.grid[x + 1][y] != self.wall:
                self.pos = (x + 1, y)
            elif x < len(self.grid) - 1 and self.grid[x + 1][y] == self.wall:
                self.turn()
            else:
                self.can_move = False

        elif self.current_direction == 3:
            if y > 0 and self.grid[x][y - 1] != self.wall:
                self.pos = (x, y - 1)
            elif y > 0 and self.grid[x][y - 1] == self.wall:
                self.turn()
            else:
                self.can_move = False

    def turn(self) -> None:
        self.current_direction = (self.current_direction + 1) % 4

    def visit(self) -> None:
        if self.pos not in self.visited:
            self.visited.add(self.pos)

initial_pos: tuple[int, int]
for row in range(len(data)):
    flag = False
    if flag:
        break
    for col in range(len(data[row])):
        if (data[row][col] in Puzzle.directions):
            flag = True
            initial_pos = (row, col)
            puzzle = Puzzle((row, col), Puzzle.directions.index(data[row][col]), data)
            print(puzzle.solve())
            print(puzzle.solve_2())
            break



