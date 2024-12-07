#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 11:10:40 2024

@author: Roger Balsach
"""
from collections.abc import Callable

with open("input.txt") as file:
    content = file.read().strip()

optype = tuple[Callable[[int, int], int], ...]


def get_min_max(first: int, rem: list[int], operations: optype
                ) -> tuple[int, int]:
    minimum = first
    maximum = first
    for num in rem:
        minimum = min(op(minimum, num) for op in operations)
        maximum = max(op(maximum, num) for op in operations)
    return minimum, maximum


def get_calibration_result(operations: optype, valid: set[str]) -> int:
    calibration = 0
    for line in content.splitlines():
        if line in valid:
            continue
        (test,), (num, *nums) = map(
            lambda s: list(map(int, s.strip().split())), line.split(':')
        )
        # Try to find impossible lines ahead of time
        minm, maxm = get_min_max(num, nums, operations)
        if minm == test or maxm == test:
            calibration += test
            valid.add(line)
            continue
        if not (minm < test < maxm):
            continue
        stack = [(num, nums)]
        # Use DFS to traverse the tree of all posibilities.
        while stack:
            tot, (num, *rem) = stack.pop()
            for op in operations:
                newtot = op(tot, num)
                if not rem:
                    if newtot == test:
                        calibration += test
                        valid.add(line)
                        stack = []
                        break
                    continue
                if newtot <= test:
                    # All operations are increasing, thus we don't need to keep
                    # looking at branches that surpas the test value.
                    stack.append((newtot, rem))
    return calibration


def main() -> None:
    operations: optype = (lambda x, y: x + y, lambda x, y: x * y)
    # lines that are valid from the first part will also be valid for the
    # second part, don't need to look them again.
    valid: set[str] = set()
    calibration = get_calibration_result(operations, valid)
    print(calibration)
    operations = (lambda x, y: x + y, lambda x, y: x * y,
                  lambda x, y: int(str(x)+str(y)))
    calibration += get_calibration_result(operations, valid)
    print(calibration)


if __name__ == '__main__':
    from time import perf_counter
    start = perf_counter()
    main()
    print(perf_counter() - start)
