def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    dp = [0] * (n+1)
    dp[1], dp[2] = 1, 2  # 초기값 설정

    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007  # 모듈러 연산 적용
    
    return dp[n]
