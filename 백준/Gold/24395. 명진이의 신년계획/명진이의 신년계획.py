import sys
data = sys.stdin.read().splitlines()

N, M = map(int, data[0].split())
diseases = [list(map(int, data[m].split())) for m in range(1, M + 1)]


dp = [[-1] * 51 for _ in range(51)]  # 갱신 X
dp[0][0] = 0  # 시작점 초기화

# DP 갱신
for r_val, b_val, c_val in diseases:
    # 역순 탐색으로 중복 갱신 방지
    for r in range(50, -1, -1):
        for b in range(50, -1, -1):
            if dp[r][b] != -1 and r + r_val <= 50 and b + b_val <= 50:
                dp[r + r_val][b + b_val] = max(dp[r + r_val][b + b_val], dp[r][b] + c_val)

# 학생 위험군 계산
answers = []
for n in range(1, N + 1):
    r, b = map(int, data[M + n].split())
    answers.append([n, dp[r][b] if dp[r][b] != -1 else 0])

# 결과 정렬 및 출력
answers.sort(key=lambda x: (x[1], x[0]))
for answer in answers:
    print(*answer)