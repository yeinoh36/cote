import sys
input = sys.stdin.read
sys.setrecursionlimit(10**6)

def dfs(node, parent):
    total_cost = 0
    for neighbor, cost in graph[node]:
        if neighbor != parent:
            total_cost += dfs(neighbor, node)
    if total_cost == 0:  # 리프 노드인 경우
        return min_cost[node][parent]
    return min(total_cost, min_cost[node][parent])

data = input().split()
index = 0
T = int(data[index])
index += 1
results = []

for _ in range(T):
    N = int(data[index])
    M = int(data[index + 1])
    index += 2

    graph = [[] for _ in range(N + 1)]
    min_cost = [[float('inf')] * (N + 1) for _ in range(N + 1)]

    for _ in range(M):
        a = int(data[index])
        b = int(data[index + 1])
        c = int(data[index + 2])
        index += 3
        graph[a].append((b, c))
        graph[b].append((a, c))
        min_cost[a][b] = min_cost[b][a] = c

    result = 0
    for neighbor, cost in graph[1]:
        result += dfs(neighbor, 1)

    results.append(result)

for res in results:
    print(res)