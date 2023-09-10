A, B, X = list(map(int, input().split(" ")))

left = 1
right = 10 ** 9

while left + 1 < right:
    N = (left + right) // 2
    d = len(str(N))
    price = A * N + B * d
    if price == X:
        print(N)
        exit()
    if price < X:
        left = N
    else:
        right = N

d = len(str(right))
price = A * right + B * d
if price <= X:
    print(right)
    exit()

d = len(str(left))
price = A * left + B * d
if price <= X:
    print(left)
else:
    print(0)