def solution(s):
    answer = True
    opclo = 0
    
    if len(s) % 2 != 0:
        return False
    
    for i, x in enumerate(s):
        # 시작과 종료 조건
        if i == 0 and x == ')':
            return False

        if i == (len(s)-1) and x == '(':
            return False
            
        # 괄호 짝짓기
        if x == '(':
            opclo += 1
        elif x == ')':
            opclo -= 1
        
        # 열린 것 없이 닫으면
        if opclo < 0:
            return False
    
    if opclo != 0:
        answer = False
        
    return answer