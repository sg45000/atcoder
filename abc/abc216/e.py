import bisect


N, K = list(map(int, input().split(" ")))
A = list(map(int, input().split(" ")))


def bin_search(left, right):
    if left + 1 >= right:
        return (left, right)
    m = (left + right) // 2
    cnt = bisect.bisect_left(A, m)
    total = 0
    for i in range(N):
        total += A[i] - cnt
    if total >= K:
        return bin_search(m, right)
    else:
        return bin_search(left, m)


left, right = bin_search(0, max(A) + 1)
