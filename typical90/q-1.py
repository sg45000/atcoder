N, M = list(map(int, input().split(" ")))
LR = [list(map(int, input().split(" "))) for _ in range(M)]

count = 0
for i in range(M):
    for j in range(i + 1, M):
        ls, rs = LR[i]
        lt, rt = LR[j]
        if ls < lt < rs < rt or lt < ls < rt < rs:
            count += 1
print(count)