from collections import deque

def check(start, end, n, graph):
    q = deque()
    visited = [False] * (n + 1)
    q.append(start)
    visited[start] = True
    while len(q) > 0:
        a = q.popleft()
        for b in graph[a]:
            if not (a == start and b == end) and not visited[b]:
                visited[b] = True
                q.append(b)
    return all(visited[1:])


def solve(n, m, bridges, graph):
    count = 0
    for b in bridges:
        if check(b[0], b[1], n, graph):
            count += 1
    return count


def main():
    N, M = map(int, input().split())
    BS = [list(map(int, input().split())) for _ in range(M)]
    G = [[] for _ in range(N + 1)]
    for B in BS:
        G[B[0]].append(B[1])
        G[B[1]].append(B[0])
    return M - solve(N, M, BS, G)          

print(main())