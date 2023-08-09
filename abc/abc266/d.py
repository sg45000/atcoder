N = int(input())
TXA = [list(map(int, input().split(" "))) for _ in range(N)]

time = TXA[-1][0]
dp = [[0] * 5 for _ in range(time + 1)]

dp[0][0] = 0  # dp[時間][座標]

i = 0
for t in range(1, time + 1):
    for x in range(min(t + 1, 5)):
        stay = dp[t - 1][x]
        back = dp[t - 1][max(0, x - 1)]
        forward = dp[t - 1][min(x + 1, 4)]
        T, X, A = TXA[i]

        if t == T and x == X:
            dp[t][x] = max(stay, back, forward) + A
        else:
            dp[t][x] = max(stay, back, forward)
        
    if t == T:
        i += 1

print(max(dp[-1]))