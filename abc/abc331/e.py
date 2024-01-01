N, M, L = list(map(int, input().split(" ")))
A = list(map(int, input().split(" ")))
B = list(map(int, input().split(" ")))

sorted_A = sorted(A, reverse=True)
sorted_B = sorted(B, reverse=True)

CD = [list(map(int, input().split(" "))) for _ in range(L)]

SET = set()
for c, d in CD:
    SET.add((c, d))

for i in range(N):
    for j in range(M):
        if () in SET
        sorted_A[i] + sorted_B[j]