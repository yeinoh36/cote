def solution(storey):
    answer = 0
    
    while storey:
        i = storey % 10
        j = (storey // 10) % 10
        
        if i < 5:
            answer += i
        elif i > 5:
            answer += (10 - i) 
            storey += 10 
        else:
            if j >= 5:
                storey += 10
            answer += 5

        storey //= 10

    return answer
