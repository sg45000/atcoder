"""
0個のたこ焼きを買う場合の支払い金額と1個のたこ焼きを買う場合の支払い金額は自明
この支払い金額を配列ansで管理する
K >= 2 の場合、
ansの末尾の値より大きい支払い金額の中で最小のものをansに追加したい
N < 10なので、i番目のたこ焼きの金額 A[i]をansの各要素に対して足してみて、
ansの末尾の値より大きいければ、ansに追加する値の候補になる
それをN個のたこやき分計算すれば、ansに追加する値がわかる

配列ansは昇順に並んでいるので2分探索を用いることで計算量を減らすことができる

計算量はO(KNlogK)
"""

import bisect

N, K = list(map(int, input().split(" ")))
A = list(map(int, input().split(" ")))
A.sort()

ans = [0]
ans.append(A[0])
for _ in range(K - 1):
    min_next = float("inf")
    for i in range(N):
        v = bisect.bisect_left(ans, max(ans[-1] + 1 - A[i], 0))
        min_next = min(min_next, ans[v] + A[i])
    ans.append(min_next)

print(ans[-1])
