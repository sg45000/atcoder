

from collections import deque


N, M = list(map(int, input().split(" ")))
A = list(map(int, input().split(" ")))
B = list(map(int, input().split(" ")))

G = [[] for _ in range(N)] 

for i in range(M):
    G[A[i] - 1].append(B[i] - 1)
    G[B[i] - 1].append(A[i] - 1)

visited = [-1] * N

def bfs(s):
    q = deque()
    q.append(s)
    visited[s] += 1

    while q:
        s = q.popleft()
        
        for nex in G[s]:
            if visited[nex] < 0:
                q.append(nex)
                visited[nex] = visited[s] + 1


for i in range(N):
    if visited[i] < 0:
        bfs(i)

for i in range(M):
    if visited[A[i] - 1] % 2 == visited[B[i] - 1] % 2:
        print("No")
        exit()

print("Yes")