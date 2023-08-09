W, N = list(map(int, input().split(" ")))
LR = [list(map(int, input().split(" "))) for _ in range(N)]

coord = set()
for l, r in LR:
    coord.add(l)
    coord.add(r)

compressed_coord = dict()
for i, c in enumerate(sorted(coord)):
    compressed_coord[c] = i

memo = [0] * (2 * N + 1)

for l, r in LR:
    max_height = 0
    for h in memo[compressed_coord[l]:compressed_coord[r] + 1]:
        max_height = max(max_height, h)
    for i in range(compressed_coord[l], compressed_coord[r] + 1):
        memo[i] = max_height + 1
    print(max_height + 1)
