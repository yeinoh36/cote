n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split()))

dice = [0] * 6  # top, bottom, north, south, west, east

# 동서북남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def roll(dir):
    top, bottom, north, south, west, east = dice[:]
    if dir == 1:  # 동
        dice[0], dice[1], dice[4], dice[5] = west, east, bottom, top
    elif dir == 2:  # 서
        dice[0], dice[1], dice[4], dice[5] = east, west, top, bottom
    elif dir == 3:  # 북
        dice[0], dice[1], dice[2], dice[3] = south, north, top, bottom
    elif dir == 4:  # 남
        dice[0], dice[1], dice[2], dice[3] = north, south, bottom, top

x, y = x, y
for cmd in commands:
    nx = x + dx[cmd - 1]
    ny = y + dy[cmd - 1]
    if 0 <= nx < n and 0 <= ny < m:
        roll(cmd)
        if board[nx][ny] == 0:
            board[nx][ny] = dice[1]
        else:
            dice[1] = board[nx][ny]
            board[nx][ny] = 0
        x, y = nx, ny
        print(dice[0])