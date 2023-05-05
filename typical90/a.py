# # https://atcoder.jp/contests/typical90/tasks/typical90_a

"""
 答えは 1 ~ L のどれかになるので
 答えの可能性のある数値を一つ一つ調べていく

 左の切れ込みから切ると仮定した時、
 答えの数値以上の長さであればそこに切れ込みを入れて
 小さければ次の切れ込みに移る
 全てのピースが答えの数値以上であれば、その中の最小値を答えの候補とする
"""

N, L = list(map(int, input().split(" ")))
K = int(input())
A = list(map(int, input().split(" ")))

def bynary_search(l, r):
    m = (l + r) // 2
    if (r - l) <= 1:
        return m
    cnt = 0
    pre = 0
    for a in A:
        if a - pre >= m and L - a >= m:
            cnt += 1
            pre = a
    if cnt >= K:
        return bynary_search(m, r)
    else:
        return bynary_search(l, m)


print(bynary_search(0, L))