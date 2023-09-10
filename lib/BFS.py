from collections import deque

"""
n: ノード総数
s: 最初に探索するノード
g: グラフ
"""
def bfs(n, s, g, unit, operation):
    q = deque()
    q.append(s)
    visited = [unit] * n

    while q:
        v = s.popleft()
        for nex in g[v]:
            if unit < visited[nex]:
                continue
            visited[nex] = operation(visited[v])
            q.append(nex)
            
    return visited


def bfs_01(n, s, g, ):
    q = deque()

    visited = [[[float("inf")] * 4 for _ in range(W)] for _ in range(H)]
    for i in range(4):
        q.append((i, rs, cs))
        visited[rs][cs][i] = 0

    while len(q) > 0:
        s = q.popleft()
        s_d, s_y, s_x = s
        for d, y, x in g(s_y, s_x):
            if not in_range(y, x):
                continue
            if S[y][x] == "#":
                continue
            if d == s_d:
                if visited[s_y][s_x][s_d] < visited[y][x][d]:
                    visited[y][x][d] = visited[s_y][s_x][s_d]
                    q.appendleft((d, y, x))
            else:
                if visited[s_y][s_x][s_d] + 1 < visited[y][x][d]:
                    visited[y][x][d] = visited[s_y][s_x][s_d] + 1
                    q.append((d, y, x))
    
    return min(visited[rt][ct])
