from collections import deque


N, M, K, S, T, X = list(map(int, input().split(" ")))
UV = [list(map(int, input().split(" "))) for _ in range(M)]
MOD = 998244353

G = [[] for _ in range(N + 1)]

for u, v in UV:
    G[u].append(v)
    G[v].append(u)

dp = [[0] * (N + 1) for _ in range(K + 1)]

dp[0][0][S] = 1

q = deque()
q.append(S)
visited = [0] * (N + 1)
visited[S] = 1

while q:
    s = q.popleft()
    for nex in G[s]:
        dp[i + 1][nex] += dp[visited[s]][s]
        visited[nex] = visited[s] + 1
        if visited[nex] < K:
            q.append(nex)

print(dp)