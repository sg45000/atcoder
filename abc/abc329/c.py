N = int(input())
S = input()

D = {}

s = 0
c = ""
count = 0
for i in range(N):
    if c != S[i]:
        count = 0
    c = S[i]
    if count == 0:
        if S[i] in D:
            D[S[i]] = max(D[S[i]], 1)
        else:
            D[S[i]] = 1
        count += 1
    else:
        count += 1
        D[S[i]] = max(D[S[i]], count)
    

ans = 0
for i in D.values():
    ans += i

print(ans)