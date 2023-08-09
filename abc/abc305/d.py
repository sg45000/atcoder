import bisect
N = int(input())
A = list(map(int, input().split(" ")))
Q = int(input())
LR = [list(map(int, input().split(" "))) for _ in range(Q)]

D = [0] * (N + 1)
for i, a in enumerate(A):
    if i % 2 == 0:
        D[i + 1] = a + D[i]
    else:
        D[i + 1] = D[i] - a

# for l, r in LR:
#     l_i = bisect.bisect(A, l) - 1
#     r_i = bisect.bisect(A, r) - 1
#     D[r_i] - D[l_i] + (l - A[l_i])
