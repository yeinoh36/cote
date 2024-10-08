""" BFS
1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.
3. 2번의 과정을 더 이상 수행할 수 없을 때까지 한다.
"""

from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    answer = 0
    mintime = [0] * len(words)
    time = 0
    queue = deque()
    queue.append([begin, time])
    
    while queue:
        # 큐에서 now 꺼내기
        now, time = queue.popleft()
        # now가 target과 같다면 answer 값 조정하기
        if now == target:
            if not(answer):
                answer = time
            else:
                answer = min(answer, time)
        
        # 인접한 노드 찾기
        time += 1
        for i, word in enumerate(words):
            error = 0 # 불일치 변수
            for j in range(len(word)):
                if word[j] != now[j]:
                    error += 1
                    
            # 하나만 불일치 하면 --> 인접하다!
            if error == 1 :
                # 거리 비교해 의미 있는 최소 거리인지 확인하기
                if not(mintime[i]): # 방문한 적 없으면 추가
                    queue.append([word, time])
                    mintime[i] = time
                elif min(mintime[i], time) != mintime[i]: # 최소 거리라면 추가
                    queue.append([word, time])
                    mintime[i] = time
                    
    return answer