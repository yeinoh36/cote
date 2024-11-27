import sys
data = sys.stdin.read().splitlines()
scores = [line.split() for line in data]

scoredict = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
}

mom, son = 0, 0
for score in scores:
    credit = float(score[1])
    grade = score[2]

    if grade == "P":
        continue

    mom += credit
    son += credit * scoredict[grade]

print(son / mom)