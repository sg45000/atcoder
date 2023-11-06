N = int(input())
P = list(map(int, input().split(" ")))

m = [0] * N
for i in range(N):
    m[i] = 0.9 ** i

# dp = [[0] * N * 5000 for _ in range(N)]

# for i in range(N):
#     dp[i + 1] = 