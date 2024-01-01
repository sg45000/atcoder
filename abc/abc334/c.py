N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

L = [2] * N

for a in A:
    L[a - 1] = 1

ans = 0
if K % 2 == 0:
    for i in range(N):
        if L[i] == 1:
            L[i + 1] -= 1
            ans += 1
else:
    b = False
    for i in range(N):
        if L[i] == 1 and i == N - 1:
            continue
        if L[i] == 1:
            if L[i + 1] == 1:
                L[i + 1] -= 1
                ans += 1
            else:
                if b:
                    L[i + 1] -= 1
                    ans += 1
                b = True

print(ans)