with open("Day 4/input.txt",'r') as file:
    d = file.read().splitlines()
    file.close()

# d = ["MMMSXXMASM","MSAMXMSMSA","AMXSXMAAMM","MSAMASMSMX","XMASAMXAMM","XXAMMXXAMA","SMSMSASXSS","SAXAMASAAA","MAMMMXMMMM","MXMXAXMASX"]

def check_up(r: int, c: int, d: list[list[str]]) -> bool:
    if r - 3 < 0: return False
    up = ""
    up += d[r][c]
    up += d[r-1][c]
    up += d[r-2][c]
    up += d[r-3][c]
    return up == "XMAS"

def check_down(r: int, c: int, d: list[list[str]]) -> bool:
    if r + 3 > len(d) - 1: return False
    down = ""
    down += d[r][c]
    down += d[r+1][c]
    down += d[r+2][c]
    down += d[r+3][c]
    return down == "XMAS"

def check_left(r: int, c: int, d: list[list[str]]) -> bool:
    if c < 3: return False
    left = ""
    left += d[r][c]
    left += d[r][c-1]
    left += d[r][c-2]
    left += d[r][c-3]
    return left == "XMAS"

def check_right(r: int, c: int, d: list[list[str]]) -> bool:
    if c + 3 > len(d[r]) - 1: return False
    right = ""
    right += d[r][c]
    right += d[r][c+1]
    right += d[r][c+2]
    right += d[r][c+3]
    return right == "XMAS"

def check_up_left(r: int, c: int, d: list[list[str]]) -> bool:
    if r < 3 or c < 3: return False
    up_left = ""
    up_left += d[r][c]
    up_left += d[r-1][c-1]
    up_left += d[r-2][c-2]
    up_left += d[r-3][c-3]
    return up_left == "XMAS"

def check_up_right(r: int, c: int, d: list[list[str]]) -> bool:
    if r < 3 or c + 3 > len(d[r]) - 1: return False
    up_right = ""
    up_right += d[r][c]
    up_right += d[r-1][c+1]
    up_right += d[r-2][c+2]
    up_right += d[r-3][c+3]
    return up_right == "XMAS"

def check_down_left(r: int, c: int, d: list[list[str]]) -> bool:
    if r + 3 > len(d) - 1 or c < 3: return False
    down_left = ""
    down_left += d[r][c]
    down_left += d[r+1][c-1]
    down_left += d[r+2][c-2]
    down_left += d[r+3][c-3]
    return down_left == "XMAS"

def check_down_right(r: int, c: int, d: list[list[str]]) -> bool:
    if r + 3 > len(d) - 1 or c + 3 > len(d[r]) - 1: return False
    down_right = ""
    down_right += d[r][c]
    down_right += d[r+1][c+1]
    down_right += d[r+2][c+2]
    down_right += d[r+3][c+3]
    return down_right == "XMAS"

def check_directions(r: int, c: int, d: list[list[str]]) -> int:
    count = 0
    if check_up(r, c, d): count += 1
    if check_down(r, c, d): count += 1
    if check_left(r, c, d): count += 1
    if check_right(r, c, d): count += 1
    if check_up_left(r, c, d): count += 1
    if check_up_right(r, c, d): count += 1
    if check_down_left(r, c, d): count += 1
    if check_down_right(r, c, d): count += 1
    return count

# Part 2
def right(r: int, c: int, d: list[list[str]]) -> bool:
    str = ""
    if r - 1 < 0 or c - 1 < 0 or c + 1 > len(d[r]) - 1 or r + 1 > len(d) - 1: return False
    str += d[r - 1][c + 1]
    str += d[r][c]
    str += d[r + 1][c - 1]
    return str == "MAS" or str == "SAM"

def left(r: int, c: int, d: list[list[str]]) -> bool:
    str = ""
    if r - 1 < 0 or c - 1 < 0 or c + 1 > len(d[r]) - 1 or r + 1 > len(d) - 1: return False
    str += d[r - 1][c - 1]
    str += d[r][c]
    str += d[r + 1][c + 1]
    return str == "MAS" or str == "SAM"



def check_directions_2(r: int, c: int, d: list[list[str]]) -> int:
    count = 0
    if right(r, c, d) and left(r, c, d): count += 1
    return count

count = 0
count_2 = 0
for row in range(len(d)):
    for col in range(len(d[row])):
            count += check_directions(row, col, d)
            if d[row][col] == "A":
                count_2 += check_directions_2(row, col, d)

print(count)
print(count_2)

