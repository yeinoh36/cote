def find_min_moves(n, sequence):
    # dp 배열 생성
    dp = [1] * n

    # LIS 길이 계산
    for i in range(1, n):
        for j in range(i):
            if sequence[i] > sequence[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    # 최장 증가 부분 수열(LIS)의 길이
    lis_length = max(dp)

    # 최소 이동 횟수 = 전체 길이 - LIS의 길이
    return n - lis_length

# 입력 받기
n = int(input())
sequence = [int(input()) for _ in range(n)]

# 결과 출력
print(find_min_moves(n, sequence))