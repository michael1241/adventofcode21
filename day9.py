#! /usr/bin/env python3

import numpy as np

with open('./day9in') as f:
    data = np.genfromtxt(f, delimiter=1)

mins = []
points = np.nditer(data, flags=['multi_index'])
for point in points:
    p = points.multi_index
    m = (data[max(p[0] - 1, 0): min(p[0] + 2, 100), max(p[1] - 1, 0): min(p[1] + 2, 100)]).min()
    if m < point:
        continue
    mins.append(point + 1)
print(sum(mins))
