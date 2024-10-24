def solution(num_list):
    answer = 0
    multi = 1
    plus = 0
    for i in num_list:
        plus += i
        multi *= i
    
    if multi < (plus)**2:
        answer = 1
    return answer