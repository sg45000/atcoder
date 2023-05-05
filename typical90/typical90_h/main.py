# https://atcoder.jp/contests/typical90/tasks/typical90_h

n = int(input())
s = input()

A = 10 ** 9 + 7
dp = [[0] * 8 for _ in range(n)]
dp[s.index("a")][0] = 1

for i in range(n):
    for j in range(8):
        dp[i][j] += dp[i - 1][j]
        if j > 0 and s[i] == "atcoder"[j - 1]:
            dp[i][j] += dp[i][j - 1]
