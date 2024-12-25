import vector  # type: ignore
from functools import lru_cache

dir_map = {
    ">": (0, 1),
    "<": (0, -1),
    "^": (-1, 0),
    "v": (1, 0),
}

class Item:
    pos: vector.obj
    type: str
    is_movable: bool

    def __repr__(self):
        return self.type
    
    def push():
        pass

class Robot(Item):
    pos: vector.obj
    type = "@"

    def __init__(self, pos: tuple[int,int]):
        self.pos = vector.obj(x=pos[1], y=pos[0])

    def push(self, direction: str, grid: list[list[Item]]):
        
        move = vector.obj(x=dir_map[direction][0], y=dir_map[direction][1])

        if grid[self.pos.x + move.x][self.pos.y + move.y].is_movable:

            if grid[self.pos.x + move.x][self.pos.y + move.y].push(move, grid)[0]:
                self.pos += move
                return (True, tuple((self.pos.x, self.pos.y)))
            else:
                return (False, tuple((self.pos.x, self.pos.y)))
            
        else:
            return (False, tuple((self.pos.x, self.pos.y)))

class Box(Item):
    pos: vector.obj
    type = "O"
    is_movable = True

    def __init__(self, pos: tuple[int,int]):
        self.pos = vector.obj(x=pos[0], y=pos[1])

    def push(self, move: vector.obj, grid: list[list[Item]]):
        
        if grid[self.pos.x + move.x][self.pos.y + move.y].is_movable:
            if grid[self.pos.x + move.x][self.pos.y + move.y].push(move, grid)[0]:
                self.pos += move
                return (True, self.pos)
            else:
                return (False, self.pos)
        else:
            return (False, self.pos)

class Wall(Item):
    pos: vector.obj
    type = "#"
    is_movable = False

    def __init__(self, pos: tuple[int,int]):
        self.pos = vector.obj(x=pos[0], y=pos[1])

    def push(self, move: vector.obj, grid: list[list[Item]]):
        return (False, self.pos)
    
class Space(Item):
    pos: vector.obj
    type = "."
    is_movable = True

    def __init__(self, pos: tuple[int,int]):
        self.pos = vector.obj(x=pos[0], y=pos[1])

    def push(self, move: vector.obj, grid: list[list[Item]]):
        return (True, self.pos)
    
class Problem:
    grid: list[list[Item]]
    robot: Robot
    boxes: list[Box]
    moves: str

    def __init__(self, robot: Robot, walls: list[Wall], boxes: list[Box], moves: str, rows: int, cols: int):
        self.robot = robot
        self.walls = walls
        self.boxes = boxes
        self.moves = moves
        self.rows = rows
        self.cols = cols
        self.construct_grid()

    def print_grid(self):
        for row in self.grid:
            for col in row:
                print(col, end="")
            print()
    
    def construct_grid(self):
        grid = [[Space((i, j)) for j in range(self.cols)] for i in range(self.rows)]
        
        # Place walls first to avoid overwriting them
        for wall in self.walls:
            grid[wall.pos.x][wall.pos.y] = wall

        # Place boxes next
        for box in self.boxes:
            grid[box.pos.x][box.pos.y] = box

        # Place robot last
        grid[self.robot.pos.x][self.robot.pos.y] = self.robot

        self.grid = grid

    def solve(self):

        for move in self.moves:
            self.robot.push(move, self.grid)
            self.construct_grid()
           
        
        print("SUM GPS COORDINATES OF BOXES")
        print("---------------------------------")
        print(sum([box.pos.x * 100 + box.pos.y for box in self.boxes]))

data = open("Day 15/input.txt", "r").read().split("\n\n")
data[0] = data[0].split("\n")
moves = data[1].split("\n") 
moves = "".join(moves)
data = data[0]
robot: Robot  
walls = []
boxes = []

for row in range(len(data)):
    data[row] = list(data[row])
    for col in range(len(data[row])):
        if data[row][col] == "@":
            robot = Robot((row, col))
        if data[row][col] == "O":
            boxes.append(Box((row, col)))
        if data[row][col] == "#":
            walls.append(Wall((row, col)))

problem = Problem(robot, walls, boxes, moves, len(data), len(data[0]))

problem.solve()