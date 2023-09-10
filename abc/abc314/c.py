from collections import deque
N, M = list(map(int, input().split(" ")))
S = input()
C = list(map(int, input().split(" ")))

B = [deque() for _ in range(M + 1)]

for i in range(N):
    B[C[i]].append(S[i])

for i in range(M + 1):
    if len(B[i]) > 0:
        B[i].appendleft(B[i].pop())

ans = ""
for c in C:
    ans += B[c].popleft()

print(ans)