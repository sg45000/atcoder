N, S, M, L = list(map(int, input().split(" ")))

ans = float("inf")
for i in range(N // 6 + 1):
    for j in range(N // 8 + 1):
        for k in range(N):
            if i * 6 + j * 8 + k * 12 >= N:
                ans = min(i * S + j * M + k * L, ans)

print(ans)