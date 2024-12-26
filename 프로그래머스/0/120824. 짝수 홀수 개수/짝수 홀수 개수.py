def solution(num_list):
    answer = []
    zero, one = 0, 0
    
    for num in num_list:
        if num%2 == 0:
            zero += 1
        else:
            one += 1
            
    answer.append(zero)
    answer.append(one)
    
    return answer