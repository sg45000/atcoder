import sys
N = int(input())

C = []
A = []
for i in range(N):
    C.append(int(sys.stdin.readline()))
    A.append(list(map(int, sys.stdin.readline().strip().split(" "))))

X = int(input())

ANS = [[] for _ in range(38)]

for i in range(N):
    c = C[i]
    for j in A[i]:
        if X == j:
            ANS[c].append(i + 1)

b = False
for a in ANS:
    if len(a) > 0:
        b = True
        print(len(a))
        print(" ".join(map(str, sorted(a))))
        break
if not b:
    print(0)