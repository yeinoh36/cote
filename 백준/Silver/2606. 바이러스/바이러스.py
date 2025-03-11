import sys
from collections import deque

# 값 입력받기
data = sys.stdin.read().splitlines()
N = int(data[0])
n = int(data[1])

computers = [[0 for _ in range(N)] for _ in range(N)]
for i in range(2, n+2):
    a, b = map(int, data[i].split())
    computers[a-1][b-1] = 1
    computers[b-1][a-1] = 1

# 변수 초기화
now, answer = 0, 0
visited = [0]*N

# BFS(너비우선탐색 <- 선입선출, 큐, popleft)
que = deque()
que.append(now)
visited[now] = 1
while que:
    now = que.popleft()
    answer += 1
    for i in range(N):
        if computers[now][i] and not visited[i]:
            que.append(i)
            visited[i] = 1

print(answer-1)