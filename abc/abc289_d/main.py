"""
貰うDPでとく
1段ずつその階段に到達できるかをメモする

計算量: O(XA) 10^6 
"""
N = int(input())
A = list(map(int, input().split(" ")))
M = int(input())
B = list(map(int, input().split(" ")))
X = int(input())


dp = [False] * (X + 1)

dp[0] = True


b_memo = [True] * (X + 1)
for b in B:
    b_memo[b] = False

for i in range(1, X + 1):
    if not b_memo[i]:
        continue
    for a in A:
        if i - a >= 0:
            dp[i] = dp[i] or dp[i - a]

print("Yes") if dp[X] else print("No")
    