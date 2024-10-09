from collections import deque

def solution(progresses, speeds):
    answer = []
    dates = deque()
    
    for i, progress in enumerate(progresses):
        if (100-progress)%speeds[i]:
            dates.append((100-progress)//speeds[i] +1)
        else:
            dates.append((100-progress)//speeds[i])

    maxtime, num = dates[0], 0
    for date in dates:
        if date > maxtime:
            answer.append(num)
            num = 1
            maxtime = date
        else:
            num += 1
            maxtime = max(maxtime, date)
    
    if num:
        answer.append(num)
            
    return answer