with open("Day 9/input.txt") as file:
    data = file.read().strip()

size = [0] * len(data)
loc = [0] * len(data)

def make_file(data):
    global size, loc

    blocks = []
    is_file = True
    id = 0
    for x in data:
        x = int(x)
        if is_file:
            loc[id] = len(blocks)
            size[id] = x
            blocks += [id] * x
            id += 1
            is_file = False
        else:
            blocks += [None] * x
            is_file = True
    return blocks

filesystem = make_file(data)

def move(filesystem):
    to_move = 0
    while size[to_move] > 0:
        to_move += 1
    to_move -= 1
    
    while to_move >= 0:
        free_space = 0
        first_free = 0
        while filesystem[first_free] is not None:
            first_free += 1
        while filesystem[first_free + free_space] is None:
            free_space += 1

        while first_free < loc[to_move] and free_space < size[to_move]:
            first_free = first_free + free_space
            free_space = 0
            while filesystem[first_free] is not None:
                first_free += 1
            while first_free + free_space < len(filesystem) and filesystem[first_free + free_space] is None:
                free_space += 1

        if first_free >= loc[to_move]:
            to_move -= 1
            continue

        while to_move >= 0 and not size[to_move] <= free_space:
            to_move -= 1

        for idx in range(first_free, first_free + size[to_move]):
            filesystem[idx] = to_move
        for idx in range(loc[to_move], loc[to_move] + size[to_move]):
            filesystem[idx] = None
        
        to_move -= 1
        
    return filesystem

def checksum(filesystem):
    ans = 0
    for i, x in enumerate(filesystem):
        if x is not None:
            ans += i * x
    return ans

ans = checksum(move(filesystem))
print(ans)


        

