"""
計算量 O(NloglogN)
"""

N, K = list(map(int, input().split(" ")))

memo = [0] * (N + 1)  # 素因数の数をメモした変数

for i in range(2, N + 1):
    if memo[i] != 0:  # 素数判定
        continue
    # これ以降のiは素数
    for j in range(i, N + 1, i):  # jはiの倍数
        memo[j] += 1  # iの倍数はiを約数として持つので、素因数の数を＋１する

answer = 0
for m in memo:
    if m >= K:
        answer += 1
print(answer)