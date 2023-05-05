from collections import deque
N = int(input())
AB = [list(map(int, input().split(" "))) for _ in range(N - 1)]

G = [[] for _ in range(N + 1)]
for a,b in AB:
    G[a].append(b)
    G[b].append(a)

q = deque()
q.append(1)
visited = [-1] * (N + 1)
visited[1] = 0
while len(q) > 0:
    n = q.popleft()
    for neighbor in G[n]:
        if visited[neighbor] < 0:
            visited[neighbor] = visited[n] + 1
            q.append(neighbor)

def is_even(v):
    return v % 2 == 0

if len(list(filter(is_even, visited))) >= N // 2:
    print(str.join(" ", [str(i + 1) for i, v in enumerate(visited[1:]) if is_even(v)][:N // 2]))
else:
    print(str.join(" ", [str(i + 1) for i, v in enumerate(visited[1:]) if not is_even(v)][:N // 2]))

