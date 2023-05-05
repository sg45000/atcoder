N = int(input())
T = int(input())
LR = [list(map(int, input().split(" "))) for _ in range(N)]

floorDiff = [0] * T
for l, r in LR:
    floorDiff[l] += 1
    floorDiff[r + 1] -= 1

cumulativeSum = [0] * (T + 1)
for i in range(len(floorDiff)):
    cumulativeSum[i + 1] += cumulativeSum[i] + floorDiff[i]

print(cumulativeSum[1:])
# for s in cumulativeSum:
#     print(s)

# for cumulativeSum

