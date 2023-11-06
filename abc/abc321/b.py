N, X = list(map(int, input().split(" ")))
A = list(map(int, input().split(" ")))

A.sort()

minimum = A[0]
maximum = A[-1]

total = sum(A) - minimum - maximum

for i in range(0, 101):
    if i <= minimum:
        if X <= total + minimum:
            print(i)
            exit()
    elif minimum < i < maximum:
        if X <= total + i:
            print(i)
            exit()
    else:
        if X <= total + maximum:
            print(i)
            exit()

print(-1)