from collections import Counter
import bisect

tnum = int(input())

for _ in range(tnum):
    answer = 0
    _ = input()

    acounts = Counter(map(int, input().split()))
    bcounts = Counter(map(int, input().split()))
    
    cul_counts = []
    cul_sum = 0
    sorted_b = sorted(bcounts.keys())
    for b in sorted_b:
        cul_sum += bcounts[b]
        cul_counts.append(cul_sum)
    
    for a in acounts:
        pos = bisect.bisect_left(sorted_b, a)
        
        if pos > 0:
            answer += acounts[a]*cul_counts[pos-1]
            
    print(answer)