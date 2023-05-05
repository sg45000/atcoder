N = int(input())
CP = [list(map(int, input().split(" "))) for _ in range(N)]
Q = int(input())
LR = [list(map(int, input().split(" "))) for _ in range(Q)]

sum1 = [0] * (N + 2)
sum2 = [0] * (N + 2)


for i, cp in enumerate(CP):
    c, p = cp
    if c == 1:
        sum1[i + 1] += sum1[i] + p
        sum2[i + 1] += sum2[i]
    else:
        sum1[i + 1] += sum1[i]
        sum2[i + 1] += sum2[i] + p


for l, r in LR:
    print(str(sum1[r] - sum1[l - 1]) + " " + str(sum2[r] - sum2[l - 1]))

