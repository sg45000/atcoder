N, L = list(map(int, input().split(" ")))
A = list(map(int, input().split(" ")))

ans = 0
for a in A:
    if L <= a:
        ans += 1

print(ans)