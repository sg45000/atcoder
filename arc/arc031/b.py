import sys
sys.setrecursionlimit(10 ** 9)


G = [list(input()) for _ in range(10)]

grand_num = 0
for r in G:
    for c in r:
        if c == 'o':
            grand_num += 1

grand_count = 0
visited = [[-1] * 10 for _ in range(10)]


def neighbors(i, j):
    return list(filter(ok, ((i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1))))


def ok(ij):
    i, j = ij
    return 0 <= i <= 9 and 0 <= j <= 9


def dfs(i, j):
    global grand_count
    for n_i, n_j in neighbors(i, j):
        if visited[n_i][n_j] < 0 and G[n_i][n_j] == 'o':
            visited[n_i][n_j] = 1
            grand_count += 1
            dfs(n_i, n_j)


for i in range(10):
    for j in range(10):
        grand_count = 0
        visited = [[-1] * 10 for _ in range(10)]
        dfs(i, j)
        if grand_num == grand_count:
            print("YES")
            exit()

print("NO")
