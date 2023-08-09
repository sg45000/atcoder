N = int(input())
SA = [tuple(input().split(" ")) for _ in range(N)]

m = 10 ** 10
i = 0
for j, sa in enumerate(SA):
    if int(sa[1]) < m: 
        m = int(sa[1])
        i = j

SA = SA[i:] + SA[:i]

for s, _ in SA:
    print(s)

