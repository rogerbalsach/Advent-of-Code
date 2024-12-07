#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 09:34:13 2024

@author: Roger Balsach
"""

import re

with open("input.txt") as file:
    content = file.read().strip()


def main() -> None:
    pattern = re.compile(r"mul\((\d+),(\d+)\)|(do(n't)?)\(\)")

    s1 = s2 = 0
    r = 1
    for instruction in pattern.finditer(content):
        if instruction.group(3) == 'do':
            r = 1
        elif instruction.group(3) == "don't":
            r = 0
        else:
            n, m = map(int, instruction.groups()[:2])
            s1 += n * m
            s2 += r * n * m

    print(s1)
    print(s2)


if __name__ == '__main__':
    main()
