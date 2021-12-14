#! /usr/bin/env python3

from more_itertools import pairwise, interleave_longest
from collections import Counter

with open('day14in') as f:
    data = f.read().splitlines()

polymer, rules = data[0], data[2:]
rules = {a: b for a, b in [rule.split(' -> ') for rule in rules]}


def one(polymer, rules):
    for n in range(10):
        newitems = [rules[a + b] for a, b in pairwise(polymer)]
        polymer = list(interleave_longest(polymer, newitems))

    res = Counter(polymer).values()
    return max(res) - min(res)


print(one(polymer, rules))
