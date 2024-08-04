# 입력 받기
anum = int(input())
alist = set(map(int, input().split()))  # 리스트를 집합으로 변환하여 중복 제거 및 빠른 검색

mnum = int(input())
mlist = list(map(int, input().split()))

# 각 요소가 집합에 존재하는지 확인
for m in mlist:
    if m in alist:
        print(1)
    else:
        print(0)
