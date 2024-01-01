import sys
import heapq

input = sys.stdin.readline

N, M, K = list(map(int, input().split()))
UVA = [list(map(int, input().split())) for _ in range(M)]
S = list(map(int, input().split()))

G = [[] for _ in range(2 * N)]
for u, v, a in UVA:
    if a > 0:
        G[u - 1].append(v - 1)
        G[v - 1].append(u - 1)
    else:
        G[u + N - 1].append(v + N - 1)
        G[v + N - 1].append(u + N - 1)

for s in S:
    G[s - 1].append(s + N - 1)
    G[s + N - 1].append(s - 1)

q = [(0, 0)]
visited = [0] * (2 * N)
visited[0] = 1

heapq.heapify(q)

while q:
    w, v = heapq.heappop(q)
    for nv in G[v]:
        if nv == N - 1 or nv == 2 * N - 1:
            print(w + 1)
            exit()
        if visited[nv]:
            continue
        if (v < N and nv == v + N) or (v >= N and nv == v - N):
            heapq.heappush(q, (w, nv))
        else:
            heapq.heappush(q, (w + 1, nv))
        visited[nv] = 1

print(-1)
