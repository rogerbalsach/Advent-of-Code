#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 09:19:36 2024

@author: Roger Balsach
"""
from collections import defaultdict
from functools import cmp_to_key

with open('input.txt') as file:
    content = file.read().strip()

rules_str, updates_str = content.split('\n\n')
rules: dict[str, set[str]] = defaultdict(set)
vertices: set[str] = set()
in_degree: dict[str, int] = defaultdict(int)
for line in rules_str.splitlines():
    first, last = line.split('|')
    rules[first].add(last)
    in_degree[last] += 1
    vertices |= {first, last}
updates = [line.split(',') for line in updates_str.splitlines()]


# This works assuming there is a rule for each pair (which is true)
# This only works if for any pair of pages there exist a rule for them. It
# checks the update in O(n).
def check_update(update: list[str]) -> bool:
    last_page = update[0]
    for page in update[1:]:
        if page not in rules[last_page]:
            return False
        last_page = page
    return True


def cmp(x: str, y: str) -> int:
    return 2*(x in rules[y]) - 1


def main() -> None:
    # The approach of Part 2 sorts the list and then gets the middle element.
    # It works in O(n log n)
    tot1 = tot2 = 0
    for update in updates:
        if check_update(update):
            tot1 += int(update[len(update)//2])
        else:
            update.sort(key=cmp_to_key(cmp))
            assert check_update(update)
            tot2 += int(update[len(update) // 2])
    print(tot1)
    print(tot2)

if __name__ == '__main__':
    main()
