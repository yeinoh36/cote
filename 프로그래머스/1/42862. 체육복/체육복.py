from collections import Counter, deque
def solution(n, lost, reserve):
    answer = n - len(lost)
    
    # 1 자기자신 빼기
    for who in lost[:]:
        if who in reserve:
            reserve.remove(who)
            lost.remove(who)
            answer += 1
            
    while lost:

        for who in lost[:]:
            former = who-1
            latter = who+1
            
            # 2 구제불가 lost 제거하기
            if not(former > 0 and former in reserve) and not(latter < n+1 and latter in reserve):
                lost.remove(who)
                
            # 3 유일구제 lost 구제하기
            elif (former > 0 and former in reserve) and not(latter < n+1 and latter in reserve):
                answer += 1
                reserve.remove(former)
                lost.remove(who)

            elif (latter < n+1 and latter in reserve) and not(former > 0 and former in reserve):
                answer += 1
                reserve.remove(latter)
                lost.remove(who)
                continue

        for who in reserve[:]:
            former = who-1
            latter = who+1
            
            # 유일무이 reserve 나눔하기
            if (former > 0 and former in lost) and not(latter < n+1 and latter in lost):
                answer += 1
                reserve.remove(who)
                lost.remove(former)

            elif (latter < n+1 and latter in lost) and not(former > 0 and former in lost):
                answer += 1
                reserve.remove(who)
                lost.remove(latter)
            
    return answer