from collections import deque


H, W = list(map(int, input().split(" ")))
rs, cs = list(map(int, input().split(" ")))
rs, cs = rs - 1, cs - 1
rt, ct = list(map(int, input().split(" ")))
rt, ct = rt - 1, ct - 1
S = [input() for _ in range(H)]

# 0=上, 1=右, 2=下, 3=左 とする 
def neighbors(y, x):
    return [(0, y - 1, x), (1, y, x + 1), (2, y + 1, x), (3, y, x - 1)]


def in_range(y, x):
    return 0 <= y < H and 0 <= x < W


def bfs():
    q = deque()

    visited = [[[float("inf")] * 4 for _ in range(W)] for _ in range(H)]
    for i in range(4):
        q.append((i, rs, cs))
        visited[rs][cs][i] = 0

    while len(q) > 0:
        s = q.popleft()
        s_d, s_y, s_x = s
        for d, y, x in neighbors(s_y, s_x):
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


ans = bfs()
print(ans)