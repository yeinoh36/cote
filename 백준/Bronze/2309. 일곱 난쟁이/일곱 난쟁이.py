import sys
heights = list(map(int, sys.stdin.read().splitlines()))

from itertools import combinations
for comb in combinations(heights, 7):
    if sum(comb) == 100:
        for c in sorted(comb):
            print(c)
        break