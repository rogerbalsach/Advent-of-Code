#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 08:50:54 2024

@author: Roger Balsach
"""
from collections import defaultdict
from itertools import combinations

with open("input.txt") as file:
    content = file.read().strip()

positions: dict[str, set[complex]] = defaultdict(set)
lines = content.splitlines()
N = len(lines)
M = len(lines[0])

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == '.':
            continue
        positions[char].add(i + j*1j)


def get_antinodes(resonance: bool = False) -> set[complex]:
    antinodes: set[complex] = set()
    for freq, pos in positions.items():
        for x, y in combinations(pos, 2):
            if resonance:
                antinodes |= {x, y}
            diff = y - x
            loop = 3
            while loop > 0:
                y += diff
                x -= diff
                if loop & 1 and (0 <= x.real < N and 0 <= x.imag < M):
                    antinodes.add(x)
                else:
                    loop &= 2
                if loop & 2 and (0 <= y.real < N and 0 <= y.imag < M):
                    antinodes.add(y)
                else:
                    loop &= 1
                if not resonance:
                    break
    return antinodes


def main() -> None:
    antinodes = get_antinodes(resonance=False)
    print(len(antinodes))
    antinodes = get_antinodes(resonance=True)
    print(len(antinodes))


if __name__ == '__main__':
    main()
