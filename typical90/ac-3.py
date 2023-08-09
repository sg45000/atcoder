"""
セグメント木
完全二分木なのでn * 2 - 1個の要素の配列で表現できる
親iの子は 左の子 i * 2 + 1, 右の子 i * 2 + 2 でアクセスできる
葉のインデックスはn ~ 2n - 1
"""

W, N = list(map(int, input().split(" ")))
LR = [list(map(int, input().split(" "))) for _ in range(N)]

segment_tree = [0] * (2 * W - 1)
INF = 10 ** 10

# 子から親を順に更新
def update(i, x):
    i += W - 1
    segment_tree[i] = x
    while (i > 0):
        i = (i - 1) // 2  # 親のインデックス
        segment_tree[i] = max(segment_tree[2 * i + 1], segment_tree[2 * i + 2])


# 親から子を順に見ていく
def get_max(a, b, k, l, r):
    if r <= a or b <= l:
        return INF
    if a <= l and r <= b:
        return segment_tree[k]
    max_left_child = get_max(a, b, k * 2 + 1, l, r // 2)
    max_right_child = get_max(a, b, k * 2 + 2, l // 2, r)
    return max(max_left_child, max_right_child)
