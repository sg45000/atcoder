"""
dp[i][j] = (i,j)のマスを右下に取った時の穴のない正方形の個数

(i, j) が穴が空いていたら、0
穴が空いていなかったら、
dp[i][j] は (i - 1, j), (i, j - 1), (i, j) の3マスのdpのmin + 1 になる
理由: (i,j)を右下にした時の最大の正方形の左上は(i - z, j - z)である -- zは任意の整数
左上(i - z, j - z), 右下(i,j)が穴のない正方形であることにとって、
左上(i - z - 1, j - z - 1)が穴のない正方形であるのは必要条件である
"""

H, W, N = list(map(int, input().split(" ")))

grid = [[True] * W for _ in range(H)]
for _ in range(N):
    a, b = list(map(int, input().split(" ")))
    grid[a - 1][b - 1] = False


dp = [[0] * (W + 1) for _ in range(H + 1)]

for i in range(H):
    for j in range(W):
        if grid[i][j]:
            dp[i + 1][j + 1] = min(dp[i][j], dp[i + 1][j], dp[i][j + 1]) + 1

ans = 0
for d in dp:
    ans += sum(d)

print(ans)
