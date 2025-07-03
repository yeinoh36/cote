def solution(msg):
    answer = []
    dictionary = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
    s, e, n = 0, len(msg)-1, len(dictionary)+1
    while s <= len(msg)-1:
        if msg[s:e+1] in dictionary:
            answer.append(dictionary[msg[s:e+1]])
            if e+2 < len(msg):
                dictionary[msg[s:e+2]] = n
                n += 1
            s = e+1
            e = len(msg)-1
        else: e -= 1
    return answer