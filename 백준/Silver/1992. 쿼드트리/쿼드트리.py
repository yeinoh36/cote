import sys
data = sys.stdin.read().splitlines()
N = int(data[0])
grid = [list(map(int, list(row))) for row in data[1:]] 

while N > 1:
    N //= 2
    ngrid = []
    for i in range(N):
        tmp = []
        for j in range(N):
            x, y = 2*j, 2*i
            if grid[y][x] == grid[y+1][x] == grid[y][x+1] == grid[y+1][x+1] == 1:
                tmp.append(1)
            elif grid[y][x] == grid[y+1][x] == grid[y][x+1] == grid[y+1][x+1] == 0:
                tmp.append(0)
            else:
                tmp.append(f"({grid[y][x]}{grid[y][x+1]}{grid[y+1][x]}{grid[y+1][x+1]})")
        ngrid.append(tmp)
    grid = ngrid
answer = grid[0][0]
print(answer)