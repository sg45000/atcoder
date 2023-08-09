N, M = list(map(int, input().split(" ")))
A = [list(map(int, input().split(" "))) for _ in range(M)]

S = set()

for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        S.add(i * 100 + j)

for a in A:
    for i in range(N - 1):
        x = min(a[i], a[i + 1])
        y = max(a[i], a[i + 1])
        k = x * 100 + y
        if k in S:
            S.remove(k)

print(len(S))



