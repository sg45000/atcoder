X = int(input())

ans = 0
for i in reversed(range(1, 35)):
    for j in range(2, 10):
        if X < i ** j:
            continue
        ans = max(i ** j, ans)
print(ans)
