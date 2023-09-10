"""
連続した青ボールの組がi個存在すれば、i回で青ボールを回収できる
例えば N = 5, K = 3 の時
赤ボールの数 R = 2個

i = 2の時、赤ボールのグループを仕切り棒に例えると
青G|青Gとなるので青ボールをi個分引いた K - i と仕切り棒i - 1個の並びの組み合わせを求めればいい
ncr(K - i, i - 1)

仕切り棒に例えた赤グループに対しても同様に
|赤G|という最小構成に対して赤ボールの配置を計算することになる
ncr(N - K + 1, i)

最後にそれぞれの組み合わせ数をかけると答えが出る

"""

def ncr_with_mod(n, r, p):
    fact = [1] * (n + 5)  # iの階乗をpで割ったあまり
    fact_inv = [1] * (n + 5)  # factの逆元
    inv = [1] * (n + 5)  # iの逆元

    fact[0] = fact[1] = 1
    fact_inv[0] = fact_inv[1] = 1
    inv[1] = 1

    for i in range(2, n + 5):
        fact[i] = fact[i - 1] * i % p
        inv[i] = p - inv[p % i] * (p // i) % p
        fact_inv[i] = fact_inv[i - 1] * inv[i] % p
    return fact[n] * ((fact_inv[r] * fact_inv[n - r]) % p) % p


N, K = list(map(int, input().split(" ")))
MOD = 10 ** 9 + 7

R = N - K  # 赤ボールの数

for i in range(1, K + 1):
    if R < i - 1:  # 赤ボールが足りないと青ボールをグループ化できない
        print(0)
        continue
    b = ncr_with_mod(K - 1, i - 1, MOD)  # 青ボールの並び
    a = ncr_with_mod(R + 1, i, MOD)  # 赤ボールの並び
    print((a * b) % MOD)
