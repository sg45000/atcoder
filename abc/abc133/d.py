"""
素直にdpで解こうとすると
dp[i][山iの降った量] = 山 i+1の降った量
になるけど、そうなると N * |A|でLTE
"""

N = int(input())
A = list(map(int, input().split(" ")))

# dp[i][山iの降った量] = 山 i+1の降った量
dp = [[0] * (10 ** 9) for _ in range(N + 1)]

for i in range(N):
    dp[i]