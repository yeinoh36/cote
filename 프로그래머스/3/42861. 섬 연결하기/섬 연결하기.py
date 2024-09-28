from copy import deepcopy

def all_linked(n, wires, removed):
    
    # 초기화
    one = set()
    two = set()
    wires_copy = deepcopy(wires)

    # 끊어진 전선의 정보
    one.add(removed[0])
    two.add(removed[1])

    # 전선 그룹 분류
    while wires_copy:
        wire = wires_copy[0]

        if wire == removed:
            wires_copy.remove(wire)
            continue

        if wire[0] in one:
            wires_copy.remove(wire)
            one.add(wire[1])

        elif wire[1] in one:
            wires_copy.remove(wire)
            one.add(wire[0])

        elif wire[0] in two:
            wires_copy.remove(wire)
            two.add(wire[1])

        elif wire[1] in two:
            wires_copy.remove(wire)
            two.add(wire[0])

        else:
            wires_copy.remove(wire)
            wires_copy.append(wire)
        
    return len(one & two) > 0

def solution(n, costs):
    answer = 0
    
    costs = sorted(costs, reverse=True, key=lambda x: x[2])
    #print("sorted: ", costs)
    costs_copy = deepcopy(costs)
    
    
    for cost in costs_copy:
        answer += cost[2]
        #print(cost)
        if all_linked(n, costs, cost):
            #print("true")
            costs.remove(cost)
            answer -= cost[2]
            #print("answer: ", answer)
        #else:
            #print("false")
            #print("answer: ", answer)
    
    return answer