"""
ナップサック問題のようなもの
"""
N = int(input())
T = list(map(int, input().split(" ")))

S = sum(T)
best = S // 2

# dp[i番目の料理をオーブンAで作った場合][t分目] = 料理を作り終えているか
dp = [[False] * (S + 1) for _ in range(N + 1)]
dp[0][0] = True

for i in range(N):
    for t in reversed(range(S + 1 - T[i])):
        if dp[i][t]:
            dp[i + 1][t] = dp[i][t]
        if dp[i + 1][t]:
            dp[i + 1][t + T[i]] = True

answer = 0
for t, a in enumerate(dp[-1]):
    if a:
        answer = answer if abs(answer - best) < abs(t - best) else t
print(max(answer, S - answer))