"""
정수 1은 익은 토마토, 
정수 0 은 익지 않은 토마토, 
정수 -1은 토마토가 들어있지 않은 칸
"""

import sys
from collections import deque

# 입력받기
data = sys.stdin.read().splitlines()
M, N, H = map(int, data[0].split())
tomatoes = [[[0] * M for _ in range(N)] for _ in range(H)]
for i in range(H):
    for j in range(N):
        tomatoes[i][j] = list(map(int, data[i * N + j + 1].split()))

# 변수 초기화
answer = 0
time = 0
moves = [(0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1), (-1, 0, 0), (1, 0, 0)] # 상하좌우앞뒤 (i, j, k)
queue = deque()
for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomatoes[h][n][m] == 1:
                queue.append((h, n, m, time))
# bfs 탐색
while queue:
    h, n, m, time = queue.popleft()
    answer = max(time, answer)
    
    for dh, dn, dm in moves:
        tmph = h + dh
        tmpn = n + dn
        tmpm = m + dm
        
        if 0<=tmph<H and 0<=tmpn<N and 0<=tmpm<M and tomatoes[tmph][tmpn][tmpm]==0:
            queue.append((tmph, tmpn, tmpm, time+1))
            tomatoes[tmph][tmpn][tmpm] = 1

if any(0 in line for floor in tomatoes for line in floor):
    print(-1)
else:
    print(answer)
    