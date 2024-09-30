def solution(name):
    # 정답, 변환 숫자 초기화
    answer, num = -1, -1
    
    num0 = []
    
    k = len(name)
    leftnright = k-1 # 좌우
    upndown = 0 # 상하
    
    # 사전 만들기
    apb_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}
    
    for i, alphabet in enumerate(name):
        numbf = num # 이전 숫자를 담는 변수
        
        # 알파벳에 해당하는 숫자 뽑기
        num = apb_dict[alphabet]
        
        # 역순으로 이동할 때와 비교
        num = min(num, abs(26-num))
        
        upndown += num
        
        # 0의 시작 인덱스, 끝 인덱스 --> num0에 추가
        if numbf != 0 and num == 0 :
            x = i
        elif numbf == 0 and num != 0 :
            y = i-1
            num0.append([x,y])
            
    # 마지막이 0으로 끝난 경우, num0 추가    
    if num == 0 :
        if numbf != 0:
            x = k-1
        y = k-1
        num0.append([x, y])
    
    # 각 경우의 수 계산
    for x, y in num0:
        if x == 0 and y != k-1 :
            leftnright = min(leftnright, k-y-1)
        elif x != 0 and y == k-1 :
            leftnright = min(leftnright, x-1)
        elif x == 0 and y == k-1 :
            leftnright = min(leftnright, 0)
        else:
            leftnright = min(leftnright, k+2*x-y-3, 2*k+x-2*y-3)
            
    answer = upndown + leftnright
    
    return answer