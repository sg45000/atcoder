
N, B, K = list(map(int, input().split(" ")))
C = list(map(int, input().split(" ")))

# 桁DPで解く
# dp[上から何桁目][現時点でのBで割ったあまり]
dp = [[0] * B for _ in range(N + 1)]

# 余り * 余りの行列
# ある余りが出る数値の桁を増やした後に割った余りは遷移可能なので1が入る
A = [[0] * B for _ in range(B)]
for j in range(B):
    for d in C:
        nex = (j * 10 + d) % B
        A[j][nex] += 1

MOD = 10 ** 9 + 7

def multiple(l, r):
    l_len = len(l)
    res = [[0] * l_len for _ in range(l_len)]

    r = zip(*r)
    for i in range(l_len):
        for j in range(l_len):
            res[i][j] = l[i][0] * r[j][0] + l[i][1] * r[j][1] + l[i][2] * r[j][2] 
    return res


cache = [A]
for b in range(64):
    cache.append(multiple(cache[b], A))

for b in range(64):
    if b >> 1 & 1:
        