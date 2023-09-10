import itertools

perm = itertools.permutations([i for i in range(1, 10)], 9)


C = [list(map(int, input().split(" "))) for _ in range(3)]
C = list(itertools.chain.from_iterable(C))

ans = 0
for p in list(perm):
    c1 = []
    c2 = []
    c3 = []
    r1 = []
    r2 = []
    r3 = []
    naname1 = []
    naname2 = []
    for i in p:
        if i == 1:
            c1.append(C[i - 1])
            r1.append(C[i - 1])
            naname1.append(C[i - 1])
        elif i == 2:
            c2.append(C[i - 1])
            r1.append(C[i - 1])
        elif i == 3:
            c3.append(C[i - 1])
            r1.append(C[i - 1])
            naname2.append(C[i - 1]) 
        elif i == 4:
            c1.append(C[i - 1])
            r2.append(C[i - 1])
        elif i == 5:
            c2.append(C[i - 1])
            r2.append(C[i - 1])
            naname1.append(C[i - 1])
            naname2.append(C[i - 1])
        elif i == 6:
            c3.append(C[i - 1])
            r2.append(C[i - 1])
        elif i == 7:
            c1.append(C[i - 1])
            r3.append(C[i - 1])
            naname2.append(C[i - 1])
        elif i == 8:
            c2.append(C[i - 1])
            r3.append(C[i - 1])
        elif i == 9:
            c3.append(C[i - 1])
            r3.append(C[i - 1])
            naname1.append(C[i - 1])
    if c1[0] != c1[1] and c2[0] != c2[1] and c3[0] != c3[1] and r1[0] != r1[1] and r2[0] != r2[1] and r3[0] != r3[1] and naname1[0] != naname1[1] and naname2[0] != naname2[1]:
        ans += 1

a = 362880
print(ans / a)