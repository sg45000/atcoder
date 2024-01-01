from itertools import accumulate

N, Q = list(map(int, input().split(" ")))
P = [input() for _ in range(N)]
P_ACC = []

P_COUNT = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if P[i][j] == 'B':
            P_COUNT[i][j] = 1

for i in range(N):
    P_ACC.append(accumulate(P_COUNT[i]))

for _ in range(Q):
    a, b, c, d = list(map(int, input().split(" ")))
    rest_height = (c - a + 1) % N
    rest_width = (d - b + 1) % N

    height_count = (c - a + 1) // N
    width_count = (d - b + 1) // N

    for i in range(rest_height):
        for j in range(rest_width):
            P_ACC[a % N + 1 + i][-1 if width_count > 0 else b % N + 1]
            
