# 명령문의 갯수
n = int(input())

# 명령문 받기
commands = []
for _ in range(n):
    commands.append(input().split())

# 스택 
stack = []

for i in range(len(commands)):
    
    if commands[i][0] == "push":
        stack.append(int(commands[i][1]))
    
    if commands[i][0] == "pop":
        if stack:
            pop = stack.pop()
            print(pop)
        else: print(-1)

    if commands[i][0] == "size":
        print(len(stack))
    
    if commands[i][0] == "empty":
        if stack:
            print(0)
        else: print(1)
            
    if commands[i][0] == "top":
        if stack:
            print(stack[-1])
        else: print(-1)

