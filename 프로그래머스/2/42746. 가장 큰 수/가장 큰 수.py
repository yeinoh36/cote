def solution(numbers):
    answer = ''
    dictionary = []
    
    for number in numbers:
        temp = str(number) * 4
        n = len(str(number))
        dictionary.append([temp[:4], n])
        
    dictionary = sorted(dictionary, reverse=True)
    
    for number, n in dictionary:
        answer += (number[:n])
    
    if int(answer) == 0:
        answer = "0"
    return answer