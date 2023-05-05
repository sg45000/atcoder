W = int(input())
N, K = list(map(int, input().split(" ")))
photos = [list(map(int, input().split(" "))) for _ in range(N)]

# ####
# W = 10
# N = 5
# K = 4
# photos = [[9, 10], [3, 7], [3, 1], [2, 6], [4, 5]]
# ####

dp = [[0] * (W + 1) for _ in range(K + 1)]
for photo in photos:
    for k in reversed(range(K)):
        for w in reversed(range(W + 1 - photo[0])):
            dp[k + 1][w + photo[0]] = max(dp[k + 1][w + photo[0]], dp[k][w] + photo[1])

print(dp[-1][-1])