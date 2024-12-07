#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 09:54:43 2024

@author: Roger Balsach
"""
from collections.abc import Callable
from itertools import product

with open('input.txt') as file:
    content = file.read().strip()

lines = content.splitlines()
check = Callable[[int, int, int, int], bool]


def scan(start_char: str, directions: tuple[tuple[int, int], ...],
         bound_check: check, scan_check: check) -> int:
    s = 0
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char != start_char:
                continue
            for di, dj in directions:
                if not bound_check(i, j, di, dj):
                    continue
                if scan_check(i, j, di, dj):
                    s += 1
    return s


def main() -> None:
    s1 = scan(
        'X',
        ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)),
        lambda i, j, di, dj: (0 <= i + 3*di < len(lines)
                              and 0 <= j + 3*dj < len(lines[0])),
        lambda i, j, di, dj: (lines[i+di][j+dj] == 'M'
                              and lines[i+2*di][j+2*dj] == 'A'
                              and lines[i+3*di][j+3*dj] == 'S')
    )
    print(s1)

    s2 = scan(
        'A', tuple(product((-1, 1), repeat=2)),  # type: ignore
        lambda i, j, di, dj: 0 < i < len(lines)-1 and 0 < j < len(lines[0])-1,
        lambda i, j, dp, dn: (
            lines[i+dp][j+dp] == lines[i+dn][j-dn] == 'M'
            and lines[i-dp][j-dp] == lines[i-dn][j+dn] == 'S'
        )
    )
    print(s2)


if __name__ == '__main__':
    main()
