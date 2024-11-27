def solution(arr, queries):
    for query in queries:
        n, m = query[0], query[1]
        arr[n], arr[m] = arr[m], arr[n]
    return arr