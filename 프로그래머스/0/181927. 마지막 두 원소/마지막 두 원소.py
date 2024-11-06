def solution(num_list):
    answer = num_list
    min1 = num_list[-1]
    min2 = num_list[-2]
    
    if min1 > min2:
        answer.append(min1-min2)
    else:
        answer.append(2*min1)
    
    return answer