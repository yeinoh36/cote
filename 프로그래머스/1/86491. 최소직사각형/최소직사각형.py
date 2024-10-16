def solution(sizes):
    max_w = 0
    max_h = 0
    
    for size in sizes:
        w, h = sorted(size)  # 가로, 세로 중 큰 값과 작은 값을 정렬
        max_w = max(max_w, w)  # 큰 값을 가로에 대응
        max_h = max(max_h, h)  # 작은 값을 세로에 대응
        
    return max_w * max_h