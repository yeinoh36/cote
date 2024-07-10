def solution(genres, plays):
    # 장르 큰
    # 재생 큰
    # 고유번호 작은
    answer = []
    play_gen = {}
    genre_song_list = {}

    for i, genre in enumerate(genres):
        if genre in play_gen:
            play_gen[genre] += plays[i]
            genre_song_list[genre].append((plays[i], i))
        else:
            play_gen[genre] = plays[i]
            genre_song_list[genre] = [(plays[i], i)]


    sorted_play_gen=sorted(list(play_gen.items()), key=lambda x: x[1], reverse=True)
    print(genre_song_list)

    for genre in sorted_play_gen:
        st = sorted(genre_song_list[genre[0]], key=lambda x:x[0], reverse = True)
        if len(st) >= 2:
            answer.append(st[0][1])
            answer.append(st[1][1])
        else:
            answer.append(st[0][1])
    return answer