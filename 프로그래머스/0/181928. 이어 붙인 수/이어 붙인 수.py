def solution(num_list):
    answer = 0
    odd = ''
    even = ''
    for i in num_list:
        if i%2:     # 홀수
            odd+=str(i)
        else:       # 짝수
            even+=str(i)
    answer = int(odd) + int(even)
    return answer