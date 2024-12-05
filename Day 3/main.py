with open("Day 3/input.txt",'r') as file:
    data = file.read()
    file.close()

# data = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

tokens = []
temp_string = ""
do_or_dont = "do"
for i in range(len(data)):
    
    if data[i:i+7] == "don't()":
        do_or_dont = "dont"
    
    if data[i:i+4] == "do()":
        do_or_dont = "do"

    if do_or_dont == "do":
        
        if data[i:i+4] == "mul(":
            j = i + 4
            
            while data[j] != ')':
                temp_string += data[j]
                j += 1
            
            try:
                
                if do_or_dont == "do":
                    print(temp_string)
                    x, y = map(int, temp_string.split(','))
                    tokens.append((x, y))
                    temp_string = ""
            
            except ValueError:
                temp_string = ""
                continue

total = 0
for x, y in tokens:
    total += x * y

print(total)
