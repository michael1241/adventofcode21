#! /usr/bin/env python3

import numpy as np

with open('./day2in') as f:
    lines = f.read().split("\n")[:-1]


def splitter(inst):
    a, b = inst.split(' ')
    return (a, int(b))


instructions = map(splitter, lines)

moves = {'up': np.array([0, -1]), 'down': np.array([0, 1]), 'forward': np.array([1, 0])}

location = np.array([0, 0])

for direction, magnitude in instructions:
    movement = moves[direction] * magnitude
    location += movement

print(location.prod())
