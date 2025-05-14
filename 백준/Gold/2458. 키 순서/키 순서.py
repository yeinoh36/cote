import sys
input = sys.stdin.readline
N, M = map(int, input().split())
ds = [list(map(int, input().split())) for _ in range(M)]

dictionary = {}
for i in range(1, N+1):
    dictionary[i] = [set(), set()]

for a, b in ds:
    dictionary[a][1].add((b))
    dictionary[b][0].add(a)

def visit(now, up):
    count = 0
    for i in dictionary[now][up]:
        if visited[i-1] == 0:
            tmp.append((i, up))
            visited[i-1] = 1
            count += 1
    return count

answer = 0
for i in range(1, N+1):
    count, tmp = 0, [(i, 0), (i, 1)]
    visited = [0] * (N)
    visited[i-1] = 1
    while tmp:
        now, up = tmp.pop()
        count += visit(now, up)
    if count == N-1:
        answer += 1

print(answer)


