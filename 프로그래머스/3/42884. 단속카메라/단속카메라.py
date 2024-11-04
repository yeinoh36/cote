def solution(routes):
    answer = 1
    routes = sorted(routes)
    
    start = routes[0][0]
    end = routes[0][1]
    
    for route in routes[1:]:
        # 포함 관계라면
        if start <= route[0] <= end or start <= route[1] <= end:
            start = max(start, route[0])
            end = min(end, route[1])
            continue
            
        # 비포함 관계라면
        else: 
            start = route[0]
            end = route[1]
            answer += 1
            
    return answer