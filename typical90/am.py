N = int(input())
AB = [list(map(int, input().split(" "))) for _ in range(N - 1)]

G = [[]] * N
for i in range(N):
    a, b = AB[i]
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

## ライブラリ

def merge(a, b):
    return a + b

def add_root(a):
    return a + 1

identity = 0


def dfs(v, p):
    deg = len(G[v])