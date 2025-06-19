def solution(cards):
    answer = []
    visited = [0]*len(cards)
    for i in range(len(cards)):
        if visited[i]==0:
            visited[i] = 1
            now, num = i, 1
            while True:
                now = cards[now]-1
                if visited[now] == 0:
                    visited[now] = 1
                    num += 1
                else: break
            if num == len(cards):
                return 0
            answer.append(num)
    answer = sorted(answer)
    return answer[-1]*answer[-2]