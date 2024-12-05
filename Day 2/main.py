with open("Day 2\input.txt",'r') as file:
    data = file.read().splitlines()
    file.close()

working_data = []
for item in data:
    temp = item.split()
    working_data.append([int(i) for i in temp])

def is_increasing(i: list) -> bool:
    flag = []
    for j in range(len(i)-1):
        if i[j] > i[j+1]:
            flag.append(False)
    return all(flag)
        

def is_decreasing(i: list) -> bool:
    flag = []
    for j in range(len(i)-1):
        if i[j] < i[j+1]:
            flag.append(False)
    return all(flag)

def is_too_different(i: list) -> bool:
    for j in range(len(i)-1):
        if abs(i[j] - i[j+1]) > 3 or abs(i[j] - i[j+1]) < 1:
            return True
        
    return False

def safe(i: list) -> bool:
    return is_increasing(i) != is_decreasing(i) and not is_too_different(i)

def problem_dampener(i: list) -> bool:
    
    for j in range(len(i)):
        temp = i.copy()
        temp.pop(j)
        if safe(temp):
            return True
        
    return False

temp = [[7,6,4,2,1],[1,2,7,8,9],[9,7,6,2,1],[1,3,2,4,5],[8,6,4,4,1],[1,3,6,7,9]] 



total = 0
for i in working_data:
    if safe(i) or problem_dampener(i):
        total += 1
    

print(total)
