from collections import deque, defaultdict


def dijkstra(edges, n, s):
    """ 経路の表現
            [終点, 辺の値]
            A, B, C, D, ... → 0, 1, 2, ...とする """
    nodes = [float('inf')] * n
    nodes[s] = 0
    fixed = [False] * n
    non_fixed = [s]


    while len(non_fixed) > 0:
        start = 0
        min_cost = float('inf')
        for i in enumerate(non_fixed):
            if nodes[i] <= min_cost:
                min_cost = nodes[i]
                start = i
            
        fixed[start] = True

        for end, cost in edges[start]:
            if not fixed[e] and nodes[end]:
                non_fixed.append(end):



# N, M = list(map(int, input().split(" ")))
# ABC = [list(map(int, input().split(" "))) for _ in range(M)]
N = 4
M = 3
ABC = [[1, 2, 1], [2, 3, 10], [3, 4, 100]]


G = defaultdict(list)
for a, b, c in ABC:
    G[a - 1].append((b - 1, c))

dist_1 = dijkstra(G, N, N - 1)
print(dist_1)

# for (d1, dn) in zip(dist_1, dist_n):
#     print(d1 + dn)
