from itertools import product

def solution(word):
    answer = 0
    alphabet = ['A', 'E', 'I', 'O', 'U']
    dictionary = []
    
    # 튜플을 문자열로 변환하여 추가
    for i in range(1, 6):
        dictionary.extend(product(alphabet, repeat = i))

    # 변환된 리스트 정렬
    dictionary = sorted(dictionary)
    dictionary = [''.join(tup) for tup in dictionary]
    
    for i, w in enumerate(dictionary):
        if w == word:
            answer = i+1
            break
    
    return answer
