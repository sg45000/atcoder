import itertools
from collections import deque

N, M, K = list(map(int, input().split(" ")))
VUW = [list(map(int, input().split(" "))) for _ in range(M)]

G = [[] for _ in range(N)]

for v, u, w in VUW:
    G[v - 1].append(u - 1)
    G[u - 1].append(v - 1)

comb = itertools.combinations(VUW, N - 1)

ans = float("inf")

for vuw_list in comb:
    G = [[] for _ in range(N)]
    for v, u, w in vuw_list:
        G[v - 1].append(u - 1)
        G[u - 1].append(v - 1)
    q = deque()
    q.append(0)
    visited = [False] * N

    while q:
        s = q.popleft()
        for nex in G[s]:
            if not visited[nex]:
                visited[nex] = True
                q.append(nex)
    SUM = 0
    if all(visited):
        for v, u, w in vuw_list:
            SUM += w
            SUM %= K
        ans = min(ans, SUM)
print(ans)