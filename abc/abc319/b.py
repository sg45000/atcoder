N = int(input())

ans = ""

for i in range(N + 1):
    l = []
    for j in range(1, 10):
        a = N / j
        if a == int(a):
            if i == 0:
                l.append(j)
            elif int(a) <= i and i % int(a) == 0:
                l.append(j)
    print(l)
    if len(l) > 0:
        ans += str(min(l))
    else:
        ans += "-"

print(ans)