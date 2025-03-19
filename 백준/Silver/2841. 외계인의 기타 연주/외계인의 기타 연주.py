import sys
import heapq

data = sys.stdin.read().splitlines()
N, P = map(int, data[0].split())

answer = 0
dictionary = {}

for i in range(N):
    s, p = map(int, data[i + 1].split())

    # 새로운 줄이 나옴면 초기화
    if s not in dictionary:
        dictionary[s] = []
    
    heap = dictionary[s]

    # 기존 힙에서 현재 값보다 큰 값들을 pop
    while heap and -heap[0] > p:
        heapq.heappop(heap)
        answer += 1

    # heap이 비어있거나 현재 값이 heap의 최대값이 아니라면 push
    if not heap or -heap[0] != p:
        heapq.heappush(heap, -p)
        answer += 1

print(answer)