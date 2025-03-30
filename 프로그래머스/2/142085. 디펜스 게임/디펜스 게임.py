import heapq

def solution(n, k, enemy):
    answer = 0
    heap = []

    for e in enemy:
        if e <= n:
            heapq.heappush(heap, -e)
            n -= e
            answer += 1
        else:
            if k:
                if heap and -heap[0] > e:
                    maxn = -heapq.heappop(heap)
                    heapq.heappush(heap, -e)
                    n += maxn - e
                k -= 1
                answer += 1
            else:
                break      
    return answer