"""
ダブリングで解く
"""

N, K = map(int, input().split(" "))
A = list(map(int, input().split(" ")))

doubling = [[0] * N for _ in range(60)]

for i, a in enumerate(A):
    doubling[0][i] = a - 1

for i in range(1, 60):
    for j in range(N):
        doubling[i][j] = doubling[i - 1][doubling[i - 1][j]]

ans = 0
for p in reversed(range(60)):
    if K & 1 << p:
        ans = doubling[p][ans]

print(ans + 1)
