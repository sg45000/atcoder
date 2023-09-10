N, D = list(map(int, input().split(" ")))
LR = [list(map(int, input().split(" "))) for _ in range(N)]

LR.sort(key=lambda x: x[1]) # Rでソート

# パンチは最も小さいR + D - 1 の範囲に放つ
# 
ans = 1
last_r = LR[0][1] + D - 1
for l, r in LR:
    if last_r < l:
        last_r = r + D - 1
        ans += 1

print(ans)