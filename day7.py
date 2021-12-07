#! /usr/bin/env python3

from statistics import median

crabs = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]

with open('./day7in') as f:
    crabs = [int(x) for x in f.read().split(',')]

med = median(crabs)  # used for part 1 instead of pos


def triangle(n):
    return int(n * (n + 1) / 2)


min_fuel = 100000000000  # large number

for pos in range(min(crabs), max(crabs) + 1):
    fuel = 0
    for crab in crabs:
        fuel += triangle(abs(crab - pos))
    min_fuel = min(min_fuel, fuel)

print(min_fuel)
