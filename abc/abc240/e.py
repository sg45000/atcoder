N = int(input())
LR = [list(map(int, input().split(" "))) for _ in range(N - 1)]

G = [[] for _ in range(N)]

for l , r in LR:
    G[l - 1].append(r - 1)
    G[r - 1].append(l - 1)

l = [0] * N
r = [0] * N
x = 1


def dfs(v, p=-1):
    global x
    l[v] = x
    for u in G[v]:
        if u == p:
            continue
        dfs(u, v)
    if len(G[v]) == 1 and p != -1:
        x += 1
    r[v] = x - 1


dfs(0)

for a, b in zip(l, r):
    print(a, b)