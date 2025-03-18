import sys
data = sys.stdin.read().splitlines()
N = int(data[0])
nums = list(map(int, data[1:]))

import heapq
max_heap = [] # 중앙값 이하의 값들을 저장하는 최대 힙
min_heap = [] # 중앙값 이상의 값들을 저장하는 최소 힙

for i, num in enumerate(nums):
    # 우선적으로 max_heap에 push
    heapq.heappush(max_heap, -num)

    ## 중앙값 맞추기
    # max_heap의 최대값이 min_heap의 최소값보다 작다면 swap
    if min_heap and -max_heap[0] > min_heap[0]:
        max_val = -heapq.heappop(max_heap)
        min_val = heapq.heappop(min_heap)
        heapq.heappush(max_heap, -min_val)
        heapq.heappush(min_heap, max_val)
    # max_heap의 길이가 min_heap의 길이보다 2이상 크다면 이동
    if len(max_heap) > len(min_heap) + 1:
        heapq.heappush(min_heap, -heapq.heappop(max_heap))
    
    print(-max_heap[0])
