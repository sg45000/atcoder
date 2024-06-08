from collections import deque

#############################
# input
#############################


get_ints = lambda: list(map(int, input().split()))
get_ints_n_lines = lambda n: [list(map(int, input().split())) for _ in range(n)]

get_chars = lambda: list(input())
get_chars_n_lines = lambda n: [input() for _ in range(n)]
get_chars_with_trim = lambda s: list(input().split(s))


#############################
# main
#############################
def dist(t):
    i, j = t
    return list(
        filter(
            lambda x: 0 <= x[0] < H and 0 <= x[1] < W,
            [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)],
        )
    )


W, H = get_ints()
A = [get_chars_with_trim(" ") for _ in range(H)]

start = (0, 0)
goal = (0, 0)
for i in range(H):
    for j in range(W):
        if A[i][j] == "s":
            start = (i, j)
        if A[i][j] == "g":
            goal = (i, j)

q = deque([start])
visited = [[0] * W for _ in range(H)]
visited[start[0]][start[1]] = 1
while q:
    s = q.popleft()
    for d_i, d_j in dist(s):
        if visited[d_i][d_j] > 0:
            continue
        if A[d_i][d_j] == "1":
            continue
        visited[d_i][d_j] = visited[s[0]][s[1]] + 1
        q.append((d_i, d_j))

if visited[goal[0]][goal[1]] == 0:
    print("Fail")
else:
    print(visited[goal[0]][goal[1]] - 1)
