def solution(k, dungeons):
    answer = [0]
    visited = [0]
    tempdgs = dungeons.copy()

    for dungeon in tempdgs[:]:
        explore(dungeons, tempdgs, dungeon, k, visited, answer)
    
    return answer[0]

def explore(dungeons, tempdgs, dungeon, k, visited, answer):
    if k >= dungeon[0]:
        visited[0] += 1
        k -= dungeon[1]
        tempdgs.remove(dungeon)
        for next in tempdgs[:]:
            explore(dungeons, tempdgs, next, k, visited, answer)

        if answer[0] < visited[0]:
            answer[0] = visited[0]
        
        visited[0] -= 1
        tempdgs.append(dungeon)
    
    else:
        if answer[0] < visited[0]:
            answer[0] = visited[0]

    return answer[0]
        
        