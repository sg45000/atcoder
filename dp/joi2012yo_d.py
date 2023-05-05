N, K = list(map(int, input().split(" ")))
plans = [list(map(int, input().split(" "))) for _ in range(K)]

# N = 5
# K = 3
# plans = [[3, 1], [1, 1], [4, 2]]

P = [0] * (N + 1)
for p in plans:
    P[p[0]] = p[1]

MOD = 10000

# dp[i][j][k]とすると i - 1日目にパスタj, i日目にパスタkを選んだ時の通り数
# j, kのインデックス0はパスタを何も選ばなかった時という状態を表すと考える
dp = [[[0] * 4 for _ in range(4)] for _ in range(N + 1)]

# 初期値
dp[0][0][0] = 1

for i in range(N):
    for j in range(4):
        for k in range(4):
            p = P[i + 1]
            if p > 0:
                if j == k == p:  # 3日間連続でパスタが同じだった時
                    continue
                # i - 1日目にパスタj、i日目にパスタkを選んだ時の通り数を
                # i日目にパスタk、i + 1日目にパスタpを選んだ通り数に足す
                dp[i + 1][k][p] += dp[i][j][k] % MOD
            else:
                for l in range(1, 4):
                    if j == k == l:  # 3日間連続でパスタが同じだった時
                        continue 
                    # i - 1日目にパスタj、i日目にパスタkを選んだ時の通り数を
                    # i日目にパスタk、i + 1日目にパスタlを選んだ通り数に足す
                    dp[i + 1][k][l] += dp[i][j][k] % MOD

answer = 0
for a in dp[-1]:
    # dpの最後の要素は
    # 最後とその前日に選んだパスタの組み合わせごとの通り数が記録してある
    answer += sum(a)
print(answer % MOD)