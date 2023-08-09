X, Y = list(map(int, input().split(" ")))
MOD = 10 ** 9 + 7
a = (2 * X - Y) / 3
b = (2 * Y - X) / 3

memo = [0] * 10 ** 7

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
    return fact[n] * ((fact_inv[r] * fact_inv[n - r]) % MOD) % MOD

if round(a) != a or round(b) != b:
    print(0)
elif a < 0 or b < 0:
    print(0)
else:
    print(ncr_with_mod(round(a + b), round(a), MOD))