N, Q = list(map(int, input().split(" ")))
S = input()
LR = [list(map(int, input().split(" "))) for _ in range(Q)]

D = [0] * (N + 1)

for i in range(N - 1):
    if S[i] == S[i + 1]:
        D[i + 1] = D[i] + 1
    else:
        D[i + 1] = D[i]

for l, r in LR:
    print(D[r - 1] - D[l - 1])