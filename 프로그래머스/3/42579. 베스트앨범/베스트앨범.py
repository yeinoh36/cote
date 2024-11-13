def solution(genres, plays):
    answer = []
    gen_sum = {}
    gen_plays = {}
    
    # 장르별 합 구하기
    for i in range(len(plays)):
        genre = genres[i]
        play = plays[i]
        if genre not in gen_sum.keys():
            gen_sum[genre] = play
            gen_plays[genre] = []
            gen_plays[genre].append([play, i])
        else:
            gen_sum[genre] += play
            gen_plays[genre].append([play, i])
    
    # 장르 순으로 두곡씩 수록하기
    for gen, total in sorted(gen_sum.items(), key=lambda x: x[1], reverse=True):
        tmp = sorted(gen_plays[gen], key=lambda x: x[0], reverse=True)
        if len(tmp) == 1:
            answer.append(tmp[0][1])
            continue
        
        answer.append(tmp[0][1])
        answer.append(tmp[1][1])
    
    return answer