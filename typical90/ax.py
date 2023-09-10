
# 配るDP
# N, L = list(map(int, input().split()))

# dp = [0] * (N + 1)
# dp[0] = 1

# mod = 10 ** 9 + 7

# for i in range(N):
#     dp[i + 1] += dp[i]
#     dp[i + 1] %= mod
#     if i + 1 - L >= 0:
#         dp[i + 1] += dp[i + 1 - L]
#         dp[i + 1] %= mod

# print(dp[-1])

# もらうDP
N, L = list(map(int, input().split()))

dp = [0] * (N + 1)
dp[0] = 1

mod = 10 ** 9 + 7

for i in range(1, N + 1):
    dp[i] += dp[i - 1]
    dp[i] %= mod
    if i - L >= 0:
        dp[i] += dp[i - L]
        dp[i] %= mod

print(dp[-1])