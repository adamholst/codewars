#!/usr/bin/env python3

import sys

def line_valid(line, part=1):
    r, c, p = line.split(" ")
    c = c.rstrip(":")
    r_low, r_high = map(int, r.split("-"))
    if part==1:
        return r_low <= p.count(c) <= r_high
    return (p[r_low - 1] == c) ^ (p[r_high - 1] == c)

with open(sys.argv[1], "r") as f:
    lines = f.readlines()

num_valid1 = len([x for x in lines if line_valid(x)])
num_valid2 = len([x for x in lines if line_valid(x, part=2)])

print(f"Part 1: {num_valid1}")
print(f"Part 2: {num_valid2}")
