n = int(input())
nlist = []

for _ in range(n):
    nlist.append(int(input()))
    
nlist.sort()
for num in nlist:
    print(num)