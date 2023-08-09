"""
全てのマスからBFSしてそれぞれのmax_distanceを求める
O(HW ^ 2)
"""

from collections import deque


H, W = list(map(int, input().split(" ")))
S = [input() for _ in range(H)]

def neighbors(n):
    y, x = n
    return [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]

def in_range(n):
    y, x = n
    return 0 <= y < H and 0 <= x < W

def bfs(start):
    q = deque()
    q.append(start)

    visited = [[-1] * W for _ in range(H)]
    visited[start[0]][start[1]] = 0

    while len(q) > 0:
        s = q.popleft()
        neighbor_cells = list(filter(in_range, neighbors(s)))
        for nex in neighbor_cells:
            y, x = nex
            if S[y][x] == "#":
                continue
            if visited[y][x] >= 0:
                continue
            visited[y][x] = visited[s[0]][s[1]] + 1
            q.append(nex)

    max_distance = 0
    for i in range(H):
        for j in range(W):
            if max_distance < visited[i][j]:
                max_distance = visited[i][j]
    return max_distance


max_distance = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            max_distance = max(max_distance, bfs((i, j)))

print(max_distance)