"""
  重複組合せを求める 素数で割ったあまりを求める時に使う
  n = 全ての球の数
  r = 片方の球の数
  p = 法
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