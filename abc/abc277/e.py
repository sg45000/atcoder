import sys
import heapq

input = sys.stdin.readline

n, m, k = map(int, input().split())
edge = [[] for _ in range(2 * n)]
for _ in range(m):
    u, v, a = map(int, input().split())
    if a:
        edge[u - 1].append(v - 1)
        edge[v - 1].append(u - 1)
    else:
        edge[u + n - 1].append(v + n - 1)
        edge[v + n - 1].append(u + n - 1)
s = list(map(int, input().split()))
for si in s:
    edge[si - 1].append(si + n - 1)
    edge[si + n - 1].append(si - 1)

hq = [(0, 0)]
seen = [0] * (2 * n)
seen[0] = 1
heapq.heapify(hq)
while hq:
    w, v = heapq.heappop(hq)
    for nv in edge[v]:
        if nv == n - 1 or nv == 2 * n - 1:
            print(w + 1)
            exit()
        if seen[nv]:
            continue
        if (v < n and nv == v + n) or (v >= n and nv == v - n):
            heapq.heappush(hq, (w, nv))
        else:
            heapq.heappush(hq, (w + 1, nv))
        seen[nv] = 1
print(-1)