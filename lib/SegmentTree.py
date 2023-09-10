N = 100

INF = 2 ** 31 - 1

# セグメント木は完全二分木のため、N以上の2の乗数で最小の値を葉の数にしたい
# 99 であれば 128
# 0 -index
LV = (N - 1).bit_length()
N0 = 2 ** LV
data = [INF] * (2*N0)
lazy = [None]*(2*N0)

# 伝播される区間のインデクス(1-index)を全て列挙するgenerator
def gindex(l, r):
    L = l + N0
    R = r + N0
    lm = (L // (L & -L)) >> 1
    rm = (R // (R & -R)) >> 1
    while L < R:
        if R <= rm:
            yield R
        if L <= lm:
            yield L
        L >>= 1
        R >>= 1
    while L:
        yield L
        L >>= 1

# 1-indexedで単調増加のインデックスリストを渡す
def propagates(*ids):
    for i in reversed(ids):
        v = lazy[i - 1]
        if v is None:
            continue
        lazy[2 * i - 1] = data[2 * i - 1] = lazy[2 * i] = data[2 * i] = v
        lazy[i - 1] = None

# 区間更新　（RUQ)
def update(l, r, x):
    *ids = gindex(l, r)

    # 1. トップダウンにlazyの値を伝播
    propagates(*ids)

    # 2. 区間[l, r)のdata, lazyの値を更新
    L = N0 + l
    R = N0 + r
    while L < R:
        if R & 1:
            R -= 1
            lazy[R - 1] = data[R - 1] = x
        if L & 1:
            lazy[L - 1] = data[L - 1] = x
            L += 1
        L >>= 1
        R >>= 1
    # 3. 伝播させた区間について、ボトムアップにdataの値を伝播する
    for i in ids:
        data[i - 1] = min(data[2*i-1], data[2*i])

# 区間[l, r)の最小値を求める
def query(l, r):
    # 1. トップダウンにlazyの値を伝播
    propagates(*gindex(l, r))
    L = l + N0
    R = r + N0

    # 2. 区間[l, r)の最小値を求める
    s = INF
    while L < R:
        if R & 1:
            R -= 1
            s = min(s, data[R - 1])
        if L & 1:
            s = min(s, data[L-1])
            L += 1
        # 親ノードのインデックスに移動(1ビット右シフトでインデックスを半分にする)
        L >>= 1
        R >>= 1
    return s