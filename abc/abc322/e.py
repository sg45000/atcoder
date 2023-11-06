def calc(k):
    i = 1
    for _ in range(k - 1):
        i = i * 10 + 1
    return i


def from_base_10(n, base):
    """10進数の整数をbase進数の文字列に変換する."""
    if n == 0:
        return '0'
    digits = []
    while n:
        digits.append(str(n % base))
        n //= base
    return ''.join(digits[::-1])


def to_base_10(s, base):
    """base進数の文字列を10進数の整数に変換する."""
    return sum(int(c) * (base ** i) for i, c in enumerate(s[::-1]))


N, K, P = list(map(int, input().split(" ")))
CA = [list(map(int, input().split(" "))) for _ in range(N)]

base = P+ 1
max_parameter = str(calc(K) * (base - 1))
max_parameter_base_10 = to_base_10(max_parameter, base)

inf = 10 ** 9 + 7
dp = [[inf] * (max_parameter_base_10 + 1) for _ in range(N + 1)]
dp[0][0] = 0


for i in range(N):
    c, *a = CA[i]
    parameter = ''.join(map(str, a))
    for j in range(max_parameter_base_10):
        move_to = j + to_base_10(parameter, base)
        dp[i + 1][j] = dp[i][j]
        dp[i + 1][min(move_to, max_parameter_base_10)] = min(dp[i][j] + c, dp[i][min(move_to, max_parameter_base_10)])

ans = dp[-1][max_parameter_base_10]
if ans == inf:
    print(-1)
else:
    print(ans)