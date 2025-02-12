from itertools import product

def solution(users, emoticons):
    answer = [0, 0]
    prods = product(range(1,5), repeat=len(emoticons))
    
    for prod in prods:
        sums = [0]*len(users)
        one, two = 0, 0
        for i, p in enumerate(prod):
            price = int(emoticons[i]*(10-p)/10)
            for j, user in enumerate(users):
                if user[0] > p*10:
                    continue
                sums[j] += price

        for i, sum in enumerate(sums):
            if sum >= users[i][1]:
                one += 1
            else:
                two += sum
        
        if one > answer[0] or (one == answer[0] and two > answer[1]):
            answer = [one, two]
            
    return answer