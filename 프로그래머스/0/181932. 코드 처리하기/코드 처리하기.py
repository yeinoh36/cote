def solution(code):
    answer = ''
    mode = 0
    
    for i, n in enumerate(code):
        if n == '1':  # n이 '1'일 때 mode를 전환
            mode = abs(mode - 1)
            continue  # 다음 루프로 넘어감
        if mode:  # mode가 1일 때
            if i % 2 == 1:  # 인덱스가 홀수인 경우
                answer += n
        else:  # mode가 0일 때
            if i % 2 == 0:  # 인덱스가 짝수인 경우
                answer += n
    if not(answer):
        answer = 'EMPTY'
    
    return answer