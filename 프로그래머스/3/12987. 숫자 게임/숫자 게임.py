from collections import deque
def solution(A, B):
    answer = 0
    A = deque(sorted(A, reverse = True))
    B = deque(sorted(B, reverse = True))
    
    while A and B:
        if A[0] < B[0]:
            A.popleft()
            B.popleft()
            answer += 1         
        else:
            A.popleft()
            B.pop()    
    return answer