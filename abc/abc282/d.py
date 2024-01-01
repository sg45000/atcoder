from collections import deque


N, M = list(map(int, input().split()))


def UndirectedGraph():
    G = [[] for _ in range(N + 1)]

    for _ in range(M):
        u, v = list(map(int, input().split()))
        G[u].append(v)
        G[v].append(u)
    return G


def odd(n):
    return n % 2 != 0


def even(n):
    return n % 2 == 0


def equal_parity(a, b):
    return odd(a) and odd(b)


visited = [-1] * (N + 1)

def bfs(start, G):
    r = [1, 0]
    q = deque()
    q.append(start)
    visited[start] = 0

    while q:
        s = q.popleft()

        for nex in G[s]:
            if visited[nex] > -1:
                if visited[nex] == visited[s]:
                    return [-1, -1]
                continue
            visited[nex] = visited[s] ^ 1
            q.append(nex)
            r[visited[nex]] += 1
    return r


ans = (N * (N - 1)) // 2
G = UndirectedGraph()
for i in range(1, N + 1):
    if visited[i] == -1:
        a = bfs(i, G)
        if a[0] == -1:
            print(0)
            exit()
        else:
            ans -= (a[0] * (a[0] - 1)) // 2
            ans -= (a[1] * (a[1] - 1)) // 2

print(ans - M)


