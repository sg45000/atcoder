import sys
sys.setrecursionlimit(10 ** 8)

N = int(input())
Q = int(input())

A = [(None, None) for _ in range(N + 1)]


def query(x, y, goal, v):
    if x < y:
        if A[x][1] is None:
            return 'Ambiguous'
        if goal == y:
            return A[x][1] - v

        return query(x + 1, y + 1, goal, A[x][1] - v)
    if x > y:
        if A[x][0] is None:
            return 'Ambiguous'
        if goal == y:
            return A[x][0] - v
        return query(x - 1, y - 1, goal, A[x][0] - v)


for _ in range(Q):
    T, X, Y, V = list(map(int, input().split()))
    if T == 0:
        A[X] = (A[X][0], V)
        A[Y] = (V, A[Y][1])
    else:
        if X == Y:
            print(V)
        else:
            ans = query(X, X + 1 if X < Y else X - 1, Y, V)
            print(ans)
