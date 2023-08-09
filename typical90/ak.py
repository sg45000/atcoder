W, N = list(map(int, input().split(" ")))
LRV = [list(map(int, input().split(" "))) for _ in range(N)]

def get_leaf_size(n):
    bit = bin(n)[2:]
    dec = 0 if "1" in bit[1:] else -1
    return 2 ** (len(bit) + dec)

leaf_size = get_leaf_size(W)

segment_tree = [0] * (2 * leaf_size - 1)
lazy = [0] * (2 * leaf_size - 1)


def eval(i):
    if lazy[i] == 0:
        return
    if i < leaf_size - 1: # 葉でなければ子に伝播
        lazy[i * 2 + 1] = lazy[i]
        lazy[i * 2 + 2] = lazy[i]
    segment_tree[i] = max(segment_tree[i], lazy[i])
    lazy[i] = 0


def query(a, b, i, left, right):
    eval(i)
    if right <= a or b <= left: # 完全に外側
        return 0
    elif a <= left and right <= b:  # 完全に内側
        return segment_tree[i]
    else:  # 一部区間が被る
        vl = query(a, b, i * 2 + 1, left, (left + right) // 2)
        vr = query(a, b, i * 2 + 2, (left + right) // 2, right)
        return max(vl, vr)


def update(a, b, left, right, i, x):
    eval(i)
    if a <= left and right <= b:  # 完全に内側
        lazy[i] = x
        eval(i)
    elif a < right and left < b:  # 一部区間が被る
        update(a, b, left, (left + right) // 2, i * 2 + 1, x)  # 左の子を更新
        update(a, b, (left + right) // 2, right, i * 2 + 2, x)  # 右の子を更新
        segment_tree[i] = max(segment_tree[i * 2 + 1], segment_tree[i * 2 + 2])  # 最大値の更新

for i in range(N):
    l, r, v = LRV[i]
    for w in range(W - r):
        value = query(w, w + 1, 0, 0, leaf_size) + v
        update(l + w, r + w, 0, leaf_size, 0, value)

print(segment_tree)
