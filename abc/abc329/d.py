N, M = list(map(int, input().split(" ")))
A = list(map(int, input().split(" ")))

m = [0] * (N + 1)

top = 0
for a in A:
    m[a] += 1
    if m[a] > m[top]:
        top = a
    elif m[a] == m[top]:
        top = min(top, a)
    print(top)