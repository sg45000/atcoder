N, K = list(map(int, input().split(" ")))
A = list(map(int, input().split(" ")))

left = 0
right = N - 1

while left + 1 < right:
    mid = (left + right) // 2
    if K == A[mid]:
        print(mid)
        exit()
    elif K < A[mid]:
        right = mid
    else:
        left = mid

if K < A[right]:
    print(right)
else:
    print(-1)