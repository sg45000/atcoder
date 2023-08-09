from collections import defaultdict, deque
import math 

N, D = list(map(int, input().split(" ")))
XY = [list(map(int, input().split(" "))) for _ in range(N)]

G = defaultdict(list)

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        x1, y1 = XY[i]
        x2, y2 = XY[j]
        if math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) <= D:
            G[i].append(j)


q = deque()

visited = [False] * (N)
visited[0] = True
q.append(0)

while len(q) > 0:
    i = q.popleft()
    for j in G[i]:
        if not visited[j]:
            visited[j] = True
            q.append(j)

for v in visited:
    print("Yes") if v else print("No")