B = int(input())

for a in range(1, 30):
    if B == a ** a:
        print(a)
        exit()

print(-1)