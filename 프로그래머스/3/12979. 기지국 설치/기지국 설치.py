def solution(n, stations, w):
    answer = 0
    pos, sta = 1, 0
    coverage = 2 * w + 1

    while pos <= n:
        # 기지국이 범위 내인 경우
        if sta < len(stations) and pos >= stations[sta] - w:
            pos = stations[sta] + w + 1
            sta += 1 
        # 기지국을 설치해야 하는 경우
        else:
            answer += 1
            pos += coverage

    return answer