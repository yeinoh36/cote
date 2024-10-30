def solution(triangle):
    answer = 0
    sumlist = [[0]*(i+1) for i in range(len(triangle))]
    sumlist[0][0] = triangle[0][0]
    for i in range(len(triangle)-1):
        for j, num in enumerate(triangle[i]):
            pre = sumlist[i][j]
            former = pre + triangle[i+1][j]
            latter = pre + triangle[i+1][j+1]
            
            sumlist[i+1][j] = max(sumlist[i+1][j], former)
            sumlist[i+1][j+1] = max(sumlist[i+1][j+1], latter)

    answer = max(sumlist[-1])
    return answer