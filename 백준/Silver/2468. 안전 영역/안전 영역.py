from collections import deque
import sys
sys.setrecursionlimit(10000)

data = sys.stdin.read().splitlines()
N = int(data[0])
grid = [list(map(int, data[i+1].split())) for i in range(N)]

max_height = max(max(row) for row in grid)

def iterative_dfs(start_x, start_y, water, visited):
    # deque를 스택처럼 사용
    stack = deque([(start_x, start_y)])
    while stack:
        x, y = stack.pop()
        if x < 0 or x >= N or y < 0 or y >= N:
            continue
        if visited[x][y] or grid[x][y] <= water:
            continue
        visited[x][y] = True
        stack.append((x-1, y))
        stack.append((x+1, y))
        stack.append((x, y-1))
        stack.append((x, y+1))

result = 0
for water in range(max_height + 1):
    visited = [[False]*N for _ in range(N)]
    safe_area = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] > water and not visited[i][j]:
                iterative_dfs(i, j, water, visited)
                safe_area += 1
    result = max(result, safe_area)

print(result)