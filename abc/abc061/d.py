def bellman_ford(edges, start, num_v):
    INF = float('inf')
    dist = [INF] * (num_v + 1)
    dist[start] = 0

    for _ in range(num_v):
        updated = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] - w < dist[v]:
                dist[v] = dist[u] - w
                updated = True
        if not updated:
            break

    # Check for negative cycles
    for u, v, w in edges:
        if dist[u] != INF and dist[u] - w < dist[v]:
            return None  # negative cycle detected

    return dist


N, M = map(int, input().split())
ABC = [tuple(map(int, input().split(" "))) for _ in range(M)]

ans = bellman_ford(ABC, 1, N)

print(-ans[-1] if ans else "inf")