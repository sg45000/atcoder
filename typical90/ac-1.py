W, N = list(map(int, input().split(" ")))
LR = [list(map(int, input().split(" "))) for _ in range(N)]

memo = [0] * (W + 1)

for l, r in LR:
    max_height = 0
    for h in memo[l:r + 1]:
        max_height = max(max_height, h)
    for i in range(l, r + 1):
        memo[i] = max_height + 1
    print(max_height + 1)
