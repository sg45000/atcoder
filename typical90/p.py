

n = int(input())
a, b, c = list(map(int, input().split(" ")))

ans = 10000
for x in range(10000):
    for y in range(10000 - x):
        rest = n - x * a - y * b
        if 0 <= rest and rest % c == 0:
            z = rest // c
            ans = min(ans, x + y + z)
print(ans)