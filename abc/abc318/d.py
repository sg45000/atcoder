N = int(input())
D = [list(map(int, input().split(" "))) for _ in range(N - 1)]
# dp[選ばれたビット] = 重みの最大
dp = [0] * (2 ** N)

for b in range(2 ** N):
    for i in range(N - 1):
        for j in range(i + 1, N):
            s = (1 << i) + (1 << j)
            if b >= s and (b >> i) & 1 and (b >> j) & 1:
                dp[b] = max(dp[b], dp[b - s] + D[i][j - i - 1])

ans = max(dp)

print(ans)