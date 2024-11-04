def solution(number, k):
    answer = ''
    stack = []
    
    for num in number:
        # 최적의 내림차순 유지하며 stack에 추가
        while k > 0 and stack and stack[-1]<num:
            stack.pop()
            k -= 1
        
        stack.append(num)
    
    # 더 지울 수 있는 경우
    if k:
        stack = stack[:-k]
        
    answer += ''.join(stack)
    return answer
