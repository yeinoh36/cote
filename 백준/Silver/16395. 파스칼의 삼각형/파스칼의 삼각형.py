n, k = map(int, input().split())

if k == 1 or n == k:
    print(1)
    
else:
    answer = 1
    n -= 1
    k -= 1

    for i in range(n-k+1, n+1):
        answer *= i

    for i in range(k):
        answer //= i+1
    
    print(answer)