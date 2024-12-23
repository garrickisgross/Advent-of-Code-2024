# get sides method implemented from u/treyhest's solution. https://www.reddit.com/r/adventofcode/comments/1hcdnk0/2024_day_12_solutions/
with open('Day 12/input.txt') as f:
    data = [[x for x in y] for y in f.read().splitlines()]

class GardenRegion():
    members: list[(tuple[int, int], str)]
    
    def __init__(self, members: list[(tuple[int, int], str)]):
        self.members = members
        self.area = self.get_area()
        self.perimeter = self.get_perimeter()
        self.price = self.area * self.perimeter
        self.discounted_price = self.area * self.get_sides()

    def get_area(self):
        return len(self.members)
    
    def get_perimeter(self):
        perimeter = 0
        for member in self.members:
            x, y = member[0]
            if (x+1, y) not in [m[0] for m in self.members]:
                perimeter += 1
            if (x-1, y) not in [m[0] for m in self.members]:
                perimeter += 1
            if (x, y+1) not in [m[0] for m in self.members]:
                perimeter += 1
            if (x, y-1) not in [m[0] for m in self.members]:
                perimeter += 1
        return perimeter
    
    def get_sides(self):
        sides = 0
        region = [m[0] for m in self.members]
        edge_coord_corners = set()
        
        for x, y in region:
            for dx, dy in [(.5, .5), (.5, -.5), (-.5, .5), (-.5, -.5)]:
                edge_coord_corners.add((x + dx, y + dy))
        
        for x, y in edge_coord_corners:
            pattern = ""
            for dx, dy in [(.5, .5), (.5, -.5), (-.5, .5), (-.5, -.5)]: 
                pattern += "X" if (x+dx, y+dy) in region else "O"
            if pattern in ("OXXO", "XOOX"):
                # When an edge coord is two the region meets itself all catty-corner
                sides += 2
            elif pattern.count("X") == 3 or pattern.count("O") == 3:
                # For when an edge coord is an interior or exterior corner.
                sides += 1

        return sides


visited = set()

def get_region(x: int, y: int, value: str) -> list[tuple[int, int]]:
    if (x, y) in visited:
        return []
    if x < 0 or y < 0 or x >= len(data) or y >= len(data[0]):
        return []
    if data[x][y] != value:
        return []
    visited.add((x, y))
    return [(x, y)] + get_region(x+1, y, value) + get_region(x-1, y, value) + get_region(x, y+1, value) + get_region(x, y-1, value)
    
regions: list[GardenRegion] = []
for i in range(len(data)):
    for j in range(len(data[0])):
        region = get_region(i, j, data[i][j])
        region = [[(x, y), data[x][y]] for x, y in region]
        if region:
            regions.append(GardenRegion(region))

print(sum([r.discounted_price for r in regions]))
