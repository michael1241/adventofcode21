#! /usr/bin/env python3

import numpy as np
from scipy.stats import mode

with open('./day3in') as f:
    lines = list(map(list, f.read().splitlines()[:-1]))

gamma_array = mode(np.array(lines).astype(int)).mode[0]
gamma = ''.join(str(i) for i in gamma_array)
epsilon = ''.join(['0' if x == '1' else '1' for x in gamma])

print(int(gamma, 2) * int(epsilon, 2))
