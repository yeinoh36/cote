def solution(a, b):
    # 2016년 1월 1일은 금요일이다.
    # 2016년은 윤년이다.
    
    answer = ''
    
    month = {
        1: 31,
        2: 29,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    
    result = {
        1: 'FRI',
        2: 'SAT',
        3: 'SUN',
        4: 'MON',
        5: 'TUE',
        6: 'WED',
        0: 'THU'
    }
    
    days = 0
    for i in range(1, a):
        print(i)
        days += month[i]
    days += b

    remains = days % 7 
    
    answer = result[remains]
    return answer