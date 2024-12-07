#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 09:26:31 2024

@author: Roger Balsach
"""
from collections import defaultdict
from functools import cache

with open("input.txt") as file:
    content = file.read().strip()

# Define dictionaries to hold the position of obstacles
obstacles_h: dict[float, set[complex]] = defaultdict(set)
obstacles_v: dict[float, set[complex]] = defaultdict(set)
lines = content.splitlines()
N = len(lines)
M = len(lines[0])
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == '.':
            continue
        if char == '#':
            obstacles_h[i].add(j+i*1j)
            obstacles_v[j].add(j+i*1j)
        elif char == '^':
            start_pos = j+i*1j


@cache
def walk_until_obstacle(pos: complex, dtn: complex, obstacles: tuple[complex]
                        ) -> int:
    '''
    Find the next obstacle from the current position in the direction given.
    Return the number of seps required to get there.
    Raises ValueError if no obstacle is in front of the guard.
    '''
    return int(min(filter(
        lambda x: x > 0, (((obs-pos)/dtn).real for obs in obstacles)
    )))


def detect_loop(pos: complex, dtn: complex, vis: set[tuple[complex, complex]]
                ) -> bool:
    '''
    Detects if, given the current position and the facing direction, the guard
    will be stuck in a loop.
    '''
    # Need to create a copy to avoid side effects.
    visited = set(vis)
    while True:
        # Get the obstacles in the current row/column.
        obstacles = (obstacles_v[pos.real] if dtn.real == 0
                     else obstacles_h[pos.imag])
        try:
            m = walk_until_obstacle(pos, dtn, tuple(obstacles))
        except ValueError:
            return False
        pos += (m - 1) * dtn
        # Update visited positions.
        visited |= {(pos-k*dtn, dtn) for k in range(m)}
        dtn *= 1j
        if (pos, dtn) in visited:
            return True


def main() -> None:
    dtn = -1j
    visited = {(start_pos, dtn)}
    visited_pos = {start_pos}
    loops = 0
    pos = start_pos
    # Traverse the loop, do it step by step because we want to check all
    # possible insertions of obstacles.
    while True:
        obstacles = (obstacles_v[pos.real] if dtn.real == 0
                     else obstacles_h[pos.imag])
        if pos + dtn in obstacles:
            dtn *= 1j
        else:
            pos += dtn
        if not (0 <= pos.real < M and 0 <= pos.imag < N):
            break
        # Check if the guard gets stuck in a loop if we put a new obstacle in
        # the next position.
        nextpos = pos + dtn
        if nextpos not in visited_pos and nextpos not in obstacles:
            obstacles_h[nextpos.imag].add(nextpos)
            obstacles_v[nextpos.real].add(nextpos)
            if detect_loop(pos, dtn*1j, visited):
                loops += 1
            obstacles_h[nextpos.imag].remove(nextpos)
            obstacles_v[nextpos.real].remove(nextpos)
        visited.add((pos, dtn))
        visited_pos.add(pos)
    print(len(visited_pos))
    print(loops)


if __name__ == '__main__':
    from time import perf_counter
    start = perf_counter()
    main()
    print(perf_counter() - start)
