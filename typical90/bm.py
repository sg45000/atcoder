R, G, B, K = list(map(int, input().split(" ")))
X, Y, Z = list(map(int, input().split(" ")))

MOD = 998244353

"""
  組合せを求める 素数で割ったあまりを求める時に使う
  n = 全数
  r = 何個選ぶか
  p = 法
  計算量: O(r)
"""
def ncr_mod(n, r, mod):
    ret = 1
    for i in range(1, r+1):
        ret = (ret * (n-i+1) * pow(i, mod-2, mod)) % mod
    return ret

ans = 0
for r in range(K + 1):
    for g in range(K + 1):
        for b in range(K + 1):
            if r + g <= X and g + b <= Y and b + r <= Z and r + g + b == K:
                a = (ncr_mod(R, r, MOD) * ncr_mod(G, g, MOD)) % MOD
                ans += (a * ncr_mod(B, b, MOD)) % MOD

print(ans)