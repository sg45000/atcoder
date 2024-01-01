"""
要素の個数を数えるdictを用意して、0~M要素の部分列を最初に数える
その中でmexを計算

そのあとは部分列を1つずつ右に移動しながらdictを更新していく
移動したことで0個になった要素があれば、その要素と現在のmexを比較してmexを更新
"""
from collections import defaultdict


N, M = list(map(int, input().split(" ")))
A = list(map(int, input().split(" ")))

d = defaultdict(int)

for i in range(M):
    d[A[i]] += 1

mex = 0
for j in range(N + 1):
    if d[j] == 0:
        mex = j
        break

for i in range(N - M):
    d[A[i + M]] += 1
    d[A[i]] -= 1

    # 部分列のmexの最小値を探せばいいので、 
    # A[i + M] == mex　の場合のmexを再計算する必要はない
    if d[A[i]] == 0:
        if A[i] < mex:
            mex = A[i]
print(mex)