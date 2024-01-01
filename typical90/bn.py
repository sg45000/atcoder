N = int(input())
LR = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N - 1):
    l1, r1 = LR[i]
    for j in range(i + 1, N):
        l2, r2 = LR[j]

        a = 0
        for v in range(l1, r1 + 1):
            for u in range(l2, r2 + 1):
                if v > u:
                    a += 1
        m = (r1 - l1 + 1) * (r2 - l2 + 1)
        ans += a / m

print(ans)