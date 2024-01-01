"""
木になっている
"""

from collections import deque


N, M = list(map(int, input().split(" ")))
P = list(map(int, input().split(" ")))
XY = [list(map(int, input().split(" "))) for _ in range(M)]

G = [[] for _ in range(N + 1)]

for i in range(N - 1):
    G[P[i]].append(i + 2)


ins = [-1] * (N + 1)
for x, y in XY:
    ins[x] = max(ins[x], y)

visited = [-1] * (N + 1)

q = deque()
q.append(1)
visited[1] = ins[1]

while q:
    s = q.popleft()
    for nex in G[s]:
        if visited[nex] >= 0:
            continue
        visited[nex] = max(visited[s] - 1, ins[nex])
        q.append(nex)

ans = 0
for d in visited:
    if d >= 0:
        ans += 1
print(ans)