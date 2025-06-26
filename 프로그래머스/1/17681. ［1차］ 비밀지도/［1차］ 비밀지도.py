def solution(n, arr1, arr2):
    answer, wall1, wall2 = [], 0, 0
    for i in range(n):
        wall1, wall2 = bin(arr1[i])[2:].zfill(n), bin(arr2[i])[2:].zfill(n)
        tmp = ""
        for j in range(n):
            if wall1[j] == '1' or wall2[j] == '1':
                tmp += ("#")
            else: tmp += (" ")
        answer.append(tmp)
            
    return answer