N = int(input())
R = input()
C = input()

G = [["."] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        G[i][j]