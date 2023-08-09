"""
10^5回くらいシミュレーションすると二つのマスを行ったり来たりする周期性に到達する
10^100のシミュレーションは偶数回で終わるので10^5回程度かつ偶数回のシミュレーションを行った結果が答えになる
"""

S = input()
s_len = len(S)


# dp[p][i] = 最初の位置がiの人を2 ^ p回シミュレーションした時の位置
dp = [[0] * s_len for _ in range(60)]

# dp　初期化
for i, s in enumerate(S):
    dp[0][i] = i + (1 if s == "R" else -1)

# ダブリング
for p in range(1, 60):
    for i, s in enumerate(S):
        dp[p][i] = dp[p - 1][dp[p - 1][i]]

ans = [0] * s_len
for i in range(s_len):
    ans[dp[32][i]] += 1

print(" ".join(map(str, ans)))