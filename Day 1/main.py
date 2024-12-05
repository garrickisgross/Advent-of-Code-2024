
with open("Day 1/input.txt",'r') as file:
    data = file.read().splitlines()
    file.close()

#Part 1
arr1 = []
arr2 = []
for each in data:
    temp = each.split()
    arr1.append(int(temp[0]))
    arr2.append(int(temp[1]))

arr1.sort()
arr2.sort()
total = 0
for i in range(len(arr1)):
    distance = abs(arr1[i] - arr2[i])
    total += distance

print(total)

#Part 2
total = 0
for each in arr1:
    similarity = 0
    for item in arr2:
        if each == item:
            similarity += 1
    total += similarity * each

print(total)