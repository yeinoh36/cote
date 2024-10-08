""" DFS
1. 탐색 시작 노드를 스택에 삽입하고 방문 처리한다.
2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리를 한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.
"""

def solution(n, computers):
    answer = 0
    # stack 초기화
    stack = []
    # 방문 처리 초기화
    visited = [0] * n
    
    for start in range(n):
        # 방문한 적 있으면 pass
        if visited[start]:
            continue
        
        # 방문한 적이 없다면 link 시작
        answer += 1
        stack.append(start)
        
        while stack:
            # 최상단 노드에 인접한 노드 추가
            top = stack[-1]
            append_TF = False
            for i, TF in enumerate(computers[top]):
                if TF and not(visited[i]):
                    append_TF = True
                    stack.append(i)
                    visited[i] = 1
            # 추가되지 않았다면 최상단 노드 제거
            if not(append_TF):
                stack.pop()

    return answer