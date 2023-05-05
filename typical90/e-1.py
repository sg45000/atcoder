"""
B = 17の時
88 % 17 = 3が成り立つので
5 * 17 + 3 = 88

末尾に2を追加した882を考える時
51 * 17 + 15 = 882 なので
(5 * 17 + 3) * 10 + 2 = 882
= (5 * 17) + 32
となる
つまり 余りを10倍して末尾に追加する数値を足したものにBを割った余りが桁を増やした時の余りになる。
"""

# N, B, K = list(map(int, input().split(" ")))
# C = list(map(int, input().split(" ")))

N = 10000
B = 27
K = 7
C = [1, 3, 4, 6, 7, 8, 9]

# 桁DPで解く
# dp[上から何桁目][現時点でのBで割ったあまり] = 通り数
# dp[最下の桁][Bで割った余が0] = N桁の数値でBで割った余が0の通り数
dp = [[0] * B for _ in range(N + 1)]

MOD = 10 ** 9 + 7

dp[0][0] = 1
for i in range(N):
    for j in range(B):
        for k in range(K):

            nex = (j * 10 + C[k]) % B
            dp[i + 1][nex] += dp[i][j]
            dp[i + 1][nex] %= MOD
print(dp[-1][0])