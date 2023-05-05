# A, B = list(map(int, input().split(" ")))
A = 1
B = 10000


def resolve_dp(N):
    digit = len(N)
    dp = [[[0, 0] for _ in range(2)] for _ in range(digit + 1)]
    # dp[桁][N未満フラグ][4 or 9を持っているフラグ]
    dp[0][0][0] = 1

    for i in range(digit):
        D = int(N[i])
        for j in range(2):
            for k in range(2):
                for d in range(1, (9 if j else D) + 1):
                        dp[i + 1][j or (1 if d < D else 0)][k or (1 if (d == 4 or d == 9) else 0)] += dp[i][j][k]
    return dp[-1][0][1] + dp[-1][1][1]


print(resolve_dp(str(B)) - resolve_dp(str(A - 1)))