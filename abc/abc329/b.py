N = int(input())
A = list(map(int, input().split(" ")))

m = max(A)

ans = 0
for a in A:
    if m != a:
        ans = max(ans, a)

print(ans)