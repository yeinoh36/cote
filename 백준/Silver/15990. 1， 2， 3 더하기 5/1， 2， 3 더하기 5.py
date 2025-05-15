T = int(input())
MOD = 1000000009

MAX_N = 100_001
dp = [[0, 0, 0] for _ in range(MAX_N)]
dp[1] = [1, 0, 0]  # 1
dp[2] = [0, 1, 0]  # 2
dp[3] = [1, 1, 1]  # 1+2, 2+1, 3

for i in range(4, MAX_N):
    dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % MOD
    dp[i][1] = (dp[i-2][0] + dp[i-2][2]) % MOD
    dp[i][2] = (dp[i-3][0] + dp[i-3][1]) % MOD

for _ in range(T):
    n = int(input())
    print(sum(dp[n]) % MOD)