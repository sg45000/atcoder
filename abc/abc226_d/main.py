"""
傾きの種類数
"""

N = int(input())
XY = [list(map(int, input().split(" "))) for _ in range(N)]

s = set()
for x1, y1 in XY:
    for x2, y2 in XY:
        if x1 == x2 and y1 == y2:
            continue
        if x1 == x2:
            s.add(0)
        elif y1 == y2:
            s.add(10 ** 10)
        else:
            a = (y1 - y2) / (x1 - x2)
            s.add(a)

print(len(s) * 2)