"""
後ろから貪欲法

後ろから辿っていってXであればその数値の個数をカウントしていく
同様にEであれば、その数値とそれまでのXの数値の個数をカウントしていく
Mが来たらカウントした状態からmexを計算
"""

N = int(input())
A = list(map(int, input().split(" ")))[::-1]
S = input()[::-1]

X = [0, 0, 0]
E = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def mex(m, e, x):
    b = 0
    b |= 1 << m
    b |= 1 << e
    b |= 1 << x
    for i in range(4):
        if not b & 1 << i:
            return i


ans = 0
for i in range(N):
    c = S[i]
    if c == "X":
        X[A[i]] += 1
    elif c == "E":
        for j in range(3):
            E[A[i]][j] += X[j]
    else:
        for e in range(3):
            for x in range(3):
                ans += mex(A[i], e, x) * E[e][x]

print(ans)
