"""
筒をdict(キーが先頭の色, 値が先頭以外のボールのリスト)で管理
ボールを取り出せる筒はキューに入れる
"""

from collections import deque


N, M = list(map(int, input().split(" ")))

D = dict()

Q = deque()

for _ in range(M):
    k = int(input())
    A = list(map(int, input().split(" ")))

    a0 = A[0]
    rest_a = A[1:]
    if a0 in D:
        rest = D.pop(a0)
        if len(rest) > 0:
            Q.append(rest)
        if len(rest_a) > 0:
            Q.append(rest_a)
    else:
        D[a0] = rest_a

while len(Q) > 0:
    a = Q.popleft()
    a0 = a[0]
    rest_a = a[1:]

    if a0 in D:
        rest = D.pop(a0)
        if len(rest) > 0:
            Q.append(rest)
        if len(rest_a) > 0:
            Q.append(rest_a)
    else:
        D[a0] = rest_a

ans = "No" if len(D) > 0 else "Yes"
print(ans)