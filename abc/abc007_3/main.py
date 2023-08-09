"""
基本的な幅優先探索で解ける
"""

from collections import deque

R, C = list(map(int, input().split(" ")))
sy, sx = list(map(int, input().split(" ")))
gy, gx = list(map(int, input().split(" ")))
M = [list(input()) for _ in range(R)]

def in_range(y, x):
    return (0 <= y < R) and (0 <= x < C)

q = deque()
q.append((sy - 1, sx - 1))

directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

visited = [[-1] * C for _ in range(R)]
visited[sy - 1][sx - 1] = 0  # スタート地点を初期化
while len(q) > 0:
    y, x = q.popleft()
    for dy, dx in directions:
        next_y = y + dy
        next_x = x + dx
        if not in_range(next_y, next_x):
            continue
        if visited[next_y][next_x] >= 0:
            continue
        if M[next_y][next_x] == "#":
            continue
        visited[next_y][next_x] = visited[y][x] + 1
        q.append((next_y, next_x))

print(visited[gy - 1][gx - 1])