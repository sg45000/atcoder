N, L, R = list(map(int, input().split(" ")))
A = list(map(int, input().split(" ")))
ans = []
for a in A:
    q = min(abs(R - a), abs(L - a))
    x = abs(q - a)
    y = abs(q + a)
    if L <= x <= R:
        ans.append(x)
    elif L <= y <= R:
        ans.append(y)

print(*ans)