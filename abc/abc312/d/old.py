"""
dp[i文字目][i文字目までの'('の数 - ')'の数] = 通り数
最終的な通り数はdp[N][0]を見る
N文字目までの'('の数 - ')'の数が0にならないと括弧列にはならない
"""

S = input()
N = len(S)

dp = [[0] * (N + 1) for _ in range(N + 1)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if S[i] == '(' or S[i] == '?':
            dp[i + 1][j + 1] += dp[i][j]
            dp[i + 1][j + 1] %= 998244353
        if j > 0 and (S[i] == ')' or S[i] == '?'):
            dp[i + 1][j - 1] += dp[i][j]
            dp[i + 1][j - 1] %= 998244353

print(dp[N][0])