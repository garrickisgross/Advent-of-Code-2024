with open('Day 12/input.txt') as f:
    data = [[x for x in y] for y in f.read().splitlines()]

class GardenRegion():
    members: list[(tuple[int, int], str)]
    
    def __init__(self, members: list[(tuple[int, int], str)]):
        self.members = members
        self.area = self.get_area()
        self.perimeter = self.get_perimeter()
        self. price = self.area * self.perimeter
    
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

print(sum([r.price for r in regions]))
