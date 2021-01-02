#!/usr/bin/env python3

import math
import sys

with open(sys.argv[1], "r") as f:
    map_ = list(map(str.strip, f.readlines()))

w = len(map_[0])

def count_trees(dx, dy):
    x, trees = 0, 0
    for y in range(0, len(map_), dy):
        if map_[y][x] == "#":
            trees += 1
        x = (x + dx) % w
    return trees

print(f"Part 1: {count_trees(3,1)}")

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
part2 = math.prod([count_trees(dx, dy) for dx, dy in slopes])
print(f"Part 2: {part2}")
