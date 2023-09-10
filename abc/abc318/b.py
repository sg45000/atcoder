N = int(input())

G = [[0] * 100 for _ in range(100)]

for _ in range(N):
    a, b, c, d = list(map(int, input().split(" ")))
    for x in range(a, b):
        for y in range(c, d):
            G[x][y] = 1
ans = 0
for x in range(100):
    for y in range(100):
        ans += G[x][y]

print(ans)