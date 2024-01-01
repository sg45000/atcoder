"""
x軸とy軸は独立して考えられる
iが奇数の時はy軸の移動, 偶数の時はx軸の移動となる
N個分移動した後にx, y に到達していればYes

DPでとく
DPはその時点での到達可能点を管理する
Aの最大値 * N 分だけ直線上を移動する可能性があるので、DPも -(Aの最大値 * N) < (Aの最大値 * N) の数で管理する
各Aの値でマイナス側プラス側に移動する可能性を考慮してDPを更新していく

計算量もO(Aの最大値 * N^2)なので 10^7程度

"""

N, x, y = list(map(int, input().split()))
A = list(map(int, input().split()))

A_max = max(A) * N
A_min = -A_max

# dpは1次元で持ち、マイナス側の位置は配列に対してマイナスインデックスで参照することで表現される
x_dp = [False] * (A_max * 2 + 2)
x_dp[0] = True

y_dp = [False] * (A_max * 2 + 2)
y_dp[0] = True

for i in range(N):
    _dp = [False] * (A_max * 2 + 2)
    if i == 0:
        _dp[A[i]] = True
        x_dp = _dp
        continue
    dp_copy = x_dp if i % 2 == 0 else y_dp
    for j in range(A_min, A_max + 1):
        if dp_copy[j] and j + A[i] <= A_max:
            _dp[j + A[i]] = True
        if dp_copy[j] and A_min <= j - A[i] <= A_max:
            _dp[j - A[i]] = True
    if i % 2 == 0:
        x_dp = _dp
    else:
        y_dp = _dp

ans = "Yes" if x_dp[x] and y_dp[y] else "No"
print(ans)