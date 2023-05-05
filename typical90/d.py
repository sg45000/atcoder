H, W = list(map(int, input().split(" ")))
A = [list(map(int, input().split(" "))) for _ in range(H)]

memoH = list(map(sum, A)) # 各行の合計
memoW = [sum(column) for column in zip(*A)] # 各列の合計

answer = [[] for _ in range(H)]
for h in range(H):
    for w in range(W):
        answer[h].append(memoH[h] + memoW[w] - A[h][w])

for a in answer:
    print(" ".join(list(map(str, a))))
