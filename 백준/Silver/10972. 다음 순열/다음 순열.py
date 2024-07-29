n = int(input())
nlist = list(map(int, input().split()))

i = len(nlist) -2
while i >= 0 and nlist[i] > nlist[i+1]:
    i -= 1
    
if i == -1:
    print(-1)
    
else:
    j = len(nlist) -1
    while nlist[j] <= nlist[i]:
        j -= 1

    nlist[i], nlist[j] = nlist[j], nlist[i]
    nlist[i+1:] = reversed(nlist[i+1:])
    
    for answernum in nlist:
        print(answernum)