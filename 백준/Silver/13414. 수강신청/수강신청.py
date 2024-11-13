import sys

# 전체 입력받기
data = sys.stdin.read().splitlines()
K, L = map(int, data[0].split())
click = {}
for i, student_id in enumerate(data[1:]):
    click[student_id] = i

# 정렬 후 출력하기
candidate = sorted(click.items(), key=lambda x: x[1])
for i in range(min(K, len(candidate))):  # K와 click의 길이 중 작은 값 사용
    print(candidate[i][0])