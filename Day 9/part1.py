with open("Day 9/input.txt") as file:
    data = file.read()

storage = []
count = 0
for i in range(len(data)):
    if i == 0:
        for j in range(int(data[i])):
            storage.append(count)
        count += 1  
    elif i % 2 == 0 and i != 0:
        for j in range(int(data[i]) ):
            storage.append(count)
        count += 1
    else:
        for j in range(int(data[i])):
            storage.append(".")

def find_first_empty(string: str) -> int:
    return string.index(".")

def find_last_digit(string):
    for i in range(len(string) - 1, -1, -1):
        if string[i] != ".":
            return i
    

def swap(string, start, end):
    string[start], string[end] = string[end], string[start]
    return string

done = False
while not done:
   start = find_first_empty(storage)
   end = find_last_digit(storage)
   if start > end:
       done = True
   else:
         storage = swap(storage, start, end)

def compute_checksum(string):
    count = 0
    for i in range(len(string)):
        if string[i] != ".":
            count += i * string[i]
        if string[i] == ".":
            break
    return count

print(compute_checksum(storage))
        

