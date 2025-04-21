from collections import deque
def solution(gems):
    
    # 진열된 모든 종류의 보석을 적어도 1개 이상 포함하는 가장 짧은 구간을 찾아서 구매
    answer = []
    num = len(set(gems)) # gem 종류
    s, sg = 1, gems[0]
    e, eg = 1, gems[0]
    # 'DIA': [1, 4, 5, 8], ... / 보석의 종류 수 / 작업 큐
    gem_dict, g_kind, que = {}, 0, deque()
    
    for i, gem in enumerate(gems):
        que.append(gem)
        e, eg = i+1, gem
        
        # 이전에 없던 보석의 등장
        if gem not in gem_dict:
            gem_dict[gem] = 1
            g_kind += 1
        
        # 이미 존재한 보석의 등장
        else:
            gem_dict[gem] += 1
            # 만약 시작 보석과 추가된 보석이 같다면
            # 시작 보석을 빼고 새로운 시작 보석이 적합한지 확인하기
            if sg == gem:
                while True:
                    gem_dict[sg] = gem_dict[sg]-1
                    que.popleft()
                    s += 1
                    sg = que[0]
                    if len(que) < 2 or gem_dict[sg] == 1:
                        break
        
        # 보석 종류 조건을 만족했다면 길이를 비교하며 정답 교체하기
        if g_kind == num:
            if not answer:
                answer = [s, e]
            elif answer[1]-answer[0] > e-s:
                answer = [s, e]
        
    return answer