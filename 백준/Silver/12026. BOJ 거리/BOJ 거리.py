N = int(input())
BOJs = input().strip()

dp = [float('inf')] * N
dp[0] = 0

for i in range(N):
    for j in range(i+1, N):
        if (BOJs[i] == 'B' and BOJs[j] == 'O') or \
           (BOJs[i] == 'O' and BOJs[j] == 'J') or \
           (BOJs[i] == 'J' and BOJs[j] == 'B'):
            cost = (j - i) ** 2
            dp[j] = min(dp[j], dp[i] + cost)

if dp[N-1] == float('inf'):
    print(-1)
else:
    print(dp[N-1])