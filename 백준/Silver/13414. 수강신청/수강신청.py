import sys
from collections import OrderedDict

# 전체 입력받기
data = sys.stdin.read().splitlines()
K, L = map(int, data[0].split())
click = OrderedDict()

# 두 번째 줄부터 마지막 줄까지 학번 처리
for student_id in data[1:]:
    if student_id in click:
        del click[student_id]  # 기존 학번을 삭제하고
    click[student_id] = None  # 최신 학번을 다시 추가하여 순서 유지

# 최대 K명의 학번만 출력
for i, student_id in enumerate(click.keys()):
    if i >= K:
        break
    print(student_id)