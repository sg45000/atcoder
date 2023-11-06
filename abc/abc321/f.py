Q, K = list(map(int, input().split(" ")))
MOD = 998244353

dp = [[0] * (K + 1) for _ in range(Q)]

dp[0][0] = 1

bucket = [0] * 5001
for i in range(Q):
    op, n = input().split()
    ball_number = int(n)
    if ball_number <= K:
        if op == '+':
            for j in range(K + 1):
                dp[i + 1][j] += dp[i][j]
                if ball_number + j <= K:
                    dp[i + 1][ball_number + j] += dp[i][j]
                    dp[i + 1][ball_number + j] %= MOD
        else:
            for j in reversed(range(K + 1)):
                dp[i - 1][j] = dp[i][j]
                if j - ball_number >= 0:
                    dp[i + 1][j] = dp[i][j - ball_number]
                    dp[i + 1][j] %= MOD

    print(dp[i + 1][K])

def plus(a,b):
    return a + b

def minus(a, b):
    return a - b

def toOperator(a):
    return plus if a == '+' else minus