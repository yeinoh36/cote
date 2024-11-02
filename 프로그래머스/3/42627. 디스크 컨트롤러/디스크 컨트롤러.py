from collections import deque
import heapq

def solution(jobs):
    answer = 0
    
    time = 0                        # 시간
    works = deque(sorted(jobs))     # 요청 시점을 기준으로 정렬된 작업 리스트
    ready = []                      # 대기열
    
    while works or ready:
        # 대기열 정리
        # time 내에 요청된 작업 ready에 추가
        while works and works[0][0] <= time:
            answer -= works[0][0]               # 요청 시간 빼기
            heapq.heappush(ready, works[0][1])
            works.popleft()
        # ready가 없다면 time 조정
        if not ready:
            time = works[0][0]
            continue
        
        # 작업
        now = heapq.heappop(ready)
        time += now
        
        answer += time                          # 소요 시간 더하기
    
    return answer // len(jobs)                  # 평균 계산하기