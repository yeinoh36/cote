N = int(input())
P = list(map(int, input().split()))

dp = [0]*(N+1)
for i in range(1, N+1):
    dp[i] = P[i-1]
    
import heapq
for i in range(2, N+1):
    tmp = []
    heapq.heappush(tmp, -dp[i])
    for j in range(1,i):
        heapq.heappush(tmp, -(dp[j] + dp[i-j]))
    dp[i] = -heapq.heappop(tmp)
        
print(dp[-1])