from collections import deque
import sys

data = sys.stdin.read().splitlines()
n = int(data[0])

for i in range(n):
    N, M = map(int, data[2*i+1].split())
    nums = list(map(int, data[2*i+2].split()))

    que = deque((num, i) for i, num in enumerate(nums))
    sorted_que = deque(sorted(que, key=lambda x: x[0], reverse=True))

    answer = 0
    while que:
        num, idx = que.popleft()

        if num < sorted_que[0][0]:
            que.append((num, idx))
        else:
            answer += 1
            sorted_que.popleft()

            if idx == M:
                break

    print(answer)