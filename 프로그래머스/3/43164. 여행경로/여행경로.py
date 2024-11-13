def solution(tickets):
    # 일반 딕셔너리로 경로 초기화 (사전순으로 정렬하여 저장)
    routes = {}
    for start, end in sorted(tickets):
        if start not in routes:
            routes[start] = []
        routes[start].append(end)
    
    result = []

    # DFS 함수 정의 (백트래킹 포함)
    def dfs(current):
        # current 위치에서 출발할 수 있는 경로가 있을 동안 반복
        while current in routes and routes[current]:
            # 사전순으로 경로를 선택하여 다음 목적지로 이동
            next_dest = routes[current].pop(0)
            dfs(next_dest)  # 재귀 호출로 다음 목적지 탐색
        
        # 더 이상 갈 곳이 없을 때 현재 위치를 결과에 추가 (백트래킹)
        result.append(current)
    
    # 탐색 시작점 설정
    start = "ICN"
    dfs(start)
    
    # 경로 역순으로 반환 (백트래킹 순서 때문에 역순이 필요)
    return result[::-1]