num = int(input())
answer = -1

def bhh(n):
    return n + sum(int(d) for d in str(n))

start = max(1, num - 9 * len(str(num)))  # 최소값은 1, 최대값은 num - 9 * 자릿수

for what in range(start, num):
    if bhh(what) == num:
        answer = what
        break

if answer != -1:
    print(answer)
else:
    print(0)
