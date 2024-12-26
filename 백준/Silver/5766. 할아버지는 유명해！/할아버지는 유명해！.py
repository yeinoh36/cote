import sys
from collections import defaultdict

data = sys.stdin.read().splitlines()
n = 0

while n < len(data):
    # 첫 번째 줄에서 N과 M 읽기
    N, M = map(int, data[n].split())
    if N == 0 and M == 0:  # 종료 조건
        break

    n += 1  # 다음 줄로 이동

    # 선수별 점수 저장
    scores = defaultdict(int)
    for _ in range(N):
        weekly_ranking = list(map(int, data[n].split()))
        for player in weekly_ranking:
            scores[player] += 1  # 랭킹에 등장하면 점수 +1
        n += 1

    # 점수를 내림차순 정렬하고 2등 점수를 찾기
    sorted_scores = sorted(scores.values(), reverse=True)
    second_place_score = sorted_scores[1]

    # 2등 점수를 가진 선수 번호를 오름차순으로 정렬
    second_place_players = [player for player, score in scores.items() if score == second_place_score]
    second_place_players.sort()

    # 출력
    print(" ".join(map(str, second_place_players)))