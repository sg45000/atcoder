N, P, Q = list(map(int, input().split(" ")))
A = list(map(int, input().split(" ")))

ans = 0
for a1 in range(N):
    for a2 in range(a1 + 1, N):
        for a3 in range(a2 + 1, N):
            for a4 in range(a3 + 1, N):
                for a5 in range(a4 + 1, N):
                    if (((A[a1] * A[a2]) % P) * ((A[a3] * A[a4]) % P) * A[a5]) % P == Q:
                        ans += 1

print(ans)