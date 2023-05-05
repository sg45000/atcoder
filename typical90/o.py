MOD = 10 ** 9 + 7


def cmb(n, r):
    if n - r < r:
        r = n - r
    if r == 0:
        return 1
    if r == 1:
        return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2, r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1, r, p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result


def resolve(k, N):
    s = 0
    for i in range(1, (N-1) // k + 2):
        n = N - (k - 1) * (i - 1)
        r = i
        s += cmb(n, r) % MOD
    return s

N = int(input())

for k in range(1, N + 1):
    print(resolve(k, N))