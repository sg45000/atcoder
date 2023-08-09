N, Q = list(map(int, input().split(" ")))
A = list(map(int, input().split(" ")))
TXY = [list(map(int, input().split(" "))) for _ in range(Q)]

D = dict()
for i, a in enumerate(A):
    D[i] = a

first_index = 0
for t, x, y in TXY:

    if t == 1:
        x = x - 1 + first_index
        y = y - 1 + first_index
        D[y], D[x] = D[x], D[y]
    elif t == 2:
        first_index -= 1
        D[first_index] = D[first_index + N]
    else:
        print(D[first_index + x - 1])
        