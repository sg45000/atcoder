"""
ある整数iについて、i以下の整数xを選んだ時の和の最小値を求める。dp_x
dp_x[i + 1] は 
dp_x[i] + A[i]  (一つ前の最小値+次はそのままの値)
と 
L * (i + 1) (全てLに置き換えた時)
のどちらか小さい方になる

これをyについても同様に行い、
dp_x[i] + dp_y[N - i] の最小値を求める
"""

N, L, R = list(map(int, input().split(" ")))
A = list(map(int, input().split(" ")))
B = A[::-1]

dp_x = [0] * (N + 1)
dp_y = [0] * (N + 1)
for i in range(N):
    dp_x[i + 1] = min(dp_x[i] + A[i], L * (i + 1))
    dp_y[i + 1] = min(dp_y[i] + B[i], R * (i + 1))

ans = float("inf")
for i in range(N + 1):
    ans = min(ans, dp_x[i] + dp_y[N - i])

print(ans)