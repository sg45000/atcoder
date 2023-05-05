# https://atcoder.jp/contests/dp/tasks/dp_c

n = int(input())
a = [list(map(int, input().split(" "))) for _ in range(n)]

dp = [[0] * 3 for _ in range(n + 1)]

for i in range(n):
    for j in range(3):
        for k in range(3):
            if j == k:
                continue
            dp[i + 1][k] = max(dp[i + 1][k], dp[i][j] + a[i][k])

print(max(max(dp[n][0], dp[n][1]), dp[n][2]))
