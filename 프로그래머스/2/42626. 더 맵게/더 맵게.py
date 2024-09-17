import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while len(scoville) > 1:
        first = heapq.heappop(scoville)
        
        if first >= K:
            break
            
        second = heapq.heappop(scoville)
        new = first + 2*second
        heapq.heappush(scoville, new)
        answer += 1
        
    return answer if scoville[0] >= K else -1