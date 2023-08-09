H, W = list(map(int, input().split(" ")))
S = [input() for _ in range(H)]

l = 1000
r = -1
u = 1000
d = -1
for h in range(H):
    for w in range(W):
        if S[h][w] == ".":
            continue
        l = min(l, w)
        r = max(r, w)
        u = min(u, h)
        d = max(d, h)




for h in range(H):
    for w in range(W):
        if l <= w <= r and u <= h <= d:
            if S[h][w] == ".":
                print(str(h + 1) + " " + str(w + 1))
                exit()