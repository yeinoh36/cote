from collections import deque
def solution(gems):
    
    answer = []
    num = len(set(gems)) # gem 종류
    s, sg = 1, gems[0]
    e, eg = 1, gems[0]
    # 작업 큐 / 보석의 종류별 개수 dict / 보석의 종류 수 int 
    que, gem_dict, g_kind  = deque(), {}, 0
    
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
            if sg == gem:
                while True:
                    # 시작 보석 제거
                    gem_dict[sg] = gem_dict[sg]-1
                    que.popleft()
                    # 새로운 시작 보석 업데이트
                    s += 1
                    sg = que[0]
                    # 해당 보석이 
                    if len(que) < 2 or gem_dict[sg] == 1:
                        break
        
        # 보석 종류 조건을 만족했다면 길이를 비교하며 정답 교체하기
        if g_kind == num:
            if not answer:
                answer = [s, e]
            elif answer[1]-answer[0] > e-s:
                answer = [s, e]
        
    return answer
