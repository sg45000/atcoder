import operator
N, K = list(map(int, input().split(" ")))
T = [list(map(int, input().split(" "))) for _ in range(N)]


def dfs(i, s, op):
    if i == N:
        return s == 0

    for k in range(K):
        if dfs(i + 1, op(s, T[i][k]), op):
            return True

    return False


print("Found") if dfs(0, 0, operator.xor) else print("Nothing")