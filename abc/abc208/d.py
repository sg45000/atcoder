N, M = map(int, input().split())

inf = 10 ** 18
dist = [[inf] * N for _ in range(N)]

for i in range(N):
    dist[i][i] = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    dist[a - 1][b - 1] = c


def warshall_floyd(d):
    V = N
    ans = 0
    for k in range(V):
        # kを経由した場合の配列を作る
        d_via_k = [[0] * V for _ in range(V)]
        for i in range(V):
            for j in range(V):
                d_via_k[i][j] = min(d[i][j], d[i][k] + d[k][j])
        for i in range(V):
            for j in range(V):
                if d_via_k[i][j] != inf:
                    ans += d_via_k[i][j]
                    
        d = d_via_k
    return ans

print(warshall_floyd(dist))