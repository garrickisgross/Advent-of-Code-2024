with open("Day 5/input.txt",'r') as file:
    data = file.read().splitlines()
    file.close()

rules = []
pages = []

for i in data:
    if "|" in i:
        temp = i.split("|")
        rules.append((int(temp[0]), int(temp[1])))
    else:
        temp = i.split(",")
        pages.append([int(j) for j in temp if j != ""])



def validate_rule(r: tuple[int, int], p: list[int]) -> bool:
    x, y = r
    if x in p and y not in p:
        return True
    elif x not in p and y in p:
        return True
    elif x in p and y in p:
        return p.index(x) < p.index(y)
    
def order_by_rules(r: list[tuple[int, int]], p: list[int]) -> list[int]:
    for r in r:
        x, y = r
        if x in p and y in p:
            if validate_rule(r, p):
                continue
            else: 
                p[p.index(x)] = y
                p[p.index(y)] = x
    return p
    
    

valid_stack = []
reordered = []

for page_stack in pages:
    flag = []
    for rule in rules:
        x, y = rule
        if x in page_stack and y in page_stack:
            if validate_rule(rule, page_stack):
                flag.append(True)
            else:
                flag.append(False)
                
    
    flag = all(flag)

    
    if flag:
        valid_stack.append(page_stack)

    else: 
        reordered.append(page_stack)

total = 0
for stack in valid_stack:
    if len(stack) > 1:
        index = len(stack) // 2
    
        total += stack[index]

print(total)

total = 0
for stack in reordered:
    index = len(stack) // 2
    stack = order_by_rules(rules, stack)
    for rule in rules:
        if validate_rule(rule, stack):
            continue
        else:
            stack = order_by_rules(rules, stack)

    total += stack[index]

print(total)
    
            
