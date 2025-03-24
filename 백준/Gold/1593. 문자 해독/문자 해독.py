import sys
data = sys.stdin.read().splitlines()
g, s = map(int, data[0].split())
W = data[1].strip()
S = data[2].strip()

dictionary, tmp = {}, {}
for i in range(g):
    if W[i] not in dictionary:
        dictionary[W[i]] = 1
    else:
        dictionary[W[i]] += 1

    if S[i] not in tmp:
        tmp[S[i]] = 1
    else:
        tmp[S[i]] += 1

answer = 0
if dictionary == tmp:
    answer += 1

for i in range(s-g):
    if tmp[S[i]] == 1:
        del tmp[S[i]]
    else:
        tmp[S[i]] -= 1

    if S[i+g] not in tmp:
        tmp[S[i+g]] = 1
    else:
        tmp[S[i+g]] += 1

    if dictionary == tmp:
        answer += 1

print(answer)
        