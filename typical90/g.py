def binary_search(L, t):
    l = 0
    r = len(L) - 1
    while l <= r:
        i = (l + r) // 2
        mid = L[i]
        if mid < t: 
            l = i - 1
        elif t < mid:
            r = i + 1
    return i
 
print(binary_search([1, 2, 4, 5, 6], 3))
 
# N = int(input())
# A = list(map(int, input().split(" ")))
# Q = int(input())
# B = [int(input()) for _ in range(Q)]
 
# A.sort()
 
# ans = []
# for q in range(Q):
#     b = B[q]
#     ap = binary_search(A, b)
#     if len(ap) == 1:
#         ans.append(str(abs(ap[0] - b)))
#     else:
#         v1 = abs(ap[0] - b)
#         v2 = abs(ap[1] - b)
#         ans.append(str(min(v1, v2)))
# print('\n'.join(ans))
