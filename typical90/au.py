N = int(input())
S = input()
T = input()

def color(s, t):
    if s == t:
        return s
    if s != 'G' and t != 'G':
        return 'G'
    elif s != 'R' and t != 'R':
        return 'R'
    else:
        return 'B'

def same(xs):
    f = xs[0]
    for x in xs:
        if f != x:
            return False
    return True

ans = 0
for k in range(-N + 1, N):
    colors = []
    for i in range(N):
        if 0 <= i + k < N:
            colors.append(color(S[i], T[i + k]))
    if len(colors) > 0 and same(colors):
        ans += 1

print(ans)
