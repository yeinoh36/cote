def solution(land):
    answer = 0
    dp = [[0]*4 for _ in range(len(land))]
    for i in range(len(land)):
        for j in range(4):
            if i == 0: 
                dp[i][j] = land[i][j] 
                continue
            for k in range(4):
                if j == k: 
                    continue
                dp[i][j] = max(dp[i][j], land[i][j]+dp[i-1][k])
    answer = max(dp[-1])          
    return answer