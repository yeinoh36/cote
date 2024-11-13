import sys

data = sys.stdin.read().splitlines()
S, E, Q = data[0].split()

answer = 0
enter = set()  # 중복을 방지하기 위해 set 사용
for line in data[1:]:
    time, student_id = line.split()  # 각 줄을 공백 기준으로 분리
    if time <= S:
        enter.add(student_id)  # 입장 시간에 맞춰 추가

    elif E <= time <= Q and student_id in enter:  # 퇴장 시간대에 해당하는 경우
        answer += 1
        enter.remove(student_id)  # 중복 카운팅 방지

print(answer)