import vector # type: ignore

with open("Day 14/input.txt", "r") as file:
    data = file.read().splitlines()

data = [d.split(" ") for d in data]
data = [[i.split("=") for i in d] for d in data]
data = [[d[0][1], d[1][1]] for d in data]
data = [[d[0].split(","), d[1].split(",")] for d in data]
data = [[(int(d[0][0]), int(d[0][1])), (int(d[1][0]), int(d[1][1]))] for d in data]



class Robot:
    def __init__(self, pos: tuple[int, int], vel: tuple[int, int]):
        self.pos = vector.obj(x=pos[1], y=pos[0])
        self.vel = vector.obj(x=vel[1], y=vel[0])

    def move(self, times: int):
        self.pos += self.vel * times

class Grid:
    robots: list[Robot]
    grid: list[list]
    grid_size: tuple[int, int]
    middle_row: int
    middle_col: int
    seconds: int

    def __init__(self, robots: list[Robot], grid_size: tuple[int, int], seconds: int):
        self.robots = robots
        self.grid_size = grid_size
        self.seconds = seconds
        self.update_robot_locations()
        self.middle_row = grid_size[0] // 2
        self.middle_col = grid_size[1] // 2
        
        


    def update_grid(self):
        visited = dict()
        self.grid = [[0 for _ in range(self.grid_size[1])] for _ in range(self.grid_size[0])]
        for r in self.robots:
            
            if (r.pos.x, r.pos.y) not in visited:
                visited[(r.pos.x, r.pos.y)] = 0

            visited[(r.pos.x, r.pos.y)] += 1
            
            self.grid[r.pos.x][r.pos.y] = visited[(r.pos.x, r.pos.y)]
        
    def update_robot_locations(self):
        for r in self.robots:           
            r.move(self.seconds)
            r.pos.x = r.pos.x % self.grid_size[0]
            r.pos.y = r.pos.y % self.grid_size[1]
        self.update_grid()

    def print_grid(self):
        for row in self.grid:
            print(row)

    def solve(self):
        quad_1 = [row[:self.middle_col] for row in self.grid[:self.middle_row]]
        quad_2 = [row[self.middle_col + 1:] for row in self.grid[:self.middle_row]]
        quad_3 = [row[:self.middle_col] for row in self.grid[self.middle_row + 1:]]
        quad_4 = [row[self.middle_col + 1:] for row in self.grid[self.middle_row + 1:]]

        r_1 = sum([sum(row) for row in quad_1])
        r_2 = sum([sum(row) for row in quad_2])
        r_3 = sum([sum(row) for row in quad_3])
        r_4 = sum([sum(row) for row in quad_4])
            

        # for row in quad_1:
        #     print(row)
        # print()
        # for row in quad_2:
        #     print(row)
        # print()
        # for row in quad_3:
        #     print(row) 
        # print() 
        # for row in quad_4:
        #     print(row)
        
        return r_1 * r_2 * r_3 * r_4


grid_size = (103, 101)
robots = []

for d in data:
    robots.append(Robot(pos=d[0], vel=d[1]))

seconds = 100
grid = Grid(robots=robots, grid_size=grid_size, seconds=seconds)




print(grid.solve())


