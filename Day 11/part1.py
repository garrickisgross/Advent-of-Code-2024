with open("Day 11/input.txt", "r") as file:
    data = file.read().strip().split()



# rule 1: if 0 flip to 1
# rule 2: if stone has an even number of digits, split it into two stones, The left half of the digits are engraved on the new left stone.
# rule 3: if none other apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
# for each blink, apply the rules to all stones in the current configuration. order is preserved

num_blinks = 0
times = 75

while num_blinks < times:
    to_insert = []
    for i in range(len(data)):
        
        if data[i] == "0":
            data[i] = "1"
        
        elif len(data[i]) % 2 == 0:
            cp = data[i]
            data[i] = str(int(cp[len(cp)//2:]))
            to_insert.append((i, cp[:len(cp)//2]))
        
        else:
            data[i] = str(int(data[i]) * 2024)
    
    for i in to_insert:
        data.insert(i[0], i[1])

    
    num_blinks += 1

print(len(data))