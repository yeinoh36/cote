import sys
from collections import deque

# 데이터 입력받기
data = sys.stdin.read().splitlines()
N, M = map(int, data[0].split())
line = [list(map(int, data[i].split())) for i in range(1, M+1)]

# 데이터 초기화하기
linked = [[] for _ in range(N)]
for u, v in line:
    linked[u-1].append(v-1)
    linked[v-1].append(u-1)

i, answer = -1, 0
tmp = deque()
visited = [0] * (N)
unvisited = set(range(N))

# 방문하지 않은 곳이 없을 때까지
while unvisited:
    # 연결이 끊긴 경우
    if not tmp:
        answer += 1
        i = unvisited.pop()
        visited[i] = 1
        tmp.extend(linked[i])
    # 연결된 경우
    else:
        i = tmp.popleft()
        if visited[i]:
            continue
        visited[i] = 1
        unvisited.remove(i)
        tmp.extend(linked[i])
    
print(answer)