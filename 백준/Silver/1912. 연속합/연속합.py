n = int(input())
nums = list(map(int, input().split()))

dp, tmp = [0] * n, 0
dp[0] = nums[0]
for i in range(1, n):
    dp[i] = max(nums[i], dp[i-1] + nums[i])

print(max(dp))