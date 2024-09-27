from collections import deque

def solution(people, limit):
    answer = 0
    
    que = deque(sorted(people))  # 몸무게를 정렬해서 덱으로 변환
    
    while len(que) > 1:
        max_w = que.pop()  # 가장 무거운 사람을 덱의 끝에서 꺼냄
        threshold = limit - max_w  # 남은 제한 무게
        
        # 덱에 사람이 남아 있고, 가장 가벼운 사람이 현재 threshold 이하일 경우
        if que and que[0] <= threshold:
            que.popleft()  # 가장 가벼운 사람을 태워 보냄
        
        answer += 1  # 한 번의 탑승 완료
    
    if que:  # 마지막으로 한 명이 남아 있으면 한 번 더 필요
        answer += 1
    
    return answer
