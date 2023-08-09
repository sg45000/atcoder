"""
セグメント木
完全二分木なのでn * 2 - 1個の要素の配列で表現できる
親iの子は 左の子 i * 2 + 1, 右の子 i * 2 + 2 でアクセスできる
子iの親は (i - 1) // 2 でアクセスできる
葉のインデックスはn ~ 2n - 1
"""

W, N = list(map(int, input().split(" ")))
LR = [list(map(int, input().split(" "))) for _ in range(N)]

segment_tree = [0] * (2 * W - 1)
MIN_INF = - (10 ** 10)
lazy = [0] * (2 * W - 1)  # 遅延評価のための配列


def update(a, b, x, k, l, r):
    lazy_eval(k)
    if a <= l and r <= b:
        lazy[k] = x
        lazy_eval(k)
    elif a < r and l < b:
        update(a, b, x, k * 2 + 1, l, (l + r) // 2)
        update(a, b, x, k * 2 + 2, (l + r) // 2, r)
        segment_tree[k] = max(segment_tree[k * 2 + 1], segment_tree[k * 2 + 2])



def lazy_eval(k):
    if lazy[k] == MIN_INF:
        return
    if k < W - 1:
        lazy[k * 2 + 1] += 1
        lazy[k * 2 + 2] += 1
    segment_tree[k] = lazy[k]
    lazy[k] = MIN_INF


# 親から子を順に見ていく
def get_max(a, b, k, l, r):
    lazy_eval(k)  # 遅延評価のため
    if r <= a or b <= l:
        return MIN_INF
    if a <= l and r <= b:
        return segment_tree[k]
    max_left_child = get_max(a, b, k * 2 + 1, l, (l + r) // 2)
    max_right_child = get_max(a, b, k * 2 + 2, (l + r) // 2, r)
    return max(max_left_child, max_right_child)

for l, r in LR:
    max_in_section = get_max(l, r, 0, 0, W)
    x = max_in_section + 1
    print(x)
    update(l, r, x, 0, 0, W)
