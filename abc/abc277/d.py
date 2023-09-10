N, M = list(map(int, input().split(" ")))
A = list(map(int, input().split(" ")))

A.sort()
now = 0
start = 0
pre = 0
for i, a in enumerate(A):
    if a == now:
        continue
    elif a == now + 1:
        now += 1
    else:
        pre = a
        start = i
        break

# 探索を始める
# 今のカードのスコア+1のカードへ遷移する
maximum = 0
m = 0
for a in A[start:]:
    if a == pre or (a == (pre + 1) % M):
        m += a
    else:
        maximum = max(maximum, m)
        m = a
    pre = a
maximum = max(maximum, m)

for a in A[:start]:
    if a == pre or (a == (pre + 1) % M):
        m += a
    else:
        maximum = max(maximum, m)
        m = a
    pre = a
maximum = max(maximum, m)

all_score = sum(A)

print(all_score - maximum)