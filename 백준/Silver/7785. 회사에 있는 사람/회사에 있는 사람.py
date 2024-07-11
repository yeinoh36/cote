n = int(input())

lst = []
for _ in range(n):
    lst.append(input().split())
    
hash = {}

for lg in lst:
    if lg[1]=="enter":
        hash[lg[0]] = 1

    elif lg[1]=="leave":
        hash[lg[0]] = 0

enter = []

for key, value in hash.items():
    if value == 1:
        enter.append(key)

enter.sort(reverse = True)

for name in enter:
    print(name)
