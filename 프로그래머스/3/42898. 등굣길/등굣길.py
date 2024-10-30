from collections import deque

def solution(m, n, puddles):
    # [최소시간, 횟수]
    mintime = [[[-1, 0] for _ in range(m)] for _ in range(n)]
    
    # 상, 하, 좌, 우 이동 설정 [dx, dy]
    moves = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    
    # 초기값 설정
    queue = deque()
    queue.append([0, 0, 0])  # x, y, time
    mintime[0][0] = [0, 1]  # 시작점: 시간 0, 경로 수 1
    
    while queue:
        x, y, time = queue.popleft()
        time += 1
        prev_count = mintime[y][x][1]
        
        # 이동 가능한 모든 방향으로
        for move in moves:
            tmpx = x + move[0]
            tmpy = y + move[1]
            
            # 격자 내에 있고 웅덩이가 아닌 경우
            if 0 <= tmpx < m and 0 <= tmpy < n and [tmpx + 1, tmpy + 1] not in puddles:
                
                # 방문하지 않은 경우
                if mintime[tmpy][tmpx][0] == -1:
                    queue.append([tmpx, tmpy, time])
                    mintime[tmpy][tmpx] = [time, prev_count]
                
                # 동일 시간에 방문한 경우, 경로 수 누적
                elif mintime[tmpy][tmpx][0] == time:
                    mintime[tmpy][tmpx][1] += prev_count
                
                # 더 짧은 시간에 방문 가능한 경우, 최소 시간 갱신 및 경로 수 초기화
                elif mintime[tmpy][tmpx][0] > time:
                    queue.append([tmpx, tmpy, time])
                    mintime[tmpy][tmpx] = [time, prev_count]
    
    # 최종 도착지의 경로 수 반환
    return mintime[n - 1][m - 1][1] % (10**9 + 7)