H, W, K = list(map(int, input().split(' ')))
C = [input() for _ in range(H)]

M = [[0] * W for _ in range(H)]

for h in range(H):
    for w in range(W):
        if C[h][w] == "#":
            M[h][w] = 1

cnt = 0
for bit in range(2 ** (H + W)):
    m = [[*m] for m in M]
    for i in range(H + W):
        if bit >> i & 1:
            if i < H:
                for w in range(W):
                    m[i][w] = 0
            else:
                for h in range(H):
                    m[h][i - H] = 0
    # sum([[1,2,3], [4,5,6]], []) == [1,2,3,4,5,6]になる。flatmapのやり方
    if sum(sum(m, [])) == K:
        cnt += 1
print(cnt)