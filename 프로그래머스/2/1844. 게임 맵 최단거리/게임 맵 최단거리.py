""" BFS
1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.
3. 2번의 과정을 더 이상 수행할 수 없을 때까지 한다.
"""

from collections import deque

def solution(maps):
    answer = 0
    
    # 가로 세로 길이
    n = len(maps[0])
    m = len(maps)
    
    # 최소 시간을 담을 변수 생성
    mintime = [[0] * n for _ in range(m)]
    time = 0
    
    # 상, 하, 좌, 우 (y, x) 변수 생성
    moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    
    # 변수 초기화
    queue = deque()
    y, x = 0, 0
    time = 1
    queue.append([y, x, time])
    
    while queue:
        y, x, time = queue.popleft()
        time += 1
        
        # 이동에 따른 변화
        for move in moves:
            tmpy = y + move[0]
            tmpx = x + move[1]
            # 인접한가
            if 0 <= tmpy < m and 0 <= tmpx < n :
                # 길인가
                if maps[y + move[0]][x + move[1]]:
                    # 단한번도 방문한 적이 없다면 최소 시간 등록
                    if mintime[tmpy][tmpx] == 0:
                        queue.append([tmpy, tmpx, time])
                        mintime[tmpy][tmpx] = time
                    
                    # 방문한 적 있다면 최소 확인 후 등록
                    elif min(mintime[tmpy][tmpx], time) != mintime[tmpy][tmpx]:
                        queue.append([tmpy, tmpx, time])
                        mintime[tmpy][tmpx] = time
                          
                    
    answer = mintime[m-1][n-1]
    
    return answer if answer else -1