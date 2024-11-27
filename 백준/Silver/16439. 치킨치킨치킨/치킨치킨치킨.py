import sys
from itertools import combinations

# 입력 데이터 처리
data = sys.stdin.read().splitlines()
N, M = map(int, data[0].split())
likes = [list(map(int, line.split())) for line in data[1:]]

# 3개 치킨 메뉴 조합 생성
num = min(N, 3)
chicks = combinations(range(M), num)

# 최대 만족도 계산
answer = 0
for chick in chicks:
    tmp = 0
    for n in range(N):  # 각 사람의 최대 만족도 계산
        tmp += max(likes[n][m] for m in chick)
    answer = max(answer, tmp)  # 최대값 갱신

print(answer)