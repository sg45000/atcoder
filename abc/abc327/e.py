import math
N = int(input())
P = list(map(int, input().split(" ")))

memo = [1] * N

for i in range(N - 1):
    memo[i + 1] = 0.9 ** (i + 1) + memo[i]

dp = [[0] * (N + 1) for _ in range(N + 1)]
dp[0][0] = 1

for i in range(1, N + 1):
    for j in range(1, i + 1):
        if j == 1:
            dp[i][j] = max(dp[i - 1][j], P[i - 1])
        elif 2 <= j < i:
            dp[i][j] = max(dp[i - 1][j], 0.9 * dp[i - 1][j - 1] + P[i - 1])
        elif i == j:
            dp[i][j] = 0.9 * dp[i - 1][j - 1] + P[i - 1]

ans = -(10 ** 10)
for i in range(1, N + 1):
    ans = max(ans, dp[N][i] / memo[i - 1] - 1200 / math.sqrt(i))

print(ans)
