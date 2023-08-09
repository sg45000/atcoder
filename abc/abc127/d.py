# 1 4 5 5 7 8 13 33 52 100
# 30 30 30 30 10 10 10 4
# 累積和
# 1 5 10 15 22 30 43 76 128 228
# セグメント木

N, M = list(map(int, input().split(" ")))
A = list(map(int, input().split(" ")))
BC = [list(map(int, input().split(" "))) for _ in range(M)]

A.sort()

BC.sort(key=lambda x: x[1], reverse=True)

j = 0
for i in range(N):
    if BC[j][0] == 0:
        j += 1
    if j == M:
        break
    b, c = BC[j]
    if A[i] < c:
        A[i] = c
        BC[j][0] -= 1

print(sum(A))