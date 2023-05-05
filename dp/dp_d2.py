N, W = list(map(int, input().split(" ")))
WV = [list(map(int, input().split(" "))) for _ in range(N)]

# dp[品物i番目までを選んだ時][重さがw以下の時] = 最大の価値
dp = [[0] * (W + 1) for _ in range(N + 1)]

for i in range(N):
    w, v = WV[i]
    for j in range(W + 1):
        if j < w:
            dp[i + 1][j] = dp[i][j]
        else:
            dp[i + 1][j] = max(dp[i][j], dp[i][j - w] + v)
print(dp[-1][-1])
    
"""
  * 0 1 2 3 4 5 6 7 8
  0 0 0 0 0 0 0 0 0 0
  1 0 0 0 3 3 3 3 3 3
  2 0 0 0 3 5 5 5 7 7
  3 0 0 0 3 5 6 6 7 9
"""