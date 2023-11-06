from bisect import bisect
from itertools import accumulate

N, M, P = list(map(int, input().split(" ")))
A = list(map(int, input().split(" ")))
B = list(map(int, input().split(" ")))
A.sort()
B.sort()

b_acc = list(accumulate(B))

s = 0
for i in range(N):
    j = bisect(B, P - A[i])
    if 0 < j:
        s += A[i] * j + b_acc[j - 1]
        s += P * (M - j)
    else:
        s += P * M

print(s)