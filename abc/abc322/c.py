N, M = list(map(int, input().split(" ")))
A = list(map(int, input().split(" ")))

j = 0
last_day = A[0]
for i in range(N):
    if last_day < i + 1:
        j += 1
        last_day = A[j]
    print(last_day - (i + 1))