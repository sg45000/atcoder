import bisect

N, M = list(map(int, input().split(" ")))
A = list(map(int, input().split(" ")))

A.sort()

ans = 0
for i in range(N):
    j = A[i] + M
    k = bisect.bisect(A, j)
    if A[k - 1] == j:
        k -= 1
    ans = max(k - i, ans)

print(ans)