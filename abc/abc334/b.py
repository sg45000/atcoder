A, M, L, R = list(map(int, input().split(" ")))

if A < L:
    s = L + (M - ((L - A) % M))
    if s > R:
        print(0)
    else:
        print((R - s + 1) // M + 1)
elif L <= A <= R:
    a = (R - A + 1) // M + (A - L + 1) // M
    print(a + 1)
else:
    L = -L
    R = -R
    A = -A
    s = L + (M - ((L - A) % M))
    if s > R:
        print(0)
    else:
        print((R - s + 1) // M + 1)