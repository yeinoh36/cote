testnum = int(input())

for _ in range(testnum):
    n = int(input())
    
    if n < 4:
        if n == 1:
            print(1)
        elif n == 2:
            print(2)
        elif n == 3:
            print(4)
    
    else:
        dp = [0] * (n+1)
        dp[1], dp[2], dp[3] = 1, 2, 4
        
        for i in range(4, n+1):
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

        print(dp[n])