from collections import deque

# 명령문의 갯수
n = int(input())

# 명령문 받기
commands = []
for _ in range(n):
    commands.append(input().split())

# 덱 
deq = deque()

for i in range(len(commands)):
    
    if commands[i][0] == "push_front":
        deq.appendleft(int(commands[i][1]))
    
    if commands[i][0] == "push_back":
        deq.append(int(commands[i][1]))
    
    if commands[i][0] == "pop_front":
        if deq:
            pop = deq.popleft()
            print(pop)
        else: print(-1)
            
    if commands[i][0] == "pop_back":
        if deq:
            pop = deq.pop()
            print(pop)
        else: print(-1)

    if commands[i][0] == "size":
        print(len(deq))
    
    if commands[i][0] == "empty":
        if deq:
            print(0)
        else: print(1)
            
    if commands[i][0] == "front":
        if deq:
            print(deq[0])
        else: print(-1)
            
    if commands[i][0] == "back":
        if deq:
            print(deq[-1])
        else: print(-1)