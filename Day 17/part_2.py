with open("Day 17/input.txt") as file:
    data = file.read().splitlines()

data = [i.split() for i in data]
program = data[-1]
data = data[:3]
program = program[1].replace(",", "")
registers = {i[1][:-1]: int(i[2]) for i in data}

def get_combo(operand):
    if operand >= 0 and operand <= 3:
        return operand
    elif operand == 4:
        return registers["A"]
    elif operand == 5:
        return registers["B"]
    elif operand == 6:
        return registers["C"]
    elif operand == 7:
        return Exception("Invalid operand")

#Opcode 0
def adv(operand):
    numerator = registers["A"]
    denominatior = 2 ** get_combo(operand)
    registers["A"] = numerator // denominatior

# Opcode 1
def bxl(operand):
    registers["B"] = operand ^ registers["B"]

# Opcode 2
def bst(operand):
    registers["B"] = get_combo(operand) % 8

# Opcode 3
def jnz(operand):
    if registers["A"] != 0:
        return operand

# Opcode 4
def bxc(operand):
    registers["B"] = registers["B"] ^ registers["C"]

# Opcode 5
def out(operand):
    return get_combo(operand) % 8

# Opcode 6
def bdv(operand):
    numerator = registers["A"]
    denominatior = 2 ** get_combo(operand)
    registers["B"] = numerator // denominatior

# Opcode 7
def cdv(operand):

    numerator = registers["A"]
    denominatior = 2 ** get_combo(operand)
    registers["C"] = numerator // denominatior

def determine_func(opcode):
    if opcode == 0:
        return adv
    elif opcode == 1:
        return bxl
    elif opcode == 2:
        return bst
    elif opcode == 3:
        return jnz
    elif opcode == 4:
        return bxc
    elif opcode == 5:
        return out
    elif opcode == 6:
        return bdv
    elif opcode == 7:
        return cdv

def execute_program(program):
    instruction_pointer = 0
    halt = False
    res = []
    while not halt:
        opcode = int(program[instruction_pointer])
        operand = int(program[instruction_pointer + 1])
    
        func = determine_func(opcode)
        if func == jnz:
            instruction_pointer = func(operand)
            if instruction_pointer == None:
                halt = True
            continue
        
        if func == out:
            res.append(func(operand))

        func(operand)
        instruction_pointer += 2

        if instruction_pointer >= len(program) - 1:
            halt = True

        if len(res) > len(program):
            halt = True

    return "".join(map(str, res))

seed = 1029715

while execute_program(program) != program:
    registers["A"] = seed
    registers["B"] = 0
    registers["C"] = 0
    seed += 1


print(registers["A"])