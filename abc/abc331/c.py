from collections import defaultdict


N = int(input())
A = list(map(int, input().split(" ")))

B = sorted(A)
D = defaultdict()
s = 0
nex = float("inf")
for v in reversed(B):
    if nex != v:
        D[v] = s
        nex = v
    s += v

for a in A:
    print(D[a])
