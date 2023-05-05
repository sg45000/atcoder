# https://atcoder.jp/contests/typical90/tasks/typical90_c

from collections import deque

N = int(input())
loads = [list(map(int, input().split(" "))) for _ in range(N - 1)]
graph = [set() for _ in range(N + 1)]

for load in loads:
    graph[load[0]].add(load[1])
    graph[load[1]].add(load[0])


def get_distance(start):
    q = deque()
    q.append(start)

    dist = [0] * (N + 1)

    while len(q) > 0:
        i = q.popleft()
        
        for next_i in graph[i]:
            if dist[i] == 0:
                dist[next_i] = dist[i] + 1
                q.append(next_i)
    max_dist = 0
    for min_dist in dist:
        max_dist = max(max_dist, min_dist)
    return max_dist


from_1 = get_distance(1)
print(get_distance(from_1) + 1)
