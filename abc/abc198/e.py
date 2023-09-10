import sys

sys.setrecursionlimit(1000000)

N = int(input())
C = list(map(int, input().split(" ")))

G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = list(map(int, input().split(" ")))
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)



color = [0] * (10 ** 5 + 100)
good = [False] * N


def dfs(i, parent):
    if color[C[i]] == 0:
        good[i] = True
    color[C[i]] += 1
    for nex in G[i]:
        if parent != nex:
            dfs(nex, i)
    color[C[i]] -= 1


dfs(0, -1)

for i in range(N):
    if good[i]:
        print(i + 1)