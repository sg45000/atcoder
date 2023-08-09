from collections import deque


H, W = list(map(int, input().split(" ")))
C = [input() for _ in range(H)]

def neighbors(n):
    y, x = n
    return [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]

def in_range(n):
    y, x = n
    return 0 <= y < H and 0 <= x < W

def start_position():
    for h in range(H):
        for w in range(W):
            if C[h][w] == "S":
                return (h, w)

visited = [[0] * W for _ in range(H)]

S = start_position()
visited[S[0]][S[1]] = 16

def bfs(start, bit):
    q = deque()
    q.append(start)
    while len(q) > 0:
        s = q.popleft()
        for y, x in filter(in_range, neighbors(s)):
            if C[y][x] == "." and not visited[y][x] & bit and not visited[y][x] & 16:
                visited[y][x] += bit
                q.append((y, x))


neighbor_S = list(filter(lambda a: C[a[0]][a[1]] == ".", filter(in_range, neighbors(S))))
answer = "No"
for bit, neighbor in zip([1, 2, 4, 8], neighbor_S):
    bfs(neighbor, bit)

for h in range(H):
    for w in range(W):
        if visited[h][w] not in [0, 1, 2, 4, 8, 16]:
            answer = "Yes"
            break

print(answer)