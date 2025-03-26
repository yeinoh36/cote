import sys
input = sys.stdin.readline

N = int(input())
nlist = [tuple(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]

for length in range(1, N):  # length = y - x
    for x in range(N - length):
        y = x + length
        dp[x][y] = float('inf')
        for k in range(x, y):
            cost = dp[x][k] + dp[k+1][y] + nlist[x][0] * nlist[k][1] * nlist[y][1]
            if cost < dp[x][y]:
                dp[x][y] = cost

print(dp[0][N-1])