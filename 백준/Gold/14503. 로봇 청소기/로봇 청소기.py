## 데이터 입력받기
import sys
data = sys.stdin.read().splitlines()
N, M = map(int, data[0].split())
r, c, d = map(int, data[1].split())
states = [list(map(int, data[i+2].split())) for i in range(N)]

## 변수 초기화하기
answer = 0

# 북, 동, 남, 서
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

from collections import deque
que = deque()
que.append((c, r, d))
while que:
    x, y, d = que.popleft()
    # 현재 칸이 청소가 되지 않은 경우
    if states[y][x] == 0:
        states[y][x] = 2
        answer += 1    # 청소한 경우 answer += 1
    
    # 반시계 방향으로 회전하며 청소되지 않은 빈칸 찾기
    TF = False
    for i in range(4):
        tmpd = (d-i+3)%4
        tmpx = x + dx[tmpd]
        tmpy = y + dy[tmpd]
        # 청소되지 않은 빈칸이 있다면 큐에 추가하기
        if 0<=tmpx<M and 0<=tmpy<N and states[tmpy][tmpx] == 0:
            que.append((tmpx, tmpy, tmpd))
            TF = True
            break
    # 청소되지 않은 빈칸이 없다면 방향을 유지하며 후진하기
    if not TF:
        tmpx = x - dx[d]
        tmpy = y - dy[d]
        if 0<=tmpx<M and 0<=tmpy<N and states[tmpy][tmpx] != 1:
            que.append((tmpx, tmpy, d))
        # 후진할 수 없다면 작동 중지하기
        else:
            break

print(answer)