n = int(input())
nlist = list(map(int, input().split()))
answer = 0

from itertools import permutations
result = list(permutations(nlist))

def difference(set):
    sum = 0
    for i in range(0, len(set)-1, 1):
        sum += abs(set[i] - set[i+1])
    return sum

for set in result:
    if answer < difference(set):
        answer = difference(set)
        
print(answer)