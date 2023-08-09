"""
いもす
"""
N = int(input())
P = [list(map(int, input().split(" "))) for _ in range(N)]

s = [[0] * 1001 for _ in range(1001)]

for lx, ly, rx, ry in P:
    # 入口と出口を記録
    s[lx][ly] += 1  # 左下
    s[lx][ry] -= 1  # 左上
    s[rx][ly] -= 1  # 右下
    s[rx][ry] += 1  # 右上

for i in range(1000):
    for j in range(1000):
        s[i][j + 1] += s[i][j]

for j in range(1000):
    for i in range(1000):
        s[i + 1][j] += s[i][j]

answer = [0] * (N + 1)

for i in range(1000):
    for j in range(1000):
        if s[i][j] > 0:
            answer[s[i][j]] += 1

for a in answer[1:]:
    print(a)