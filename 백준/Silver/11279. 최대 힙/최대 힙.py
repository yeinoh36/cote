import heapq
import sys

data = sys.stdin.read().splitlines()
N = int(data[0])
nums = list(map(int, data[1:]))

heap = []

for num in nums:
    if num == 0:
        try:
            print(-heapq.heappop(heap))
        except:
            print(0)
    
    else:
        heapq.heappush(heap, -num)