def solution(phone_book):
    answer = True

    phone_book.sort()
    before = phone_book[0]
    
    for i in range(1, len(phone_book)):
        if phone_book[i].startswith(before):
            answer = False
            break
        else:
            before = phone_book[i]
            
    return answer