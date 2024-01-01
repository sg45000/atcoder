"""
ビット全探索
"""

H, W = list(map(int, input().split(" ")))
P = [list(map(int, input().split(" "))) for _ in range(H)]

B = [[0] * (H * W + 1) for _ in range(2 ** (H + 1))]

for i in range(1, 2 ** (H + 1)):
    for j in range(W):
        num = 0
        p = 0
        for k in range(H):
            if i & 1 << k:
                if num == 0:
                    num = P[k][j]
                if num == P[k][j]:
                    p += 1
                else:
                    p = 0
                    B[i][num] = max(p, B[i][num])
                    break
        B[i][num] += p

ans = 0
for b in B:
    for a in b:
        ans = max(a, ans)

print(ans)