# https://atcoder.jp/contests/dp/tasks/dp_o
import sys, math
# input = lambda: sys.stdin.readline()[:-1]
# def MI(): return map(int, input().split())
inf = 10**18
mod = 10**9 + 7
 
# n, = MI()
# a = [list(MI()) for _ in range(n)]

n = 3
a = [[0,1,1],[1,0,1],[1,1,1]]
 
# dp[i][j]=男性i人目まで見てマッチング済みの女性の状態がjのときの通り数
dp = [0]*(1<<n)
dp[0] = 1
 
for i in range(n):
    ndp = [0]*(1<<n)
    for bit in range(1<<n):
        if not dp[bit]: continue
        for j in range(n):
            if bit >> j & 1: continue
            if not a[i][j]: continue
            new = bit | (1<<j)
            ndp[new] += dp[bit]
            ndp[new] %= mod
    dp = ndp
print(dp[-1] % mod)