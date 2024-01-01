import bisect
from itertools import accumulate


N, Q = list(map(int, input().split()))
R = list(map(int, input().split()))
R.sort()

ACC = list(accumulate(R))

for _ in range(Q):
    X = int(input())
    a = bisect.bisect(ACC, X)
    print(a)