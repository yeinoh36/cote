from collections import deque

# 명령문의 갯수
n = int(input())

# 명령문 받기
commands = []
for _ in range(n):
    commands.append(input().split())

# 큐 
que = deque()

for i in range(len(commands)):
    
    if commands[i][0] == "push":
        que.append(int(commands[i][1]))
    
    if commands[i][0] == "pop":
        if que:
            pop = que.popleft()
            print(pop)
        else: print(-1)

    if commands[i][0] == "size":
        print(len(que))
    
    if commands[i][0] == "empty":
        if que:
            print(0)
        else: print(1)
            
    if commands[i][0] == "front":
        if que:
            print(que[0])
        else: print(-1)
            
    if commands[i][0] == "back":
        if que:
            print(que[-1])
        else: print(-1)