from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer, cur_w = 0, 0
    queue = deque(truck_weights)
    bridge = deque()
    
    cur = queue.popleft()
    cur_w += cur
    bridge.append((0, cur))

    while queue or bridge:
        answer += 1
        
        for i in range(len(bridge)):
            t = list(bridge[i])
            t[0] += 1
            
            bridge[i] = tuple(t)
            
        if bridge[0][0] >= bridge_length:
            cur_w -= bridge[0][1]
            bridge.popleft()
                
        if queue and cur_w + queue[0] <= weight and len(bridge) < bridge_length:
            cur = queue.popleft()
            cur_w += cur
            bridge.append((0, cur))
    
    answer +=1
    
    return answer