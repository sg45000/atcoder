"""
LIS 最長増加部分列を数列の両側から求める
"""

import bisect

N = int(input())
A = list(map(int, input().split(" ")))

ASC_LIS = []  # LISテーブル index: 単調増加部分列の長さ, value: 部分列の末尾の数値で最小になり得る値
ASC_L = [0] * N  # index: 数列Aの何個目までの列を使うか, value: 単調増加部分列の長さ

for i in range(N):
    cnt = bisect.bisect_left(ASC_LIS, A[i])  # bisect_leftは同じ値を見つけた時に一番左にある値のインデックスを返す
    if len(ASC_LIS) == cnt:
        ASC_LIS.append(A[i])
    else:
        ASC_LIS[cnt] = A[i]
    ASC_L[i] = cnt + 1

DESC_LIS = []
DESC_L = [0] * N
DESC_A = A[::-1]
for i in range(N):
    cnt = bisect.bisect_left(DESC_LIS, DESC_A[i])
    if len(DESC_LIS) == cnt:
        DESC_LIS.append(DESC_A[i])
    else:
        DESC_LIS[cnt] = DESC_A[i]
    DESC_L[i] = cnt + 1

ans = 0
for i in range(N):  # 各要素を山の頂上にした時の部分列の長さ
    ans = max(ans, ASC_L[i] + DESC_L[N - i - 1])

print(ans - 1)
