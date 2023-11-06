
def ncr_mod(n, r, mod):
    ret = 1
    for i in range(1, r+1):
        ret = (ret * (n-i+1) * pow(i, mod-2, mod)) % mod
    return ret

N, A, B = list(map(int, input().split(" ")))

MOD = 10 ** 9 + 7

ans = pow(2, N, MOD)

ans -= ncr_mod(N, A, MOD)
ans %= MOD
ans -= ncr_mod(N, B, MOD)
ans %= MOD

print(ans - 1)
