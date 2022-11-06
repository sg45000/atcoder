from typing import List
from collections import deque

def visit(start, N, G):
    q = deque()
    q.append(start)
    visited = [False] * (N+ 1)
    visited[start] = True
    while len(q) > 0:
        head = q.popleft()
        for goal in G[head]:
            if not visited[goal]:
                visited[goal] = True
                q.append(goal)
    
    return len([ok for ok in visited if ok])


def solve(N, M, loads):
    G: List[List[int]] = [[] for _ in range(N + 1)]

    for load in loads:
        G[load[0]].append(load[1])

    count = 0
    
    for start in range(1, N + 1):
        count += visit(start, N, G)

    print(count)


def main():
    N, M = map(int, input().split())
    loads = [list(map(int, input().split())) for _ in range(M)]
    solve(N, M, loads)          

main()