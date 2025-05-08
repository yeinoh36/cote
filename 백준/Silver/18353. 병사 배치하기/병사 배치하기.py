n = int(input())
soldiers = list(map(int, input().split()))

dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if soldiers[j] > soldiers[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))