import sys

data = sys.stdin.read().splitlines()
N = int(data[0])
I = list(data[1].split())
J = list(data[2].split())

HP = 100
happiness = 0

from itertools import combinations
for i in range(N, 0, -1):
    for comb in combinations(range(N), i):
        tmp = 0
        HP = 100
        for c in comb:
            HP -= int(I[c])
            tmp += int(J[c])

            if HP <= 0:
                tmp = 0
                break
        
        happiness = max(happiness, tmp)

print(happiness)

            