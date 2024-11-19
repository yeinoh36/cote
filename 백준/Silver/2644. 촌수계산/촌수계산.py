import sys

# 입력받기
data = sys.stdin.read().splitlines()
n = int(data[0])
one, two = map(int, data[1].split())
visited = [0]*int(data[2])
relations = [list(map(int, x.split())) for x in data[3:]]

# 변수 초기화
answer = -1
stack = []
stack.append([one, 0])

# bfs 탐색
while stack:
    x = stack.pop()
    who, chon = x[0], x[1]
    
    if who == two:
        answer = x[1]
        break
    
    for i, relation in enumerate(relations):
        if who in relation and visited[i] == 0:
            for a in relation:
                if a != who:
                    whonext = a
            stack.append([whonext, chon+1])
            visited[i] = 1

print(answer)