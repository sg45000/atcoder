from bisect import bisect
N = int(input())
A = list(map(int, input().split(" ")))

a = sorted(list(set(A)))
duplicated = len(A) - len(a)

for i in range(1, N + 1):
    j = bisect(a, i)
    l = a[:j]
    r = a[j:]
    if i > len(l) + (len(r) + duplicated) // 2:
        print(i - 1)
        break
 