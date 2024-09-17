from collections import deque
import bisect

def solution(operations):
    answer = []
    
    que = deque()
    for operation in operations:
        act = operation[0]
        num = int(operation[2:])
    
        if act == "I":
            bisect.insort(que, num)
            
        elif act == "D":
            if not que:
                continue
                
            if num == -1:
                que.popleft()
            
            elif num == 1:
                que.pop()
        
    if que:
        answer.append(que[-1])
        answer.append(que[0])
    else: 
        answer.append(0)
        answer.append(0)
        
    return answer