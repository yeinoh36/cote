import sys
data = sys.stdin.read().splitlines()
line = data[0]
bomb = data[1]

answer = []
for word in line:
    answer.append(word)
    if len(answer) >= len(bomb) and "".join(answer[-len(bomb):]) == bomb:
        del answer[-len(bomb):]

if answer:
    print("".join(answer))
else:
    print("FRULA")