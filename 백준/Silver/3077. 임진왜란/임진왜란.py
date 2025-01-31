import sys
data = sys.stdin.read().splitlines()
N = int(data[0])
A = list(data[1].split())
B = list(data[2].split())

dictionary = {}
answer = 0
for a in range(len(A)):
    dictionary[A[a]] = set(A[a+1:])

from itertools import combinations
for comb in combinations(B, 2):
    if comb[1] in dictionary[comb[0]]:
        answer += 1

print(f"{answer}/{N*(N-1)//2}")