"""
貪欲法
N, M, Qが <= 50なので、結構余裕
小さい箱から見ていく。
箱の大きさに合う商品の中で価値が最も高いものから貪欲に埋めていく
O(NMQ)
"""

from bisect import bisect

N, M, Q = map(int, input().split())
WV = [list(map(int, input().split())) for _ in range(N)]
X = list(map(int, input().split()))

for _ in range(Q):
    L, R = list(map(int, input().split()))
    items_sorted_w = sorted(WV, key=lambda x: x[0])
    sorted_w = list(map(lambda x: x[0], items_sorted_w))
    usable_X = X[:L - 1] + X[R:]  # 使える箱を設定しておく
    usable_X.sort()  # 箱は小さいものから貪欲で入れていく
    total_v = 0
    for x in usable_X:
        max_v = 0
        k = -1
        # 2分探索で小さい商品〜箱の大きさに合う最大の商品までをピックアップ
        for i, wv in enumerate(items_sorted_w[:bisect(sorted_w, x)]):
            _w, v = wv
            # 箱の大きさに合う商品の中で価値が最も高いものから貪欲に埋めていく
            if max_v <= v:
                max_v = v
                k = i
        if k != -1:
            items_sorted_w = items_sorted_w[:k] + items_sorted_w[k+1:]
            sorted_w = list(map(lambda x: x[0], items_sorted_w))
            total_v += max_v
    print(total_v)