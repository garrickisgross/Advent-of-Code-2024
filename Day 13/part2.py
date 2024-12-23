from math import sqrt

with open("Day 13/input.txt") as file:
    data = file.read().split("\n\n")

data = [r.split("\n") for r in data]

def parse_string(s):
    if "=" in s:
        s = s.split("=")
        s = s[1:]
        s = [s[0].split(",") , s[1].split(",")]
        s = (int(s[0][0]), int(s[1][0]))
    if "+" in s:
        s = s.split("+")
        s = s[1:]
        s = [s[0].split(",") , s[1].split(",")]
        s = (int(s[0][0]), int(s[1][0]))
        

    return s

def parse_data(data):
    map = {}
    for i in range(len(data)):
        for j in range(len(data[i]) -1, -1, -1):
            map[parse_string(data[i][j])] = {}
            map[parse_string(data[i][j])]["B"] = parse_string(data[i][j - 1])
            map[parse_string(data[i][j])]["A"] = parse_string(data[i][j - 2])
            break
    return map

data = parse_data(data)

class TwoDimVector:
    x: int
    y: int
    magnitude: int

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.magnitude = x + y
    
    
    def distance(self, other):
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def __add__(self, other):
        return TwoDimVector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return TwoDimVector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        if type(other) == int:
            return TwoDimVector(self.x * other, self.y * other)
        return TwoDimVector(self.x * other.x, self.y * other.y)
    
    def __repr__(self):
        return f"({self.x}, {self.y})"
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def __lt__(self, other):
        return self.magnitude < other.magnitude
    
    def __le__(self, other):
        return self.magnitude <= other.magnitude
    
    def __gt__(self, other):
        return self.magnitude > other.magnitude
    
    def __ge__(self, other):
        return self.magnitude >= other.magnitude
    
    def __ne__(self, other):
        return self.magnitude != other.magnitude
    
    def __floordiv__(self, other):
        return TwoDimVector(self.x // other.x, self.y // other.y)



class Machine:
    destination: TwoDimVector
    a_button: TwoDimVector
    b_button: TwoDimVector

    def __init__(self, destination, a_button, b_button):
        self.destination = destination
        self.a_button = a_button
        self.b_button = b_button
        self.start = TwoDimVector(0, 0)
        self.current = self.start

    def a_press(self):
        self.current = self.current + self.a_button
    
    def b_press(self):
        self.current = self.current + self.b_button
    
    def solve(self):
        result = 0
        
        a = self.a_button
        b = self.b_button
        p = self.destination
        af = (a.y/a.x)
        bf = (b.y/b.x)

        line_intersection_x = round((p.x * af - p.y) / (af - bf))
        
        b_factor = line_intersection_x // b.x
        remain_dist = p - b * b_factor
        
        a_factor = remain_dist.x // a.x
        if b * b_factor + a * a_factor == p:
            result += b_factor + a_factor * 3

        return result
            

machines = []
for key, value in data.items():
    destination = key
    a = None
    b = None
    for subkey, value in value.items():
        if subkey == "A":
            a = value
        if subkey == "B":
            b = value

    destination = TwoDimVector(destination[0], destination[1]) + TwoDimVector(10000000000000,10000000000000)
    a = TwoDimVector(a[0], a[1])
    b = TwoDimVector(b[0], b[1])
    machines.append(Machine(destination, a, b))

print(sum([m.solve() for m in machines if m.solve() != False]))

        


        
