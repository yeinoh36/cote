import sys
from collections import deque

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    
    # Collect all non-zero cells up front
    nonzeros = [(i, j, grid[i][j])
                for i in range(N)
                for j in range(M)
                if grid[i][j] != 0]
    
    # A single visited array plus a stamp counter to avoid re-allocating on each BFS
    visited = [[0]*M for _ in range(N)]
    stamp = 1
    
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    best_dist = 0
    best_sum  = 0
    
    for si, sj, sval in nonzeros:
        max_dist = 0
        max_val  = sval
        
        dq = deque([(si, sj, 0)])
        visited[si][sj] = stamp
        
        while dq:
            x, y, d = dq.popleft()
            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M \
                   and visited[nx][ny] != stamp \
                   and grid[nx][ny] != 0:
                    
                    visited[nx][ny] = stamp
                    nd = d + 1
                    dq.append((nx, ny, nd))
                    
                    # Track farthest distance and, on ties, the largest room-value
                    if nd > max_dist:
                        max_dist = nd
                        max_val  = grid[nx][ny]
                    elif nd == max_dist and grid[nx][ny] > max_val:
                        max_val = grid[nx][ny]
        
        total = sval + max_val
        # Update global best: first by distance, then by sum
        if max_dist > best_dist or (max_dist == best_dist and total > best_sum):
            best_dist = max_dist
            best_sum  = total
        
        stamp += 1
    
    print(best_sum)

if __name__ == "__main__":
    main()