"""
人の視線が効いている箇所に印をつけていく
最悪計算量はO(HW)なので問題ない

そのあとbfs グリッド上の幅優先探索なのでO(HW)
"""

import sys

from collections import deque

sys.setrecursionlimit(10 ** 9)

H, W = list(map(int, input().split(" ")))
A = [list(input()) for _ in range(H)]

def direction(yx):
    y, x = yx
    return [(y, x + 1), (y + 1, x), (y - 1, x), (y, x - 1)]

def in_range(yx):
    y, x = yx
    return 0 <= y < H and 0 <= x < W

def see(i, j, d):
    _y, _x = d
    y = i + _y
    x = j + _x
    if 0 <= y < H and 0 <= x < W:
        if A[y][x] == '.' or A[y][x] == 'X':
            A[y][x] = 'X'
            see(y, x, d)
        elif A[y][x] == 'S' or A[y][x] == 'G':
            see(y, x, d)
        else:
            return
    else:
        return

s = (0, 0)
g = (0, 0)
for i in range(H):
    for j in range(W):
        m = A[i][j]
        if m == '>':
            see(i, j, (0, 1))
        elif m == '<':
            see(i, j, (0, -1))
        elif m == 'v':
            see(i, j, (1, 0))
        elif m == '^':
            see(i, j, (-1, 0))
        elif m == 'S':
            s = (i, j)
        elif m == 'G':
            g = (i, j)


q = deque()
q.append(s)

visited = [[0] * W for _ in range(H)]

while q:
    s = q.popleft()
    for yx in filter(in_range, direction(s)):
        y, x = yx
        if (A[y][x] == '.' or A[y][x] == 'G') and visited[y][x] == 0:
            visited[y][x] = visited[s[0]][s[1]] + 1
            q.append((y, x))

if visited[g[0]][g[1]] > 0:
    print(visited[g[0]][g[1]])
else:
    print(-1)