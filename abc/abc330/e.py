from collections import defaultdict
import heapq


N, Q = list(map(int, input().split(" ")))
A = list(map(int, input().split(" ")))

SORT_A = sorted(A)
s = set()

M = defaultdict(int)


for a in A:
    M[a] += 1

mex = float("inf")
for i in range(N):
    if i not in M:
        s.add(i)
        mex = min(mex, i)

for _ in range(Q):
    i, x = list(map(int, input().split(" ")))
    i -= 1
    origin = A[i]
    A[i] = x
    M[origin] -= 1
    M[x] += 1
    if M[origin] == 0:
        s.add(origin)
        mex = min(mex, origin)
    if M[x] == 1:
        s.remove(x)
        if x == mex:
            

    print(mex)