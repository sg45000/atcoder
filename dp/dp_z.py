# https://atcoder.jp/contests/dp/tasks/dp_z

N, C = list(map(int, input().split(" ")))
hs = list(map(int, input().split(" ")))

# N = 5 
# C = 6
# hs =[1, 2, 3, 4, 5]


dp = [float('inf')] * N
dp[0] = 0

for j in range(N):
    for i in range(j):
        dp[j] = min(dp[j], dp[i] + (hs[j] - hs[i]) ** 2 + C)
print(dp[-1])