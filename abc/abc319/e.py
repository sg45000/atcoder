N, X, Y = list(map(int, input().split(" ")))
PT = [list(map(int, input().split(" "))) for _ in range(N-1)]

Q = int(input())

q_memo = [0] * Q
Q_list = []
for i in range(Q):
    q = int(input())
    Q_list.append(q + X)
    p = PT[0][0]
    if (q + X) % p != 0:
        q_memo[i] = p - ((q + X) % p)

m = PT[0][1]
for p, t in PT[1:]:
    if m % p == 0:
        m += t
    else:
        m += p - (m % p) + t


for i in range(Q):
    print(Q_list[i] + q_memo[i] + m + Y)