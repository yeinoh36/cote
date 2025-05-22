def solution(arr):
    stk = []
    i = 0
    while len(arr) > i:
        if not(stk):
            stk.append(arr[i])
            i += 1
        elif stk[-1] < arr[i]:
                stk.append(arr[i])
                i += 1
        else:
            stk.pop()
    return stk