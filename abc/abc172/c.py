"""
AとB両方の累積和を出す
Aの累積和を線型探索し、Bに対して残りの時間分で2分探索する
"""

import itertools
import bisect

N, M, K = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
a_total = sum(A)
b_total = sum(B)
total = a_total + b_total

acc_a = list(itertools.accumulate(A))
acc_b = list(itertools.accumulate(B))

ans = 0
for i in range(-1, N):
    if i == -1:
        rest_time = K
    else:
        rest_time = K - acc_a[i]
    if rest_time < 0:
        continue
    b_count = bisect.bisect(acc_b, rest_time)
    ans = max(ans, i + 1 + b_count)
print(ans)
