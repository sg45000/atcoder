from itertools import combinations
from bisect import bisect

N, K, P = list(map(int, input().split()))
A = list(map(int, input().split()))

a1 = A[:N // 2]
a2 = A[N // 2:]


def calc(price_list):
    p_sum = []

    for i in range(len(price_list) + 1):
        combs = list(combinations(price_list, i))
        sums = []
        for comb in combs:
            sums.append(sum(comb))
        sums.sort()
        p_sum.append(sums)
    return p_sum


p_a1 = calc(a1)
p_a2 = calc(a2)

count = 0
for i in range(len(p_a1)):
    if K - i < 0 or len(p_a2) <= K - i:
        continue
    for a1_price in p_a1[i]:
        count += bisect(p_a2[K - i], P - a1_price)

print(count)