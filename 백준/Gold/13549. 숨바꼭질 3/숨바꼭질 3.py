N, K = map(int, input().split())

import heapq
heap, time, MAX,  = [], 0, max(2*K, N)
visited = [False] * (MAX+1)
tmp = N
while 0 <= tmp <= MAX and not visited[tmp]:
    visited[tmp] = True
    heapq.heappush(heap, [time, tmp])
    tmp = 2*tmp

while heap:
    time, X = heapq.heappop(heap)
    if X == K:
        break

    tmp = [X+1, X-1]
    for i in tmp:
        while 0 <= i <= MAX and not visited[i]:
            visited[i] = True
            heapq.heappush(heap, [time+1, i])
            i = 2*i

print(time)
