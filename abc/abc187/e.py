from collections import deque


N = int(input())
AB = [list(map(int, input().split(" "))) for _ in range(N - 1)]

G = [[] for _ in range(N)]

for a, b in AB:
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

depth = [-1] * N
depth[0] = 0  # 頂点1を根とする

q = deque()
q.append(0)

while q:
    s = q.popleft()
    for nex in G[s]:
        if depth[nex] == -1:
            depth[nex] = depth[s] + 1
            q.append(nex)

Q = int(input())

M = [0] * N
for i in range(Q):
    T, E, X = list(map(int, input().split(" ")))
    a, b = AB[E - 1]
    a -= 1
    b -= 1
    if depth[a] > depth[b]:
        a, b = b, a
        T ^= 3
    if T == 1:
        M[0] += X
        M[b] -= X
    else:
        M[b] += X




q = deque()
q.append(0)
while q:
    s = q.popleft()
    for nex in G[s]:
        if depth[nex] > depth[s]:
            M[nex] += M[s]
            q.append(nex)

for a in M:
    print(a)