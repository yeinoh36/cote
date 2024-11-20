import sys

data = map(int, sys.stdin.read().splitlines())

for num in data:
    one = 1
    while True:
        if one%num == 0:
            print(len(str(one)))
            break     
        one = one*10 + 1