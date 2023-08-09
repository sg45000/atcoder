"""
条件1と2の読み換え
 Xが9の倍数の時は、Kも9の倍数である

各桁の和がKの時のXの通り数はdpで解くことができる
dp[i] = dp[i - 9] + dp[i - 8] ... dp[i - 1]
Xの先頭の数を1 ~ 9で固定した時の通り数をそれぞれdpで参照して足し合わせてあげる
"""

K = int(input())
MOD = 10 ** 9 + 7

# dp[各桁の和] = Xの通り数
dp = [0] * (K + 1)
dp[0] = 1



if K % 9 != 0:
    print(0)
else:
    for i in range(K):
        for j in range(1, min(i + 2, 10)):
            dp[i + 1] += dp[i + 1 - j]
            dp[i + 1] %= MOD
    print(dp[K])