N, D, P = list(map(int, input().split(" ")))
F = list(map(int, input().split(" ")))

F.sort(reverse=True)

ans = 0
for i in range(0, N, D):
    s = 0
    for j in range(min(D, N - i)):
        s += F[i + j]
    if s > P:
        ans += P
    else:
        ans += s

print(ans)