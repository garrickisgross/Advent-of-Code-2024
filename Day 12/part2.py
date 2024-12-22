with open('Day 12/test_input.txt') as f:
    data = [[x for x in y] for y in f.read().splitlines()]


class GardenRegion():
    members: list[(tuple[int, int], str)]
    discount_price: int
    perimeter_points: set[tuple[int, int]]
    value: str
    
    
    def __init__(self, members: list[(tuple[int, int], str)]):
        self.members = members
        self.area = self.get_area()
        self.perimeter = self.get_perimeter()
        self.price = self.area * self.perimeter
        self.get_discount_price()
        self.discount_price = self.discount_price * self.area
        self.value = self.members[0][1]

    def get_area(self):
        return len(self.members)
    
    def get_perimeter(self)-> list[tuple[int, int]]:
        perimeter = 0
        perimeter_points = []
        for member in self.members:
            x, y = member[0]
            if (x+1, y) not in [m[0] for m in self.members]:
                perimeter += 1
                perimeter_points += [(x, y)]

            if (x-1, y) not in [m[0] for m in self.members]:
                perimeter += 1
                perimeter_points += [(x, y)]
  
            if (x, y+1) not in [m[0] for m in self.members]:
                perimeter += 1
                perimeter_points += [(x, y)]

            if (x, y-1) not in [m[0] for m in self.members]:
                perimeter += 1
                perimeter_points += [(x, y)]

        self.perimeter_points = perimeter_points
        return perimeter
    
    def get_discount_price(self):
        self.discount_price = 0
        for i in range(len(self.perimeter_points)):
            x, y = self.perimeter_points[i]
            x1, y1 = self.perimeter_points[(i+1)%len(self.perimeter_points)]
            if x == x1:
                for j in range(min(y, y1), max(y, y1)):
                    if (x, j) in [m[0] for m in self.members]:
                        self.discount_price += 1
            else:
                for j in range(min(x, x1), max(x, x1)):
                    if (j, y) in [m[0] for m in self.members]:
                        self.discount_price += 1
           
        return self.discount_price
        
                  
        
        
        
                



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

print(sum([r.discount_price for r in regions]))

                


    
