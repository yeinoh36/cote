import sys

# 입력받기
data = sys.stdin.read().splitlines()
N = int(data[0])
housemap = [list(map(int, line.strip())) for line in data[1:N+1]]

# 변수 초기화
num, numlist = 0, []
moves = [[0, -1], [0, 1], [-1, 0], [1, 0]]    # 상하좌우(x, y)

# BFS 탐색
for i in range(N * N):
    x, y = i % N, i // N

    if housemap[y][x]:  # 방문하지 않은 집이라면
        stack, length = [], 1
        stack.append([x, y])
        housemap[y][x] = 0

        while stack:    # 탐색 시작
            tmp = stack.pop()

            for move in moves:
                tmpx = tmp[0] + move[0]
                tmpy = tmp[1] + move[1]

                if 0 <= tmpx < N and 0 <= tmpy < N and housemap[tmpy][tmpx]:
                    stack.append([tmpx, tmpy])
                    housemap[tmpy][tmpx] = 0
                    length += 1

        num += 1
        numlist.append(length)

# 출력
print(num)
for onenum in sorted(numlist):
    print(onenum)