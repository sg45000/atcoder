
N, Q = list(map(int, input().split(" ")))
C = list(map(int, input().split(" ")))


D = [set() for _ in range(N)]

for i in range(N):
    D[i].update({C[i]})

i = 1
for _ in range(Q):
    a, b = list(map(int, input().split(" ")))
    a -= 1
    b -= 1
    if len(D[a]) > len(D[b]): 
        D[a].update(D[b])
        D[b] = set()
    else:
        D[b].update(D[a])
        D[a] = set()
    
    print(len(D[b]))
