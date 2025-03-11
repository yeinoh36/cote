import sys
from collections import deque

# 데이터 입력 받기
data = sys.stdin.read().splitlines()
T = int(data[0])

index = 1
for _ in range(T):
    N = int(data[index])
    home = list(map(int, data[index+1].split()))
    conv = [list(map(int, data[index+i].split())) for i in range(2, N+2)]
    fest = list(map(int, data[index+N+2].split()))
    index += N+3
    
    # 변수 초기화
    beer = 20
    visited = [0]*len(conv)
    que = deque()
    
    # BFS(너비우선탐색 -> 큐, 선입선출)
    que.append(home)
    while que:
        now = que.popleft()
        # 페스티벌에 도착할 수 있는가
        if abs(now[0]-fest[0])+abs(now[1]-fest[1]) <= beer*50:
            now = fest
            break

        # 갈 수 있는 편의점이 있는가
        for i, where in enumerate(conv):
            x, y = where[0], where[1]
            if abs(now[0]-x)+abs(now[1]-y)<=beer*50 and not visited[i]:
                visited[i] = 1
                que.append([x, y])


    if abs(now[0]-fest[0])+abs(now[1]-fest[1]) <= beer*50:
        now = fest
        print("happy")
    else: print("sad")

