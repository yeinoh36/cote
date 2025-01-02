string = input()

dictionary = {
    "q": 1,
    "u": 2,
    "a": 3,
    "c": 4,
    "k": 5
}

answer = 0
tmps = []

for char in string:
    num = dictionary.get(char, 0)
    if num == 0:
        print(-1)  # 잘못된 문자
        exit()
    
    if num == 1:  # q
        tmps.append(1)
        answer = max(answer, len(tmps))
    else:  # uack
        found = False
        for i in range(len(tmps)):
            if tmps[i] == num - 1:
                tmps[i] = num
                if num == 5:  # k
                    tmps.pop(i)
                found = True
                break
        if not found:  # 잘못된 문자
            print(-1)
            exit()

if tmps:
    print(-1)
else:
    print(answer)