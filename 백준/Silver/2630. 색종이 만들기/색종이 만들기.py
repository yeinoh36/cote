import sys
data = sys.stdin.read().splitlines()
N = int(data[0])
paper = [list(map(int, row.split())) for row in data[1:1+N]]

while N > 1:
    N //= 2
    tmp = []
    
    for i in range(N):
        row = []
        for j in range(N):
            if isinstance(paper[2*i][2*j], list) or isinstance(paper[2*i+1][2*j], list) or isinstance(paper[2*i][2*j+1], list) or isinstance(paper[2*i+1][2*j+1], list):
                row.append([paper[2*i][2*j], paper[2*i+1][2*j], paper[2*i][2*j+1], paper[2*i+1][2*j+1]])
            elif paper[2*i][2*j] == paper[2*i+1][2*j] == paper[2*i][2*j+1] == paper[2*i+1][2*j+1] == 0:
                row.append(0)
            elif paper[2*i][2*j] == paper[2*i+1][2*j] == paper[2*i][2*j+1] == paper[2*i+1][2*j+1] == 1:
                row.append(1)
            else:
                row.append([paper[2*i][2*j], paper[2*i+1][2*j], paper[2*i][2*j+1], paper[2*i+1][2*j+1]])
        tmp.append(row)

    paper = tmp 

def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))  # 재귀 호출
        else:
            result.append(item)
    return result

flattened = flatten(paper)

print(flattened.count(0))
print(flattened.count(1))