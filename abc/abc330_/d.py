N = int(input())
S = [input() for _ in range(N)]

R = [[0] * N for _ in range(N)]
C = [[0] * N for _ in range(N)]

R_count = [0] * N
C_count = [0] * N

for i in range(N):
    for j in range(N):
        if S[i][j] == 'o':
            R_count[i] += 1
            C_count[j] += 1

for i in range(N):
    for j in range(N):
        if S[i][j] == 'o':
            R[i][j] = R_count[i]
            C[i][j] = C_count[j]


ans = 0
for i in range(N):
    for j in range(N):
        if R[i][j] >= 2 and C[i][j] >= 2:
            ans += (R[i][j] - 1) * (C[i][j] - 1)

print(ans)