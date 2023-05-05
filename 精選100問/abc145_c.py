import itertools
import math

N = int(input())
towns = [list(map(int, input().split(" "))) for _ in range(N)]

total = 0
for comb in itertools.permutations(towns):
    for i in range(N - 1):
        total += math.sqrt((comb[i][0] - comb[i + 1][0]) ** 2 + (comb[i][1] - comb[i + 1][1]) ** 2)
print(total / math.factorial(N))
