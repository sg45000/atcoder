N = int(input())
S = list(input())
Q = int(input())
TXC = [list(input().split(" ")) for _ in range(Q)]

all_rep = -1
op = 0
for i in reversed(range(Q)):
    t, x, c = TXC[i]
    t = int(t)
    if t == 2 or t == 3:
        all_rep = i
        op = t
        break

for i in range(Q):
    t, x, c = TXC[i]
    t = int(t)
    x = int(x) - 1
    if t == 1:
        S[x] = c
    elif i == all_rep:
        if op == 2:
            S = list("".join(S).lower())
        elif op == 3:
            S = list("".join(S).upper())

print("".join(S))
