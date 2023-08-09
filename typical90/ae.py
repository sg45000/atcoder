from functools import reduce
from operator import xor

N = int(input())
W = list(map(int, input().split(" ")))
B = list(map(int, input().split(" ")))

grundy = [0] * N

# 集合sの範囲外で最小の整数
def mex(s):
    if len(s) == 0:
        return 0
    m = min(s)
    return m - 1 if m > 0 else 1

for n in range(N):
    w = W[n]
    b = B[n]
    g = [[0] * ((w * (w + 1) // 2) + b + 1) for _ in range(w + 1)]  # g[白石個数][青石個数] = grundy数
    for i in range(w + 1):  # wのインデックス
        start = (w - i) * (w - i + 1) // 2  # ここが怪しい
        for j in range(start, start + b + 1):  # bのインデックス
            s = set()
            if i >= 1:
                s.add(g[i - 1][i + j])
            if j >= 2:
                for k in range(1, j // 2 + 1):
                    s.add(g[i][j - k])
            g[i][j] = mex(s)

    grundy[n] = g[-1][-1]   # ここが怪しい

for n in range(N):
    reduce(xor, grundy)
    grundy[n] ^ grundy[n + 1] > 0
print("First") if answer else print("Second")