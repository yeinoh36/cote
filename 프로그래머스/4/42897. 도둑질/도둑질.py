def rob(money, first):
    answer = 0
    dp = [[] for _ in range(len(money))]
    if first:
        dp[2] = [money[0], money[0]+money[2]]
    else:
        dp[1] = [0, money[1]]
        dp[2] = [max(dp[1][0], dp[1][1]), dp[1][0]+money[2]]
    
    if len(dp)>3:
        for i in range(3,len(dp)):
            dp[i] = [max(dp[i-1][0], dp[i-1][1]), dp[i-1][0]+money[i]]
    
    answer = max(dp[-1])
    if first:
        answer = dp[-1][0]
    return answer
        
def solution(money):
    return max(rob(money, True), rob(money, False))