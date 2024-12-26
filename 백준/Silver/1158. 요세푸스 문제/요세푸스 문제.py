N, M = map(int, input().split())

nums = list(range(1, N + 1))
answer = []
index = 0

for _ in range(N):
    index = (index + M - 1) % len(nums)
    answer.append(nums.pop(index))

print("<" + ", ".join(map(str, answer)) + ">")