#! /usr/bin/env python3

from collections import defaultdict

with open('./day12in') as f:
    lines = [l.split('-') for l in f.read().splitlines()]

graph = defaultdict(set)
for line in lines:
    a, b = line
    graph[a].add(b)
    graph[b].add(a)


def isRepeatable(letter):
    return letter.lower() != letter


def findPaths(g, s, e, path=None):
    path = [] if path == None else path
    path = path + [s]
    if s == e:
        return path
    paths = []
    for vert in g[s]:
        if vert not in path or isRepeatable(vert):
            new_paths = findPaths(g, vert, e, path)
            for p in new_paths:
                paths.append(p)
    return paths


result = (findPaths(graph, 'start', 'end'))

# print(result)
print(sum([1 for v in result if v == 'start']))
