# N, W = list(map(int, input().split(" ")))
# WV = [list(map(int, input().split(" "))) for _ in range(N)]

N=3 
W =8
WV=[[3, 30],[4, 50],[5, 60]]

V = 0
for i in range(N):
    _, v = WV[i]
    V += v

dp = [[10 ** 10] * (V + 1) for _ in range(N + 1)]


for i in range(N):
    w, v = WV[i]
    for j in range(V + 1):
        if j < v:
            dp[i + 1][j] = dp[i][j]
        else:
            if dp[i][j] == 10 ** 10:
                dp[i + 1][j] = w
            else:
                dp[i + 1][j] = min(dp[i][j], dp[i][j - v] + w)

for v, w in zip(reversed(range(V + 1)), reversed(dp[-1])):
    if w <= W:
        print(v)
        break
