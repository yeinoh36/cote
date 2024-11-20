import sys

data = sys.stdin.read().splitlines()
A, B, C = map(int,data[0].split())

print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)