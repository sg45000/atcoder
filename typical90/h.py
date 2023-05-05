N = int(input())
S = input()
# N = 41
# S = "btwogablwetwoiehocghiewobadegwhoihegnldir"

dp = [[0] * 8 for _ in range(N + 1)]
dp[0][0] = 1

M = {
    "a": 1,
    "t": 2,
    "c": 3,
    "o": 4,
    "d": 5,
    "e": 6,
    "r": 7
}

MOD = 10 ** 9 + 7

for i in range(1, N + 1):
    cur_char_num = M.get(S[i - 1])
    for j in range(8):
        dp[i][j] = dp[i - 1][j]
        if j > 0 and j == cur_char_num:
            dp[i][j] += dp[i - 1][j - 1]
            dp[i][j] %= MOD

print(dp[-1][-1])

# attcordeer
#  , *, a, t, c, o, d, e, r   
# *, 1, 0, 0, 0, 0, 0, 0, 0
# a, 1, 1, 0, 0, 0, 0, 0, 0
# t, 1, 1, 1, 0, 0, 0, 0, 0
# t, 1, 1, 2, 0, 0, 0, 0, 0
# c, 1, 1, 2, 2, 0, 0, 0, 0
# o, 1, 1, 2, 2, 2, 0, 0, 0
# r, 1, 1, 2, 2, 2, 0, 0, 0
# d, 1, 1, 2, 2, 2, 2, 0, 0
# e, 1, 1, 2, 2, 2, 2, 2, 0
# e, 1, 1, 2, 2, 2, 2, 4, 0
# r, 1, 1, 2, 2, 2, 2, 4, 4
