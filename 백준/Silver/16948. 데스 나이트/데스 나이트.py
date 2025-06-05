N = int(input())
r1, c1, r2, c2 = map(int, input().split())

dx, dy = [-2,-2, 0, 0, 2, 2], [-1, 1, -2, 2, -1, 1]

from collections import deque
if 0<=r1<N and 0<=c1<N and 0<=r2<N and 0<=c2<N:
    que = deque()
    visited = [[0]*N for _ in range(N)]
    
    que.append((r1, c1, 0))
    visited[r1][c1] = 1

    while que:
        x, y, n = que.popleft()
        for i in range(6):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny] == 0:
                if nx == r2 and ny == c2:
                    visited[nx][ny] = 1
                    print(n+1)
                    break
                else:
                    que.append((nx, ny, n+1))
                    visited[nx][ny] = 1
        if nx == r2 and ny == c2:
            break

    if visited[r2][c2] == 0:
        print(-1)

else:
    print(-1)