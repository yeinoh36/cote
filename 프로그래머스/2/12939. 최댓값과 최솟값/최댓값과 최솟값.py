def solution(s):
    answer = ''
    small = int(s.split()[0])
    big = int(s.split()[0])
    for n in map(int, s.split()[1:]):
        small = min(small, n)
        big = max(big, n)
    answer = str(small) + " " + str(big)
    return answer