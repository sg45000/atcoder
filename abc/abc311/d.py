"""
方向毎に到達したかの状態を持つ
"""

from collections import deque

D = {
    (0, -1): 1,
    (1, 0): 2,
    (-1, 0): 4,
    (0, 1): 8
}

N, M = list(map(int, input().split(" ")))
S = [input() for _ in range(N)]

q = deque()
q.append((1, 1, (0, -1)))
q.append((1, 1, (1, 0)))
q.append((1, 1, (-1, 0)))
q.append((1, 1, (0, 1)))

visited = [[0] * M for _ in range(N)]
visited[1][1] = 15

while q:
    y, x, d = q.popleft()

    next_y = y + d[0]
    next_x = x + d[1]
    if S[next_y][next_x] == '.':
        if not visited[next_y][next_x] & D[d]:
            q.append((next_y, next_x, d))
            visited[next_y][next_x] |= D[d]
    else:
        if S[y][x - 1] == '.':
            q.append((y, x, (0, -1)))
        if S[y + 1][x] == '.':
            q.append((y, x, (1, 0)))
        if S[y - 1][x] == '.':
            q.append((y, x, (-1, 0)))
        if S[y][x + 1] == '.':
            q.append((y, x, (0, 1)))

ans = 0

for i in range(N):
    for j in range(M):
        if visited[i][j] > 0:
            ans += 1
print(ans)
