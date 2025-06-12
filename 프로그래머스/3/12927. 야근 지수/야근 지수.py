import heapq
def solution(n, works):
    answer = 0
    heap = []
    for w in works:
        heapq.heappush(heap, -w)
        
    while n:
        n -= 1
        w = heapq.heappop(heap) + 1
        if w > 0:
            w = 0 
        heapq.heappush(heap, w)
        
    for w in heap:
        answer += w*w
        
    return answer