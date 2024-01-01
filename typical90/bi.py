Q = int(input())

A = []  # 山の上に追加したカード
B = []  # 山の下に追加したカード

for _ in range(Q):
    t, x = list(map(int, input().split(" ")))
    if t == 1:
        A.append(x)
    elif t == 2:
        B.append(x)
    else:
        if len(A) >= x:
            print(A[len(A) - x])
        else:
            print(B[x - len(A) - 1])