X = int(input())
dp = [0] * (X+1)
dp[-1] = 0

for i in range(X-1, 0, -1):
    dp[i] = dp[i+1] + 1
    if 1<=2*i<=X:
        dp[i] = min(dp[i], dp[2*i]+1)
    if 1<=3*i<=X:
        dp[i] = min(dp[i], dp[3*i]+1)

print(dp[1])