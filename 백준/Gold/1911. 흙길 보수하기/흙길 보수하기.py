import sys
from collections import deque

data = sys.stdin.read().splitlines()
N, L = map(int, data[0].split())
pounds = deque(sorted([tuple(map(int, line.split())) for line in data[1:N+1]]))

answer, now = 0, 0

while pounds:
    start, end = pounds.popleft()
    if now >= end:
        continue
    if now < start:
        now = start

    plus = (end - now + L - 1) // L
    answer += plus
    now += plus * L

print(answer)
