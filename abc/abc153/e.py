"""
dp[i番目までの魔法を使う][与えたダメージ] = 消費mp
最初にdp[0][0] = 0で初期化してそれ以外はinf
infのところはi番目までの魔法を使っても、与えられないダメージ
j(与えたダメージ)を1ずつ増やしてdp遷移していき、
jダメージ目の状態からi + 1番目の魔法を使ってaダメージを与えたdp[i + 1][j + a]を更新する
その後にdp[i + 1][j]とdp[i][j]を比べてi + 1番目の魔法を使った方がいいか判断する
"""

H, N = list(map(int, input().split(" ")))
AB = [list(map(int, input().split(" "))) for _ in range(N)]


dp = [[float("inf")] * (H + 1) for _ in range(N + 1)]

dp[0][0] = 0

for i in range(N):
    a, b = AB[i]
    for j in range(0, H + 1):
        # i + 1番目の魔法を使った方がいいか判定する
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
        # jダメージ目からi+1番目の魔法を使った時のdpを更新
        dp[i + 1][min(H, j + a)] = min(dp[i + 1][min(H, j + a)], dp[i + 1][j] + b)

print(dp[-1][-1])