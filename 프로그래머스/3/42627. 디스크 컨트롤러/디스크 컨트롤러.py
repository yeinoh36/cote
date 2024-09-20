import heapq

def solution(jobs):
    answer = 0
    time = 0
    n = len(jobs)
    
    #print("정렬 전: ", jobs)
    heapq.heapify(jobs)
    #print("정렬 후: ", jobs)
    ready = []
    
    
    while jobs or ready:
        if ready:
            #print("ready")
            cur = heapq.heappop(ready)
            answer += (time)
            time += cur
            #print("time: ", time)
        else:
            #print("not ready")
            work = heapq.heappop(jobs)
            answer -= work[0]
            answer += work[1]
            time = work[0]
            heapq.heappush(ready, work[1])
            #print("work: ", work, ", time: ", time)
        
        if jobs:
            jobs_copy = sorted(jobs.copy())
            #print("left: ", jobs_copy)
            for req, _ in jobs_copy:
                #print("time: ", time, ", req: ", req)
                if req <= time:
                    work = heapq.heappop(jobs)
                    #print("work: ", work)
                    answer -= work[0]
                    answer += work[1]
                    heapq.heappush(ready, work[1])
                    #print("+ ready: ", ready)
                else:
                    #print("break")
                    break

    return answer // n