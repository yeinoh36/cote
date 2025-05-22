def solution(places):
    answer = []
    direct_1 = [(1,0), (-1, 0), (0, 1), (0, -1)]
    direct_2_straight = [(2,0), (-2,0), (0,2), (0,-2)]
    direct_2_diag = [(1,1), (1,-1), (-1,1), (-1,-1)]

    for lines in places:
        safe = 1
        for i in range(5):
            for j in range(5):
                if lines[i][j] != 'P':
                    continue

                for dx, dy in direct_1:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < 5 and 0 <= nj < 5 and lines[ni][nj] == 'P':
                        safe = 0
                        break
                if not safe:
                    break

                for dx, dy in direct_2_straight:
                    ni, nj = i + dx, j + dy
                    mi, mj = i + dx//2, j + dy//2
                    if 0 <= ni < 5 and 0 <= nj < 5 and lines[ni][nj] == 'P':
                        if lines[mi][mj] != 'X':
                            safe = 0
                            break
                if not safe:
                    break

                for dx, dy in direct_2_diag:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < 5 and 0 <= nj < 5 and lines[ni][nj] == 'P':
                        if lines[i][nj] != 'X' or lines[ni][j] != 'X':
                            safe = 0
                            break
            if not safe:
                break
        answer.append(safe)
    return answer