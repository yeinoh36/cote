import math

n = int(input())
answer = 0
for i in range(0, n // 2 + 1):
    answer += math.comb(n - i, i)*2**i
print(answer%10007)