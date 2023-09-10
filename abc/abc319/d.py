N, M = list(map(int, input().split(" ")))
L = list(map(int, input().split(" ")))

# 空白分を足しとく
for i in range(N):
    L[i] += 1

min_w = max(L) - 1
max_w = sum(L)

middle_w = 0
while min_w + 1 < max_w:
    middle_w = (min_w + max_w) // 2

    length = 0
    row_count = 1
    for i in range(N):
        length += L[i]
        if length > middle_w:
            row_count += 1
            length = L[i]
    if row_count <= M:
        max_w = middle_w
    else:
        min_w = middle_w

print(max_w - 1)