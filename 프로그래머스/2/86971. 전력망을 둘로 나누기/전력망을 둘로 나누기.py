def solution(n, wires):
    answer = n
    
    for i in range(n-1):
        # 초기화
        one = []
        two = []
        wires_copy = wires.copy()
        
        # 끊어진 전선의 정보
        one.append(wires[i][0])
        two.append(wires[i][1])
        
        while wires_copy:
            wire = wires_copy[0]
            
            if wire == wires[i]:
                wires_copy.remove(wire)
                continue
                
            if wire[0] in one:
                wires_copy.remove(wire)
                one.append(wire[1])

            elif wire[1] in one:
                wires_copy.remove(wire)
                one.append(wire[0])

            elif wire[0] in two:
                wires_copy.remove(wire)
                two.append(wire[1])

            elif wire[1] in two:
                wires_copy.remove(wire)
                two.append(wire[0])

            else:
                wires_copy.remove(wire)
                wires_copy.append(wire)
        
        diff = abs(len(one) - len(two))
        answer = min(answer, diff)
    
    return answer