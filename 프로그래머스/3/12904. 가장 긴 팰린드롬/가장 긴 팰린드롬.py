def solution(s):
    def expand(left, right):
        # 위치 조건 & 대칭 조건 확인
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    answer = 0

    for i in range(len(s)):
        # 홀수
        odd_len = expand(i, i)
        
        # 짝수
        even_len = expand(i, i + 1)
        
        # 최대 길이 갱신
        answer = max(answer, odd_len, even_len)

    return answer