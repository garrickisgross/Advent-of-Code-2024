# Solve by u/zniperr on reddit https://www.reddit.com/r/adventofcode/comments/1hhlb8g/2024_day_19_solutions/
# I really like this solution, it's very clean and easy to understand. I'm going to use it as a reference for future problems.

from functools import cache
import sys

with open("Day 19/input.txt") as file:
    towels = tuple(file.readline().rstrip().split(', '))
    designs = file.read().strip().split("\n")

@cache
def possible(design, towels):
    if not design:
        return 1
    return sum(possible(design[len(towel):], towels)
               for towel in towels if design.startswith(towel))         


pos = [possible(design, towels) for design in designs]
print(sum(map(bool, pos)))
print(sum(pos))
