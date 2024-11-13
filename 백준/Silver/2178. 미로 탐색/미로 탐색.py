from collections import deque
# 입력 받기
n, m = map(int, input().split())
possible = []
for _ in range(n):
    possible.append(list(map(int, input().strip())))

# 변수 초기화
moves = [[0, -1], [0, 1], [-1, 0], [1, 0]]
answer = [[0]* m for _ in range(n)]
x, y = 0, 0
num = 1

que = deque()
que.append([x, y, num])
possible[y][x] = 0

while que:
    x, y, num = que.popleft()

    for move in moves:
        tmpx = x + move[0]
        tmpy = y + move[1]

        if 0<=tmpx<m and 0<=tmpy<n and possible[tmpy][tmpx]==1:
            que.append([tmpx, tmpy, num+1])
            possible[tmpy][tmpx] = 0
            answer[tmpy][tmpx] = num+1

print(answer[n-1][m-1])