from itertools import combinations

# 입력 처리
import sys
input = sys.stdin.read
data = input().splitlines()
N = int(data[0])
S = [list(map(int, line.split())) for line in data[1:]]

# 모든 플레이어의 인덱스
players = list(range(N))
min_diff = float('inf')

# N명의 플레이어에서 N/2명을 선택하는 조합
for team1 in combinations(players, N // 2):
    # team2는 전체에서 team1을 뺀 나머지
    team2 = [p for p in players if p not in team1]
    
    # 능력치 계산
    team1_score = sum(S[i][j] + S[j][i] for i, j in combinations(team1, 2))
    team2_score = sum(S[i][j] + S[j][i] for i, j in combinations(team2, 2))
    
    # 두 팀의 점수 차이
    diff = abs(team1_score - team2_score)
    min_diff = min(min_diff, diff)
    
    # 차이가 0이면 더 이상 탐색 필요 없음
    if min_diff == 0:
        break

# 최소 차이 출력
print(min_diff)