import sys
import heapq

input = sys.stdin.read
data = input().split()

n = int(data[0])
heap = []

# 힙에 원소를 추가
for i in range(1, n + 1):
    heapq.heappush(heap, int(data[i]))

# 정렬된 결과를 출력
output = []
while heap:
    output.append(heapq.heappop(heap))

# 결과를 한 번에 출력
sys.stdout.write("\n".join(map(str, output)) + "\n")
