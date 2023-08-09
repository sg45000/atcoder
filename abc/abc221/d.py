N = int(input())
AB = [list(map(int, input().split(" "))) for _ in range(N)]

D = []

for a, b in AB:
    D.append((a, 1))
    D.append((a + b, -1))


def fst(x):
    return x[0]


D.sort(key=fst)

answer = [0] * (N + 1)
pre_day = 0
people = 0

for day, p in D:
    answer[people] += day - pre_day
    pre_day = day
    people += p


print(' '.join(map(str, answer[1:])))