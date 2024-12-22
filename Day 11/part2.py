# solve by reddit user u/Spinnenente - a clever solve that keeps track of a map of stones and their counts vs a list. 

import math
with open("Day 11/input.txt", "r") as file:
    line = [int(x) for x in file.read().strip().split()]



# rule 1: if 0 flip to 1
# rule 2: if stone has an even number of digits, split it into two stones, The left half of the digits are engraved on the new left stone.
# rule 3: if none other apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
# for each blink, apply the rules to all stones in the current configuration. order is preserved

def num_len(num): return int(math.log10(num)) + 1

def blink(n):
    if n == 0:
        return [1]
    elif num_len(n) % 2 == 0:
        p = 10 ** (num_len(n) / 2)
        return [int(n / p) , int(n % p)]
    else:
        return [n * 2024]

line_dict = dict((n, 1) for n in line)
for i in range(75):
    tmp = dict()
    for num, n in line_dict.items():
        for n_new in blink(num):
            if n_new in tmp:
                tmp[n_new] += n
            else:
                tmp[n_new] = n

    line_dict = tmp

result = sum(n for n in line_dict.values())
print("result " + str(result))
