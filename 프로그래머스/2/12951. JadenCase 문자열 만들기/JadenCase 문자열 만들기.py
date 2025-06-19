def solution(string):
    answer = ''
    blank = True
    for s in string:
        if s == ' ':
            answer += s
            blank = True
            continue
        
        s = ord(s)
        if blank: 
            blank = False
            if s>=97:
                s -= 32
                
        elif not blank and 65<=s<=90:
            s += 32
            
        answer += chr(s)        
    return answer