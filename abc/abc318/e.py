from collections import defaultdict
N = int(input())
A = list(map(int, input().split(" ")))

A.sort()

D = defaultdict(int)
ik = []
for a in A:
    D[a] += 1

for a, count in list(D.items()):
    if 2 <= count:
        ik.append(a)

ans = 0
for i in ik:
    ans = (i * (i - 1) // 2) * (N - i)

print(ans)