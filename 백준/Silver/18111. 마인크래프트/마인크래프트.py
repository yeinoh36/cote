import sys
from collections import Counter
from itertools import chain

# 데이터 입력 받기
data = sys.stdin.read().splitlines()
N, M, B = map(int, data[0].split())
states = list(chain.from_iterable([list(map(int, row.split())) for row in data[1:]]))

# 층수 세기
counter = Counter(states)
low = min(counter)
high = max(counter)

# 작업하며 시간 비교하기
answer_time = float('inf')
answer_level = 0
for level in range(low, high+1):
    time = 0
    block = B

    for height, count in counter.items():
        if height < level:
            diff = level - height
            time += diff * count     
            block -= diff * count  
        elif height > level:
            diff = height - level
            time += diff * 2 * count
            block += diff * count

    if block < 0:
        continue

    if time < answer_time or (time == answer_time and level > answer_level):
        answer_time = time
        answer_level = level

print(answer_time, answer_level)