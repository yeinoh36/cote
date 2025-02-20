import sys
data = sys.stdin.read().splitlines()
N = int(data[0])
stairs = list(map(int, data[1:]))

dp = [[] for _ in range(N)]

def up(n, stairs, dp):
    if n == 0:
        return [[stairs[0], 1]]
    elif n == 1:
        return [[stairs[0]+stairs[1], 1], [stairs[1], 0]]  
    else:
        tmp = []
        
        tmp2 = 0
        for past in dp[n-2]:
            tmp2 = max(tmp2, past[0]+stairs[n])   
        tmp.append([tmp2, 0])
        
        tmp1 = 0
        for past in dp[n-1]:
            if past[1] < 1:
                tmp1 = max(tmp1, past[0]+stairs[n])
        tmp.append([tmp1, 1])
        return tmp

for i in range(N):
    dp[i] = up(i, stairs, dp)

print(max(past[0] for past in dp[-1]))
