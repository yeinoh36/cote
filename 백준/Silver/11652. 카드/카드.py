from collections import deque

n = int(input())

cards={}

for _ in range(n):
    new = int(input())
    if new not in cards:
        cards[new] = 1
    else:
        cards[new] += 1
        
max_c = max(cards.values())
max_e = deque()

for num, count in cards.items():
    if count == max_c:
        max_e.append(num)

print(min(max_e))