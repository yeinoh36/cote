def solution(answers):
    answer = []
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    scores = []
    scores.append(calculate(answers, one))
    scores.append(calculate(answers, two))
    scores.append(calculate(answers, three))
    
    best = max(scores)

    for i, score in enumerate(scores):
        if score == best:
            answer.append(i+1)
            
    return answer

def calculate(answer, who):
    score = 0
    for i, ans in enumerate(answer):
        if ans == who[i%(len(who))]:
            score += 1
            
    return score